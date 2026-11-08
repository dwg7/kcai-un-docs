#!/usr/bin/env python3
"""miso の検査器(CONCEPT §5.3 の最小仕様)。使い方: python3 scripts/check_miso.py [miso/un-docs.md]
エラー: UTF-8、空でない、Office バイナリでない、第1レベル見出しが `# /…` で一意、コード囲みの閉じ忘れ。
警告: 内部パス参照が解決しない、状態語が宣言した語彙にない、/sources/ の参照が実在しない。"""
import re, sys
from pathlib import Path
STATUS = {"verified","derived","normative","open","volatile","stated","secondary","recalled","observed","reported","viewpoint","draft","untested","pass","partial","fail"}
def main():
    p = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "miso" / "un-docs.md")
    raw = p.read_bytes(); err = []; warn = []
    if not raw.strip(): print("ERROR: 空"); return 1
    if raw[:4] in (b"PK\x03\x04", b"\xd0\xcf\x11\xe0"): print("ERROR: Office バイナリ"); return 1
    try: text = raw.decode("utf-8")
    except UnicodeDecodeError as e: print("ERROR: UTF-8 でない", e); return 1
    heads = []; fence = None; props = {}; cur = None
    for i, ln in enumerate(text.split("\n"), 1):
        m = re.match(r"^\s*(`{3,}|~{3,})", ln)
        if m:
            t = m.group(1)
            if fence is None: fence = (t, i)
            elif t[0] == fence[0][0] and len(t) >= len(fence[0]): fence = None
            continue
        if fence: continue
        if re.match(r"^# ", ln):
            if not re.match(r"^# /[a-z0-9][a-z0-9-]*/[^\s]+$", ln) and not re.match(r"^# /[a-z0-9-]+$", ln): err.append(f"{i}: 第1レベル見出しが形式外: {ln[:60]}")
            heads.append((ln[2:].strip(), i)); cur = ln[2:].strip(); props[cur] = {}
        elif cur and (mm := re.match(r"^- ([a-zA-Z_\-]+):\s*(.*)$", ln)) and mm.group(1) not in props[cur]:
            props[cur][mm.group(1)] = mm.group(2)
    if fence: err.append(f"{fence[1]}: コード囲みが閉じていない")
    names = [h for h, _ in heads]
    for h, c in __import__("collections").Counter(names).items():
        if c > 1: err.append(f"見出しが重複: {h}")
    nset = set(names)
    for h, pr in props.items():
        s = pr.get("status")
        if s:
            for w in re.split(r"[,、]\s*", re.sub(r"\(.*", "", s)):
                w = w.strip()
                if w and w not in STATUS: warn.append(f"{h}: 状態語が語彙外: {s}")
        for key in ("source", "derived-from", "related", "requires"):
            for ref in re.findall(r"`?(/[a-z0-9-]+/[a-z0-9][a-z0-9.-]*)`?", pr.get(key, "")):
                if ref not in nset: warn.append(f"{h}: {key} の参照が見つからない: {ref}")
    print(f"見出し {len(names)} 件、エラー {len(err)}、警告 {len(warn)}")
    for e in err: print("ERROR", e)
    for w in warn[:40]: print("WARN", w)
    return 1 if err else 0
if __name__ == "__main__": sys.exit(main())
