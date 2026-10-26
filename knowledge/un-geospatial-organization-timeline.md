---
id: un-geospatial-organization-timeline
title: 国連事務局の地図課から地理空間情報課へ、ブリンディジの GIS センターから地理空間・情報通信技術サービス部へ：名称と組織の年表
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。手順は checks/geospatial-institutions-recheck.md
  - A/RES/57/300、58/101、60/267、61/277、67/287、69/308、69/309、70/288、72/287、73/310（公式サイトの PDF と照合）
  - https://docs.un.org/en/A/RES/69/308
  - hfu/kcai-yuiseki-datasets の knowledge/cross/un-docs-geospatial-institutions.md（本書で「前身の調査」と呼ぶ。本書で文書ごとに確かめ直した）
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり。独立レビュー（2026-10-26）の指摘を反映して改訂
reviewed_by: []
updated: 2026-10-26
related: [un-geospatial-institutions-in-un-docs, un-mission-gis-mentions-in-un-docs, un-docs-reading-guide, unlb-gis-function-in-budget-documents]
cites:
  - un-docs: 組織の決定を述べる総会決議の本文
  - undocs-site: 各決議の該当する文の照合
  - hfu-institutions: 前身の調査の年表との照合
finding:
  - two-similarly-named-units-are-different
  - name-forms-vary-in-text
---

## 要点

> 範囲: un-docs（総会と安保理の英語文書）で、組織の名称や再編を述べる文書を追った。ミッション予算や事務局内部の文書は含まれないので、呼称の変遷は、**総会決議が述べた範囲**でしか追えない。予算文書で補った部分は `unlb-gis-function-in-budget-documents` にある。

名前の似た二つの組織を区別する。

1. **ニューヨークの地図課。** 2015-06-25 の総会決議 69/308 で、現地支援局（DFS、2007〜2019 年に平和維持活動を支えた事務局の部局）の情報通信技術部の「Cartographic Section（地図課）」が、「Geospatial Information Section（地理空間情報課）」に改称された。呼称は 2000 年から文書に出る（当初は「Chief Cartographer（地図作成官）」や「Cartographic Unit」で、「Cartographic Section」は 2001-04-19 の S/PV.4310 から）。
2. **ブリンディジの国連兵站基地（UNLB、現在はグローバル・サービスセンターの一部）にある GIS の組織。** 2006 年に総会が「地理情報システムセンター」の設置提案に留意した。2015 年の決議 69/309 には「Service for Geospatial, Information and Telecommunications Technologies（地理空間・情報通信技術サービス部）」の名前で出てくる。この二つが同じ組織の改称なのか、再編なのかは、総会決議だけでは分からず、予算文書で補った（`unlb-gis-function-in-budget-documents`）。

## 詳しく

### 年表

日付は、公式の PDF に採択日が書かれているものは採択日、それ以外は un-docs の日付欄の日付（種別を併記）である。

