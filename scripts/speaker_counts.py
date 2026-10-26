#!/usr/bin/env python3
"""会議録（S/PV、A/PV）で、語が出る発言を、発言者の国（"Mr. X (Country):" の表記）で数える。

    python3 -I scripts/speaker_counts.py DATA.parquet REGEX [--from YYYY] [--to YYYY]
発言者の見出しは抽出テキストの正規表現で拾う簡易判定。議長の発言（The President (…)）や、見出しの崩れは拾えない。
"""
import re, sys, collections
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import undocs

HDR = re.compile(r"(?:Mr\.|Ms\.|Mrs\.|Miss|Sir|Lord|Dame|Baroness|Dr\.|Sheikh|Prince|Archbishop)\s+[^():\n]{2,60}?\s*\(([A-Z][A-Za-z'’ ,\-]{2,45})\)(?:\s*\([^)]{0,60}\))?\s*:")

BOUND = re.compile(r"(?:The|the)\s+(?:Acting\s+|Deputy\s+)?(?:President|Secretary-General|Chairman|Chairperson|Chair|Vice-President)\b[^:\n]{0,90}:")


def main(argv):
    data, rx = argv[0], argv[1]
    lo = int(argv[argv.index("--from") + 1]) if "--from" in argv else 0
    hi = int(argv[argv.index("--to") + 1]) if "--to" in argv else 9999
    con = undocs.connect(data)
    docs = collections.defaultdict(set); ment = collections.Counter(); unattr = 0; nd = 0
    for sym, d, b in con.execute("select sym,date,body from docs where family in ('S/PV','A/PV') and regexp_matches(body,?)", [rx]).fetchall():
        y = int((d or "0000")[:4])
        if not (lo <= y <= hi): continue
        nd += 1
        hdr = [(m.start(), m.group(1).strip()) for m in HDR.finditer(b)] + [(m.start(), None) for m in BOUND.finditer(b)]
        hdr.sort()
        for m in re.finditer(rx, b):
            prev = [h for h in hdr if h[0] <= m.start()]
            if prev and prev[-1][1]:
                docs[prev[-1][1]].add(sym); ment[prev[-1][1]] += 1
            else:
                unattr += 1
    print(f"docs={nd} attributed_countries={len(docs)} unattributed_mentions={unattr}")
    for c, s in sorted(docs.items(), key=lambda kv: -len(kv[1]))[:25]:
        print(f"{c}\t{len(s)}\t{ment[c]}")

if __name__ == "__main__":
    main(sys.argv[1:])
