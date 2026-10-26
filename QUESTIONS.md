# 種の問いの台帳と、hfu への質問

## 種の問い

| # | 問い | 踏み跡 | 状態 |
|---|---|---|---|
| 0 | un-docs をどう読むか（段階 0） | `un-docs-reading-guide` | draft（提出済み） |
| 1 | 国連の文書で地理空間情報という言葉はいつ頃から使われ、どのような課題・枠組みで議論され、どのような結論で、どのような地理的傾向か | `geospatial-search-terms`、`geospatial-first-appearance`、`geospatial-themes-frameworks-conclusions`、`geospatial-geographic-tendency` | draft（結論の面は UN-GGIM 等の一次資料が要る） |
| 2 | 「保護する責任」の概念としての初出は | `responsibility-to-protect-first-appearance` | draft |
| 3 | 地理空間情報課・UNLB の地理空間サービス・ミッションの GIS 機能の表現 | `un-geospatial-organization-timeline`、`un-geospatial-institutions-in-un-docs`、`un-mission-gis-mentions-in-un-docs` | draft（予算文書は未確認） |

## hfu への質問

（答えが出たら `DECISIONS.md` に移し、ここから消す。）

### A. 判断が要るもの

（なし。2026-10-26 の回答は `DECISIONS.md` へ移した。）

### B. 進め方の確認

5. **「初出」の検索の既定**（S/INF と合冊を除く、条件を表にして並べる）を規約にしてよいか（今は踏み跡ごとに書いている）。
6. 公式サイトへの届き方: `docs.un.org/en/<記号>` のページ自体は PDF を `documents.un.org` から読み込む枠で、PDF の取得はその公開経路（ブラウザと同じ）で行った。制限や認証をすり抜けてはいない。今回、届かなかった配信先は無かった。
7. （解決）会議録の発言者は公式の PDF で確認した: S/PV.4660 (Resumption 1) はカナダ（Heinbecker 氏）、A/58/PV.78 はカナダ（Price 氏）。`responsibility-to-protect-first-appearance` に反映。

### C. 種の問いの候補（hfu に優先度を聞く）

「よい問いの条件」（1 出典の記号に落ちる、2 素朴な検索に落とし穴がある、3 範囲を言える、4 多面的、5 語の表が残る）に照らした見立て。件数は 2026-10-26 の un-docs（6cd1cf0、ユニーク記号・合冊除外）。

| # | 候補の問い | 件数・手がかり | 条件との見立て | 見立ての難しさ |
|---|---|---|---|---|
| C1 | **安保理で衛星画像は誰が、何のために持ち出すか**（`satellite imagery`） | 194 文書（S/yyyy/n 113、S/PV 68）。2010 年代が中心。主体は IAEA・専門家パネル・各国・ミッションに分かれる（`geospatial-search-terms`）。発言国の集計は `scripts/speaker_counts.py` | 1 ○（記号に落ちる）、2 ○（主体の取り違え、`imagery` の比喩）、3 ○、4 ○（主体・目的・年代・紛争）、5 ○。**紛争・疑惑に触れるので、記述にとどめ評価しない** | 中。主体の分類は文書ごとの読みが要る |
| C2 | **安保理の採決の記録はどう書かれているか**（`votes in favour`） | S/PV 2,047 文書（前身は 1,970）。1946 年 4、1960 年 5、2000 年 49、2010 年 54、2020 年 25（年あたり） | 1 ○（S/PV と S/RES の記号）、2 ○（`(OR)` 版・再開会合・訂正の別記号、仏語頁、日付欄の誤り）、3 ○、4 △（結果・賛否・理由は別の問い）、5 △。決議の採択結果を S/RES と突き合わせる設計なら強い | 低〜中。採決は S/RES の本文にも出る（二重計上に注意） |
| C3 | **宇宙空間平和利用の決議の定型文は年ごとにどう変わったか**（`International cooperation in the peaceful uses of outer space`） | A/RES 41 文書（2005〜2022 年。2017・2018・2021・2022 年は 2〜3 件）。`geospatial` を含む決議は 61/111 以降ほぼ毎年 | 1 ○、2 ○（定型文の繰り返し＝新しい議論ではない。同年の複数決議）、3 ○、4 △、5 ○。本書の `geospatial-themes-frameworks-conclusions` の裏づけになる | 低。文書数が少なく、差分を取りやすい |

見立ての提案: **C3 → C2 → C1**（確かめやすい順）。C1 は価値が大きいが、主体の分類と紛争の記述の扱いに注意が要る。

### D. 配布物（kcai の `docs/distribution.md`）をこのインスタンスでどうするかの案

実装は hfu の判断後。このインスタンスに固有の点だけを書く（一般の選択肢は kcai 側の文書）。

- 大きさの目安（2026-10-26、踏み跡 11 本）: 本文 UTF-8 で約 0.1 MB。単一 Markdown と zip の両方を作っても、各 1 MB に満たない。データ本体（un-docs 409 MB）は**束に含めない**。含めるのは、再現に要る `checks/` の記録（クエリと件数）、`scripts/undocs.py` などの小さなスクリプト、`SOURCES.md`（データの版と sha256）。
- 推薦: kcai の推薦に沿い、**C（単一 Markdown と zip を同じ元から機械的に作る）**、**日付版**（例 `2026.10.26`、コミットを併記）、**タグで Actions が検査・作成・添付（b）**。
- このインスタンスに固有の追加: `MANIFEST.json` に **un-docs のコミット（6cd1cf0）、ファイルの sha256、「範囲を一文で言う」文**を入れる。目次の先頭に、**範囲の一文**（総会・安保理の英語、安保理決議は 2699 まで）と、`verified_how` ごとの件数（`searched-undocs`、`read-official`、`mixed`）を置く。読み手が、どの踏み跡が公式原文と照らされたかをすぐ判断できる。
- 留意: 国連文書の本文は束に含めない（要約と記号のみ）。`checks/` の TSV は、記号と短い要約で、本文の転載ではない。
- 未決（hfu）: 上の推薦の採否。リポジトリが公開の間は、GitHub Releases の公開で足りるとみなしてよいか。

### E. 今回の作業で増えた質問

8. **ブランチの削除をお願いしたい。** `dwg7/kcai-un-docs` の `claude/bootstrap-un-docs` と `hfu/kcai-yuiseki-datasets` の `claude/youthful-goldberg-tq7dzs` は、内容を `main` に取り込み済み。このセッションからは削除できなかった（git の push が切断され、`gh` は許可されなかった）。GitHub の画面での削除をお願いする。
9. **`dwg7` の読み。** `dwg7` を UN Open GIS Initiative のドメイン作業部会 7（UN Smart Maps Group）と読んだ。正しいか。正しければ、`peace-operations-review-2026-implications-for-un-open-gis` に、あなたの関わり方に即した影響（担当する試験の内容、資金源など）を足したい。
10. **取得できなかった公式サイトの一覧**（HTTP 403）: `peacekeeping.un.org` の DPO 技術戦略の研究論文（2021）と Action for Peacekeeping+ の第 8 次進捗報告（2026）、`un.org` の「Enhancing Situational Awareness in United Nations Peacekeeping」、`oios.un.org` の OIOS の評価・監査報告、`ecosoc.un.org` の決議 2011/24 の PDF。いずれも SAGE と UN Open GIS の裏づけになりうる。ブラウザから開ける場合は、保存して渡していただければ読める。

