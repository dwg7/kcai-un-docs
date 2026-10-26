#!/usr/bin/env python3
"""ミッション名を冒頭に持つ文書のうち、地図・GIS・地理空間の語を含む文書の割合（knowledge/un-mission-gis-mentions-in-un-docs.md の数値の再現）。

    python3 -I scripts/mission_gis_ratio.py DATA.parquet
対象: 記号の型が S/yyyy/n（S/ 数字の文書）、A/NN/n、S/INF の文書。冒頭 900 字に MISSIONS のどれかが含まれるもの。
語: cartograph（英語・仏語を含む）、geospatial、GIS（大文字）、geographic information system。
"""
import re, sys, collections
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import undocs

MISSIONS = (r"UNIFIL|UNDOF|UNFICYP|UNMIK|MONUSCO|MONUC|UNMISS|UNAMID|MINUSMA|MINUSCA|UNMIL|UNOCI|MINUSTAH|UNISFA|MINURSO|UNMEE|UNMIT|"
            r"UNAMA|UNAMI|UNSMIL|UNSOA|UNSOS|UNMHA|United Nations Interim Force in Lebanon|Disengagement Observer Force|"
            r"Peacekeeping Force in Cyprus|Interim Administration Mission in Kosovo|Organization Stabilization Mission|"
            r"Mission in South Sudan|Hybrid Operation in Darfur|Multidimensional Integrated Stabilization Mission|"
            r"Stabilization Mission in the Central African|Mission in Liberia|Operation in Côte d.Ivoire|Stabilization Mission in Haiti|"
            r"Interim Security Force for Abyei|Mission for the Referendum in Western Sahara|Mission in Ethiopia and Eritrea|"
            r"Assistance Mission in Afghanistan|Assistance Mission for Iraq|Support Mission in Libya|Support Mission in Somalia|"
            r"Mission to Support the Hodeidah")
WORDS = r"(?i:cartograph)|(?i:geo-?\s?spatial)|(?i:geographic(al)?\s+information\s+system)|\bGIS\b"

def main(path):
    con = undocs.connect(path)
    rows = con.execute("select sym,family,body from docs where family in ('S/yyyy/n','A/NN/n','S/INF')").fetchall()
    head, hit = [], []
    for sym, f, b in rows:
        if re.search(MISSIONS, b[:900]):
            head.append(sym)
            if re.search(WORDS, b): hit.append(sym)
    print(f"対象（S/yyyy/n・A/NN/n・S/INF）{len(rows)}、冒頭にミッション名 {len(head)}、うち語を含む {len(hit)}")
    print(sorted(hit))

if __name__ == "__main__":
    main(sys.argv[1])
