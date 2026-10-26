# 検査記録：S/PV.4310 と「地図課」の呼称の件数（2026-10-26）

データ: un-docs 6cd1cf0。`python3 -I scripts/undocs.py --data <parquet> search '<式>' --first N --by-year`（合冊除外、記号の正規化・重複除去済み）。

| 式 | 件数 | 備考 |
|---|---|---|
| `(?i:Chief\s+Cartographer)` | 3 | S/PRST/2000/21、S/PV.4160、S/INF/56。S/PV.4310 は含まない |
| `(?i:Chief\s+of\s+the\s+Cartographic)` | 1 | S/PV.4310 のみ |
| `(?i:Cartographic\s+Unit)` | 1 | S/PV.4227（2000-11-17） |
| `(?i:Cartographic\s+Section)` | 8 | S/PV.4310、A/RES/57/300、58/101、S/2011/30、A/RES/67/287、S/2014/442、S/2014/893、A/RES/69/308 |
| `(?i:Geospatial\s+Information\s+Section)` | 4 | A/RES/69/308、S/2015/1025、S/2017/78、S/2017/1034 |

S/PV.4310 の `show --grep artograph` は 2 か所（ゲエノ氏の答弁、アニャビ氏の答弁）を返し、公式の PDF の全文通読と一致した。公式の PDF は `scripts/official.py` と同じ経路（documents.un.org の API）で取得できた。届かなかった先は無い。

未実施: S/PV.4227、S/PV.4160、決議 1177/1298/1344、事務総長の報告の読み直し。
