# UNLB の GIS センター（2006 年の提案、A/63/824 附属書 III）の確かめ記録（2026-10-26）

- un-docs 検索: `python3 -I scripts/undocs.py --data $D search '(?i)geograph\w*\s+information\s+system\s+cent'` → 2 件（A/RES/60/267、A/RES/61/277）。
- un-docs に無い（`show` が not found）: A/60/715、A/60/787、A/60/916、A/61/752、A/61/852/Add.14、A/C.5/60/SR.65・66。A/60/PV.92 はある（未読）。`search '(?i)Logistics\s+Base' --family A/C.5` は 0 件。
- 公式 PDF（`scripts/official.py`）で取得できた: A/60/696、699、700、711、715、787、870、896、916、A/61/679、752、795、852/Add.14、968、A/63/824。届かなかった先は無い。
- GIS 語の grep（`geographic(al)? information|GIS\b|cartograph`）: A/60/715 第 9〜10 項に提案。A/60/787 第 29、31 項。A/60/700、711、699 には出ない。
- A/63/824: `global service` の検索で UNGSC に当たる文は無い（5231 行付近の「global service outage」のみ）。附属書 III は第 1〜16 項。
