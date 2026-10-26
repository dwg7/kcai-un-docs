# AGENTS

この文書は、`dwg7/kcai-un-docs` で作業するすべての AI のための案内の本体です。特定の AI 製品に依存しない書き方にします。

## このリポジトリは何か

[kcai](https://github.com/dwg7/kcai)（Knowledge Co-created with AI、AI と共創した知識。kcai は AI の名前ではなく、BYOA のための知識表現）のインスタンスで、**国連の総会と安保理の文書（[yuiseki/un-docs](https://huggingface.co/datasets/yuiseki/un-docs)）を一次資料とする踏み跡**を残します。管理責任者は hfu（外部への発信、承認、マージの権限）。

目的は、国連文書の要約を作ることではありません。**問いごとに、どう確かめたか、どこまで確かめられたか、どこが外れやすいか**を残すことです。kcai がうまく回るかは、よい問いをシードできるかにかかっている、という見立てを試す場です。

先行するインスタンス: `dwg7/kcai-terrio`（運用の例）、`dwg7/kcai-survey-training`。

## 範囲を一文で言う

> un-docs ＝ 総会と安保理の**英語**文書（39,363 行）。安保理決議は S/RES/2699（2023-10-02）まで。ECOSOC、専門機関、委員会、各ミッションの予算文書は含まない。

「国連が○○を議論してきた」と一般化しない。「un-docs（総会・安保理の英語文書）では」と書く。

## 踏み跡

- `knowledge/` に 1 主題 1 ファイル。一覧は `knowledge/README.md`。小さく、`status: draft` で出す。
- 形式は kcai の形式に、次の項目を足したもの（足した理由は `DECISIONS.md`）:

```markdown
---
id: <英小文字とハイフン。一度付けたら変えない。ファイル名と一致>
title: <日本語の題名>
status: draft | reviewed | stable | deprecated
verified_how: searched-undocs | read-official | read-only | mixed   # 下の「確かめた度合い」
dataset_rev: <yuiseki/un-docs のコミット。pin した版>
as_of: <YYYY-MM-DD>
sources:
  - <文書記号、公式サイトの URL、checks/ の記録>
authors:
  - <書いた人。AI 支援の有無を必ず書く>
reviewed_by: []
updated: <YYYY-MM-DD>
related: []
---

## 要点
## 詳しく
## よくあるまちがい
## 確かめた度合い
## 出典
```

(最初の見出しは「要点」、最後は「出典」。`python3 scripts/validate_knowledge.py knowledge` で検査し、CI でも実行する。)

## 確かめた度合い（`verified_how` と本文の書き分け）

1. **un-docs を検索して確かめた**（`searched-undocs`）: 実際に pin した版を検索した。クエリと件数を `checks/` に残す。
2. **公式の原文で確かめた**（`read-official`）: `https://docs.un.org/en/<記号>` の原文と照らした。
3. **読んだだけ**（`read-only`）: 文書や二次資料を読んだが、突き合わせていない。
4. **未確認**: 書く場合は「未確認」と明記し、推測で埋めない。

un-docs の抽出テキストは**二次的な写し**。引用する箇所は可能なら公式の原文と照らす。届かない場合は、届かないと書く。

## 書き方の約束

- 出典は**文書記号**（例 `S/RES/1674 (2006)`、`A/RES/69/308`）と公式サイトの文書（`https://docs.un.org/en/<記号>`）。
- 本文の転載はしない。要約と該当箇所の指示にとどめる。引用が必要なら一文以内。
- 検索語、試して外れた語、外れ方（多義、重複、OCR、合冊）を残す。同義語・関連語の表は次の問いに再利用する。
- AI は `reviewed` 以上にしない。人（hfu）が確認して `reviewed_by` に記録する。
- 国連の立場、国境、地図、紛争に関わる主題は、文書の記述を引くにとどめ、評価を足さない。公開できる内容に限り、敬意をもって書く。

## 守ること

- 外部（国連、Hugging Face、GitHub の他のリポジトリ）への投稿・コメント・PR はしない。発信は hfu が行う。
- 認証情報を扱わない。公開データだけを使う。大きなデータ（un-docs の 409MB など）をリポジトリに入れない。一時ファイルはリポジトリ外（スクラッチ）に置く。
- 通信先の制限をすり抜けない。届かない配信先は hfu に一覧で伝える。
- 判断が分かれることは推測で埋めず、hfu に質問する（`QUESTIONS.md`）。決定は `DECISIONS.md` に追記する（消さない）。
- コミットは小さく。PR は、hfu が求めたときだけ作る。

## 関わり方（kcai の原則 10〜13）

働きかけない。参加は個人として、公開できることだけ。閉じた環境でも読める形で配る。隠さないが、前に出さない。国連や特定の組織の公式な取り組みとして示さない。

## データの読み方

`checks/README.md` を見る。データは `https://huggingface.co/datasets/yuiseki/un-docs/resolve/6cd1cf0/documents.parquet`（409MB、pin した版）。
