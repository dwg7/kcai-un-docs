---
id: un-mission-gis-mentions-in-un-docs
title: 各ミッションの GIS・地理空間の機能は、総会・安保理の文書でどう語られるか（un-docs の範囲、25 文書の確かめ直し）
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。手順は checks/geospatial-institutions-recheck.md
  - hfu/kcai-yuiseki-datasets checks/un-docs-geospatial-institutions.tsv（M-ミッション 25 文書）
  - A/RES/61/287、A/RES/71/272、S/2014/130、S/2019/787、S/2021/1110、S/2023/3、S/PV.9039 ほか（公式サイトの PDF と照合）
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-26
related: [un-geospatial-institutions-in-un-docs, un-geospatial-organization-timeline, geospatial-geographic-tendency]
cites:
  - un-docs: M-ミッションの 25 文書の本文
  - undocs-site: 該当文の照合
  - hfu-institutions: 前身の分類
finding:
  - mission-gis-lives-in-budget-documents-not-in-un-docs
  - gis-appears-in-reports-as-incidents-and-tools
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書。**各ミッションの要員・予算・成果物を述べるミッション予算・実績報告（総会の文書）は含まない**ので、ミッションの GIS 機能の本体は未確認。

un-docs で見えるのは、ミッションの報告・書簡の中の**挿話的な言及**と、総会決議の**ポストの決定**だけ。冒頭にミッション名を持つ S/yyyy/n・A/NN/n・S/INF のうち、地図・GIS・地理空間の語を含む文書は、再現では **21 / 1,045（約 2%）**（前身は 23 / 1,180。数え方が違う）。MONUSCO、UNMISS、MINUSCA、UNMIK、UNMIL、UNOCI、MINUSTAH の報告にはこれらの語が出ない（冒頭にミッション名を持つ文書の範囲）。

## 詳しく

### 25 文書の確かめ直し（本文と前身の要約を突き合わせた）

要約は本文と合っている。区分ごとに整理する。

| ミッション・主題 | 文書（日付） | 何が書かれているか |
|---|---|---|
| UNDOF | A/RES/61/287（2007-06-29） | 部隊に「Geographic Information System mapping project」の専任の人員を維持（Decides）。公式の PDF と一致 |
| UNIFIL | S/2011/488、S/2012/632 | 地元住民に、要員から「cameras, geographical information systems, communication equipment and maps」などの国連財産が奪われた事件 |
| UNIFIL | S/2014/130（2014-02-26） | 「UNIFIL Geographic Information System (GIS) measurements」で、見つかった物体がブルーラインのわずかに南にあると判定。公式の PDF と一致 |
| UNIFIL | S/2020/195 | 「comprehensive geographical information systems data platforms」の拡充（成果分析と意思決定） |
| マリ（AFISMA 支援案） | S/2013/37 | 国連が、AFISMA の地理情報の需要に「dedicated products and applications」で応じる案（UNSOA のモデル）。衛星画像と GIS による地下水・環境の評価も案に含む |
| UNAMID | S/2014/515 | ダルフール土地委員会の職員に、GIS・リモートセンシング・GPS・地図読みの研修を 4 回 |
| UNSMIL | A/RES/71/272（2016-12-23） | 共同ミッション分析センターの「Geographic Information Systems Officer」（P-3）がポストの表にある。公式の PDF と一致（表の見出しは未確認） |
| AU 平和支援活動への国連支援の選択肢 | S/2017/454（2017-05-26） | 国連が提供しうる支援の項目に「geospatial information systems and cartographic services」。公式の PDF と一致 |
| G5 サヘル合同部隊への国連支援 | S/2017/869、S/2018/432、S/2020/476 | 支援の包括案に「maintenance contracts, geospatial, telecommunications and information technology and infrastructure support」の形の語（文言は文書により少し違う）。**前身の要約は S/2017/454 の文言をこの 3 文書にも付けていたが、3 文書にその文言は無い** |
| G5 サヘルと MINUSMA | S/2018/945 | 地理空間情報（地理データ）の共同作業部会の計画 |
| MINUSMA | S/2020/952 | 文民保護の取組の影響を評価する「geospatial data-driven tool」を新たに作成 |
| MINURSO | S/2019/787、S/2020/938、S/2021/843 | EU（のち米国も）の二国間支援による地理空間の画像と分析を、停戦違反の早期警戒・観測の補完に使う。S/2019/787 の本文を公式の PDF で確認 |
| UNFICYP | S/2021/1110（2021-12-31） | 「Situational Awareness Geospatial Enterprise (SAGE)」の報告システムを根本的に見直した。公式の PDF と一致 |
| UNFICYP 報告内の行方不明者委員会 | S/2023/3 | 3 事務所で共有する「web based geographic information system application」を使用。公式の PDF と一致 |
| UNMHA（ホデイダ） | S/PV.9039（2022-05-23） | 「mapping, geographic information system and satellite technology tools」で停戦の監視を強化。公式の PDF と一致 |
| UNSOS／AMISOM | S/2017/653 | ミッション支援の構成要素（医療・工兵・地理空間・IT・通信）の調整不足を述べる表の中の語 |
| **（区分を直す）ギニアビサウの選挙支援** | S/2018/110、S/PV.8261、S/2018/771、S/PV.8337 | 「electoral cartography」＝投票所の位置を更新する選挙の地図作成。**GIS 機能の話ではなく、選挙支援の事業**（UNDP と UNIOGBIS の資金調達）。P（別の意味）へ移す |

