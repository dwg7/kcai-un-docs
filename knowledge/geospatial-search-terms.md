---
id: geospatial-search-terms
title: 「地理空間情報」を un-docs で探す語の表：展開、件数、外れ方
status: draft
verified_how: searched-undocs
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）の検索。手順は checks/geospatial-terms.md
  - hfu/kcai-yuiseki-datasets checks/check-2026-10-26-un-docs-geospatial.md（前身の検索）
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-26
related: [un-docs-reading-guide, geospatial-first-appearance]
cites:
  - un-docs: 語ごとの文書数と最初の文書
  - hfu-feasibility: 前身の語の選び方
finding:
  - ambiguous-term-needs-collocation
  - case-insensitive-acronym-false-hits
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書（ユニーク記号 37,567、合冊除外）。安保理決議は 2699 まで。

「地理空間情報」を探す語は 1 つでは足りず、**多義の語**（`mapping`、`cartograph*`、`imagery`、`GIS`）は、そのまま数えると外れる。次の表は、語ごとの件数と、外れ方。次の問い（防災、測地、衛星画像、ミッション）にも再利用できる。

| 語（regex） | 文書 | 最初（日付・種別）記号 | OCR | 主な系列 |
|---|---|---|---|---|
| geospatial `(?i)geo-?\s?spatial` | 73 | 2006-12-14（採択）A/RES/61/111 | 0 | A/RES 34、S/yyyy/n 30、A/PV 2 |
| geographic information `(?i)geographic(al)?\s+information` | 81 | 1987-12-11 A/RES/42/186 | 0 | A/RES 48、S/yyyy/n 11、A/PV 9 |
| geographic information system(s) | 60 | 同上 | 0 | A/RES 32、S/yyyy/n 11、A/PV 9 |
| GIS `\bGIS\b`（大文字の語） | 9 | 2001-05-14 S/PV.4319 | 0 | S/yyyy/n 5、S/RES 2、A/RES 1 |
| remote sensing `(?i)remote[\s-]+sensing` | 100 | 1971-11-29 A/RES/2778(XXVI)（un-docs の日付欄は 1970-12-16 で誤り） | 18 | A/RES 64、A/NN/n 17、A/PV 10 |
| earth observation `(?i)earth[\s-]+observation` | 48 | 1978-12-14 A/RES/33/71 | 1 | A/RES 36、A/NN/n 5、A/PV 4 |
| geodetic / geodesy `(?i)geodet|geodesy` | 31 | 1967-05-23 A/PV.1522 | 0 | S/yyyy/n 14、A/RES 13 |
| cartograph*（英語の語形）`(?i)\bcartograph(er|ers|ic|y)\b` | 67 | 1954-09-08 S/PV.680 | 0 | S/yyyy/n 28、S/PV 21、A/RES 7 |
| satellite imagery `(?i)satellite\s+(imagery|images?)` | 194 | 1987-12-11 A/RES/42/186 | 1 | S/yyyy/n 113、S/PV 68 |
| imagery `(?i)\bimagery\b` | 231 | 1963（比喩の用法を含む） | 1 | S/yyyy/n 133、S/PV 70 |
| spatial data `(?i)spatial\s+data` | 18 | 2006-12-14 A/RES/61/111 | 0 | A/RES 15 |
| geo-referenc* | 8 | 2018-07-25 S/2018/732 | 0 | A/RES 3、S/PV 2、S/yyyy/n 2 |
| UN-GGIM `GGIM|Global Geospatial Information Management|Committee of Experts on Global Geospatial`（大文字小文字を区別） | 2 | 2015-02-26 A/69/PV.80、A/RES/69/266 | 0 | A/RES 1、A/PV 1 |
| UNOSAT `UNOSAT` | 4 | 2014-06-11 S/PV.7196 | 0 | S/yyyy/n 3、S/PV 1 |
| SAGE `\bSAGE\b`（大文字の語） | 1 | 2021-12-31 S/2021/1110 | 0 | S/yyyy/n 1 |
| mapping `(?i)\bmapping\b`（全体） | 539 | 1960-07-13 S/PV.883 | 1 | S/yyyy/n 214、S/PV 150、A/RES 76 |
| mapping（地理的な連語に限る。checks/geospatial-terms.md の式） | 30 | 1997-09-19 A/RES/S-19/2 | 0 | A/RES 13 |

## 詳しく

### 外れ方

