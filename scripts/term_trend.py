#!/usr/bin/env python3
"""語の出現を期間別に数える（生の件数、文書 1,000 件あたり、100 万字あたり、系列別）。

    python3 -I scripts/term_trend.py DATA.parquet
踏み跡 knowledge/geospatial-activity-over-time.md の表は、この出力から作った。
語の式は TERMS を直す。年の範囲は 1970〜2023（un-docs は 2023 年 10 月ごろまで）。
"""
import re, sys, collections
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import undocs

TERMS = {
    "core": r"(?i:geo-?\s?spatial)|(?i:geographic(al)?\s+information\s+system)|\bGIS\b|(?i:geodet)|GGIM|UNOSAT|(?i:geo-?referenc)",
    "geospatial": r"(?i:geo-?\s?spatial)",
    "RS/EO": r"(?i)remote[\s-]+sensing|earth[\s-]+observation",
    "satellite imagery": r"(?i)satellite\s+(imagery|images?)",
}
ORDER = ["1970-79", "1980-89", "1990-99", "2000-04", "2005-09", "2010-14", "2015-19", "2020-23"]


def period(y):
    return ("1970-79" if y < 1980 else "1980-89" if y < 1990 else "1990-99" if y < 2000 else "2000-04" if y < 2005
            else "2005-09" if y < 2010 else "2010-14" if y < 2015 else "2015-19" if y < 2020 else "2020-23")


def main(path):
    con = undocs.connect(path)
    rx = {k: re.compile(r) for k, r in TERMS.items()}
    tot, chars, totA = collections.Counter(), collections.Counter(), collections.Counter()
    cnt = {k: collections.Counter() for k in TERMS}
    cntA = {k: collections.Counter() for k in TERMS}
    for y, f, n, b in con.execute(
            "select cast(substr(date,1,4) as int), family, length(body), body from docs "
            "where date is not null and substr(date,1,4) between '1970' and '2023'").fetchall():
        p = period(y); tot[p] += 1; chars[p] += n
        if f == "A/RES": totA[p] += 1
        for k, r in rx.items():
            if r.search(b):
                cnt[k][p] += 1
                if f == "A/RES": cntA[k][p] += 1
    print("period docs Mchars A/RES")
    for p in ORDER: print(p, tot[p], round(chars[p] / 1e6), totA[p])
    for k in TERMS:
        print("==", k)
        print(" raw       ", *[f"{p}:{cnt[k][p]}" for p in ORDER])
        print(" per1000   ", *[f"{p}:{1000 * cnt[k][p] / tot[p]:.1f}" for p in ORDER])
        print(" perMchar  ", *[f"{p}:{1e6 * cnt[k][p] / chars[p]:.2f}" for p in ORDER])
        print(" A/RES/1000", *[f"{p}:{1000 * cntA[k][p] / max(totA[p], 1):.1f}" for p in ORDER])


if __name__ == "__main__":
    main(sys.argv[1])
