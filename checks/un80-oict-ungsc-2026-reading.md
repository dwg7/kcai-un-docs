# UN80 と 2026/27 年度予算：OICT と UNGSC の読みの記録（2026-11-03）

`scripts/official.py` で公式の PDF を取得し、`pdftotext`（-layout なし）で全文にして検索した。取得物はスクラッチ（リポジトリの外）。

| 記号 | 内容 | 検索語 | 主な当たり |
|---|---|---|---|
| A/80/400 | 2026 年の計画予算と 2025/26 年度の支援勘定の改訂見積り（UN80） | `geospatial\|geographic information\|cartograph\|GIS`、`open.source`、`Valencia\|Brindisi` | 第 192 項(b)(iv)(d)（オープンソース不支援）、第 250 項（混合委員会の GIS 担当官 P-4 廃止）、運用支援局の節（ブリンディジ・バレンシアへの移転）。「Geospatial Information Section」の語は 0 件 |
| A/80/605 | UNLB の 2024/25 実績と 2026/27 予算案 | 同上、`UN80` | 第 65・69・73 項、第 88・92・94〜95 項、表 |
| A/80/6 (Sect.29C) | 2026 年の提案計画予算（OICT） | `open.source`、`geographic information` | 成果の表にオープンソースの記述、目標(d) GIS サービスの促進 |
| A/81/6 (Sect.29C) | 2027 年の提案計画予算（OICT。2026-05-01） | 同上 | オープンソース 0 件、目標(d)は「標準化された」GIS サービス、D-1 のバレンシアへの移転 |
| A/80/7/Add.9 | ACABQ の改訂見積りの報告 | `open.source`、`Geographic Information Officer` | 第 VIII.84〜VIII.110 項、表 VIII.18 |
| A/81/7 | ACABQ の 2027 年の提案計画予算の報告（OICT は第 VIII.82〜VIII.109 項） | `open.source`、`Geospatial\|Geographic`、`Valencia\|Brindisi\|Bangkok` | 第 VIII.85 項（Open Source Week）、第 VIII.87 項（データセンター）、第 VIII.89〜VIII.90 項（ポスト）、第 VIII.105 項（オープンソース）。地理空間の語は OICT の節に 0 件 |
| A/RES/80/253 | 情報通信技術戦略（2026-04-15） | `digital hub`、`data cent` | 第 9・15・17 項 |
| A/RES/80/254、80/255 | 政治問題の改訂見積り、合同監査団 | — | OICT とは別の議題（確認のみ） |

見つからなかったもの: 「Geospatial Information Section」（A/80/400、A/80/605）、`Open GIS` の語、運用支援局の移転での地理空間の名指し。

届かなかった先: なし（documents.un.org は取得できた）。取得できなかったもの: A/80/7 の第 VIII 部（初回報告）、A/81/7 の OICT の節（未取得）、総会が承認した最終のポスト数。

## A/80/6 と A/81/6 の比較の方法
`pdftotext -layout` で表の列を保って読み、小計画 1 の「計画した成果」の見出し（Result 1〜3）を並べて比べた。A/80/6: Result 1 革新的な技術のパートナーシップ、2 生成 AI、3 倫理的・責任ある AI。A/81/6: Result 1 生成 AI、2 倫理的・責任ある AI、3 ICT 戦略の効果的な適用。オープンソースの語は A/80/6 で表 29C.2 に複数（2022、2025、2026 の欄）、A/81/6 で 0 件。

A/81/7 の OICT の節（第 VIII.82〜VIII.109 項）は、`pdftotext`（-layout なし）の全文で通読した。第 VIII.82（規模）、83〜85（効率化、システム全体の取り組み、Open Source Week）、86（OICT と ERP 部の統合）、87〜88（データセンター、データ管理）、89〜93（ポスト）、94〜100（非ポスト）、101〜105（ICT 戦略、AI、ベンダー多様化とオープンソース）、106〜109（人員構成）。地理空間・GIS の語は 0 件。A/81/6 (Sect.29C) 全体で「geographic」「geospatial」を検索すると、小計画 2 の目標(d)（標準化された GIS サービス）と「geographical relocations」の 2 か所のみ。地理空間情報課の名は出ない。