| 日付 | 文書 | 事項 | 公式原文との照合 |
|---|---|---|---|
| 2000-06-18（配布） | S/PRST/2000/21 | 安保理議長声明が、レバノンからの撤退線の確認で、事務総長の「Chief Cartographer」の努力に評価を示した | 照合済み |
| 2000-11-17（会議日） | S/PV.4227 | エチオピアとエリトリアの国境画定で、国連の「Cartographic Unit」の役割に、発言国（フランス）が言及した | 未照合 |
| 2000-12-15（配布） | S/2000/1194 | 合意で、国連の地図作成官が国境委員会の書記を務める | 日付と該当語を確認 |
| 2001-04-19（会議日） | S/PV.4310 | 国境委員会の後方支援の見積りで、事務次長ゲエノ氏の答弁で「地図課長室（the office of the Chief of the Cartographic Section）」の班が現地調査中、事務次長補アニャビ氏も「Cartographic Section」に触れる（`s-pv-4310-cartographic-section-and-chief-cartographer`）。「Chief Cartographer」「Cartographic Unit」の語はこの会合に無い | 公式の PDF で照合済み |
| **2002-12-20**（採択。配布は 2003-02-07） | A/RES/57/300 | 総会が、事務総長の「地図課の機能と資源を広報局から平和維持活動局へ移す」提案に留意し、この提案を 2004〜2005 年度の予算案の審議の中で検討すると決めた | 照合済み |
| 2003-12-09（採択。配布は 12-17） | A/RES/58/101 | 総会が、地図課の機能の広報局から平和維持活動局への移管を歓迎した（地図課の成果が平和維持活動局の需要に近いため） | 照合済み |
| 2006-06-30（採択） | A/RES/60/267 | 総会が、UNLB に 2007/08 年度に「geographical information system centre」を置くという事務総長の提案に留意した | 照合済み |
| 2006-12-01 | S/2006/933 | レバノンのシェバア農地について、事務総長が**上級地図作成官**を任命したと述べる。安保理議長声明 S/PRST/2006/52（12-12）がこれに留意した | S/PRST/2007/29 の「cartographer」の語を照合 |
| 2007-06-29（採択） | A/RES/61/277 | 総会が、GIS センター長（P-4 のポスト）の新設と、臨時の職として、GIS 担当官（P-3）、GIS 管理者（Field Service）、国内の一般職員 5 人を承認した | 照合済み |
| 2007-06-29（採択） | A/RES/61/287 | 総会が、国連兵力引き離し監視隊（UNDOF）に、GIS による地図作成事業のための専用の体制を維持すると決めた | 照合済み |
| 2013-06-28（採択） | A/RES/67/287 | 総会が、地図課を、兵站部の戦略支援課から、情報通信技術部の現地通信・情報技術運用課へ再配置し、一般職の 1 ポストを廃止した | 照合済み |
| **2015-06-25**（採択） | **A/RES/69/308** | 現地支援局の情報通信技術部の「Cartographic Section」を「**Geospatial Information Section**」に**改称** | 照合済み |
| 2015-06-25（採択） | A/RES/69/309 | UNLB の「Service for Geospatial, Information and Telecommunications Technologies」の長のポストの移転の検討を先送りした。事務総長に、地理空間情報システムの集約で、現地ミッションでこの分野に充てる資源が減ることを確実にするよう要請した | 照合済み |
| 2015-12-23、2017-01-26、2017-12-08 | S/2015/1025、S/2017/78、S/2017/1034 | カメルーンとナイジェリアの混合委員会の境界声明に付ける地図を、現地支援局の Geospatial Information Section の支援で作成している | 照合済み |
| 2016-06-17（採択） | A/RES/70/288 | 総会が、地理空間情報システムの集約と、「Geospatial Information Systems Section」の再編に留意した。臨時の職 5 つ（P-5 1、P-3 1、P-2 3）をポストに転換することを承認した | 照合済み |
| 2018-07-05（採択） | A/RES/72/287 | 総会が、当サービス部を「Field Technology Service」に改称しないと決めた。臨時の職 6 つをポストに転換した（Geospatial Information Systems Officer（P-3）1 を含む） | 照合済み |
| 2019-07-03（採択） | A/RES/73/310 | 総会が、「Global Technology Service」への改称の決定を先送りした | 照合済み |

「照合済み」は、un-docs の本文と公式の PDF で、該当文が一致したことをいう。

- 2020 年以降に組織の決定を述べる総会決議は、検索では見つからなかった（A/RES/73/310 が最後）。
- 2007〜2015 年の間の UNLB 側の名称と人員は、UNLB の予算・実績報告で追える。GIS センター（2007/08）から Geospatial Information Services Centre（2014/15 の再編）、Geospatial Information Systems Section（2016/17）へと変わった。詳細は `unlb-gis-function-in-budget-documents`（un-docs の外）。un-docs の範囲では、改称を述べる文書は見つからなかった。

