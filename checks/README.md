# checks

検索の記録と、再現用の入力を置く。大きなデータは置かない。

## データの取得（pin した版）

```sh
mkdir -p "$SCRATCH/data" && cd "$SCRATCH/data"
curl -L --fail -o documents.parquet \
  https://huggingface.co/datasets/yuiseki/un-docs/resolve/6cd1cf0/documents.parquet
sha256sum documents.parquet   # dd9edebc14969c8ef0bc6912d6b4d08e3729b0ce02c7720414349ffa77ad54f5
pip install duckdb
```

直接 URL を `read_parquet` に渡す方法もある（`install httpfs; load httpfs`）が、繰り返し検索するなら取得したほうが速い。

## 検索

```sh
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)geo-?spatial' --first 10 --by-year
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" show 'S/RES/1674(2006)' --grep 'responsib'
```

`undocs.py` の規則: 記号は空白を除いて正規化／同じ記号は 1 本（pdf 優先、本文の長いほう）／記号に `vol` を含む合冊は除く（`--keep-vol` で残す）／日付は `date_adopted` > `date_distributed` > `date_other`（どれを採ったかを `date_kind` で出す）。
