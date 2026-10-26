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