- **`mapping`**: 539 文書に当たるが、多くは「作業の洗い出し（mapping exercise）」などで地理と無関係。地理的な連語に絞ると 30 文書。**単独の語では使わない。**
- **`cartograph*`**: 大文字小文字を無視する素朴な式は、**フランス語の発言**（`cartographie`、1950 年代の S/PV）に当たる。英語の語形に限ると 67 文書だが、1990 年以前はほとんどが演説の中の「地図作成者」で、国連事務局の地図課とは無関係。
- **`GIS`**: 大文字の語に限る。大文字小文字を無視すると人名・地名の `gis` を拾う（前身の調査でも外していた）。大文字でも別の意味がある（`Global Implementation Surveys`＝テロ対策委員会執行局。S/RES/2395(2017)、S/RES/2617(2021)、S/2021/1107、S/2021/1116）。
- **`UN-GGIM`**: 最初の式（大文字小文字を無視し、`Geographic Information Management` も含む）は **117 文書**に当たったが、ほぼすべて**偽陽性**だった。大文字小文字を区別し、`GGIM` と正式名に限ると **2 文書**。UN-GGIM を設置したのは経済社会理事会で、その文書は un-docs に無い。総会決議 69/266 が引く形でしか現れない。
- **`imagery`**: 比喩の用法（修辞）にも当たる。`satellite imagery` に限ると 194 文書。
- **重複**: S/INF（決議集）と A/NN/L・A/NN/n の合冊・草案が、同じ文言を再掲する。**本数を言うときは系列を書く**。例: `geospatial` の 73 文書は、A/RES 34、S/ 番号の報告・書簡（S/yyyy/n）30、A/NN/n 2、A/PV 2、S/PV 2、A/NN/L 1、S/RES 1、S/INF 1。
- **OCR**: `remote sensing` は 18 文書が OCR（1970〜90 年代）。`geospatial` は OCR 0（2006 年以降しか出ないため）。他の語は古い年代の OCR の取りこぼしを含む。
- **日付**: A/RES は採択日、S/PV は会議日。**日付欄が誤っている行がある**（A/RES/2778(XXVI) の日付欄は 1970-12-16）。

### 対応する日本語

「地理空間情報」は、英語の `geospatial information` が中心だが、国連の文書では `geographic information (system)`、`remote sensing`、`earth observation`、`geodetic` が、文脈ごとに別の語として使われる。**公式の日本語訳（国連の他言語版）との対応は、英語版だけを見て整理したため未確認**。

## 悉皆の語彙（決定）と、衛星画像の主体の分け方

次の問い（防災、測地、衛星画像、ミッション）が使う語彙を、精度で 3 段に分けて決めた。件数はユニーク記号（合冊除外）の文書数。

| 段 | 語 | 件数 | 使い方 |
|---|---|---|---|
| A（そのまま使える） | `geospatial`（73）、`GIS`（大文字、9）、`geographic information system`（60）、`geodet*`（31）、`UN-GGIM` の名称（2）、`Cartographic (Section\|Unit)`（9）、`Geospatial Information Section`（4）、`UNOSAT`（4）、`SAGE`（1）、`geo-referenc*`（8）、`spatial data`（18）、`geographic data`（28。大半が A/RES の人道支援の定型文）、`geo-information`（2） | 小 | 件数は議論の厚みではない |
| B（連語・文脈で絞る） | `remote sensing`（100）、`earth observation`（48）、`satellite imagery`（194）、`mapping`（539→連語で 30）、`topographic`（76。1947 年の S/PV から出る）、`aerial photograph`（51）、`GPS`（74）、`situational awareness`（294。ほとんどが GIS と無関係）、`UAV/drone`（657。地理空間情報そのものではない） | 大 | 周辺 300 字の主体と目的を読む |
| C（使わない） | `imagery` 単独、大文字小文字を無視した `GIS`、大文字小文字を無視した `cartograph`（仏語の `cartographie`）、`spatial analysis`（0）、`geodatabase`（0） | — | 偽陽性が多い、または 0 件 |

### 衛星画像（`satellite imagery|images`、`imagery`）の主体（粗い分け）

合わせて 252 文書。周辺 300 字と冒頭 1,500 字の語で分けると（複数に当たる文書がある）、IAEA の査察・保障措置 53、国連ミッション・事務局の報告 35、制裁の専門家パネル・監視チーム 23、各国の発言・情報 19、OPCW 8、調査・人権 7、UNOSAT/UNITAR 2、どれにも当たらない 135。十年代別は 2000 年代 41、2010 年代 143、2020 年代 59、1990 年代以前は 7。系列は S/yyyy/n 136、S/PV 87。

- **国連自身の機能として語られる衛星画像**（UNOSAT、ミッションの地理空間の画像）は一部で、多くは**他機関・各国・専門家パネルが使う画像**の記述。「国連が衛星画像を使う」と読むには、主体を文書ごとに読む必要がある。
- 判定は機械的な簡易判定で、文書ごとの確認はしていない。確かめるなら B の語を、主体の語（Panel of Experts、UNITAR、IAEA など）と組み合わせた式で再検索する。

## よくあるまちがい

- `mapping` や `imagery` を足して「地理空間情報の議論が増えた」と言う。
- `UN-GGIM` を大文字小文字無視で数える。
- 語の件数を、本文が同一の行（S/INF、合冊、草案）を含めて数える。

## 確かめた度合い

- 件数、最初の文書は un-docs を検索して確かめた（`searched-undocs`）。表の式は `checks/geospatial-terms.md` と `scripts/undocs.py` で再現できる。
- 文脈の確認（外れ方の分類）は、各語の最初の数件と、`GIS`・`UNOSAT` の全件を読んだ。`mapping` の 539 文書は全件を読んでいない（連語で絞った 30 文書の割合を示したにとどまる）。
- 公式原文との照合は、`geospatial` の最初（A/RES/61/111）などに限る（`geospatial-first-appearance`）。

## 出典

- yuiseki/un-docs `documents.parquet`（コミット 6cd1cf0）
- hfu/kcai-yuiseki-datasets `checks/check-2026-10-26-un-docs-geospatial.md`
