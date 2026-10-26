---
id: un-geospatial-organization-timeline
title: 国連の地図課→地理空間情報課と、UNLB の GIS センター→地理空間・情報・通信技術サービス：名称と組織の年表
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。手順は checks/geospatial-institutions-recheck.md
  - A/RES/57/300、58/101、60/267、61/277、67/287、69/308、69/309、70/288、72/287、73/310（公式サイトの PDF と照合）
  - https://docs.un.org/en/A/RES/69/308
  - hfu/kcai-yuiseki-datasets knowledge/cross/un-docs-geospatial-institutions.md（前身の年表。本書で文書ごとに確かめ直した）
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-26
related: [un-geospatial-institutions-in-un-docs, un-mission-gis-mentions-in-un-docs, un-docs-reading-guide, unlb-gis-function-in-budget-documents]
cites:
  - un-docs: 組織の決定を述べる総会決議の本文
  - undocs-site: 各決議の該当する文の照合
  - hfu-institutions: 前身の年表との照合
finding:
  - two-similarly-named-units-are-different
  - name-forms-vary-in-text
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書。ミッション予算・事務局の内部文書は含まない。呼称の変遷は、**総会決議が述べた範囲**でしか追えない。

名前の似た**二つの組織**を混同しない。

1. **ニューヨーク（現地支援局の情報通信技術部）の地図課**。2000 年から文書に出る「Cartographic Section」→ 2015-06-25 に決議 69/308 で「**Geospatial Information Section**」に改称。
2. **ブリンディジ（国連兵站基地 UNLB／グローバル・サービスセンター）の GIS 系の組織**。2006 年の「地理情報システムセンター」の提案から、「**Service for Geospatial, Information and Telecommunications Technologies**」（2015 年の決議から見える）。

## 年表（un-docs の日付欄の種別を併記）

| 日付 | 文書 | 事項 | 公式原文との照合 |
|---|---|---|---|
| 2000-06-18（配布） | S/PRST/2000/21 | 安保理議長声明が、レバノンからの撤退線の確認で事務総長の「Chief Cartographer」の努力を評価 | 照合済み |
| 2000-11-17（会議日） | S/PV.4227 | エチオピア・エリトリアの国境画定で、国連の「Cartographic Unit」の役割に発言国が言及 | 未照合（un-docs のみ） |
| 2000-12-15（配布） | S/2000/1194 | 合意で国連の地図作成官（cartographer）が国境委員会の書記を務める | 未照合（配布日のみ確認） |
| 2001-04-19（会議日） | S/PV.4310 | 国境委員会の後方支援の見積りで「Cartographic Section」のチームが現地を調査中 | 未照合 |
| 2003-02-07（配布） | A/RES/57/300 | 総会が、事務総長の「地図課の機能と資源を広報局から平和維持活動局へ移す」提案に**留意**し、検討を決める | 照合済み（採択日は日付欄に無く未確認） |
| 2003-12-17（配布） | A/RES/58/101 | 総会が、地図課の機能の広報局→平和維持活動局への移管を**歓迎**（成果が平和維持活動局の需要に近いため） | 照合済み（採択日は未確認） |
| 2006-06-30（採択） | A/RES/60/267 | 総会が、UNLB に 2007/08 年度に「geographical information system centre」を置く提案に**留意** | 照合済み |
| 2006-12-12 | S/PRST/2006/52 ほか | レバノン（シェバア農地）で事務総長が**上級地図作成官**を任命。最初に見える文書は S/2006/933（2006-12-01） | 地図作成官の語は S/PRST/2007/29 で照合 |
| 2007-06-29（採択） | A/RES/61/277 | 「Chief, Geographic Information System Centre」（P-4）の新設と、GIS 担当官（P-3）、GIS 管理者（現地職員）、国内職員 5 人の臨時職を承認 | 照合済み |
| 2007-06-29（採択） | A/RES/61/287 | UNDOF に「Geographic Information System mapping project」の専任の人員を維持 | 照合済み |
| 2013-06-28（採択） | A/RES/67/287 | 地図課を、兵站部の戦略支援課から、情報通信技術部の現地通信・情報技術運用課へ**再配置**。GS 職 1 ポストを廃止 | 照合済み |
| 2015-06-25（採択） | **A/RES/69/308** | 現地支援局・情報通信技術部の「Cartographic Section」を「**Geospatial Information Section**」に**改称** | 照合済み |
| 2015-06-25（採択） | A/RES/69/309 | UNLB の「Service for Geospatial, Information and Telecommunications Technologies」の長のポストの移転の検討を先送り。地理空間情報システムの集約で、現地ミッションの資源が減ることを求める | 照合済み |
| 2015-12-23、2017-01-26、2017-12-08 | S/2015/1025、S/2017/78、S/2017/1034 | カメルーン・ナイジェリア混合委員会の境界声明の地図を、現地支援局の Geospatial Information Section の支援で作成 | 照合済み |
| 2016-06-17（採択） | A/RES/70/288 | 地理空間情報システムの集約と「Geospatial Information Systems Section」の再編に**留意**。臨時職 5 つ（P-5 1、P-3 1、P-2 3）をポストに転換 | 照合済み |
| 2018-07-05（採択） | A/RES/72/287 | 当サービスを「Field Technology Service」に**改称しない**と決定。臨時職 6 つをポストに転換（Geospatial Information Systems Officer（P-3）1 を含む） | 照合済み |
| 2019-07-03（採択） | A/RES/73/310 | 「Global Technology Service」への改称を**先送り** | 照合済み |

