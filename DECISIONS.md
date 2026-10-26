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