### 運用の記述：国連イラク支援ミッション（UNAMI）の行方不明者の報告

イラクとクウェートの行方不明者と財産に関する事務総長の報告（安保理決議 2107 (2013) の第 4 項の実施。以下、UNAMI の報告）から、技術サービス部の運用が見える。**文書ごとに年が違う**。

| 報告の日付 | 文書 | 内容 |
|---|---|---|
| 2019-04-29 | S/2019/352 | 現地調査に、ブリンディジの技術サービス部の専門家が参加した。地中レーダーでハミシーヤ（Khamisiyah）の遺体捜索ができるかを評価した |
| 2019-08-06 | S/2019/632 | 評価報告書を、ブリンディジの「Service for Geospatial Information and Telecommunications Technologies」（コンマが無い綴り）が作成した（2019 年 2 月の現地訪問にもとづく） |
| 2019-11-07 | S/2019/865 | 同部の訓練部門と協力して、イラク国防省職員約 10 人の地中レーダーの訓練を準備している |
| 2020-02-20 | S/2020/133 | 訓練の準備を進めている。訓練は、イラクの政治・治安の情勢のため延期されていたが、2020 年の上半期に最初の部を実施できる見込み |
| 2020-05-05 | S/2020/358 | 訓練は、新型コロナのため 2020 年の第 3 四半期に延期された |
| 2021-04-22、2021-11-08 | S/2021/395、S/2021/930 | 訓練は 2021 年後半、のち 11 月に予定 |
| 2022-02-08 | S/2022/100 | 2021-11-07〜18 に、バグダッドでイラク国防省職員 20 人の訓練を完了した（UNLB の地理空間の訓練講師と） |
| 2023-01-19 | S/2023/51 | 2022-11-07〜11 に、ブリンディジで同省職員 6 人の上級訓練を完了した |

## よくあるまちがい

- ニューヨークの地理空間情報課と、ブリンディジの技術サービス部を、同じ組織とみなす。所属も場所も別の部署である。ただし、2007〜2009 年のブリンディジの GIS センターは、ニューヨークの地図課長の指示を受けていた（`unlb-gis-function-in-budget-documents`）。
- ニューヨークの地図課の 2015 年の改称（69/308）を、UNLB の組織の改称と取り違える。UNLB については 2018 年（72/287）と 2019 年（73/310）に改称案が出たが、採られなかった。
- 「2022 年に 20 人、2023 年にブリンディジで 6 人」を、訓練の実施年とする。実施は 2021 年 11 月と 2022 年 11 月で、報告は翌年に出ている（前身の調査の要約を直した）。
- 部の名称は文書ごとに綴りが揺れる（コンマの有無、`Technology` の単複）。検索は、`Service\s+for\s+Geospatial` のように前半で行うのがよいが、UNAMI の訓練の記述（S/2020/133 など）は別の言い方をするので、この式では当たらない。

## 確かめた度合い

- 年表の総会決議は、un-docs の本文と公式の PDF の該当文が一致することを確かめた（`read-official`）。57/300 と 58/101 の採択日は、公式の PDF の末尾に書かれた日付にもとづく。S/PV.4227、S/PV.4310 は未照合。S/2000/1194、S/PRST/2000/21 は日付と該当語を確認した。
- UNAMI の報告は、un-docs の本文で全件を読み、S/2019/352、S/2019/632、S/2020/133、S/2023/51 は公式の PDF でも該当文を確認した。S/2020/358、S/2021/395、S/2021/930、S/2022/100、S/2019/865 は un-docs のみ。
- 未確認: 他言語版、国連事務局の公式な組織図。

## 出典

- yuiseki/un-docs（コミット 6cd1cf0）
- 各文書の記号は表のとおり（`https://docs.un.org/en/<記号>`）
- hfu/kcai-yuiseki-datasets `knowledge/cross/un-docs-geospatial-institutions.md`
