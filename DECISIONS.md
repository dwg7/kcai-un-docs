# DECISIONS

決めたことと理由を時系列で追記します。既存の決定は消しません。

## 2026-10-26: 初期設定

### 決定事項

1. 管理責任者は hfu。外部（国連、Hugging Face、他の GitHub リポジトリ）への発信は hfu が行う。
2. ライセンスは CC0 1.0（国連文書・un-docs には適用しない）。
3. 形式は kcai の核（`id` `title` `status` `sources` `authors` `reviewed_by` `updated` `related`、見出しは「要点」で始まり「出典」で終わる）に従い、次の任意タグを足す: `verified_how`（`searched-undocs | read-official | read-only | mixed`）、`dataset_rev`、`as_of`、`cites`。`status` は kcai 標準（`stale` は使わない）。データの版が変わったら `dataset_rev` と `as_of` で示す。
4. データは **pin した版（コミット 6cd1cf0）** を使う。409 MB はリポジトリに入れず、スクラッチに取得し、sha256 を `SOURCES.md` に記録した。
5. 検索は `scripts/undocs.py` に一本化する（記号の空白除去、同記号の重複除去、合冊の除外、日付の優先順位）。踏み跡の数値はこのスクリプトで再現できる形で `checks/` に残す。

### kcai との食い違い・気づき

- 最初のセッションは `dwg7/kcai` と `hfu/kcai-yuiseki-datasets` を add_repo で追加できず（拒否）、先に `kcai-terrio` のコピーのスクリプトを土台にしていた。その後、hfu の指示で両リポジトリを取り込めたので、`scripts/` は **kcai 本体（a666869）のもの**に差し替えた（terrio のコピーとの違いは `stale` の 1 行のみだった）。
- 作業ブランチの指定が無かったため、`claude/bootstrap-un-docs` で作業した（`QUESTIONS.md` に質問）。
- `templates/instance/README.md` は「測量分野」の文言を含むので、本リポジトリ向けに書き直した。

## 2026-10-26: 公式原文の照合の経路、S/INF の扱い、数え方

### 決定事項

1. 公式原文との照合は `scripts/official.py` で行う。`https://docs.un.org/en/<記号>` のページは PDF を iframe で埋め込む枠で、実体は `https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf`。これは公開ページが自ら読み込む経路で、認証や制限のすり抜けではない。取得物（PDF）はリポジトリに入れない。文字化は `pdftotext`（`-layout` は 2 段組みで段が混ざるので使わない）。
2. 記号の正規化は「空白を除き、大文字にする」。`S/inf/72` と `S/INF/72`、`ADD.3` と `Add.3` が別の行で入っていたため（最初の実装は空白のみで、数値が数本ずれた。踏み跡の数値は大文字化後に統一した）。
3. 「初出」の検索では、**S/INF（決議集）と合冊を除く**。決議の本文を再掲し、日付が当てにならない。除かない場合は、除かなかったと書く。
4. 日付は採択>配布>その他の順に採り、種別を書く。日付欄の誤りがありうるので、「最も早い日付」の先頭は疑う。
5. 前身（`hfu/kcai-yuiseki-datasets`）の分類・要約を直す場合も、前身のリポジトリには書かず、本リポジトリの `checks/…recheck.tsv` に差分を置く。

### kcai との食い違い・気づき

- 形式の核は kcai のまま。`verified_how` の値を `searched-undocs | read-official | read-only | mixed` とした（kcai-terrio の `played | read-source | read-docs` に相当する un-docs 用の区分）。
- 公式の PDF は、1970〜80 年代の総会決議で**決議集の見開き**（複数の決議が列組みで並ぶ）の場合がある。un-docs の抽出テキストにも隣の決議が混ざる（`un-docs-reading-guide`）。「公式の原文と照合した」と書くときは、該当する決議の節に語があるかまで見る必要がある。

## 2026-10-26（hfu の回答）

