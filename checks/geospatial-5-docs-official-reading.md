# 5 文書の公式 PDF の確認（2026-10-26）

経路: `python3 -I scripts/official.py --cache <スクラッチ> '<記号>' --grep '<式>'`。各文書とも取得できた（UNREACHABLE なし）。

式: `geospatial|geographic information|GIS\b|SAGE|Situational`

| 記号 | 頁数 | 結果 |
|---|---|---|
| S/2020/952 | 20 | `geospatial` 1 件（第 39 項）。SAGE 0 |
| S/2021/843 | 19 | `geospatial` 1 件（第 32 項）。SAGE 0 |
| S/2021/1110 | 15 | `SAGE`／正式名 1 件（第 23 項、第 III 節 C）。図・表・出典表記なし。`geospatial` は正式名の中のみ |
| S/2023/3 | 15 | `geographic information system` 1 件（行方不明者委員会）。SAGE 0、`geospatial` 0 |
| S/PV.9039 | 28 | `geospatial` 0。`geographic information system` 1 件（ディカルロ氏）。Unite Aware 1 件（インド） |

un-docs: `python3 -I scripts/undocs.py --data $DATA search '\bSAGE\b'` は 1 件（S/2021/1110）。

