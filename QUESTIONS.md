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
7. 会議録の発言者（S/PV.4660 (Resumption 1) の ICISS 報告書の題に触れた発言者、A/58/PV.78 の二段の責任の発言者）は、抽出テキストの話者の見出しから確かめきれていない。公式の PDF の列組みを読んで確かめてよいか（優先度は低い）。

### C. 種の問いの候補（hfu に優先度を聞く）

「よい問いの条件」（1 出典の記号に落ちる、2 素朴な検索に落とし穴がある、3 範囲を言える、4 多面的、5 語の表が残る）に照らした見立て。件数は 2026-10-26 の un-docs（6cd1cf0、ユニーク記号・合冊除外）。

| # | 候補の問い | 件数・手がかり | 条件との見立て | 見立ての難しさ |
|---|---|---|---|---|
| C1 | **安保理で衛星画像は誰が、何のために持ち出すか**（`satellite imagery`） | 194 文書（S/yyyy/n 113、S/PV 68）。2010 年代が中心。主体は IAEA・専門家パネル・各国・ミッションに分かれる（`geospatial-search-terms`）。発言国の集計は `scripts/speaker_counts.py` | 1 ○（記号に落ちる）、2 ○（主体の取り違え、`imagery` の比喩）、3 ○、4 ○（主体・目的・年代・紛争）、5 ○。**紛争・疑惑に触れるので、記述にとどめ評価しない** | 中。主体の分類は文書ごとの読みが要る |
| C2 | **安保理の採決の記録はどう書かれているか**（`votes in favour`） | S/PV 2,047 文書（前身は 1,970）。1946 年 4、1960 年 5、2000 年 49、2010 年 54、2020 年 25（年あたり） | 1 ○（S/PV と S/RES の記号）、2 ○（`(OR)` 版・再開会合・訂正の別記号、仏語頁、日付欄の誤り）、3 ○、4 △（結果・賛否・理由は別の問い）、5 △。決議の採択結果を S/RES と突き合わせる設計なら強い | 低〜中。採決は S/RES の本文にも出る（二重計上に注意） |
| C3 | **宇宙空間平和利用の決議の定型文は年ごとにどう変わったか**（`International cooperation in the peaceful uses of outer space`） | A/RES 41 文書（2005〜2022 年。2017・2018・2021・2022 年は 2〜3 件）。`geospatial` を含む決議は 61/111 以降ほぼ毎年 | 1 ○、2 ○（定型文の繰り返し＝新しい議論ではない。同年の複数決議）、3 ○、4 △、5 ○。本書の `geospatial-themes-frameworks-conclusions` の裏づけになる | 低。文書数が少なく、差分を取りやすい |

見立ての提案: **C3 → C2 → C1**（確かめやすい順）。C1 は価値が大きいが、主体の分類と紛争の記述の扱いに注意が要る。

