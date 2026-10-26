# 出典台帳

踏み跡の `cites:` が参照する出典の一覧です。出典の **版** と **確認日** をここで管理します。

| id | 発行者 | 名称 | URL | 版 | 確認日 |
|---|---|---|---|---|---|
| un-docs | yuiseki（Hugging Face） | un-docs `documents.parquet`（総会・安保理の英語文書の抽出テキスト。二次的な写し） | https://huggingface.co/datasets/yuiseki/un-docs/resolve/6cd1cf0/documents.parquet | コミット 6cd1cf0、39,363 行、409,417,767 バイト、sha256 dd9edebc…ad54f5 | 2026-10-26 |
| undocs-site | 国連 | 国連公式文書システム（記号で原文に届く） | https://docs.un.org/en/<記号>（PDF の実体は https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf） | 随時 | 2026-10-26（約 40 文書で照合） |
| hfu-feasibility | hfu | un-docs の実測と試した問い（本リポジトリの前身の調査） | https://github.com/hfu/kcai-yuiseki-datasets （ブランチ claude/youthful-goldberg-tq7dzs、1b0f565）`knowledge/cross/un-docs-kcai-feasibility.md` | 1b0f565 | 2026-10-26 |
| hfu-institutions | hfu | 地理空間の機関に関する 226 文書の分類 | 同上 `knowledge/cross/un-docs-geospatial-institutions.md`、`checks/un-docs-geospatial-institutions.tsv` | 1b0f565 | 2026-10-26 |
