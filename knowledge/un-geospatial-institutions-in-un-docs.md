---
id: un-geospatial-institutions-in-un-docs
title: 国連の地理空間組織とミッションの GIS を、un-docs でどこまで数え上げられるか：前身の調査の確かめ直し
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。手順は checks/geospatial-institutions-recheck.md
  - hfu/kcai-yuiseki-datasets checks/un-docs-geospatial-institutions.tsv（226 文書の前身の分類）
  - 公式サイトの PDF との照合（約 40 文書。一覧は checks/geospatial-institutions-recheck.md）
  - https://docs.un.org/en/A/RES/69/308
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり。独立レビュー（2026-10-26）の指摘を反映して改訂
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

> 範囲: un-docs（総会と安保理の英語文書。安保理決議は 2699 まで）で、国連の地理空間に関する組織と、ミッションの GIS 機能を、どこまで数え上げられるかを調べた。ミッション予算の文書は un-docs に含まれない。そこで読んだ結果は、別の踏み跡（`mission-budgets-geospatial-output-lines`、`unlb-gis-function-in-budget-documents`）に分けた。

本書で「前身の調査」とは、hfu が先に行った調査（`hfu/kcai-yuiseki-datasets` の `knowledge/cross/un-docs-geospatial-institutions.md` と `checks/un-docs-geospatial-institutions.tsv`）を指す。前身の調査は、地図・GIS・地理空間の語を含む 226 文書を集め、区分に分けた。本書はそれを独立に再現して、確かめ直した。結論は四つある。

1. **226 文書の集合は、検索式を直すと正確に再現できた。** 式は `(?i:cartograph)|(?i:geo-?\s?spatial)|(?i:geographic(al)?\s+information\s+system)|\bGIS\b` で、大文字小文字の指定を語ごとに分ける（`GIS` は大文字のみ）。式全体を一つの `(?i)` で包むと、`GIS` が人名・地名の `gis` に当たって 290 文書に増え、64 文書が余計に入る。226 のうち 30 文書は、年次報告などの合冊（総会の `A/NN/49` 型の 25 本）と、安保理決議集 S/INF の 5 本で、同じ内容の二重計上になるため、前身は「合冊」として集計から除いた（`A/56/49[Vol.I](SUPP)` は記号の括弧が角括弧のため、前身は合冊と判定せず「その他」に入れていた）。
2. **前身の分類は概ね妥当だったが、三点を直した。** (a) 前身が「その他（自動）」とした 54 文書のうち 8 文書は、ニューヨークの地理空間情報課や UNLB とは別に、国連事務局が、海洋の境界を示す海図・座標を締約国から預かるために整備している地理情報システムの話だった。(b) ギニアビサウの 4 文書は「選挙の地図作成」の話で、GIS 機能ではない。(c) 前身の表の「要約」の列は、同じ主題の文書に同じ文が付けてあり、個々の文書の日付と合わないものがあった（UNAMI の訓練の年、シェバア農地の地図作成官の任命）。
3. **名称と組織の年表を、決議の文言から確定した**（`un-geospatial-organization-timeline`）。ニューヨークの地理空間情報課と、ブリンディジの地理空間・情報通信技術サービス部は別の部署である。
4. **検索語の漏れは小さかった。** `UNOSAT` が 4 文書あり（前身の 226 に入っているのは 1 文書）、`SAGE` の正式名を含む文書は 4 件ある（前身は 1 件と数えた。`sage-situational-awareness-geospatial-enterprise`）。`imagery` と `mapping` は多義で、機関の把握には使えない。

## 詳しく

### 226 文書の内訳（前身の分類と、今回の確かめ）

前身の区分の記号は次のとおり。H＝国連本部（ニューヨーク）の組織、U＝ブリンディジの国連兵站基地（UNLB）、M＝ミッション、P＝政策・技術の文脈での言及、N＝国連の GIS 機能とは別の意味で使われた語。

