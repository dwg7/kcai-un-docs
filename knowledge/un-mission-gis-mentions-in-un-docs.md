---
id: un-mission-gis-mentions-in-un-docs
title: 各ミッションの GIS・地理空間の機能は、総会・安保理の文書でどう語られるか（un-docs の範囲、25 文書の確かめ直し）
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。手順は checks/geospatial-institutions-recheck.md と scripts/mission_gis_ratio.py
  - hfu/kcai-yuiseki-datasets の checks/un-docs-geospatial-institutions.tsv（本書で「前身の調査」と呼ぶ。M-ミッション 25 文書）
  - A/RES/61/287、A/RES/71/272、S/2014/130、S/2018/945、S/2019/787、S/2021/1110、S/2023/3、S/PV.9039 ほか（公式サイトの PDF）
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり。独立レビュー（2026-10-26）の指摘を反映して改訂
reviewed_by: []
updated: 2026-10-26
related: [un-geospatial-institutions-in-un-docs, un-geospatial-organization-timeline, mission-budgets-geospatial-output-lines, sage-situational-awareness-geospatial-enterprise, geospatial-geographic-tendency]
cites:
  - un-docs: M-ミッションの 25 文書の本文
  - undocs-site: 該当文の照合
  - hfu-institutions: 前身の調査の分類
finding:
  - mission-gis-lives-in-budget-documents-not-in-un-docs
  - gis-appears-in-reports-as-incidents-and-tools
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書。**各ミッションの要員・予算・成果物を述べる予算案・実績報告（総会の文書）は含まれない**ので、ミッションの GIS 機能の本体は un-docs からは見えない。予算文書を読んだ結果は `mission-budgets-geospatial-output-lines` に分けた。

本書で「前身の調査」とは、hfu が先に行った調査（`hfu/kcai-yuiseki-datasets` の `checks/un-docs-geospatial-institutions.tsv`）を指す。前身の調査は、地図・GIS・地理空間の語を含む 226 文書を分類し、そのうち 25 文書を「ミッション」に入れた。本書はその 25 文書の本文を読み直した。

読み直した結果、要約の多くは本文と合っていたが、次の 4 点を直した。ミッションの GIS 機能に関する記述は、**報告の中の道具の使用例、研修、支援の項目の列挙、ポストの表**にとどまり、機能の設計を論じる文は見つからなかった。

1. 前身の調査がミッションに入れた「ギニアビサウの選挙支援」の 4 文書は、投票所の位置を更新する「選挙の地図作成」の話で、GIS 機能ではない（「別の意味で使われた語」に分類し直す）。
2. 「地理空間情報システムと地図作成サービス」という文言は、S/2017/454（アフリカ連合の平和支援活動への支援の選択肢）だけにある。G5 サヘル合同部隊への支援案の 3 文書（S/2017/869、S/2018/432、S/2020/476）は、別の形の文言である。
3. S/2018/945 は、G5 サヘルとマリのミッションの話ではない（下の表）。
4. A/RES/71/272 の GIS 担当官のポストは、**設置されなかったポスト**の一覧に載っている（下の表。前身の調査の記述が正しかった）。

## 詳しく

### 25 文書の確かめ直し

