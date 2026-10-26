---
id: geospatial-first-appearance
title: 「地理空間情報」の初出：語ごとに違う、そして日付と隣の決議に注意
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）の検索。手順は checks/geospatial-terms.md
  - A/RES/61/111、A/RES/66/288、A/RES/69/266、A/RES/70/1（公式サイトの PDF と照合）
  - https://docs.un.org/en/A/RES/61/111
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-26
related: [un-docs-reading-guide, geospatial-search-terms, geospatial-themes-frameworks-conclusions]
cites:
  - un-docs: 語ごとの最初の文書と、その文脈
  - undocs-site: A/RES/61/111 第 48 項などの文言の照合
finding:
  - word-first-differs-by-term
  - date-field-can-be-wrong
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書。安保理決議は 2699 まで。以下は「un-docs で見つかった最も早い文書」であり、国連全体の初出ではない。

`geospatial`（geo-spatial）という**語**の un-docs での初出は、**A/RES/61/111（2006-12-14 採択）**。宇宙空間平和利用委員会の議題に「宇宙由来の地理空間データの持続可能な開発への国際協力」を加える決定の中に出る（第 48 項。公式の PDF で確認）。ただし、**「地理空間の情報」という内容**の語は、これより前から別の語で出る。

| 語 | un-docs で最も早い文書 | 一言 |
|---|---|---|
| remote sensing | A/RES/2778(XXVI)（1971-11-29 採択。un-docs の日付欄は 1970-12-16 で誤り） | 「衛星による地球のリモートセンシング作業部会の召集」。宇宙の平和利用の枠 |
| geodetic | A/PV.1522（1967-05-23）、総会の議事録の発言 | 衛星による測地基準系の話。決議・議長声明ではない |
| earth observation | A/RES/33/71（1978-12-14）、J 部「軍縮協定の監視」 | 軍縮の検証手段として |
| geographic information (system) | A/RES/42/186（1987-12-11）、附属書「2000 年以降の環境の展望」 | 天然資源のデータベース作りに衛星画像・航空写真・GIS を使う |
| satellite imagery | 同上（A/RES/42/186） | 同上 |
| GIS（略語） | S/PV.4319（2001-05-14）、安保理の会議録 | ギニア・シエラレオネ・リベリアの小地域での情報交換に GIS データ |
| **geospatial** | **A/RES/61/111（2006-12-14）** | 上記。以後 2015 年に 11 文書に増える |
| UN-GGIM | A/69/PV.80、A/RES/69/266（2015-02-26） | 設置は経済社会理事会（un-docs に無い）。総会決議が引く形 |
| UNOSAT | S/PV.7196（2014-06-11） | 4 文書のみ |

## 詳しく

- **geospatial の年別**（ユニーク記号）: 2006・07・08 年に各 1、2011 年 1、2012 年 2、2013 年 1、2014 年 2、**2015 年 11**、2016 年 5、2017 年 7、2018 年 4、2019 年 8、2020 年 8、2021 年 9、2022 年 9、2023 年 3。2009・2010 年は 0。2015 年の山は、UN-GGIM と測地基準系の決議 69/266 とその議事録（A/69/PV.80）、仙台防災枠組 69/283、2030 アジェンダ 70/1、事務局の組織の決議 69/308・69/309 などが同じ年に出たため。S/ 番号の報告・書簡は 2015 年に 2、2017 年に 6、2019〜2021 年に 18、2022・2023 年に各 1。2019〜2023 年の 37 文書のうち 20 が S/ 番号の文書（`geospatial-themes-frameworks-conclusions`）。
- **宇宙委員会の枠**: A/RES/61/111 の後、2006 年から毎年の「宇宙空間の平和利用における国際協力」の決議に、`geospatial` を含む定型文が繰り返される（62/217、63/90、66/71、67/113、68/75、69/85、70/82、71/90、72/77、73/91、74/82、76/76、77/121 ほか）。
- **日付欄の誤り**: A/RES/2778(XXVI) は日付欄が 1970-12-16（文中に引かれた別の決議の日付に見える）だが、同じ年の決議集（A/RES/2776(XXVI) の OCR 本文、A/8429 の補遺）は 1971-11-29 の採択とする。「最も早い日付」で並べると、このような行が先頭に来る。

## よくあるまちがい

- 「国連で地理空間情報が議論されるのは 2006 年から」。`geospatial` という語が 2006 年からで、衛星・測地・GIS は 1960〜80 年代から別の語で出る。
- 1970〜80 年代の A/RES の語の初出を、その決議の内容とする。A/RES/2776〜2779(XXVI) の 4 行はいずれも「2778 (XXVI) Convening of the Working Group on Remote Sensing …」の見出しを含む（決議集の見開き・目次に由来）。A/RES/33/71 は 13 部の総合的な軍縮決議のうち J 部。A/RES/42/186 の当該箇所は、決議自身の附属書の中（un-docs の節の位置と公式の PDF で確認済み）。
- 古い年代の初出を「実際の初出」とする。OCR（1980 年代 20%）で取りこぼしうる。
- UN-GGIM の活動を un-docs で追う。設置決議（経済社会理事会 2011/24）は、決議 69/266 の前文が番号を引いているが、原文は un-docs に無い。

## 確かめた度合い

- `searched-undocs`: 語ごとの最初の文書と、年別の件数、最初の数件の文脈。
- `read-official`: A/RES/61/111 第 48 項（`geospatial` を含む文）、A/RES/66/288、A/RES/69/266、A/RES/70/1 の該当文言を公式の PDF で確かめた。A/RES/69/308 の「Renaming of the Cartographic Section to the Geospatial Information Section」、A/RES/42/186（附属書の (q) 項）、A/RES/73/231 も確認。
- 同じく公式の PDF と文言が一致: A/RES/2778(XXVI)、A/RES/33/71（J 部）、A/PV.1522（PAGEOS の一文）、S/PV.4319。
- `read-only`: 上の一致は語を含む文の確認にとどまる。決議の内容全体の解釈、各語の次点以降の文書は読んでいない。
- 未確認: 公式サイトの他言語版での対応語。1971 年の決議の採択日は、un-docs 内の別の文書（決議集の OCR）からの推定で、公式原文では確かめていない。

## 出典

- yuiseki/un-docs（コミット 6cd1cf0）。手順は `checks/geospatial-terms.md`
- A/RES/61/111、A/RES/62/217、A/RES/66/288、A/RES/69/266、A/RES/69/283、A/RES/69/308、A/RES/70/1、A/RES/2778(XXVI)、A/RES/33/71、A/RES/42/186、A/PV.1522、S/PV.4319、A/69/PV.80（いずれも `https://docs.un.org/en/<記号>`）
