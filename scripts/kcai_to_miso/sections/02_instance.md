# /system-record/instance
- status: stated
- name: miso-un-docs(国連の総会と安保理の文書を一次資料とする踏み跡。kcai のインスタンス `kcai-un-docs` を、単一の Markdown(miso)に移したもの)
- id: un-docs
- version: {{VERSION}}
- as_of: {{AS_OF}}
- 作成方法: 国連の総会と安保理の英語文書(`yuiseki/un-docs`、コミット 6cd1cf0)を AI が検索・通読し、一部は公式サイト(`docs.un.org`)の原文と照らして、{{N_TRACES}} 件の踏み跡を `status: draft` で書いた。それを、**本文と元の front matter を一字も変えずに**、仮想パスのオブジェクトとして収めた。そこに、踏み跡だけを材料にした導出オブジェクト(手順、用語、判断支援、受け入れテスト)を加えた(`status: derived`)。AI(Claude)が hfu の依頼に基づいて作った。**人による内容確認は未了。**
- 管理責任者: hfu(外部への発信、承認、マージの権限)。AI は `reviewed` 以上にしない。
- 位置づけ: 個人(hfu)による公開資料の整理の試作であり、国連や特定の組織の公式な取り組みでも、誰かの推薦を受けたものでもない。**業務の根拠にそのまま使わず、文書記号と公式サイトで確かめる。**
- 目的: 国連文書の要約を作ることではない。**問いごとに、どう確かめたか、どこまで確かめられたか、どこが外れやすいか**を残す。
- 境界づけ(範囲内): un-docs(総会と安保理の英語文書、39,363 行、安保理決議は S/RES/2699 まで、データの末尾は 2023-10-16)で検索・通読できる事柄と、そこから公式サイトで原文を読んで確かめた事柄。主な題材は、地理空間情報と国連の地理空間の組織、衛星画像と安保理、国境画定、保護する責任、人間の安全保障・ネクサス・エージェンシーの語、文書の記号の読み方。
- 範囲外: ①2023-10 以降の安保理決議(S/RES/2700 以降)と、それ以降の会議録の内容。②ECOSOC、専門機関、委員会、各ミッションの予算文書など、総会と安保理の文書の外(一部は公式サイトで読んだ跡があるが、網羅ではない。各踏み跡の範囲の注記に従う)。③英語以外の文書。④国連や加盟国の立場の評価、国境・紛争の当否の判断。⑤所属組織の内部の知識。⑥現在の組織の人員や予算の最新値(`volatile`。公式サイトで確かめる)。
- 時間範囲: データは 2023-10-16 まで。公式サイトで読んだ文書は踏み跡ごとの `as_of` による(最新は 2026 年の文書を含む)。
- データ版: yuiseki/un-docs の `documents.parquet`、コミット 6cd1cf0(409MB)。大きなデータはこのリポジトリに入れない。
- 機微情報: 含まない。
- 正本: この `.md` ファイル(`/system-record/canonical-source`)。
- ライセンス: CC0 1.0(`/system-record/license-original`)。出典自体の権利は、各出典に従う。

# /system-record/concept-version
- status: stated
- concept-version: dwg7/miso コミット 2ce1553(2026-11-07 時点の CONCEPT.md)
- 備考: 本書の写しはインスタンスに持たない。写しはずれるので、版の識別だけを宣言する。

# /system-record/execution-types
- status: normative
- 宣言: このインスタンスは、**チャット型**(Copilot、Gemini など。このファイルを添付して使う)と、**コードエージェント型**(リポジトリのファイルを直接編集する)の両方を想定する。
- チャット型: 正本はこのファイルの全文で、会話中にあるのは添付の写しである。規則は `/system-record/agent-contract`(更新したら全文を `.md` で返す、断片から正本を作らない)。**約 46 万字(UTF-8 で約 0.8MB)のため、添付や返却が上限を超える製品がありうる。その場合は、読むだけの用途にとどめ、更新は行わない**(`/open-questions/single-file-size`)。
- コードエージェント型: 正本は `miso/un-docs.md`。このファイルを直接編集し、検査器を通す(`/system-record/tooling`)。
- 実行環境の型ごとの実際の動作は、**未検証**である(`/inventory/test-backlog`)。

# /system-record/status-vocabulary
- status: normative
- authority: dwg7/miso の CONCEPT.md §5.1(中核語彙とローカル別名の対応表)を、このインスタンスに適用した形。承認権者は hfu。
- 三つの語彙を混ぜない:

| 語彙 | 何についての語か | 語 |
|---|---|---|
| 内容の状態(`status`) | オブジェクトの性質 | `stated`(出典の記述の要約)、`derived`(複数から導いた解釈)、`normative`(守るべき規則)、`open`(未解決)、`volatile`(変わりやすい)。将来、人が確認したものに `verified` |
| kcai の確認状況(`kcai-status`、`human-review`) | 踏み跡の人による確認 | `draft`(全件)、`reviewed`、`stable`、`deprecated`。`human-review: none` は確認者の記録がないこと |
| 受け入れテストの結果(`result`) | テストの結果 | `pass`、`partial`、`fail`、`volatile`、`untested` |