| ミッション・主題 | 文書（日付） | 何が書かれているか |
|---|---|---|
| UNDOF（国連兵力引き離し監視隊） | A/RES/61/287（2007-06-29） | 総会は、部隊に「GIS による地図作成事業」のための**専用の体制**（dedicated capacity）を維持すると決めた（Decides）。公式の PDF と一致 |
| UNIFIL（国連レバノン暫定軍） | S/2011/488、S/2012/632 | 現地の民間人が、UNIFIL の要員から、カメラ、地理情報システム、通信機器、地図などの国連財産を取った事件の報告の中の語 |
| UNIFIL | S/2014/130（2014-02-26） | 「UNIFIL の GIS による測定」で、見つかった物体がブルーラインのわずかに南にあると判定した。公式の PDF と一致 |
| UNIFIL | S/2020/195 | 「包括的な地理情報システムのデータ基盤」を拡充し、業績の分析と判断を支えたと述べる |
| マリ（アフリカ主導のマリ国際支援ミッション AFISMA の支援案） | S/2013/37 | 国連は、AFISMA の地理情報の需要に「専用の成果物とアプリケーション」で応じる案を示した（UNSOA のモデルに倣う）。衛星画像と GIS による地下水と環境の評価も案に含む。公式の PDF と一致 |
| UNAMID（ダルフールの国連・アフリカ連合合同ミッション） | S/2014/515 | ダルフール土地委員会の職員に、GIS・リモートセンシング・GPS・地図読みの研修を 4 回行った。公式の PDF と一致 |
| UNSMIL（国連リビア支援ミッション） | A/RES/71/272（2016-12-23） | 共同ミッション分析センターの「Geographic Information Systems Officer」（P-3）は、**設置しないポストの表**（Annex III「Positions not to be established in the United Nations Support Mission in Libya」）に載っている。ポストの決定の例ではなく、設置されなかった例である。公式の PDF と un-docs の本文で確認 |
| アフリカ連合の平和支援活動への国連支援の選択肢 | S/2017/454（2017-05-26） | 国連が提供しうる支援の項目に「geospatial information systems and cartographic services」。公式の PDF と一致 |
| G5 サヘル合同部隊への国連支援 | S/2017/869、S/2018/432、S/2020/476 | 支援の包括案に「geospatial, telecommunications and information technology … support」の形の語（文言は文書により少し違う） |
| **マリのミッション（MINUSMA）とフランスの Barkhane 部隊** | S/2018/945（un-docs の日付欄は 2018-06-28 だが誤り。S/RES/2423 の採択日で、書簡は 2018-10-19 付、配布は 10-25） | 事務総長が、フランスの口上書を安保理に送ったもの。Barkhane 部隊が MINUSMA に与えた支援を述べ、情報の節に「**地理空間の情報収集（geospatial intelligence）**（地理データ）の合同作業部会」の計画がある。前身の調査は「G5 サヘルと MINUSMA」「地理空間情報」と書いたが、当事者は Barkhane 部隊と MINUSMA で、語は intelligence（情報収集）である。公式の PDF と一致 |
| MINUSMA | S/2020/952 | 民間人保護の取り組みの影響を評価する「地理空間データにもとづく新しい手段」を作った。公式の PDF と一致 |
| MINURSO（西サハラ住民投票国連ミッション） | S/2019/787、S/2020/938、S/2021/843 | EU の二国間支援（S/2021/843 は EU と米国）による地理空間の画像と分析を、停戦違反の早期警戒と観測の補完に使う。S/2019/787 は公式の PDF と一致 |
| UNFICYP（国連キプロス平和維持隊） | S/2021/1110（2021-12-31） | ミッションが SAGE の報告システムを根本的に見直した（`sage-situational-awareness-geospatial-enterprise`）。公式の PDF と一致 |
| UNFICYP の報告にある行方不明者委員会 | S/2023/3 | 委員会の 3 つの事務所が共有する Web 型の地理情報システムを使う。公式の PDF と一致 |
| UNMHA（ホデイダ合意支援ミッション） | S/PV.9039（2022-05-23） | 発言で、マッピング・地理情報システム・衛星技術の道具を使って停戦の監視を強めたと述べる。公式の PDF と一致 |
| UNSOS／AMISOM（ソマリア） | S/2017/653 | AMISOM のミッション支援で、医療・工兵・地理空間・情報技術・通信の各班の間の調整が足りないと述べる表の中に、「geospatial」の語が列挙されている |
| UNISFA（アビエ）と国連ロジスティクス基地 | S/2019/319 | グローバル・サービスセンターと、ほかのミッションの「地理空間・情報通信技術サービス」の要員との調整で、通信設備の被害を修復できたと述べる（`unlb-gis-function-in-budget-documents`）。公式の PDF と一致 |
| ギニアビサウ（国連ギニアビサウ統合平和構築事務所の選挙支援） | S/2018/110、S/PV.8261、S/PV.8337、S/2018/771 | 投票所の位置を更新する「選挙の地図作成（electoral cartography）」の事業が、選挙準備の遅れの一因として挙がる。GIS 機能の話ではない（上の 1）。S/2018/110 は公式の PDF と一致（S/PV.8261 の語は「cartography activities」） |

