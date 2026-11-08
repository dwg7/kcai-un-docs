# /authorities/source-hierarchy
- status: derived
- derived-from: /guides/un-docs-reading-guide, /guides/un-document-symbols-primer, /sources/un-docs, /sources/undocs-site
- verified-by: 未了(導出オブジェクト。書いた主体とは別の主体による照合は、`/inventory/derived-verification`)
- scope: このインスタンスで、出典の権威をどう順位づけるか

1. **公式の原文**(`https://docs.un.org/en/<記号>`、PDF の実体は `https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf`): 引用・段落番号の根拠(日付は、公式の PDF に採択日が無い場合があるので、日付の種類を確かめて使う。例は `/guides/un-docs-reading-guide`)。`/sources/undocs-site`。
2. **un-docs の抽出テキスト**(`/sources/un-docs`): 検索・集計の対象。**二次的な写し**で、OCR、合冊、隣の決議の混入、日付欄の誤りがある。引用する箇所は、可能なら公式の原文と照らす。
3. **二次資料**(論文、ブログ、紹介ページなど): 背景の手がかり。事実の根拠にしない。
4. **踏み跡どうしの引き**: 踏み跡の記述は、`draft`(人の確認前)。(作業指針 `/system-record/agents-original` の「出典のない断定はしない」に基づく、このインスタンスの運用の私の整理:)別の踏み跡を根拠にするときも、元の文書記号まで戻る。

# /procedures/search-un-docs-and-record
- status: derived
- derived-from: /guides/un-docs-reading-guide, /guides/geospatial-search-terms, /system-record/instance
- verified-by: 別のサブエージェントが照合済み(2026-11-08。`/inventory/derived-verification`)
- scope: un-docs を検索して、問いに答える手順(記録の残し方を含む)

1. 範囲を一文で言う(un-docs ＝ 総会と安保理の英語文書。S/RES は 2699 まで)。範囲外なら、そう答える。
2. 記号を、空白を除き大文字にして正規化する。合冊(`Vol` を含む記号)を除く。S/INF を初出の検索から除く。同じ記号は 1 本にする(pdf を優先)。
3. 日付の種類(採択、配布、その他)を決め、どれを使ったかを書く。
4. 語の表(同義語、関連語、試して外れた語、外れ方)を残す。外れ方の型は、多義、重複、OCR(古い年代の語は取りこぼしやすい)、合冊、隣の決議の混入、`lang` が `en` でも混ざるフランス語の行、日付欄の誤り。
5. 件数は、ユニークな記号の数か、本文が異なる文書の数かを書く(`/guides/un-docs-reading-guide` の実測表のように、両方が違う値になりうる)。
6. 引用する箇所は、公式の原文で照らす。届かないときは、届かないと書く。
7. 確かめた度合い(`searched-undocs` / `read-official` / `read-only` / `mixed` / 未確認)を明記する。
8. 検索式と件数を記録する(`checks/` に置く。このファイルには取り込んでいない。`/system-record/exclusions`)。

# /procedures/before-saying-first-appearance
- status: derived
- derived-from: /searches/responsibility-to-protect-first-appearance, /searches/geospatial-first-appearance, /searches/first-and-latest-cartographer-appointments
- verified-by: 別のサブエージェントが照合済み(2026-11-08。`/inventory/derived-verification`)
- scope: 「初出」「最初」「最新」と答える前の手順

1. 「同じものとみなす条件」を決める(句か概念か、語か内容か、どの種類の文書か)。条件が変われば答えが変わる。
2. 範囲を添える(un-docs の範囲の初出で、国連全体の初出ではない)。
3. 日付の種類を添える(会議日、採択日、配布日)。
4. 日付欄の誤りと、OCR による古い文書の取りこぼしを疑う(`/guides/un-docs-reading-guide`)。
4b. 公式の原文で段落まで確かめられたものと、検索の結果だけのものを分けて書く。
5. 「最初」「最新」は、その検索式と範囲に限ると書く。