### 平和維持活動全般の議論（ミッションを名指ししない）

- S/PV.7802（2016-11-07）: 専門家パネルが「aerial data, geospatial and geographic information and other remotely acquired data」を、平和維持活動に常時利用できるべきものとして指摘したという発言。
- S/PV.9389（2023-07-28）: 「Situational Awareness Geospatial Enterprise platform」で、軍、警察、文民の各部門が入力する（一つのミッションの代表の発言）。多くの国連ミッションで共通のデータ基盤が使われているという発言。

### 読み方

- **言及は、道具の挿話（UNIFIL の GIS 測定、UNMHA の停戦監視）、研修、支援の項目、ポストの表**であって、機能の制度設計の議論ではない。
- **名称**: 現地での GIS 機能は、`Geographic Information System`、`geospatial`、`SAGE`、`situational awareness` のように表現が分かれる。語の漏れの調査は `un-geospatial-institutions-in-un-docs`。
- 同じ表現が複数の報告に繰り返される（G5 サヘル支援 4、MINURSO 3、UNIFIL 3、ギニアビサウ 4）。**件数は、議論の厚みでなく報告の本数**。

## よくあるまちがい

- 「ミッションごとに GIS が議論された件数」を、ミッションの GIS 機能の大小とみなす。
- `electoral cartography`（選挙の地図作成）を、国連の GIS 機能とみなす。
- 平和維持活動の議事録の発言（S/PV.9389 の SAGE）を、事務局の決定とみなす。

## 確かめた度合い

- `searched-undocs`: 25 文書の本文を読み、前身の要約と照合。再現した比率（21/1,045）は、ミッション名の式 約 50 語を自作した結果。
- `read-official`: A/RES/61/287、A/RES/71/272、S/2014/130、S/2019/787、S/2021/1110、S/2023/3、S/PV.9039、S/2019/319、S/2017/454、S/PV.7802、S/PV.9389、S/2020/952、S/2018/945、S/2020/195、S/2014/515、S/2013/37、S/2018/110 の該当文を公式の PDF で照合。残りは un-docs のみ。
- 未確認: ミッション予算・実績報告、ミッションごとの GIS 要員・機器、A/RES/71/272 の表の見出し（「設置しないポスト」という前身の記述は本書で確かめていない）。

## 出典

- yuiseki/un-docs（コミット 6cd1cf0）
- 各文書の記号は表のとおり（`https://docs.un.org/en/<記号>`）
- hfu/kcai-yuiseki-datasets `checks/un-docs-geospatial-institutions.tsv`
