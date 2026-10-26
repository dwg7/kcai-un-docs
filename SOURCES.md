# 出典台帳

踏み跡の `cites:` が参照する出典の一覧です。出典の **版** と **確認日** をここで管理します。

| id | 発行者 | 名称 | URL | 版 | 確認日 |
|---|---|---|---|---|---|
| un-docs | yuiseki（Hugging Face） | un-docs `documents.parquet`（総会・安保理の英語文書の抽出テキスト。二次的な写し） | https://huggingface.co/datasets/yuiseki/un-docs/resolve/6cd1cf0/documents.parquet | コミット 6cd1cf0、39,363 行、409,417,767 バイト、sha256 dd9edebc…ad54f5 | 2026-10-26 |
| undocs-site | 国連 | 国連公式文書システム（記号で原文に届く） | https://docs.un.org/en/<記号>（PDF の実体は https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf） | 随時 | 2026-10-26（約 40 文書で照合） |
| hfu-feasibility | hfu | un-docs の実測と試した問い（本リポジトリの前身の調査） | https://github.com/hfu/kcai-yuiseki-datasets （ブランチ claude/youthful-goldberg-tq7dzs、1b0f565）`knowledge/cross/un-docs-kcai-feasibility.md` | 1b0f565 | 2026-10-26 |
| hfu-institutions | hfu | 地理空間の機関に関する 226 文書の分類 | 同上 `knowledge/cross/un-docs-geospatial-institutions.md`、`checks/un-docs-geospatial-institutions.tsv` | 1b0f565 | 2026-10-26 |
| ecosoc-2011-24 | 経済社会理事会 | 決議 2011/24「Committee of Experts on Global Geospatial Information Management」（2011-07-27）。決議集 E/2011/INF/2 の該当節（`E/RES/2011/24` の記号では documents.un.org が PDF を返さなかった） | https://documents.un.org/api/symbol/access?s=E/2011/INF/2&l=en&t=pdf | E/2011/INF/2 | 2026-10-26 |
| ecosoc-2016-27 | 経済社会理事会 | 決議 2016/27「Strengthening institutional arrangements on geospatial information management」（2016-07-27） | https://docs.un.org/en/E/RES/2016/27 | E/RES/2016/27 | 2026-10-26 |
| ecosoc-2018-14 | 経済社会理事会 | 決議 2018/14「Strategic Framework on Geospatial Information and Services for Disasters」（2018-07-02） | https://docs.un.org/en/E/RES/2018/14 | E/RES/2018/14 | 2026-10-26 |
| ggim-13th-report | UN-GGIM 専門家委員会 | 第13会期（2023-08-02〜04）の報告 | https://docs.un.org/en/E/2024/46 | E/2024/46-E/C.20/2023/19 | 2026-10-26 |