| 区分 | 件数 | 今回の確かめ |
|---|---|---|
| H-境界 | 33 | 国境画定への地図課・地図作成官の技術支援。安保理議長声明（S/PRST）と会議録（S/PV）が同じ声明を重複して含む |
| H-組織 | 4 | 全件で、本文と公式の PDF が一致（A/RES/57/300、58/101、67/287、69/308） |
| H-地図作成 | 1 | S/2011/30（地図の出典が地図課） |
| U-UNLB | 16 | 総会決議 6、UNAMI の行方不明者の報告 9、アビエ（UNISFA）の報告 1（S/2019/319）。要約の年が文書と合わないものがある（下記） |
| M-ミッション | 25 | 本文と合う。ただしギニアビサウの 4 文書は、選挙の地図作成として別の区分に移す。詳細は `un-mission-gis-mentions-in-un-docs` |
| P-政策 / P-技術 | 31 / 6 | 本書では再確認していない（`geospatial-themes-frameworks-conclusions` に重なる） |
| N-別の意味 | 26 | 例: 国連テロ対策委員会執行局の「Global Implementation Surveys（実施状況調査）」の略語 GIS、大陸棚限界委員会の審査用の GIS 研究室 |
| 合冊 | 30 | 二重計上のため除く |
| その他（自動） | 54 | 読み直した（下記） |

H-境界のうち、S/2005/673 の要約は、地図作成官の任命を述べるが、この文書の語は「legal, cartographic and historical evidence」だけで、任命の記述は無い。任命が文書に現れるのは、S/2006/933（2006-12-01）からである。

### 「その他（自動）」54 文書の読み直し

全件について、最初の出現の前後約 120 字を読んだ。多くは、各国の発言、政策決議、1950〜60 年代の会議録のフランス語 `cartographie`、「地図作成者」という比喩で、前身の判断のとおり、国連の組織や任務の話ではなかった。例外は次のとおり。

- **事務局の別の GIS（海洋の境界の寄託用）**: 「海洋と海洋法」の決議 A/RES/70/235（2015）、71/257、72/73、73/124、74/19、75/239、76/72 と、草案 A/77/L.36（2022）は、「事務総長が、国連海洋法条約にもとづいて締約国が寄託する海洋の境界の海図・座標のために整備している地理情報システム」に留意する（70/235 では第 7 項。公式の PDF と一致。同項は、2004 年の決議 59/24 第 6 項の要請に言及する）。担当部署の名前は文面に無い。前身は海洋法部（DOALOS）の GIS と書いたが、**文面では未確認**である。同じ文は、A/RES/77/248（A/77/L.36 の採択版）にもあり、前身は「政策」に分類している。分類の扱いは、これらの間で揃っていない。
- **候補（要読解）**: S/PV.518（1950-11-06）は、休戦協定の署名のために、「国連の軍事監視員のうち地図作成の作業を担う者」が公式地図を作る場面である（フランス語の通訳部分に `cartographie`）。国連の地図作成機能の早い例かもしれないが、どの機関かは確かめていない。
- 地域機関の記述: A/59/PV.40（2004）は、中部アフリカ諸国経済共同体（ECCAS）の職員に地図作成の研修を行う話である。
- 化学兵器禁止機関（OPCW）と国連の合同調査機構の記述: S/2017/552 は、地理空間の専門性をもつ外部機関に分析を依頼した、という話で、国連の GIS 機能ではない。

### 前身の表の「要約」が、文書ごとの事実と合わない例

前身の表の要約の列は、同じ主題の文書に同じ文が付けてあり、個々の文書の日付より後の出来事が書かれた行がある。

- **UNAMI の地中レーダーの訓練**: 「2022 年に 20 人。2023 年にブリンディジで 6 人」が S/2020/133、S/2020/358、S/2021/930、S/2022/100、S/2023/51 の全部に付いている。しかし S/2020/133 などは、訓練がまだ**延期中**と述べる。実施は、2021-11-07〜18（20 人、バグダッド）と、2022-11-07〜11（6 人、ブリンディジ）で、報告は S/2022/100 と S/2023/51 である。
- **G5 サヘルとアフリカ連合への支援**: 「地理空間情報システムと地図作成サービス」は S/2017/454 だけの文言である。S/2017/869、S/2018/432、S/2020/476 は「geospatial, telecommunications and information technology … support」の形である。
- **カメルーンとナイジェリア**: 「2015 年の合同技術チームに地理空間情報担当官が参加」という文が、2004〜2014 年の S/ 番号の文書にも付いている。これは、文書の日付より後の出来事なので外した。判断は日付の論理にもとづくもので、これらの文書の中身は通読していない。

