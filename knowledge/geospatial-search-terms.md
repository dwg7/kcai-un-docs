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

「地理空間情報」について un-docs を検索するには、語を 1 つに決めることができない。さらに、複数の意味を持つ語（`mapping`、`cartograph*`、`imagery`、`GIS`）は、そのまま数えると、地理空間情報と関係のない文書まで数えてしまう。次の表は、語ごとの文書数と、外れる理由をまとめたものである。防災、測地、衛星画像、国連ミッションを扱う次の問いでも、この表を使い回せる。

| 語と式（regex） | 文書数 | 最初の文書（日付。種別は A/RES は採択日、S/PV は会議日など） | OCR の文書数 | 主な系列 |
|---|---|---|---|---|
| geospatial `(?i)geo-?\s?spatial` | 73 | 2006-12-14（採択）A/RES/61/111 | 0 | A/RES 34、S/yyyy/n 30、A/PV 2 |
| geographic information `(?i)geographic(al)?\s+information` | 81 | 1987-12-11 A/RES/42/186 | 0 | A/RES 48、S/yyyy/n 11、A/PV 9 |
| geographic information system(s) `(?i)geographic(al)?\s+information\s+systems?` | 60 | 同上 | 0 | A/RES 32、S/yyyy/n 11、A/PV 9 |
| GIS `\bGIS\b`（大文字の語。9 文書のうち 4 文書は別の意味） | 9 | 2001-05-14 S/PV.4319 | 0 | S/yyyy/n 5、S/RES 2、A/RES 1 |
| remote sensing `(?i)remote[\s-]+sensing` | 100 | 1971-11-29 A/RES/2778(XXVI)（un-docs の日付欄は 1970-12-16 で誤り） | 18 | A/RES 64、A/NN/n 17、A/PV 10 |
| earth observation `(?i)earth[\s-]+observation` | 48 | 1978-12-14 A/RES/33/71 | 1 | A/RES 36、A/NN/n 5、A/PV 4 |
| geodetic / geodesy `(?i)geodet|geodesy` | 31 | 1967-05-23 A/PV.1522 | 0 | S/yyyy/n 14、A/RES 13 |
| cartograph の英語の語形 `(?i)\bcartograph(er|ers|ic|y)\b` | 67 | 1954-09-08 S/PV.680 | 0 | S/yyyy/n 28、S/PV 21、A/RES 7 |
| satellite imagery `(?i)satellite\s+(imagery|images?)` | 194 | 1987-12-11 A/RES/42/186 | 1 | S/yyyy/n 113、S/PV 68 |
| imagery `(?i)\bimagery\b` | 231 | 1963（比喩の用法を含む） | 1 | S/yyyy/n 133、S/PV 70 |
| spatial data `(?i)spatial\s+data` | 18 | 2006-12-14 A/RES/61/111 | 0 | A/RES 15 |
| geo-referenc*（`(?i)geo-?referenc`） | 8 | 2018-07-25 S/2018/732 | 0 | A/RES 3、S/PV 2、S/yyyy/n 2 |
| UN-GGIM `GGIM|Global Geospatial Information Management|Committee of Experts on Global Geospatial`（大文字小文字を区別） | 2 | 2015-02-26 A/69/PV.80、A/RES/69/266 | 0 | A/RES 1、A/PV 1 |
| UNOSAT `UNOSAT` | 4 | 2014-06-11 S/PV.7196 | 0 | S/yyyy/n 3、S/PV 1 |
| SAGE `\bSAGE\b`（大文字の語） | 1 | 2021-12-31 S/2021/1110 | 0 | S/yyyy/n 1 |
| mapping `(?i)\bmapping\b`（全体） | 539 | 1960-07-13 S/PV.883 | 1 | S/yyyy/n 214、S/PV 150、A/RES 76 |
| mapping（地理に関わる連語に限る。式は `checks/geospatial-terms.md` にある） | 30 | 1997-09-19 A/RES/S-19/2 | 0 | A/RES 13 |

