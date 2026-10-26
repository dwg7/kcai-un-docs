#!/usr/bin/env python3
"""踏み跡を、問い合わせできる索引（JSON）にし、タグの使われ方を集計する。

目的: 構造化された知識に「さらに問う」ことで、予想していなかった発見を得る（人も LLM も）。
フロントマターのキー（タグ）と関係の種類は自由に増やせる。ここでは、使われ方をそのまま集計する
（OSM の taginfo に近い）。標準ライブラリのみ。

使い方:
    python3 scripts/build_index.py                      # build/index.json と build/tags.md を作る
    python3 scripts/build_index.py --stats              # タグ・関係・出典の使われ方を表示
    python3 scripts/build_index.py --tag as_of          # そのタグを持つ踏み跡
    python3 scripts/build_index.py --tag kind=review    # タグと値が一致する踏み跡（値は部分一致）
    python3 scripts/build_index.py --rel contrasts      # その種類の関係を持つ踏み跡
    python3 scripts/build_index.py --cites junsoku-r7   # その出典を引いている踏み跡（該当箇所つき）
    python3 scripts/build_index.py --links topic-x      # topic-x へのリンク元とリンク先
    python3 scripts/build_index.py --orphans            # どこからもリンクされず、どこへもリンクしない踏み跡
    python3 scripts/build_index.py --grep 条番号         # 本文に語を含む踏み跡
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_knowledge import parse_front_matter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ID_IN_TEXT = re.compile(r"`([a-z][a-z0-9-]+)`|\(knowledge/([a-z0-9-]+)\.md\)")
CORE = {"id", "title", "status", "sources", "authors", "reviewed_by", "updated", "related"}


def pair(item):
    k, _, v = item.partition(":")
    return k.strip(), v.strip()


def load(root):
    kdir = root / "knowledge"
    chunks = {}
    for p in sorted(kdir.glob("*.md")):
        if p.name.lower() == "readme.md":
            continue
        fm, body = parse_front_matter(p.read_text(encoding="utf-8"))
        chunks[fm["id"]] = (fm, body)
    ids = set(chunks)
    index = {}
    for cid, (fm, body) in chunks.items():
        kind = cid.split("-", 1)[0]
        tags = {k: v for k, v in fm.items() if k not in CORE and k not in ("relations", "cites")}
        rels = [pair(r) for r in fm.get("relations", [])]
        cites = [pair(c) for c in fm.get("cites", [])]
        mentions = sorted({a or b for a, b in ID_IN_TEXT.findall(body) if (a or b) in ids and (a or b) != cid})
        index[cid] = {
            "id": cid, "kind": kind, "title": fm["title"], "status": fm["status"], "updated": fm["updated"],
            "tags": tags,
            "relations": [{"type": k, "to": v} for k, v in rels],
            "related": fm.get("related", []),
            "cites": [{"source": k, "where": v} for k, v in cites],
            "sources": fm["sources"],
            "mentions": mentions,
            "headings": [l.strip() for l in body.splitlines() if l.startswith("## ")],
            "chars": len(body),
        }
    back = defaultdict(set)
    for cid, c in index.items():
        outs = set(c["mentions"]) | set(c["related"]) | {r["to"] for r in c["relations"]}
        c["links_out"] = sorted(outs)
        for o in outs:
            back[o].add(cid)
    for cid, c in index.items():
        c["links_in"] = sorted(back.get(cid, ()))
    return index, chunks


def stats(index):
    tagkeys, tagvals, rels, srcs = Counter(), defaultdict(Counter), Counter(), Counter()
    for c in index.values():
        for k, v in c["tags"].items():
            tagkeys[k] += 1
            for x in (v if isinstance(v, list) else [v]):
                tagvals[k][x] += 1
        for r in c["relations"]:
            rels[r["type"]] += 1
        for s in c["cites"]:
            srcs[s["source"]] += 1
    return tagkeys, tagvals, rels, srcs


def tags_md(index):
    tagkeys, tagvals, rels, srcs = stats(index)
    out = ["# タグの使われ方（自動集計）", "", "`python3 scripts/build_index.py` が作る。手で編集しない。", ""]
    out += ["## フロントマターのタグ（必須項目を除く）", "", "| タグ | 使われた踏み跡の数 | 主な値 |", "|---|---|---|"]
    for k, n in tagkeys.most_common():
        vals = "、".join("%s（%d）" % (v, c) for v, c in tagvals[k].most_common(4))
        out.append("| `%s` | %d | %s |" % (k, n, vals))
    out += ["", "## 関係の種類（relations）", "", "| 種類 | 件数 |", "|---|---|"]
    out += ["| `%s` | %d |" % (k, n) for k, n in rels.most_common()]
    out += ["", "## 出典（cites）の使われ方", "", "| 出典 id | 引用した踏み跡の数 |", "|---|---|"]
    out += ["| `%s` | %d |" % (k, n) for k, n in srcs.most_common()]
    kinds = Counter(c["kind"] for c in index.values())
    out += ["", "## 踏み跡の種類（id の接頭辞）", "", "| 接頭辞 | 踏み跡の数 |", "|---|---|"]
    out += ["| `%s-` | %d |" % (k, n) for k, n in kinds.most_common()]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--tag")
    ap.add_argument("--rel")
    ap.add_argument("--cites")
    ap.add_argument("--links")
    ap.add_argument("--orphans", action="store_true")
    ap.add_argument("--grep")
    ap.add_argument("--out", default="build")
    a = ap.parse_args()
    index, chunks = load(ROOT)

    if a.stats:
        print(tags_md(index))
    elif a.tag:
        k, _, v = a.tag.partition("=")
        for c in index.values():
            if k in c["tags"]:
                val = c["tags"][k]
                vs = val if isinstance(val, list) else [val]
                if not v or any(v in x for x in vs):
                    print("%s\t%s=%s\t%s" % (c["id"], k, "、".join(vs), c["title"]))
    elif a.rel:
        for c in index.values():
            for r in c["relations"]:
                if r["type"] == a.rel:
                    print("%s --%s--> %s" % (c["id"], r["type"], r["to"]))
    elif a.cites:
        for c in index.values():
            for s in c["cites"]:
                if s["source"] == a.cites:
                    print("%s\t%s" % (c["id"], s["where"]))
    elif a.links:
        c = index[a.links]
        print("リンク先:", *c["links_out"], sep="\n  ")
        print("リンク元:", *c["links_in"], sep="\n  ")
    elif a.orphans:
        for c in index.values():
            if not c["links_in"] and not c["links_out"]:
                print(c["id"])
    elif a.grep:
        for cid, (fm, body) in chunks.items():
            if a.grep in body:
                print("%s\t%s" % (cid, fm["title"]))
    else:
        out = ROOT / a.out
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
        (out / "tags.md").write_text(tags_md(index), encoding="utf-8")
        print("索引を作成: %s（踏み跡 %d 件）、%s" % (out / "index.json", len(index), out / "tags.md"))


if __name__ == "__main__":
    main()
