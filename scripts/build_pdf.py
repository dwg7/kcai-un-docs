#!/usr/bin/env python3
"""README.md から辿れる踏み跡を、1 つの HTML（必要なら PDF）にまとめる。

標準ライブラリのみで HTML を生成する。PDF への変換は、手元のブラウザ（Chromium 系）の
印刷機能を呼び出す。使い方:
    python3 scripts/build_pdf.py            # build/kcai.html を作る
    python3 scripts/build_pdf.py --pdf      # さらに build/kcai.pdf を作る（ブラウザが必要）

踏み跡の並び順は、README.md の中でリンクされている順（`knowledge/<id>.md`）に従う。
README.md にリンクされていない踏み跡は末尾に付け、警告を出す。
"""
import argparse
import datetime
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_knowledge import parse_front_matter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"knowledge/([a-z0-9-]+)\.md")
BROWSERS = ["chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome"]
# 開発者向けの節は、PDF の表紙から除く
SKIP_HEADINGS = {"構成", "準拠する kcai"}
STATUS_LABEL = {"draft": "草案（人の確認前）", "reviewed": "確認済み", "stable": "安定", "deprecated": "廃止予定"}

CSS = """
@page { size: A4; margin: 20mm 16mm 18mm 16mm;
  @bottom-center { content: counter(page) " / " counter(pages); font-size: 8pt; color: #666; }
  @top-right { content: "草案（人の確認前）・非公開"; font-size: 8pt; color: #a00; }
}
.cover h1 { font-size: 24pt; border: none; margin-top: 30mm; }
.part { page-break-before: always; font-size: 16pt; color: #334; border-bottom: 1px solid #99a; }
body { font-family: 'IPAGothic','Noto Sans CJK JP','Hiragino Sans','Yu Gothic',sans-serif;
       font-size: 10pt; line-height: 1.7; color: #222; }
h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 4px; }
h2 { font-size: 14pt; margin-top: 1.6em; border-left: 5px solid #556; padding-left: 8px; }
h3 { font-size: 11.5pt; margin-top: 1.2em; }
table { border-collapse: collapse; width: 100%; margin: 0.6em 0; font-size: 9pt; }
th, td { border: 1px solid #999; padding: 3px 6px; vertical-align: top; }
th { background: #eee; }
code { font-family: 'IPAGothic', monospace; background: #f3f3f3; padding: 0 2px; }
blockquote { margin: 0.8em 0; padding: 4px 12px; border-left: 4px solid #c60; background: #fff7ee; }
a { color: #14c; text-decoration: none; }
.chunk { page-break-before: always; }
.part-page + .chunk { page-break-before: avoid; }
.meta { font-size: 8.5pt; color: #555; border: 1px solid #ccc; padding: 4px 8px; margin-bottom: 0.8em; }
.badge { display: inline-block; padding: 0 6px; border-radius: 3px; background: #fde; font-weight: bold; }
.toc { list-style: none; padding-left: 0; }
.toc li { margin: 2px 0; }
.toc-part { list-style: none; margin-top: 8px; }
.toc-page { page-break-after: always; }
.part-page { page-break-before: always; page-break-after: always; }
.part-page .part { border: none; margin-top: 90mm; font-size: 22pt; page-break-before: avoid; }
.cover { page-break-after: always; }
"""


TITLES = {}


def link_ids(m):
    cid = m.group(1)
    if cid in TITLES:
        return '<a href="#%s">「%s」</a>' % (cid, html.escape(TITLES[cid]))
    return "<code>%s</code>" % cid