## 詳しく

### 外れ方

- **`mapping`**: 539 文書に当たるが、多くは「作業の洗い出し（mapping exercise）」などで地理と無関係。地理的な連語に絞ると 30 文書。**単独の語では使わない。** 539 文書から 30 文書を無作為に抜いて最初の出現を読むと、地理に関わる使い方は 8 件ほどで、残りは「mapping exercise」のほか、関係者や能力の洗い出しなど多様だった。
- **`cartograph*`**: 大文字小文字を無視する素朴な式は、**フランス語の発言**（`cartographie`、1950 年代の S/PV）に当たる。英語の語形に限ると 67 文書だが、1990 年以前はほとんどが演説の中の「地図作成者」で、国連事務局の地図課とは無関係。
- **`GIS`**: 大文字の語に限る。大文字小文字を無視すると人名・地名の `gis` を拾う（前身の調査でも外していた）。大文字でも別の意味がある。テロ対策委員会執行局（CTED）が行う「世界実施調査」（Global Implementation Surveys）を指す場合で、S/RES/2395(2017)、S/RES/2617(2021)、S/2021/1107、S/2021/1116 がそうである。
- **`UN-GGIM`**: 最初の式（大文字小文字を無視し、`Geographic Information Management` も含む）は **117 文書**に当たったが、ほぼすべて**偽陽性**だった。大文字小文字を区別し、`GGIM` と正式名に限ると **2 文書**。UN-GGIM（国連地球規模の地理空間情報管理専門家委員会）を設置したのは経済社会理事会で、その決議は un-docs に入っていない。un-docs では、総会決議 69/266 が経済社会理事会の決議を引く形でしか出てこない。
- **`imagery`**: 比喩の用法（修辞）にも当たる。`satellite imagery` に限ると 194 文書。
- **重複**: S/INF（決議集）と、総会の文書番号の形が `A/NN/L.NN`（決議案）や `A/NN/NN`（報告書など）の合冊・草案は、ほかの記号の文書と同じ文言を再掲する。文書の本数を示すときは、どの系列かを併記する。例: `geospatial` の 73 文書は、A/RES 34、S/ 番号の報告・書簡（S/yyyy/n）30、A/NN/n 2、A/PV 2、S/PV 2、A/NN/L 1、S/RES 1、S/INF 1。
- **OCR**: `remote sensing` は 18 文書が OCR（1970〜90 年代）。`geospatial` は OCR 0（2006 年以降しか出ないため）。他の語は古い年代の OCR の取りこぼしを含む。
- **日付**: A/RES は採択日（無ければ配布日）、S/PV は会議日。日付欄が誤っている行がある（A/RES/2778(XXVI) の日付欄は 1970-12-16）。

### 対応する日本語

「地理空間情報」は、英語の `geospatial information` が中心である。un-docs の英語文書では、これに近い内容が `geographic information (system)`、`remote sensing`、`earth observation`、`geodetic` という別々の語で書かれ、話題（環境、宇宙、軍縮、測量）ごとに使い分けられている。**公式の日本語訳（国連の他言語版）との対応は、英語版だけを見て整理したため未確認**。

## 次の問いで使う語彙の 3 段階と、衛星画像の主体の分け方

次の問い（防災、測地、衛星画像、ミッション）で使う語を、精度で 3 段に分ける。これはこの踏み跡限りの暫定の分け方で、`DECISIONS.md` の決定ではない。件数は、同じ記号を 1 本にまとめ合冊を除いた文書数。

