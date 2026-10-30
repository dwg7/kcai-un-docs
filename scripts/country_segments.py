#!/usr/bin/env python3
"""会議録（S/PV、A/PV）で、ある国の代表の発言（見出し "Mr. X (Country):" から次の見出しまで）に語が出る箇所を抜き出す。

    python3 -I scripts/country_segments.py DATA.parquet COUNTRY REGEX [--tsv OUT.tsv] [--json OUT.json]
TSV には記号・日付・発言者の見出し・語の出現数・発言の長さだけを書く（本文は書かない）。JSON には本文も書く（スクラッチ用。リポジトリに入れない）。
見出しの判定は scripts/speaker_counts.py と同じ簡易判定。国連職員や国際機関の代表の発言は、直前の国の発言に誤って帰属することがある。
"""
import json, re, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import undocs
from speaker_counts import HDR, BOUND


def main(argv):
    data, country, rx = argv[0], argv[1], argv[2]
    tsv = argv[argv.index("--tsv") + 1] if "--tsv" in argv else None
    js = argv[argv.index("--json") + 1] if "--json" in argv else None
    con = undocs.connect(data)
    pat = re.compile(rx)
    out = []
    for sym, d, fam, b in con.execute("select sym,date,family,body from docs where family in ('S/PV','A/PV') and regexp_matches(body,?)", [rx]).fetchall():
        hs = sorted([(m.start(), m.group(1).strip(), m.group(0)) for m in HDR.finditer(b)] + [(m.start(), None, m.group(0)) for m in BOUND.finditer(b)])
        pos = [h[0] for h in hs]
        for i, h in enumerate(hs):
            if h[1] != country:
                continue
            seg = b[h[0]:(pos[i + 1] if i + 1 < len(hs) else len(b))]
            if not pat.search(seg):
                continue
            t = re.sub(r"\s+", " ", seg)
            out.append(dict(sym=sym, date=d, speaker=re.sub(r"\s+", " ", h[2]).strip(), n=len(pat.findall(t)), len=len(t), text=t))
    out.sort(key=lambda x: (x["date"] or "", x["sym"]))
    if tsv:
        with open(tsv, "w") as f:
            f.write("sym\tdate\tspeaker_heading\tmentions\tsegment_chars\n")
            for r in out:
                f.write(f"{r['sym']}\t{r['date']}\t{r['speaker']}\t{r['n']}\t{r['len']}\n")
    if js:
        json.dump(out, open(js, "w"), ensure_ascii=False)
    print(len(out), "発言;", len({r["sym"] for r in out}), "文書")


if __name__ == "__main__":
    main(sys.argv[1:])
