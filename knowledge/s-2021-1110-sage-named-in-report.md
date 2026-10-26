---
id: s-2021-1110-sage-named-in-report
title: S/2021/1110（2021-12-31、キプロス）：SAGE を名指しした事務総長報告の一文を、位置と文脈から読む
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - S/2021/1110（国連キプロス平和維持隊 UNFICYP に関する事務総長報告、2021-12-31。公式サイトの PDF 全 15 頁と un-docs の本文）
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。式と件数は checks/geospatial-5-docs-official-reading.md
  - https://docs.un.org/en/S/2021/1110
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-26
related: [sage-situational-awareness-geospatial-enterprise, sage-in-security-council-discussions, un-mission-gis-mentions-in-un-docs, geospatial-geographic-tendency, un-document-symbols-primer]
cites:
  - un-docs: 略称 SAGE の語が出る唯一の文書であること
  - undocs-site: 第 23 項の文言と位置、図表の有無
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書（安保理決議は S/RES/2699 まで）。un-docs の範囲では、大文字の略称 `SAGE` を含む文書は S/2021/1110 の 1 件だけである。

S/2021/1110 は、事務総長が安保理に出す定期の報告（記号 S/年/番号の報告）で、UNFICYP の 2021 年 6 月 19 日から 12 月 15 日までの活動を述べる。SAGE（Situational Awareness Geospatial Enterprise）が出るのは**第 23 項の 1 文**だけである。文は、緩衝地帯で民間人が関わった出来事が前年同期の 989 件から 343 件に減ったように見えるが、ミッションが SAGE の報告の仕組みを「根本的に見直した」（fundamental review）ので、その見直しが差の一部の理由かもしれない、と述べる。つまりここでの SAGE は、地図や地理空間の成果物としてではなく、**件数の読み方への注意**として出る。報告に図、表、出典表記の付いた図は無い。

## 詳しく

### 文書の型と発出元

- 型: 事務総長報告（Report of the Secretary-General）。冒頭は、安保理決議 186 (1964) 以降の決議、直近は決議 2587 (2021) に基づく報告だと述べる。発出元は事務総長（事務局）で、会議録（S/PV）でも書簡でもない。
- 前の報告は 2021 年 7 月 9 日付の S/2021/635（UNFICYP）と S/2021/634（good offices ミッション）と、本文が述べる。後の同種の報告として S/2022/533（2022-07-05）と S/2023/3 がある（S/2023/3 の本文による）。S/2023/3 以外は読んでいない。

### 位置と文脈

- 位置は、第 III 節「UNFICYP の活動」の C「民間人の活動の管理と法と秩序の維持」（Management of civilian activity and maintenance of law and order）の冒頭近く、第 22 項（ミッションの覚書への双方の態度）の次の第 23 項である。第 24 項は、デモの管理で警察と協力した件（デモ 18 件）に移る。
- 報告の主題は、緩衝地帯の無許可の建設、ヴァロシャ、ピラ高原、ドローンの飛行、監視技術の強化、行方不明者委員会、難民申請者などで、SAGE の一文はそのどれの説明でもなく、**件数の比較の但し書き**である。
- 文中の SAGE の説明は、「報告の仕組みを、構成部門の間でより統合するため」の見直しという点だけで、SAGE が何をするものかは報告に書かれていない。位置情報や地図には触れない。

### 既存の踏み跡との照合

- `sage-in-security-council-discussions` の記述（989 件から 343 件、見直しが一因かもしれない、略称 `SAGE` は 1 件だけ）は、公式の PDF と一致した。
- `sage-situational-awareness-geospatial-enterprise` の記述（2021-12-31、キプロス、989 と 343）も一致した。その表は「見直しが差の一因かもしれない」と書き、原文の「大きな差の一部かもしれない」（may partly explain）より少し強い。直すなら "partly" を入れる。
- `geospatial-geographic-tendency` の「SAGE に触れる一文があるにすぎない」は、第 23 項の 1 文という点で合う。

### 定型か例外か

- 同じ UNFICYP の報告 S/2023/3 には、`SAGE` も `geospatial` も無い（公式 PDF で確認）。地理系の語は「Web 型の地理情報システム」（行方不明者委員会）の 1 件で、別の話である。したがって、UNFICYP の報告で SAGE が出るのは、確かめた 2 本のうち 1 本で、定型とは言えない。S/2021/635、S/2022/533 は読んでいないので、繰り返し出るのかは未確認。
- 他のミッションの報告で SAGE が出るか（un-docs の範囲では `SAGE` が 1 件のみ）は un-docs の検索による。範囲外の S/2025/779 は図の出典に SAGE を書く別の型で、`sage-situational-awareness-geospatial-enterprise` が扱う。

## よくあるまちがい

- 第 23 項を、UNFICYP が SAGE の地図を安保理に示した例とみなす。文は件数の読み方の但し書きである。
- 989 件と 343 件を、実際の減少とみなす。報告自身が、集計の仕組みの見直しが一因かもしれないと述べる。
- S/2025/779 のような図の出典表記が、この報告にもあるとみなす。S/2021/1110 に図表は無い。

## 確かめた度合い

- `read-official`: 公式サイトの PDF（全 15 頁）で、第 23 項の文言、第 III 節 C の位置、`SAGE`・`geospatial` の語の件数（SAGE 1 件、図表の出典表記なし）を確かめた。S/2023/3 も同様。
- `searched-undocs`: `\bSAGE\b` の 1 件（S/2021/1110）。
- 未確認: S/2021/635、S/2022/533 などの前後の UNFICYP 報告の SAGE の有無、見直しの内容、SAGE が UNFICYP でいつ導入されたか。

## 出典

- S/2021/1110、S/2023/3（`https://docs.un.org/en/<記号>`）
