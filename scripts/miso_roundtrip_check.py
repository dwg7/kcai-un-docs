#!/usr/bin/env python3
"""miso/un-docs.md の踏み跡のオブジェクトが、knowledge/*.md(凍結した写し)と一致するかを検査する。
各オブジェクトの `origin-file:` と、元の front matter の囲み、本文から、元のファイルを復元して比べる(末尾の改行の数は無視)。
元のファイルが無ければ、復元できることだけを確かめる。さらに、knowledge/ の全ファイルが miso 側に在ることも確かめる。"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
MS = ROOT / "miso" / "un-docs.md"
def objects(text):
    out, cur, fence = [], None, None
    for ln in text.split("\n"):
        m = re.match(r"^\s*(`{3,}|~{3,})", ln)
        if m:
            t = m.group(1)
            if fence is None: fence = t
            elif t[0] == fence[0] and len(t) >= len(fence): fence = None
        if fence is None and ln.startswith("# /"):
            cur = [ln]; out.append(cur)
        elif cur is not None: cur.append(ln)
    return ["\n".join(o) for o in out]
def main():
    ok = bad = 0; seen = set()
    for o in objects(MS.read_text(encoding="utf-8")):
        m = re.search(r"^- origin-file: (knowledge/[^\n]+\.md)$", o, re.M)
        f = re.search(r"<!-- kcai front matter \(verbatim\) -->\n````yaml\n(.*?)````\n\n(.*)\Z", o, re.S)
        if not (m and f): continue
        rebuilt = "---\n" + f.group(1).rstrip("\n") + "\n---\n" + f.group(2)
        seen.add(m.group(1)); orig = ROOT / m.group(1)
        if orig.exists() and orig.read_text(encoding="utf-8").rstrip("\n") == rebuilt.rstrip("\n"): ok += 1
        else: bad += 1; print("DIFF/MISSING", m.group(1))
    allk = {str(p.relative_to(ROOT)) for p in (ROOT / "knowledge").glob("*.md") if p.name != "README.md"}
    for miss in sorted(allk - seen): bad += 1; print("NOT IN MISO", miss)
    print(f"--- 一致 {ok} / 不一致 {bad} / knowledge 側 {len(allk)} 件")
    return 1 if bad else 0
if __name__ == "__main__": sys.exit(main())