# /decision-support/out-of-scope-response-protocol
- status: derived
- derived-from: /system-record/instance, /guides/un-docs-reading-guide
- verified-by: 別のサブエージェントが照合済み(2026-11-08。`/inventory/derived-verification`)
- scope: 範囲外の問いへの答え方

- **範囲内**: un-docs の範囲(総会と安保理の英語文書、S/RES/2699 まで)か、踏み跡が公式サイトで読んだと記す文書。根拠のオブジェクトのパスを示して答える。
- **範囲外だが示唆できる**: 例えば S/RES/2700 以降の決議。このファイルに内容はないと述べ、公式サイト(`https://docs.un.org/en/<記号>`)で確かめるよう示す。内容を推測で埋めない。
- **範囲外で示唆もできない**: 国連や加盟国の立場の評価、現在の組織の最新の人員・予算の値、所属組織の内部の知識。答えられないと述べる。

# /lexicon/terms
- status: derived
- derived-from: /syntheses/un-geospatial-organization-timeline, /readings/a-res-69-309-geospatial-consolidation-and-unlb-service-chief-post, /syntheses/un80-oict-ungsc-2026-changes-for-geospatial, /syntheses/sage-situational-awareness-geospatial-enterprise, /syntheses/un-ggim-ecosoc-geospatial-institutional-arc, /guides/un-document-symbols-primer
- verified-by: 別のサブエージェントが一部照合(`/inventory/derived-verification`)。英語名は「私の補足」で、公式サイトでは未照合
- scope: このファイルで使う略語と用語(初出で展開)

| 語 | 意味 |
|---|---|
| un-docs | yuiseki が公開する、総会と安保理の英語文書の抽出テキストのデータセット(`/sources/un-docs`) |
| S/PV | 安保理の会議録(会合ごとに 1 件)。`/guides/un-document-symbols-primer` |
| S/RES | 安保理決議 |
| S/PRST | 安保理議長声明(決議ではない) |
| A/RES | 総会決議 |
| A/PV | 総会本会議の会議録 |
| S/INF | 安保理の決議と決定を期間ごとにまとめた冊子 |
| ACABQ | 行財政問題諮問委員会(英語名 Advisory Committee on Administrative and Budgetary Questions は私の補足) |
| UNLB | 国連ロジスティクス基地(ブリンディジ。英語名は私の補足) |
| UNGSC | 国連グローバル・サービスセンター(ブリンディジとバレンシアの 2 か所。UNLB(ブリンディジ)とは別の名で、取り違えない。関係は `/syntheses/un80-oict-ungsc-2026-changes-for-geospatial` を参照。英語名は私の補足) |
| OICT | 情報通信技術局(英語名は私の補足) |
| UN-GGIM | 地球規模の地理空間情報管理に関する国連専門家委員会(ECOSOC 決議 2011/24 に基づく。`/syntheses/un-ggim-ecosoc-geospatial-institutional-arc`) |
| SAGE | Situational Awareness Geospatial Enterprise(`/syntheses/sage-situational-awareness-geospatial-enterprise`) |
| OCR | 画像から文字を読み取る処理。綴りが崩れる |

# /inventory/derived-verification
- status: open
- scope: 導出オブジェクト(`/authorities/`、`/procedures/`、`/decision-support/`、`/lexicon/`、`/acceptance-tests/`)の検証状況
- 書いた主体は AI(Claude、この作業の主エージェント)。
- 2026-11-08: 別のサブエージェントが、踏み跡と `checks/` の記録に照らして照合した(AI による照合で、`verified` ではない)。`/system-record/instance` の範囲の数値は一致。直した点: 件数の数え方、OCR・日付欄の誤り・仏語混入の追記、日付の根拠の言い過ぎ、略語表の出所と SAGE の展開、UNGSC と UNLB の関係。
- 未了: 数値のデータ再集計(parquet が手元になく、未実施)。略語の英語名の公式サイトでの照合。データ末尾 2023-10-16 の出所は SAGE 関連の記録にのみあり、`/guides/un-docs-reading-guide` には無い。
- 人による確認: 未了。