- **補足（予算文書）**: 2007〜2015 年の間の UNLB 側の名称・人員は、UNLB の予算・実績報告で追える。GIS センター（2007/08）→ Geospatial Information Services Centre（2014/15 の再編）→ Geospatial Information Systems Section（2016/17）。詳細は `unlb-gis-function-in-budget-documents`（un-docs の外）。un-docs の範囲では、改称を述べる文書は見つからない。
- 2020 年以降の組織の決定を述べる総会決議は、検索では見つからなかった（A/RES/73/310 が最後）。

## 運用の記述（UNAMI の行方不明者の文書）

イラク・クウェートの「行方不明者・クウェートの財産」報告（安保理決議 2107 (2013) 第 4 項の実施）の文書から、当サービスの運用が見える。**文書ごとに年が違う**。

| 報告の日付 | 文書 | 内容 |
|---|---|---|
| 2019-04-29 | S/2019/352 | 現地調査に、ブリンディジの「Service for Geospatial, Information and Telecommunications Technologies」の専門家が参加。地中レーダーでハミシーヤ（Khamisiyah）の遺体捜索ができるかを評価 |
| 2019-08-06 | S/2019/632 | 評価報告書を、ブリンディジの「Service for Geospatial Information and Telecommunications Technologies」（コンマ無しの綴り）が作成（2019 年 2 月の現地訪問に基づく） |
| 2019-11-07 | S/2019/865 | 同サービスの訓練部門と、イラク国防省職員約 10 人の地中レーダー訓練の準備 |
| 2020-02-20、2020-05-05 | S/2020/133、S/2020/358 | 訓練を準備中。新型コロナで延期 |
| 2021-04-22、2021-11-08 | S/2021/395、S/2021/930 | 訓練は 2021 年後半、のち 11 月に予定 |
| 2022-02-08 | S/2022/100 | **2021-11-07〜18 に**、バグダッドでイラク国防省職員 **20 人**の訓練を完了（UNLB の地理空間の訓練講師と） |
| 2023-01-19 | S/2023/51 | **2022-11-07〜11 に**、ブリンディジで同省職員 **6 人**の上級訓練を完了 |

## よくあるまちがい

- ニューヨークの地理空間情報課と、ブリンディジの地理空間・情報・通信技術サービスを同じ組織とみなす。別の部署（所属も場所も違う）。ただし 2007〜2009 年の GIS センターは、ニューヨークの地図課長の指示を受けていた（`unlb-gis-function-in-budget-documents`）。
- 呼称が 2015 年に一つの組織の中で変わった、とみなす。地図課の改称（69/308）と、UNLB の改称の議論（72/287、73/310）は別の話。
- 「2022 年に 20 人、2023 年にブリンディジで 6 人」を訓練の実施年とする。実施は 2021 年 11 月と 2022 年 11 月で、前年末に報告されている（前身の要約を直した）。
- `Service for Geospatial, Information and Telecommunications Technologies` の綴り（コンマの有無、`Technology` の単複）を一つに決めつけて検索する。**語の検索は部分一致で**。

## 確かめた度合い

- 年表の総会決議は、un-docs の本文と公式の PDF の該当文が一致することを確かめた（`read-official`）。S/PV.4227、S/PV.4310 は未照合。S/2000/1194、S/PRST/2000/21 は日付と該当語を確認。
- 運用の記述（UNAMI の文書）は、un-docs の本文で全件を読み、S/2019/352、S/2019/632、S/2020/133、S/2023/51 は公式の PDF でも該当文を確認した。S/2020/358、S/2021/395、S/2021/930、S/2022/100、S/2019/865 は un-docs のみ。
- 未確認: 採択日（57/300、58/101）、他言語版、国連事務局の公式な組織図。

## 出典

- yuiseki/un-docs（コミット 6cd1cf0）
- 各文書の記号は表のとおり（`https://docs.un.org/en/<記号>`）
- hfu/kcai-yuiseki-datasets `knowledge/cross/un-docs-geospatial-institutions.md`
