---
id: un-geospatial-institutions-in-un-docs
title: 地理空間情報課・UNLB の地理空間サービス・ミッションの GIS 機能：un-docs の悉皆的な把握の確かめ直し
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。手順は checks/geospatial-institutions-recheck.md
  - hfu/kcai-yuiseki-datasets checks/un-docs-geospatial-institutions.tsv（226 文書の前身の分類）
  - 公式サイトの PDF との照合（約 30 文書。対象は checks/geospatial-institutions-recheck.md）
  - https://docs.un.org/en/A/RES/69/308
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-26
related: [un-geospatial-organization-timeline, un-mission-gis-mentions-in-un-docs, geospatial-search-terms, un-docs-reading-guide]
cites:
  - un-docs: 226 文書の集合の再現と、分類の読み直し
  - undocs-site: 引用する文の照合
  - hfu-institutions: 前身の分類表
finding:
  - recount-reproduces-226-exactly
  - group-level-summaries-misdate-documents
  - missing-category-secretariat-gis-for-ocean-boundaries
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書（安保理決議は 2699 まで）。**ミッションの GIS 機能の本体はミッション予算の文書にあり、un-docs には無い**ので、その部分は未確認のまま。

前身（hfu）の悉皆的な把握を、独立に再現して確かめ直した。結論は 4 つ。

1. **226 文書の集合は、検索式を直すと正確に再現できた。** 式は `(?i:cartograph)|(?i:geo-?\s?spatial)|(?i:geographic(al)?\s+information\s+system)|\bGIS\b`（大文字小文字の指定を語ごとに分ける。`GIS` は大文字のみ）。式を一つの `(?i)` で包むと `GIS` が人名・地名に当たって 290 文書に増え、64 文書が余計に入る。226 には、記号に Vol を含む総会決議の合冊が 26、決議集 S/INF が 5 含まれ、前身はこれらを（`A/74/49(Vol.I)` を含めて）「合冊」30 として集計から除いている。
2. **分類は概ね妥当。ただし 3 点を直す。** (a)「その他（自動）」54 文書のうち 8 は、**事務局の別の GIS（海洋の境界の図・座標の寄託用）**で、国連の GIS 機能の話。(b) ギニアビサウの 4 文書は「選挙の地図作成」で、GIS 機能ではない。(c) 要約文は**グループ単位**で、個々の文書の日付と合わないものがある（UNAMI の訓練の年、シェバア農地の地図作成官の任命）。
3. **名称と組織の年表を、決議の文言から確定した**（`un-geospatial-organization-timeline`）。ニューヨークの地理空間情報課と、ブリンディジの地理空間・情報・通信技術サービスは別の組織。
4. **検索語の漏れ**は小さい。`UNOSAT` が 4 文書（前身の 226 に 1）、`SAGE` が 1 文書（226 に入っている）、`imagery` と `mapping` は多義で、機関の把握には使えない。

## 詳しく

### 226 文書の内訳（前身の分類と、今回の確かめ）

| 区分 | 件数 | 今回の確かめ |
|---|---|---|
| H-境界 | 33 | 国境画定への地図課・地図作成官の技術支援。S/PRST と S/PV が同じ声明を重複して含む。**S/2005/673 の要約は、地図作成官の任命を述べるが、この文書の語は「legal, cartographic and historical evidence」で、任命の記述は無い**（任命は S/2006/933、2006-12-01 から） |
| H-組織 | 4 | 全件で本文と公式の PDF が一致（A/RES/57/300、58/101、67/287、69/308） |
| H-地図作成 | 1 | S/2011/30（地図の出典が地図課） |
| U-UNLB | 16 | 決議 6、UNAMI の文書 10。**要約の年が文書と合わない**ものがある（下記） |
| M-ミッション | 25 | 本文と合う。ただしギニアビサウ 4 は選挙の地図作成（P）に移す。詳細は `un-mission-gis-mentions-in-un-docs` |
| P-政策 / P-技術 | 31 / 6 | 本書では再確認していない（`geospatial-themes-frameworks-conclusions` に重なる） |
| N-別の意味 | 26 | `Global Implementation Surveys` など。S/PV.518 の仲間は下記 |
| 合冊 | 30 | 二重計上。除外 |
| その他（自動） | 54 | 読み直した（下記） |

### 「その他（自動）」54 文書の読み直し

全件の周辺（前後約 120 字）を読んだ。多くは、各国の発言、政策決議、フランス語の `cartographie`（1950〜60 年代の S/PV）、「地図作成者」の比喩で、前身の判断のとおり**国連の組織・任務の話ではない**。例外は次のとおり。