def inline(s):
    s = html.escape(s)
    s = re.sub(r"`([a-z0-9][a-z0-9-]*)`", link_ids, s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(knowledge/([a-z0-9-]+)\.md\)", r'<a href="#\2">\1</a>', s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"(?<![\"=>])(https?://[^\s<)、。）]+)", r'<a href="\1">\1</a>', s)
    return s


def render_md(text, shift=0):
    """Markdown の部分集合（見出し、段落、箇条書き、番号付き、表、引用）を HTML にする。"""
    out, lines, i = [], text.splitlines(), 0
    stack = []  # 開いているリスト（'ul'/'ol'）

    def close_lists(depth=0):
        while len(stack) > depth:
            out.append("</li></%s>" % stack.pop())

    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            close_lists()
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", ln)
        if m:
            close_lists()
            n = min(len(m.group(1)) + shift, 6)
            out.append("<h%d>%s</h%d>" % (n, inline(m.group(2)), n))
            i += 1
            continue
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1]):
            close_lists()
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            out.append("<table><tr>%s</tr>" % "".join("<th>%s</th>" % inline(c) for c in head))
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in cells))
                i += 1
            out.append("</table>")
            continue
        if ln.startswith(">"):
            close_lists()
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ").rstrip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(buf)))
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", ln)
        if m:
            depth = len(m.group(1)) // 2 + 1
            kind = "ol" if m.group(2)[0].isdigit() else "ul"
            if depth > len(stack):
                out.append("<%s><li>" % kind)
                stack.append(kind)
            else:
                close_lists(depth)
                out.append("</li><li>")
            out.append(inline(m.group(3)))
            i += 1
            continue
        close_lists()
        para = [ln.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|\s*([-*]|\d+\.)\s)", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))
    close_lists()
    return "\n".join(out)


def strip_sections(text, skip):
    """README.md から、skip に挙げた見出し（## ）の節を取り除く。"""
    out, skipping = [], False
    for ln in text.splitlines():
        m = re.match(r"^##\s+(.*)", ln)
        if m:
            skipping = m.group(1).strip() in skip
        if not skipping:
            out.append(ln)
    return "\n".join(out)


def grouped_links(readme_text, kdir):
    """README.md の「知識の索引」から、(見出し, [id...]) の組を順に取り出す。"""
    files = {p.stem: p for p in sorted(kdir.glob("*.md")) if p.name.lower() != "readme.md"}
    groups, cur, seen = [], None, set()
    in_index = False
    for ln in readme_text.splitlines():
        m = re.match(r"^##\s+(.*)", ln)
        if m:
            in_index = m.group(1).strip() == "知識の索引"
            continue
        if not in_index:
            continue
        h = re.match(r"^###\s+(.*)", ln)
        if h:
            cur = (h.group(1).strip(), [])
            groups.append(cur)
            continue
        for cid in LINK_RE.findall(ln):
            if cid in files and cid not in seen:
                if cur is None:
                    cur = ("", [])
                    groups.append(cur)
                cur[1].append(cid)
                seen.add(cid)
    rest = [c for c in files if c not in seen]
    return groups, rest, files


def git_version(root):
    try:
        h = subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        return h
    except Exception:
        return "不明"