- **kcai の `verified_how` との対応**(各踏み跡の front matter の語。踏み跡のオブジェクトでは `verified-how:` に写してある):

| `verified_how` | 意味 | miso での扱い |
|---|---|---|
| `searched-undocs` | pin した un-docs を検索して確かめた | `status: stated`。「un-docs を AI が検索して確かめた」範囲に限り確かめられたもので、`verified` は付けない(人の確認がないため) |
| `read-official` | 公式の原文と照らした | 同上(「公式の原文と AI が照らした」) |
| `mixed` | 上の混合 | 同上。主張ごとに確かめた度合いが違う。本文の「確かめた度合い」の節に従う |
| `read-only` | 読んだだけ | `stated`。突き合わせていないので、`secondary` に近い扱いで引く |
| (未確認と明記したもの) | | 本文の「未確認」を `open` として扱う |

- `verified` は、人(hfu)が確認し、`reviewed_by` に記録したときに、確認した範囲を限定して付ける。現時点で `verified` のオブジェクトはない。
- `stated` は「出典がそう述べている」ことで、**主張が事実として正しいことを保証しない**。un-docs の抽出テキストは二次的な写しで、引用する箇所は公式の原文と照らす。

# /system-record/trace-meaning
- status: stated
- 「踏み跡」は、このインスタンスでは**出典踏み跡**(どの文書をどう検索・通読し、どこまで確かめたかの跡)である。miso の `/traces/`(運用の出来事の記録)は、まだ使っていない。種別は `/guides/`(読み方・記号・落とし穴)、`/searches/`(検索・集計・初出の問い)、`/readings/`(個別文書の読み)、`/syntheses/`(複数の整理)。

# /system-record/file-set
- status: stated
- scope: このインスタンスのファイル集合
- `miso/un-docs.md`: **正本**(本ファイル。単一の Markdown で完結する)。
- `knowledge/`: 移行時点(2026-11-08)の踏み跡の**凍結した写し**。正本ではない。往復検査(`scripts/miso_roundtrip_check.py`)は、このファイルから `knowledge/` と同じ内容を復元できることを確かめる。凍結後に正本を直したときは、`knowledge/` は古くなる。
- `checks/`(検索の記録、TSV、独立レビューの記録)、`scripts/`(検索補助と検査器)、`handoffs/`、`drafts/`: 証拠と道具。このファイルの外にあり、取り込んでいない(`/system-record/exclusions`)。
- 他のファイルがなくても、このファイルだけで答えられるよう作ってある。

# /system-record/canonical-source
- status: normative
- 決定: 2026-11-08、hfu の決定により、踏み跡の正本を `miso/un-docs.md` に移す。以後の編集はこのファイルで行う。`knowledge/` は凍結した写しで、`scripts/validate_knowledge.py` は移行時点の写しの検査にのみ使う。
- 移行の道具 `scripts/kcai_to_miso/build.py` は、`knowledge/` からこのファイルを**再生成する**ため、実行すると正本を上書きする。実行には `--force-migration` が要る。
- 更新の単位は、単一の Markdown 全文。検査器(`scripts/check_miso.py`)と往復検査を通ったものを正本とする。

# /system-record/exclusions
- status: stated
- 取り込まなかったもの(意図的な除外):
  - `checks/`(検索のクエリ・件数・手順の記録、TSV、独立レビューの記録 `checks/reviews/`)。各踏み跡の「確かめた度合い」の節から参照されている。再現のための証拠で、リポジトリに残す。
  - `scripts/`(`undocs.py` など)、`handoffs/`、`drafts/`、`.github/`。道具と作業の引き継ぎで、知識ではない。
  - un-docs のデータ本体(409MB)。
  - `.git/` の履歴。
- 元のリポジトリの**情報**のうち、取り込んだもの: 踏み跡 {{N_TRACES}} 件(本文と元の front matter)、`README.md`、`knowledge/README.md`、`AGENTS.md`、`CLAUDE.md`、`DECISIONS.md`、`QUESTIONS.md`、`SOURCES.md`、`LICENSE`(`/system-record/path-map`)。

# /system-record/tooling
- status: stated
- `scripts/check_miso.py`: miso の検査器(CONCEPT §5.3 の最小仕様。エラー: UTF-8、空でない、Office バイナリでない、第 1 レベル見出しが `# /…` の形で一意。警告: 内部パス参照の解決、状態語、出典 id)。
- `scripts/miso_roundtrip_check.py`: 各踏み跡のオブジェクトから元の `knowledge/*.md` を復元し、元のファイルと比べる(可逆性)。
- `scripts/kcai_to_miso/`: 移行の道具(`--force-migration` が要る)。`core.py` と `build.py` は、`dwg7/kcai-survey-training` の `scripts/kcai_to_kcaim/` の構造を参考に作り直した。`kindmap.py` と `sections/` はこのインスタンス用に新しく書いた(先行例の内容は持ち込んでいない)。
- `scripts/undocs.py`、`official.py` ほか: 検索と公式サイト照合の補助(`checks/README.md`)。

# /system-record/migration-record
- status: stated
{{MIGRATION_RECORD}}

