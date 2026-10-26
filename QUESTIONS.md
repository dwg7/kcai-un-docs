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

1. **作業ブランチとマージ。** 指定が無かったため `claude/bootstrap-un-docs` で作業し、push した（PR は作っていない）。`main` に直接入れてよいか、PR を作るか。
2. **`reviewed_by` に誰の名前を入れるか。** 9 本すべて `draft`。先に見てほしい候補: `un-docs-reading-guide`、`responsibility-to-protect-first-appearance`、`un-geospatial-institutions-in-un-docs`。
3. **un-docs の外の一次資料を使ってよいか。** 問い 1 の「結論」と問い 3 の「ミッションの GIS 機能」を言い切るには、UN-GGIM と経済社会理事会の文書、ミッション予算・実績報告（総会文書 A/…）、宇宙委員会の報告（A/AC.105/…）が要る。いずれも公式サイトにあるが un-docs に無い。踏み跡の `sources` に加えてよいか（その場合、`verified_how` の区分に `read-official` で足す）。
4. **「初出」の書き方の規約。** `S/INF`（決議集）を既定で除く、`responsibility to protect` のように条件を表にして並べる、を既定にしてよいか（今は踏み跡ごとに書いている）。

### B. 進め方の確認

5. 前身（`hfu/kcai-yuiseki-datasets`）の `un-docs-geospatial-institutions.tsv` の要約に、文書ごとの事実と合わないものがあった（`un-geospatial-institutions-in-un-docs`、`checks/un-docs-geospatial-institutions-recheck.tsv`）。前身側の訂正は hfu が行う（私はそのリポジトリに書かない）。
6. 公式サイトへの届き方: `docs.un.org/en/<記号>` のページ自体は PDF を `documents.un.org` から読み込む枠で、PDF の取得はその公開経路（ブラウザと同じ）で行った。制限や認証をすり抜けてはいない。今回、届かなかった配信先は無かった。
7. 会議録の発言者（S/PV.4660 (Resumption 1) の ICISS 報告書の題に触れた発言者、A/58/PV.78 の二段の責任の発言者）は、抽出テキストの話者の見出しから確かめきれていない。公式の PDF の列組みを読んで確かめてよいか（優先度は低い）。
