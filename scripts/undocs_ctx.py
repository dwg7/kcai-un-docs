#!/usr/bin/env python3
"""語が当たった文書の周辺（前後 N 字）を、日付順に出す。undocs.py と同じ規則（正規化・重複除去・合冊除外）。

    python3 -I scripts/undocs_ctx.py DATA.parquet REGEX FROM TO [WIDTH]
"""
import re, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import undocs

con = undocs.connect(sys.argv[1])
rx, lo, hi = sys.argv[2], sys.argv[3], sys.argv[4]
w = int(sys.argv[5]) if len(sys.argv) > 5 else 110
for sym, date, body in con.execute(
        "select sym,date,body from docs where regexp_matches(body,?) and date>=? and date<=? order by date,sym",
        [rx, lo, hi]).fetchall():
    ms = list(re.finditer(rx, body))
    m = ms[0]
    print(f"## {sym} {date} n={len(ms)}\n   …{re.sub(r'\\s+', ' ', body[max(0, m.start() - w):m.end() + w])}…")
