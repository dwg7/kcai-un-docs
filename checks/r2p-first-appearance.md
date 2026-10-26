# 検査記録：保護する責任（2026-10-26）

データ: un-docs コミット 6cd1cf0。数は 2026-10-26 に、記号を空白除去・大文字化で正規化した版の `undocs.py` で再実行した。検索は `scripts/undocs.py`（正規化・重複除去・合冊除外）。文脈の切り出しは `scripts/undocs_ctx.py`（正規表現の周辺 ±N 字を日付順に出す）。

## 実行したクエリ

| 目的 | 正規表現（`search`） | 結果 |
|---|---|---|
| 句 | `(?i)responsibilit(y|ies)\s+to\s+protect` | 947 文書。S/PV 549、S/yyyy/n 139、S/RES 97、A/PV 90、A/RES 34、S/INF 15、S/PRST 15 |
| 句＋集団殺害など | `(?i)responsibilit(y|ies)\s+to\s+protect[^.]{0,80}(populations?|genocide|war\s+crimes)|protect\s+(its|their)\s+(own\s+)?populations?\s+from\s+genocide` | 336 文書 |
| 略語 | `\bR2P\b|(?i)responsibility\s+to\s+protect\s+\(R2P\)` | 15 文書。初出 A/63/PV.97（2009-07-23） |
| ICISS | `(?i)International\s+Commission\s+on\s+Intervention\s+and\s+State\s+Sovereignty`（〜2006） | S/PV.4660(Resumption1) 2002-12-10、S/PV.4990(Resumption1) 2004-06-14、S/PV.5052(Resumption1) 2004-10-06 |
| 138・139 項の参照 | `(?i)paragraphs?\s+138\s+(and|to|-|–)\s*139` | S/RES 7（初出 1674）、S/PRST 1（2013/2）、A/RES 2（63/308、75/277） |

## 記号の有無（検索 0 件）

`A/57/303`（ICISS 報告書）、`A/59/565`、`A/59/2005`、`A/63/677`、`A/59/L.64` は un-docs に無い。

## 公式原文との照合（`scripts/official.py`）

取得: `https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf`（`https://docs.un.org/en/<記号>` のページが iframe で埋め込む公開経路）。S/RES/1674(2006)、S/RES/1393(2002)、A/RES/60/1、A/RES/59/314、S/PV.4660(Resumption1) で一致。A/RES/36/231 は決議集の見開きで確認不能。
