#!/usr/bin/env python3
"""会議録（S/PV、A/PV）で、ある国の代表の発言（見出し "Mr. X (Country):" から次の見出しまで）に語が出る箇所を抜き出す。

    python3 -I scripts/country_segments.py DATA.parquet COUNTRY REGEX [--tsv OUT.tsv] [--json OUT.json] [--wide-heading] [--president-hat]
--wide-heading: 見出しの末尾の括弧（"(spoke in Japanese; English interpretation provided by the delegation)" など）の上限を 60 字から 200 字に広げる。
--president-hat: 議長を務める国の代表が、議長席から自国の代表として述べる区間（見出しは "The President:"。直後に "in my capacity as the representative of <国>" または "... Minister for Foreign Affairs of <国>" と続き、"resume the functions of the President" で終わる）も、その国の発言として数える。TSV の最後の列 kind に president-hat と書く。
TSV には記号・日付・発言者の見出し・語の出現数・発言の長さだけを書く（本文は書かない）。JSON には本文も書く（スクラッチ用。リポジトリに入れない）。
見出しの判定は scripts/speaker_counts.py と同じ簡易判定。国連職員や国際機関の代表の発言は、直前の国の発言に誤って帰属することがある。
"""
import json, re, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import undocs
from speaker_counts import HDR, BOUND

HDR_WIDE = re.compile(HDR.pattern.replace(r"\([^)]{0,60}\)", r"\([^)]{0,200}\)"))
PRES = re.compile(r"The President\s*(?:\([^)]{0,200}\))?\s*:")
RESUME = re.compile(r"resum\w*\s+(?:my|the)\s+functions\s+as\s+President|resume\s+the\s+functions\s+of\s+the\s+President", re.I)


def main(argv):
    data, country, rx = argv[0], argv[1], argv[2]
    tsv = argv[argv.index("--tsv") + 1] if "--tsv" in argv else None
    js = argv[argv.index("--json") + 1] if "--json" in argv else None
    con = undocs.connect(data)
    pat = re.compile(rx)
    hdr = HDR_WIDE if "--wide-heading" in argv else HDR
    hat = "--president-hat" in argv
    cap = re.compile(r"capacity\s+as\s+[^.:]{0,100}?\b" + re.escape(country) + r"\b", re.I)  # "representative of Japan"、"Minister for Foreign Affairs of Japan" など
    out = []
    for sym, d, fam, b in con.execute("select sym,date,family,body from docs where family in ('S/PV','A/PV') and regexp_matches(body,?)", [rx]).fetchall():
        hs = sorted([(m.start(), m.group(1).strip(), m.group(0)) for m in hdr.finditer(b)] + [(m.start(), None, m.group(0)) for m in BOUND.finditer(b)])
        pos = [h[0] for h in hs]
        pres = [(m.start(), m.group(0)) for m in PRES.finditer(b)] if hat else []
        for i, h in enumerate(hs):
            kind = "heading"
            if h[1] != country:
                continue
            seg = b[h[0]:(pos[i + 1] if i + 1 < len(hs) else len(b))]
            if not pat.search(seg):
                continue
            t = re.sub(r"\s+", " ", seg)
            out.append(dict(sym=sym, date=d, speaker=re.sub(r"\s+", " ", h[2]).strip(), n=len(pat.findall(t)), len=len(t), text=t, kind=kind))
        # 議長席からの自国発言: "The President:" の区間のうち、"in my capacity as the representative of <国>" から "resume the functions" までを数える
        allpos = sorted([h[0] for h in hs if h[1] is not None] + [p for p, _ in pres])  # 区間の終わりは、名前つきの見出しか次の "The President:" だけ（BOUND は、文中の語に当たって区間を切るため使わない）
        for start, head in pres:
            nxt = [q for q in allpos if q > start]
            seg = b[start:(nxt[0] if nxt else len(b))]
            c = cap.search(seg)
            if not c:
                continue
            seg = seg[c.start():]
            r = RESUME.search(seg)
            if r:
                seg = seg[:r.start()]
            if not pat.search(seg):
                continue
            t = re.sub(r"\s+", " ", seg)
            out.append(dict(sym=sym, date=d, speaker="The President (in national capacity: %s)" % country, n=len(pat.findall(t)), len=len(t), text=t, kind="president-hat"))
    out.sort(key=lambda x: (x["date"] or "", x["sym"]))
    if tsv:
        with open(tsv, "w") as f:
            f.write("sym\tdate\tspeaker_heading\tmentions\tsegment_chars\tkind\n")
            for r in out:
                f.write(f"{r['sym']}\t{r['date']}\t{r['speaker']}\t{r['n']}\t{r['len']}\t{r['kind']}\n")
    if js:
        json.dump(out, open(js, "w"), ensure_ascii=False)
    print(len(out), "発言;", len({r["sym"] for r in out}), "文書")


if __name__ == "__main__":
    main(sys.argv[1:])