def build(root, out_html):
    readme = (root / "README.md").read_text(encoding="utf-8")
    kdir = root / "knowledge"
    groups, rest, files = grouped_links(readme, kdir)
    for c in rest:
        print("警告: README.md にリンクされていない踏み跡を末尾に追加: %s" % c, file=sys.stderr)
    if rest:
        groups.append(("（索引にない踏み跡）", rest))

    data = {}
    for _, cids in groups:
        for cid in cids:
            data[cid] = parse_front_matter(files[cid].read_text(encoding="utf-8"))
    TITLES.update({cid: fm["title"] for cid, (fm, _) in data.items()})
    n = len(data)
    counts = {}
    for fm, _ in data.values():
        counts[fm["status"]] = counts.get(fm["status"], 0) + 1
    summary = "、".join("%s %d 件" % (STATUS_LABEL.get(k, k), v) for k, v in sorted(counts.items()))

    toc, parts = [], []
    for gtitle, cids in groups:
        if gtitle:
            toc.append('<li class="toc-part"><strong>%s</strong></li>' % html.escape(gtitle))
            parts.append('<section class="part-page"><h2 class="part">%s</h2></section>' % html.escape(gtitle))
        for cid in cids:
            fm, body = data[cid]
            toc.append('<li><a href="#%s">%s</a> <small>(%s)</small></li>' % (cid, html.escape(fm["title"]), STATUS_LABEL.get(fm["status"], fm["status"])))
            rev = "、".join(fm["reviewed_by"]) if fm["reviewed_by"] else "未確認"
            meta = '<div class="meta"><span class="badge">%s</span> 確認者: %s ／ 更新: %s ／ 作成: %s</div>' % (
                html.escape(STATUS_LABEL.get(fm["status"], fm["status"])), html.escape(rev),
                html.escape(fm["updated"]), html.escape("、".join(fm["authors"])))
            parts.append('<section class="chunk" id="%s"><h1>%s</h1>%s%s</section>' % (cid, html.escape(fm["title"]), meta, render_md(body, shift=1)))

    # 付録: 特定の出典（既定: 日本測量協会 jsurvey.jp）に依拠する踏み跡の一覧
    appendix = ""
    domain = "jsurvey.jp"
    rows = []
    for gtitle, cids in groups:
        for cid in cids:
            fm, _ = data[cid]
            srcs = [s for s in fm["sources"] if domain in s]
            if srcs:
                rows.append("<tr><td><a href=\"#%s\">%s</a></td><td>%s</td></tr>" % (cid, html.escape(fm["title"]), "<br>".join(inline(s) for s in srcs)))
    if rows:
        appendix = ('<section class="chunk"><h1>付録　日本測量協会の公表資料を出典とする踏み跡の一覧</h1>'
                    '<p>この資料で、日本測量協会（%s）のページを出典に挙げている踏み跡と、その出典です。本文の転載はせず、要約と出典の提示にとどめています。</p>'
                    '<table><tr><th>踏み跡</th><th>出典（協会）</th></tr>%s</table></section>' % (domain, "".join(rows)))

    cover_path = root / "cover.md"
    title = "踏み跡のまとめ"
    if cover_path.exists():
        ctext = cover_path.read_text(encoding="utf-8")
        ctext = ctext.replace("{{件数}}", str(n)).replace("{{内訳}}", summary).replace("{{版}}", git_version(root)).replace("{{日付}}", datetime.date.today().isoformat())
        m = re.match(r"^#\s+(.*)", ctext)
        if m:
            title = m.group(1).strip()
        cover_html = render_md(ctext)
    else:
        cover_html = render_md(strip_sections(readme, SKIP_HEADINGS))
    cover = '<section class="cover">%s</section><section class="toc-page"><h2>目次</h2><ul class="toc">%s</ul></section>' % (cover_html, "\n".join(toc))
    doc = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>%s%s%s</body></html>' % (
        html.escape(title), CSS, cover, "\n".join(parts), appendix)
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(doc, encoding="utf-8")
    print("HTML を作成: %s（踏み跡 %d 件）" % (out_html, n))


def to_pdf(html_path, pdf_path, browser):
    cmd = [browser, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
           "--print-to-pdf=%s" % pdf_path, html_path.resolve().as_uri()]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("PDF を作成: %s" % pdf_path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", action="store_true", help="ブラウザで PDF も作る")
    ap.add_argument("--browser", help="使用するブラウザの実行ファイル")
    ap.add_argument("--out", default="build", help="出力先ディレクトリ（既定: build）")
    a = ap.parse_args()
    out = ROOT / a.out
    build(ROOT, out / "kcai.html")
    if a.pdf:
        b = a.browser or next((shutil.which(x) for x in BROWSERS if shutil.which(x)), None)
        if not b:
            sys.exit("ブラウザ（chromium 等）が見つかりません。--browser で指定するか、build/kcai.html をブラウザで開いて PDF に印刷してください。")
        to_pdf(out / "kcai.html", out / "kcai.pdf", b)


if __name__ == "__main__":
    main()
