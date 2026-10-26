---
id: unlb-gis-function-in-budget-documents
title: ブリンディジ（UNLB）の GIS 機能：予算文書から読む名称・人員・成果物（un-docs の外の一次資料）
status: draft
verified_how: read-official
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - A/62/781/Add.12、A/63/824、A/69/733、A/69/839/Add.9、A/70/609、A/70/779、A/78/735（公式サイトの PDF）
  - A/RES/60/267、61/277、69/309、70/288、72/287（un-docs と公式サイトで確認済み）
  - https://docs.un.org/en/A/63/824
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-26
related: [un-geospatial-organization-timeline, un-mission-gis-mentions-in-un-docs, un-geospatial-institutions-in-un-docs]
cites:
  - a-63-824: 付録「GIS センターの分析」、第 11〜13 項
  - a-69-733: 概要と組織図
  - a-70-609: 第 19〜20 項
  - a-70-779: 第 29〜31 項
finding:
  - gis-centre-became-section-via-centralization
  - ny-section-directs-brindisi-centre
---

## 要点

> 範囲: これは **un-docs の範囲外**の一次資料（UNLB の予算・実績報告とその審査報告）を読んだ踏み跡。ミッション個別の予算は読んでいない。

UNLB の GIS 機能は、予算文書から次の弧が読める。

| 時期 | 名称 | 何が書かれているか |
|---|---|---|
| 2007/08〜 | **GIS Centre**（Geographic Information System Centre） | 2007-12-31 から完全に運用。ニューヨークの地図課長から「プログラムの指示」を受け、UNLB が管理する（A/63/824 付録 第 11 項）。初年度の成果は、UNIFIL の 1:50,000 地形図 7 枚と UNDOF との共通地理データベース（20 図葉）、UNAMID の衛星画像地図約 140 枚と地形図 32 枚（欧州委員会共同研究センターと連携）、キャンプ候補地の地形・洪水危険の分析、34 か所の地下水の評価（同 第 13 項） |
| 2009/10 の計画 | 同上 | UNAMID に 1:50,000 地形図 80 図葉、全野外活動への地理可視化データの提供、GIS 研修 4 回（A/63/824 本体の成果物） |
| 2014/15 | **Geospatial Information Services Centre**／**Service for Geospatial, Information and Telecommunications Technologies** | 総会決議 68/284 が、GIS の 2 年間の**集約計画**を支持したと報告される。初年度はミッションで 14 ポストを廃止し、グローバル・サービスセンターに 7 つの臨時職を設置（A/70/609 第 20 項）。センターは「後勤サービス」から当サービスへ移った |
| 2015/16 | 同上 | 集約の 2 年目。累計で**ミッションの 36 ポストを廃止、センターに 11 を設置**（A/70/779 第 30 項）。審査報告 A/69/839/Add.9 は、ミッションの資源の減少を確認するよう求め、総会決議 69/309 がそれを要請 |
| 2016/17〜 | **Geospatial Information Systems Section**（当サービスの下） | 11 の臨時職をポストに転換する提案（A/70/779）に対し、総会決議 70/288 は **5 つ**（P-5 1、P-3 1、P-2 3）の転換を承認した |
| 2024/25 | Service for Geospatial, Information and Telecommunications Technologies | 当サービスは存続し、国民職員の GS ポスト 1 の廃止が提案される（A/78/735）。名称の変更は無い（改称は決議 72/287、73/310 で見送り） |

## 詳しく

- **ニューヨークの地図課との関係**: 2007〜2009 年の GIS センターは、ニューヨークの地図課長から計画の指示を受ける別の拠点だった。`un-geospatial-organization-timeline` が書いた「別の組織」は、**所属と場所が別**であって、**無関係**ではない。
- **名称の変遷は予算文書が決議より細かい**: 決議が述べるのは「GIS センター」（60/267、61/277）と「当サービス」（69/309 以後）で、その間の「Geospatial Information Services Centre」は予算文書にしか見えない。2013/14 の実績報告（A/69/585）には当サービスの名が出ず、**当サービスの出現は 2014/15 の再編の時期**と読める。
- **集約の方向**: ミッションに分散していた GIS 要員を、グローバル・サービスセンターに集める（ミッションの 36 ポスト廃止→センターの 11）。ミッションの報告に GIS の記述が少ないこと（`un-mission-gis-mentions-in-un-docs`）と整合する読みだが、因果は本書では確かめていない。

## よくあるまちがい

- 提案（11 ポストへの転換）を決定とみなす。総会が承認したのは 5 つ（決議 70/288 第 11 項）。
- 「ミッションの GIS 機能」を、ミッション予算の文書がある、と考える。UNLB の文書にはあるが、ミッション個別の予算は別の文書（未読）。
- 2007〜2009 年の GIS センターの活動を、ニューヨークの地図課の活動とみなす（指示は地図課長、運用と管理は UNLB）。

## 確かめた度合い

- `read-official`: 上の文書を documents.un.org の API から取得し、該当箇所を読んだ。引用は要約と項番号の指示にとどめた。A/RES/68/284 は公式の PDF で確認した（GIS の語を含まない。集約計画の支持は A/70/779 と A/70/609 の記述）。
- 未読: ミッション個別の予算案・実績報告（UNIFIL、MINURSO、UNFICYP、MINUSMA、UNSOS）。A/69/839/Add.9 の第 44 項の全文。中間年（2009/10〜2013/14）の UNLB 予算。
- 未確認: 「GIS センター」→「Geospatial Information Services Centre」の改称の正確な時期。

## 出典

- A/62/781/Add.12、A/63/824、A/69/733、A/69/839/Add.9、A/70/609、A/70/779、A/78/735
- A/RES/60/267、61/277、68/284、69/309、70/288、72/287、73/310