- **事務局の別の GIS**: A/RES/70/235（2015）、71/257、72/73、73/124、74/19、75/239、76/72、A/77/L.36（草案、2022）の「海洋と海洋法」の決議・草案は、「**事務総長が、国連海洋法条約に基づき締約国が寄託する、海洋の境界の海図・座標のために整備している地理情報システム**」に留意する（A/RES/70/235 第 7 項。公式の PDF と一致。同項は 2004 年の決議 59/24 第 6 項の要請に言及する）。担当部署の名前は文面に無い（前身は海洋法部 DOALOS の GIS と書いたが、**文面では未確認**）。
- **候補（要読解）**: S/PV.518（1950-11-06）は、休戦協定の署名に向けて「国連の軍事監視員のうち地図作成の作業を担う者」が公式地図を作る場面（フランス語の通訳部分に `cartographie`）。国連の地図作成機能の早い例かもしれないが、機関の特定は未確認。
- 地域機関の記述: A/59/PV.40（2004、ECCAS の職員に地図作成の研修）。
- OPCW・国連共同調査機構の記述: S/2017/552（地理空間の専門性を持つ外部機関に分析を依頼）。国連の GIS ではない。

### 要約文が文書ごとの事実と合わない例

前身の表の `gist_ja` は、同じ主題のグループに同じ文言が付いている。その結果、文書の日付以降の出来事が書かれた行がある。

- **UNAMI の地中レーダーの訓練**: 「2022 年に 20 人。2023 年にブリンディジで 6 人」が S/2020/133、S/2020/358、S/2021/930、S/2022/100、S/2023/51 の全部に付くが、S/2020/133 などは訓練が**延期中**と述べる。実施は **2021-11-07〜18（20 人、バグダッド）** と **2022-11-07〜11（6 人、ブリンディジ）**（報告は S/2022/100 と S/2023/51）。
- **シェバア農地**: S/2005/673（2005-10-26）に「上級地図作成官の任命」は無い。
- **G5 サヘル・AU 支援**: 「地理空間情報システムと地図作成サービス」は S/2017/454 だけの文言で、S/2017/869、S/2018/432、S/2020/476 は「geospatial, telecommunications and information technology … support」の形。
- **カメルーン・ナイジェリア**: 「2015 年の合同技術チームに地理空間情報担当官が参加」が 2004〜2014 年の S/ 文書にも付く。

### 検索語の漏れ（問い 3 の (a)）

| 語 | 結果 |
|---|---|
| `UNOSAT` | 4 文書（S/PV.7196、S/2015/368、S/2017/969、S/2018/171）。226 に入っているのは S/2017/969 のみ。国連訓練調査研修所（UNITAR）の衛星応用プログラムの分析が、シリアの報告や北朝鮮の専門家パネルの報告に引かれる。S/PV.7196 は無人機の議論で「UNOSAT の衛星データ処理システム」に触れる。**国連の別の機関による衛星画像の分析**として追加の候補。 |
| `SAGE` | 1 文書（S/2021/1110）。226 に入っている |
| `mapping` | 539 文書だが地理と無関係が大半。`Vulnerability Analysis and Mapping Unit`（WFP）が S/PV.4507（2002）に 1 件 |
| `imagery` / `satellite imagery` | 231 / 194 文書。大半は他機関・各国の分析（IAEA の査察、制裁の専門家パネルなど）で、国連の地理空間機能の記述ではない。**機関の把握には使えない** |
| `United Nations Satellite Centre` | 0 |

### 言えないこと

- ミッションの GIS 機能の大きさ・要員・成果物（予算文書）。冒頭にミッション名を持つ S/yyyy/n・A/NN/n・S/INF のうち地図・GIS・地理空間の語を含む文書は、再現では 21/1,045（約 2%）。前身の 23/1,180 とは数え方（ミッション名の式、系列）が違い、**完全な再現ではない**。
- 「議論されていない」と言うこと。報告の本文に出ないだけ。

## よくあるまちがい

- `(?i)` を式全体に付けて `GIS` を数える。人名・地名の `gis` に当たる。
- 要約文の年を、その文書の年とみなす。
- 公式サイトのページ（`docs.un.org/en/…`）を、そのまま取得して本文が読めると考える。ページは PDF を埋め込む枠で、PDF は別の経路にある（`checks/geospatial-institutions-recheck.md`）。

## 確かめた度合い

- `searched-undocs`: 226 の再現（記号の集合が両方向で一致）、54 文書と 25 文書の読み直し、検索語の漏れの調査、系列別の数。
- `read-official`: H-組織 4、U-UNLB の決議 6、M の代表 8、H-境界の代表 6、UNAMI の文書 4 など約 30 文書の該当文を、公式の PDF と照合した（一覧は `checks/geospatial-institutions-recheck.md`）。
- `read-only`: 上記以外の文書は un-docs の抽出テキストのみ。P-政策・P-技術・N の分類は再確認していない。
- 未確認: ミッション予算の文書、UN-GGIM、ECOSOC。S/PV.518 の機関。DOALOS の GIS という前身の記述。

## 出典

- yuiseki/un-docs（コミット 6cd1cf0）
- hfu/kcai-yuiseki-datasets `knowledge/cross/un-docs-geospatial-institutions.md`、`checks/un-docs-geospatial-institutions.tsv`
- A/RES/70/235 ほか（上記）、S/PV.518、S/2005/673、S/2006/933、S/PV.7196、S/2015/368、S/2017/969、S/2018/171、S/PV.4507（いずれも `https://docs.un.org/en/<記号>`）
