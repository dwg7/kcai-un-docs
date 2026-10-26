# 次のエージェントへの依頼（叩き台）

作成: 2026-10-26。hfu が別のエージェントに渡すためのプロンプト。日本語で作業し、敬語は不要。

---

あなたは `dwg7/kcai-un-docs` の作業担当のエージェントです。このリポジトリは kcai（`dwg7/kcai`）のインスタンスで、国連の総会・安保理の文書（yuiseki/un-docs、コミット 6cd1cf0 を pin）を一次資料として、問いごとに「どう確かめたか、どこまで確かめられたか、どこが外れやすいか」を踏み跡（Markdown）に残します。

## まず読む（この順）

1. このリポジトリの `AGENTS.md`、`DECISIONS.md`（特に 2026-10-26 の節）、`QUESTIONS.md`、`checks/README.md`
2. `knowledge/README.md` と、既存の踏み跡 9 本（先に `un-docs-reading-guide`）
3. `dwg7/kcai` の `PRINCIPLES.md`、`docs/knowledge-format.md`（必要なら）

## これまでの状態

- 足場、補助スクリプト（`scripts/undocs.py` 検索、`undocs_ctx.py` 文脈、`official.py` 公式原文の照合）、踏み跡 9 本（すべて `draft`）が `main` にある。
- 公式原文は `https://docs.un.org/en/<記号>` のページが埋め込む `https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf` から取得できる（`scripts/official.py`、`pdftotext` 要）。`-layout` は 2 段組みで段が混ざるので使わない。
- 前身の調査（`hfu/kcai-yuiseki-datasets`）の分類と要約の訂正は済んでいる。差分は `checks/un-docs-geospatial-institutions-recheck.tsv`。

## 作業の進め方（hfu の決定）

- **`main` に直接コミットして push してよい。ブランチは切らない。** コミットは小さく。PR は作らない。
- `reviewed_by` は空のまま。AI は `reviewed` 以上にしない。
- **un-docs の外の一次資料（UN-GGIM、経済社会理事会、宇宙委員会、ミッション予算・実績報告など、docs.un.org にあるもの）を `sources` に加えてよい。** その場合、`verified_how: read-official` を使い、本文に「un-docs の範囲外」と明記する。
- 外部（国連、Hugging Face、他の GitHub リポジトリ）への投稿・コメント・PR はしない。大きなデータをリポジトリに入れない。通信先の制限をすり抜けない。届かないものは hfu に一覧で伝える。
- 判断が分かれることは推測で埋めず、`QUESTIONS.md` に書く。決定は `DECISIONS.md` に追記する（消さない）。
- 本文の転載はしない（要約と該当箇所の指示、引用は一文以内）。国連の立場、国境、地図、紛争に関わる主題は、文書の記述を引くにとどめ、評価を足さない。
- 数値は `scripts/undocs.py` で再現できる形で `checks/` に残す。形式検査: `python3 scripts/validate_knowledge.py knowledge`。

## 作業（優先度順）

### 高

1. **問い 1 の「結論」の面を、un-docs の外の一次資料で補う。** UN-GGIM の設置（経済社会理事会決議 2011/24）と、その後の主な成果（決議・報告）、総会決議 69/266、経済社会理事会が 2018-07-02 に承認した「災害のための地理空間情報とサービスの戦略的枠組み」、宇宙委員会の議題「宇宙由来の地理空間データの持続可能な開発への利用」の経過。`geospatial-themes-frameworks-conclusions` の「未確認」を、確かめた度合いを分けて更新する（新しい踏み跡に分けてもよい）。
2. **問い 3 の「ミッションの GIS 機能」を、予算・実績報告で補う。** 例: UNLB／グローバル・サービスセンターの予算報告（A/…/…）、UNIFIL・MINURSO・UNFICYP・MINUSMA・UNSOS の予算文書の GIS・地理空間の項。`un-mission-gis-mentions-in-un-docs` の「予算文書は未確認」を更新する。UNLB の GIS センターが「Service for Geospatial, Information and Telecommunications Technologies」になった時期（2007〜2015 年）を確定する（`un-geospatial-organization-timeline` の未確認の点）。
3. **ZIP などの配布物**（kcai の `docs/distribution.md`）をどうするかの案を `QUESTIONS.md` に書く（実装は hfu の判断後）。

### 中

4. **語の展開の検討（問い 3 (a) の続き）。** `imagery` 231 文書、`mapping`（連語に絞る）、`geo-information|geographic data|spatial analysis`、`UNOSAT`（4 文書）。ミッション報告での衛星画像・マッピングの扱いを、国連の機関が行うもの（UNOSAT など）と他機関・各国の分析（IAEA、制裁パネル）に分け、悉皆の語彙を決める。`GIS` は大文字の語に限る（大文字小文字無視は人名・地名の `gis` を拾う）。結果は `geospatial-search-terms` に反映する。
5. **地理的傾向の集計の拡張。** `geospatial` 以外の語（衛星画像など）で、S/PV の発言国（`Mr. X (Country)` の表記）の集計を試す。`geospatial-geographic-tendency` に追記するか別の踏み跡にする。国連は国を「語る」文書で、地図上の位置を示す文書ではない点に注意。
6. **種の問いの候補を `QUESTIONS.md` に載せ、hfu に優先度を聞く。** 候補: 安保理における衛星画像（`satellite imagery` 194 文書、S/PV 68、S/yyyy/n 113）／S/PV の採決記録（`votes in favour` を含む会議）／宇宙空間決議の定型文の年別の追跡（61/111 以降の毎年の決議）。各候補について、よい問いの条件（出典の記号に落ちる、素朴な検索に落とし穴がある、範囲を言える、多面的、語の表が残る）に照らした見立てを 1〜2 行で。

### 低

7. **下準備の宿題（`un-docs-reading-guide` の未確認）。** S/RES/2700〜2722（2023 年 10〜12 月）が un-docs に無い理由（公式側にあるか）、S/PV の欠番 90 の中身、`S/RES/1 (1946)` と `S/RES/1(1946)` の重複 1,548 番号のうち本文が違う 74 組の違い、`A/RES/2776〜2779(XXVI)` が同じ見出しを含む理由（決議集の見開き）。記号の正規化関数（空白除去・大文字化）のテストを `scripts/` に追加する。
8. **上流（yuiseki/un-docs）への報告候補の下書き。** 重複綴り、範囲の切れ目（S/RES/2699 まで）、OCR の説明（カードの「総会の補遺が中心」と実測の A/RES 82%）の食い違い、日付欄の誤り（A/RES/2778(XXVI)、S/PV.2411(OR)）、1970〜80 年代の A/RES への隣の決議の混入。`drafts/upstream/` に置く。**投稿はしない。** hfu が判断する。
9. 会議録の発言者（S/PV.4660 (Resumption 1) の ICISS 報告書の題に触れた発言、A/58/PV.78 の二段の責任の発言）を、公式の PDF の列組みを読んで確かめる。

## 最初の報告に含めること

- 何をしたか（踏み跡の追加・更新、確かめた度合いの変化）。
- 公式サイトや外部資料で届かなかったものの一覧。
- hfu への質問（未確定の点）。