### 検索語の漏れ（調べた結果）

| 語 | 件数 | 備考 |
|---|---|---|
| `UNOSAT` | 4 文書 | S/PV.7196、S/2015/368、S/2017/969、S/2018/171。前身の 226 に入っているのは S/2017/969 のみ |
| `SAGE`（Situational Awareness Geospatial Enterprise、ミッション内の状況把握の仕組み） | 正式名で 4 文書 | S/2021/501、S/PV.8838、S/2021/1110、S/PV.9389。略称 `SAGE` だけでは S/2021/1110 の 1 件しか当たらない |
| `mapping` | 539 文書 | 地理と無関係な用法が大半。WFP の「Vulnerability Analysis and Mapping Unit」が S/PV.4507（2002）に 1 件ある |
| `satellite imagery` | 171 文書 | `satellite imagery|images` にすると 194 文書。`imagery` 単独は 231 文書 |
| `United Nations Satellite Centre` | 0 | |

UNOSAT は、国連訓練調査研修所（UNITAR）の衛星応用プログラムで、衛星画像の分析を他の機関に提供する。4 文書では、その分析が引用されている（S/2015/368 はシリアの報告、S/2018/171 は北朝鮮の専門家パネルの報告）。S/PV.7196 は無人機の議論で、UNOSAT の衛星データ処理システムに触れる。国連の別の機関による衛星画像の分析として、地理空間の機関の候補に加える。

`satellite imagery` と `imagery` は、大半が他の機関や各国の分析（IAEA の査察、制裁の専門家パネルなど）で、国連の地理空間機能の記述ではないため、機関の把握には使えない（`satellite-imagery-in-security-council-who-and-why`）。

### 言えないこと

- ミッションの GIS 機能の大きさ（要員、予算、成果物）。un-docs には予算文書が無いので、予算文書を別に読んだ結果を参照する。予算案には、地理空間データの分析の面積と地図の枚数が成果物の行として書かれている（`mission-budgets-geospatial-output-lines`）。
- 「議論されていない」と言うこと。報告の本文に出ないだけである。
- 冒頭にミッション名のある報告のうち、地理空間の語を含む割合（21/1,045、約 2%）は、`scripts/mission_gis_ratio.py` で再現できるが、前身の 23/1,180 とは数え方が違う。

## よくあるまちがい

- 式全体に `(?i)` を付けて `GIS` を数える。人名・地名の `gis` に当たる。
- 前身の表の要約の年を、その文書の年とみなす。
- 公式サイトのページ（`docs.un.org/en/…`）を取得すれば本文が読めると考える。ページは PDF を埋め込む枠で、PDF は別の経路にある（`checks/geospatial-institutions-recheck.md`）。

## 確かめた度合い

- `searched-undocs`: 226 の再現（記号の集合が、両方向で一致した）、「その他」54 文書と M 25 文書の読み直し、検索語の漏れの調査、系列別の数。
- `read-official`: H-組織 4、U-UNLB の決議 6、ミッションの代表 8、H-境界の代表 6、UNAMI の文書 4 など約 40 文書の該当文を、公式の PDF と照合した（一覧は `checks/geospatial-institutions-recheck.md`）。
- `read-only`: 上記以外の文書は、un-docs の抽出テキストのみ。P-政策・P-技術・N の分類は再確認していない。カメルーン・ナイジェリアの要約の訂正は、日付の論理による。
- 未確認: S/PV.518 の機関。DOALOS の GIS という前身の記述。

## 出典

- yuiseki/un-docs（コミット 6cd1cf0）
- hfu/kcai-yuiseki-datasets `knowledge/cross/un-docs-geospatial-institutions.md`、`checks/un-docs-geospatial-institutions.tsv`
- A/RES/70/235 ほか（上記）、S/PV.518、S/2005/673、S/2006/933、S/PV.7196、S/2015/368、S/2017/969、S/2018/171、S/PV.4507（いずれも `https://docs.un.org/en/<記号>`）
