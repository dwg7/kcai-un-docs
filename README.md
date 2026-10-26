# kcai-un-docs

[kcai](https://github.com/dwg7/kcai)（Knowledge Co-created with AI、AI と共創した知識。kcai は AI の名前ではなく、BYOA のための知識表現）のインスタンスです。**国連の総会と安保理の文書（[yuiseki/un-docs](https://huggingface.co/datasets/yuiseki/un-docs)）を一次資料とする踏み跡**を、Markdown で残します。

目的は、国連文書の要約を作ることではありません。**問いごとに、どう確かめたか、どこまで確かめられたか、どこが外れやすいか**を残すことです。「kcai がうまく回るかは、よい問いをシードできるかにかかっている」という見立てを試す場でもあります。

## 範囲

> un-docs ＝ 総会と安保理の**英語**文書（39,363 行）。安保理決議は S/RES/2699（2023-10-02）まで。ECOSOC、専門機関、委員会、各ミッションの予算文書は含まない。

このリポジトリの踏み跡は、「国連が○○を議論してきた」とは言いません。「un-docs（総会・安保理の英語文書）の範囲では」と言います。

## 構成

- `knowledge/`: 踏み跡（一覧は [`knowledge/README.md`](knowledge/README.md)）
- `checks/`: 検索の記録（クエリ、件数、手順）と、再現用の入力
- `scripts/undocs.py`: un-docs を、記号の正規化・重複除去・合冊除外つきで検索する補助
- `QUESTIONS.md`: 種の問いの台帳と、hfu への質問
- `DECISIONS.md`、`SOURCES.md`、`AGENTS.md`（`CLAUDE.md` は入口）
- `scripts/validate_knowledge.py`: 形式検査（`python3 scripts/validate_knowledge.py knowledge`）

## 位置づけと作り方

踏み跡は AI が下書きし、`status: draft` で出します。人（hfu）が確認して初めて `reviewed` になります。確認前の `draft` は実験区画の成果で、仕事の根拠にする前に、出典（文書記号と docs.un.org）で確かめてください（`dwg7/kcai` の `docs/responsible-use.md`）。

## 管理責任者

hfu（外部への発信、承認、マージの権限）。

## 準拠する kcai

`dwg7/kcai` コミット a666869（2026-10-26 時点の main）。

## 関わり方

kcai の原則 10〜13 に従う。組織に参加や採用を求めない。参加は個人として、公開できることだけ。国連や特定の組織の公式な取り組みとして示さない。宣伝や勧誘はしない。

## ライセンス

CC0 1.0。ただし、国連文書そのもの、un-docs のデータには適用されません（それぞれの条件に従ってください）。このリポジトリは本文を転載せず、文書記号と要約・該当箇所の指示にとどめます。