### 平和維持活動全般の議論（ミッションを名指ししない）

- S/PV.7802（2016-11-07）: 専門家パネルが、空撮データ、地理空間・地理情報、その他の遠隔取得データを、平和維持活動に常時利用できるようにすべきだと指摘した、という発言。公式の PDF と一致。
- S/PV.9389（2023-07-28）: あるミッションの代表が、軍・警察・文民の各部門が入力する SAGE の基盤を説明し、「ほとんどの国連ミッションで共通のデータ基盤が使われている」と述べた。同じ発言は、国連が SAGE を Unite Aware という新しいシステムに置き換える作業を進めているとも述べる。公式の PDF と一致。
- S/2021/501（オランダ）と S/PV.8838（ノルウェー）の発言も、SAGE と Unite Aware に触れる（`sage-situational-awareness-geospatial-enterprise`）。

### 読み方

- 25 文書では、言及は、道具の使用例（UNIFIL の測定、UNMHA の停戦監視）、研修、支援項目の列挙、ポストの表にとどまり、機能の設計を論じる文は見つからなかった。
- 現場の GIS 機能の表現は、`Geographic Information System`、`geospatial`、`SAGE`、`situational awareness` のように分かれる。語の漏れの調査は `un-geospatial-institutions-in-un-docs`。
- 同じ文言が報告ごとに繰り返し出る。G5 サヘル支援案 3 本、MINURSO 3 本、UNIFIL 4 本（S/2011/488、S/2012/632、S/2014/130、S/2020/195）、ギニアビサウ 4 本。数えているのは報告の本数で、議論の厚みではない。

### ミッション報告での言及の少なさ

事務総長報告・書簡など（安保理文書 S/年/番号、総会文書 A/会期/番号、決議集 S/INF）のうち、本文の冒頭 900 字にミッション名（略称または正式名）がある文書は 1,045 件あり、そのうち地図・GIS・地理空間の語（`cartograph`、`geospatial`、GIS、`geographic information system`）を含むのは 21 件（約 2%）。式と対象は `scripts/mission_gis_ratio.py` に記録した。前身の調査の「約 1,180 文書のうち 23」とは、ミッション名の式と対象の系列が違い、完全には再現できない。

コンゴ民主共和国（MONUSCO）、南スーダン（UNMISS）、中央アフリカ共和国（MINUSCA）、コソボ（UNMIK）、リベリア（UNMIL）、コートジボワール（UNOCI）、ハイチ（MINUSTAH）の報告では、冒頭にこれらの略称がある文書の範囲で、これらの語は 1 件も出なかった。正式名だけで始まる文書は、この確認から漏れる。

## よくあるまちがい

- 「ミッションごとに GIS が議論された件数」を、ミッションの GIS 機能の大小とみなす。
- `electoral cartography`（選挙の地図作成）を、国連の GIS 機能とみなす。
- 平和維持活動の議事録の発言（S/PV.9389 の SAGE）を、事務局の決定とみなす。
- 設置しないポストの表を、設置を決めたポストの表と読む（A/RES/71/272）。

## 確かめた度合い

- `searched-undocs`: 25 文書の本文を読み、前身の調査の要約と照合した。比率（21/1,045）は `scripts/mission_gis_ratio.py` で再現できる。
- `read-official`: A/RES/61/287、A/RES/71/272、S/2013/37、S/2014/130、S/2014/515、S/2017/454、S/2018/110、S/2018/945、S/2019/319、S/2019/787、S/2020/195、S/2020/952、S/2021/1110、S/2023/3、S/PV.7802、S/PV.9039、S/PV.9389 の該当文を公式の PDF で照合した。残りは un-docs のみ。
- 未確認: ミッション予算の中身は別の踏み跡で扱う。S/2018/945 の作業部会の相手方。

## 出典

- yuiseki/un-docs（コミット 6cd1cf0）
- 各文書の記号は表のとおり（`https://docs.un.org/en/<記号>`）
- hfu/kcai-yuiseki-datasets `checks/un-docs-geospatial-institutions.tsv`
