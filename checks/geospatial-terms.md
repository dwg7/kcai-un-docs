# 検査記録：地理空間の語の展開（2026-10-26）

データ: un-docs コミット 6cd1cf0。`scripts/undocs.py` の規則（空白除去・大文字化・同記号 1 本・合冊除外・日付は採択>配布>その他）。ユニーク記号 37,567。

各語を `regexp_matches(body, 式)` で数え、「最初」は `order by date nulls last, sym`（S/INF を除く）。式は `knowledge/geospatial-search-terms.md` の表の `regex`。

`mapping`（地理的な連語に限る）の式:

```
(?i)(?:global|digital|satellite|geospatial|land|mine|minefield|boundary|border|hazard|risk|crop|cadastral|topographic|seabed|ocean|forest|geological|thematic|base|aerial)\s+mapping|mapping\s+of\s+(?:the\s+)?(?:land|forest|mine|minefield|hazard|seabed|boundar\w+|terrain|areas?|resources)
```

最初の実行での誤り（記録）: UN-GGIM の式を `(?i)GGIM|Global\s+Geospatial\s+Information\s+Management|Geographic\s+Information\s+Management` と書いたため 117 文書に当たった（偽陽性）。大文字小文字を区別し、`GGIM` と正式名に限って 2 文書に直した。`cartograph` を `(?i)cartograph` と書くと、フランス語の `cartographie` に当たる（直した式は英語の語形に限る）。
