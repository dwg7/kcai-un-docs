---
id: keyword-agency-in-un-docs
title: 「エージェンシー」（agency）：機関の意味が圧倒的で、行為主体性の用法は 2008 年以降に増える
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-27
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。式と件数は checks/keywords-human-security-nexus-agency.md
  - S/PV.6005、S/PV.9276（Resumption 1）ほか（行為主体性の用法の例。un-docs の本文）
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-27
related: [keyword-human-security-in-un-docs, keyword-nexus-in-un-docs, un-docs-reading-guide]
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書、安保理決議は 2699 まで。以下は un-docs で見つかった範囲の話である。

`agency` は 16,026 文書（un-docs の約 43%）に出るが、ほとんどは**「機関」**の意味である（専門機関 9,735 文書、人道・援助の機関 1,856、情報機関・法執行機関 1,322、国際原子力機関 2,022、大文字の "the Agency" 1,222）。語の件数は、そのままでは**意味のある指標にならない**。

**行為主体性**（人や集団が自ら選び行動する力、英語の agency の社会科学的な用法）は、高精度の式（"women's agency"、"voice, agency and leadership"、"sense of agency" など）で 59 文書しか当たらず、1,000 文書あたりの文書数は 2005〜09 年に 0.2、2010〜14 年に 0.5、2015〜19 年に 2.5、2020〜23 年に 10.3 と、**2010 年代半ば以降に増える**。ただし式が狭く、実際の使用はこれより多いはずである。

- **最初の明確な例**: S/PV.6005（2008-10-29）の「平和と安全保障の領域で、女性の行為主体性の全力をどう引き出せるか」。
- **文脈**: 女性・平和・安全保障、青年、生存者（紛争関連の性暴力の被害者）、保健（産科瘻孔の決議 A/RES/73/147 の「声、行為主体性、リーダーシップ」）、核兵器への「人間の行為主体性と管理」（S/PV.9381、2023）。
- **機関の用法と混ざる**: 高精度の式でも、目視で読んだ 16 件のうち 3 件は機関の意味（"collective agency" は集団的な機関、"individual agency turf wars" は各機関の縄張り争い）だった。精度はおよそ 80%。

## 詳しく

### 語義ごとの式

| 語義 | 式（要約） | 文書数 |
|---|---|---|
| 機関（総称） | `(?i)\bagenc(y\|ies)\b` | 16,026 |
| 専門機関・国連の機関 | `specialized agenc`、`United Nations agenc`、`UN agenc` | 9,735 |
| 固有名（IAEA） | `International Atomic Energy Agency` | 2,022 |
| 固有名の略称 | `\bthe Agency\b`（大文字） | 1,222 |
| 人道・援助の機関 | `humanitarian agenc` など | 1,856 |
| 情報・法執行の機関 | `intelligence agenc` など | 1,322 |
| 行為主体性（高精度） | 別記（checks） | 59 |

### 広い式が使えない理由

"local agency"、"political agency"、"human agency" のような、行為主体性にも機関にも読める綴りは、最初に試した式では 684 文書に当たったが、1946〜53 年の決議の「国連朝鮮復興機関」（United Nations Korean Reconstruction Agency）や、"the Agency to act"（UNRWA）に当たる偽陽性が大量に混じった。そのため、左側の語を女性・青年・生存者などに限り、`agency` を小文字に固定した狭い式に絞った。

### 地理空間の語とのつながり

行為主体性の用法と地理空間の語が同じ文書に出るのは 2 文書で、つながりは読んでいない。「データの主体性」「地域社会の行為主体性」のような使い方が、地理空間・オープンデータの議論に出るかは、別途、語を足して調べる必要がある。

## よくあるまちがい

- `agency` の件数を、行為主体性の議論の広がりとみなす。大半は機関である。
- 左側の語を限らない広い式で、行為主体性の用法の初出を決める。
- 狭い式の 59 文書を、行為主体性の用法の全数とみなす。取りこぼしが大きい。

## 確かめた度合い

- `searched-undocs`: 件数、語義ごとの式、年別。高精度の式の当たり 16 件を目視で確認した（精度およそ 80%）。
- 未確認: 行為主体性の用法の全数、社会科学の用語としての初出（un-docs の外）、国別の使用、公式の PDF との突き合わせ。

## 出典

- yuiseki/un-docs（コミット 6cd1cf0）。式は `checks/keywords-human-security-nexus-agency.md`
- S/PV.6005、S/PV.9276 (Resumption 1)、S/PV.9381、A/RES/73/147（`https://docs.un.org/en/<記号>`）