1. **`main` に直接入れる。ブランチは切らない。** 最初の作業ブランチ `claude/bootstrap-un-docs` は `main` に取り込んだ（fast-forward）。
2. `reviewed_by` は当面空のまま（すべて `draft`）。
3. **un-docs の外の一次資料（UN-GGIM、経済社会理事会、ミッション予算など）を `sources` に加えてよい。** `verified_how: read-official` で示し、「un-docs の範囲外」と明記する。
4. **前身リポジトリ（`hfu/kcai-yuiseki-datasets`）の要約の訂正は行う。** ブランチ `claude/youthful-goldberg-tq7dzs` に、`knowledge/cross/un-docs-geospatial-institutions.md` の訂正節と、TSV の要約・区分の訂正を push した（コミット cb12af5、50cbaf2。TSV の改行は元の CRLF）。`main` への反映は hfu。
5. 追加作業（`handoffs/next-agent-prompt.md`）は、このセッションでは行わず、hfu が別のエージェントに依頼する。

## 2026-10-26（続き）: 外部の一次資料、独立レビュー、ブランチ

1. 外部の公式文書（経済社会理事会、UN-GGIM、UNLB とミッションの予算、特別委員会の報告）は、`documents.un.org` の API で取得できたものを `read-official` として扱う。`ecosoc.un.org`、`un.org`、`peacekeeping.un.org`、`oios.un.org` は HTTP 403/405 で届かなかったため、回避せず「届かなかった」と各踏み跡に書く（SAGE、UN Open GIS の踏み跡）。
2. `dwg7` は、UN Open GIS Initiative の「ドメイン作業部会 7（UN Smart Maps Group）」を指すと読める（FOSS4G 2025 の講演要旨。二次資料）。踏み跡 `peace-operations-review-2026-implications-for-un-open-gis` はこの読みにもとづく。誤りなら訂正する（`QUESTIONS.md`）。
3. **独立レビューを導入した**（hfu の提案）。書き出した踏み跡を、別の担い手（別のエージェント）が、データと公式原文で主張を抜き取り検証し、文章の質も評価する。作成者はレビューの報告を受けて直す。巨大な文書集合では、作成と検証を分けるのが有効という見立て（`large-corpus-work-volume-versus-trace-yield`）。
4. 文章の質を重視する（「言葉足らず」への指摘）。踏み跡の本文は、主語と条件を省かない完全な文で書く。表の中の語は、説明なしの専門語や体言止めの連続にしない。
5. ブランチ: 取り込み済みの `claude/bootstrap-un-docs`（本リポジトリ）と `claude/youthful-goldberg-tq7dzs`（前身）は、リモートからの削除を試したが、git の push が切断され（プロキシ側の拒否と見られる）、`gh` の使用は許可されなかった。回避せず、削除は hfu が GitHub 上で行う。内容はすべて `main` に取り込み済み。


## 2026-10-26 独立レビュー A・B の反映（続き）

- レビュー A（読み方、保護する責任、検索語、初出の 4 本）の指摘を反映した。事実の誤り（`S/PV.4990`/`S/PV.5052` は `(Resumption 1)`、`cites` の 947 文書）、合冊の説明、「毎年」の言い過ぎ、段 B の式の明記、略語の展開を直した。
- 再現できなかった値（隣の決議が混ざる行の件数、仏語行の件数、衛星画像の主体の分け）は、再現できないと本文に書いた。
- `geospatial-themes-frameworks-conclusions` に、レビュー B の残りを反映した（Decides の数え方、UN-GGIM 踏み跡への参照、「旗」の説明）。

## 2026-10-26 独立レビュー D・E・F の反映

- 1 回目に見ていなかった 9 本を、3 人（D: 深掘り 3 本、E: 活発度・宇宙空間決議・衛星画像、F: 予算・平和活動の見直し・大規模文書集合）で独立にレビューし、指摘を反映した。
- 主な事実の訂正: A/RES/42/186 の GIS は勧告 (q) と第 92 項の 2 か所に出る。S/PV.4319 の勧告は McAskie 氏の訪問のもので、S/2001/434（ファル氏のミッション）とは別。宇宙空間決議の災害管理の文は 69/85（2014 年）から。75/92 は COVID-19 への対応の特別の決議。UNFICYP の 2026/27 年度予算案は、成果物の一覧を Umoja Analytics に移している。
- 弱めた結論: 活発度の仮説は「支持されない」から「支持する材料は見つからなかった」へ。「制度化された」「間接的なものになる」「追い風」など、根拠より強い言い方を、条件つきに直した。
- 衛星画像の踏み跡の「加盟国と国連の機関にほぼ二分」は、件数表が無いので「大まかには」に弱め、IAEA を国連の機関と一括りにしない書き方にした。
- 再現できない値（衛星画像の主体の分け、S/ 文書 113 件の内訳）は、再現できないと本文に書いた。