| 段 | 語（式は上の表のものを除き、下に示す） | 文書数の目安 | 使い方 |
|---|---|---|---|
| A（そのまま検索できる） | `geospatial`（73）、`geographic information system`（60）、`geodet*`（31）、`UN-GGIM` の名称（2）、`Cartographic (Section\|Unit)`（9）、`Geospatial Information Section`（4）、`UNOSAT`（4）、`SAGE` の正式名 `Situational\s+Awareness\s+Geo`（4。大文字 `\bSAGE\b` だけでは 1）、`geo-referenc*`（8）、`spatial data`（18）、`geographic data`（`(?i)geographic(al)?\s+data`、28。大半が A/RES の人道支援の定型文）、`geo-information`（2） | 少ない | 件数の少なさは、議論の薄さを意味しない |
| B（連語や文脈で絞る） | `GIS`（大文字、9。うち 4 は別の意味）、`remote sensing`（100）、`earth observation`（48）、`satellite imagery`（194）、`mapping`（539。連語に絞って 30）、`topograph`（`(?i)topograph`、76。1947 年の S/PV から出る）、`aerial photograph` に近い語（`(?i)aerial\s+(photo\w*\|survey\w*\|imag\w+\|map\w*)`、51）、`GPS`（`\bGPS\b\|(?i)global\s+positioning`、74）、`situational awareness`（`(?i)situational\s+awareness`、294。ほとんどが GIS と無関係）、`UAV/drone`（`(?i)\bUAVs?\b\|(?i)\bdrones?\b\|(?i)unmanned\s+aerial`、657。地理空間情報そのものではない） | 多い | 周辺 300 字を読み、主体と目的で絞る |
| C（使わない） | `imagery` 単独、大文字小文字を無視した `GIS`、大文字小文字を無視した `cartograph`（仏語の `cartographie` に当たる）、`spatial analysis`（検索すると 0 件）、`geodatabase`（同じく 0 件） | — | 偽陽性が多いか、0 件で使えない |

### 衛星画像（`satellite imagery|images`、`imagery`）の主体（粗い分け）

合わせて 252 文書。周辺 300 字と冒頭 1,500 字の語で機械的に分けた参考値は次のとおり（複数に当たる文書がある。この分けの式は `checks/` に残しておらず、独立の再計算では再現できなかった）。IAEA（国際原子力機関）の査察・保障措置 53、国連ミッション・事務局の報告 35、制裁の専門家パネル・監視チーム 23、各国の発言・情報 19、OPCW 8、調査・人権 7、UNOSAT/UNITAR 2、どれにも当たらない 135。十年代別は 2000 年代 41、2010 年代 143、2020 年代 59、1990 年代以前 7（日付の無い 2 文書は含まない）。系列は S/yyyy/n 136、S/PV 87。

- **国連自身の機能として語られる衛星画像**（UNOSAT、ミッションの地理空間の画像）は一部で、多くは**他機関・各国・専門家パネルが使う画像**の記述。「国連が衛星画像を使う」と読むには、主体を文書ごとに読む必要がある。
- 判定は機械的な簡易判定で、文書ごとの確認はしていない。確かめるなら B の語を、主体の語（Panel of Experts、UNITAR、IAEA など）と組み合わせた式で再検索する。

## よくあるまちがい

- `mapping` や `imagery` を足して「地理空間情報の議論が増えた」と言う。
- `UN-GGIM` を大文字小文字無視で数える。
- 語の件数を、本文が同一の行（S/INF、合冊、草案）を含めて数える。

## 確かめた度合い

- 件数と最初の文書は、un-docs を検索して確かめた（`searched-undocs`）。上の表と段 B の式は、`scripts/undocs.py search` にそのまま渡して再現できる。再現できないのは、衛星画像の主体の分けである。
- 文脈の確認（外れ方の分類）は、各語の最初の数件と、`GIS`・`UNOSAT` の全件を読んだ。`mapping` の 539 文書は全件を読んでいない（連語で絞った 30 文書の割合を示したにとどまる）。
- 公式原文との照合は、`geospatial` の最初（A/RES/61/111）などに限る（`geospatial-first-appearance`）。

## 出典

- yuiseki/un-docs `documents.parquet`（コミット 6cd1cf0）
- hfu/kcai-yuiseki-datasets `checks/check-2026-10-26-un-docs-geospatial.md`
