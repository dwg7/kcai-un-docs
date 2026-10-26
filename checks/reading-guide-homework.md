# 検査記録：下準備の宿題（2026-10-26）

- 公式側の有無: `https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf` の応答の `Content-Type` が `application/pdf` かで判定した（HTML の枠が返る場合は PDF 無し）。S/PV の欠番 90 件は、`S/PV.<n>` と `S/PV.<n>(OR)` の 2 通りで探した（結果: 72 件あり。65 件が `(OR)`）。S/RES は 2699〜2723、2750、2800 を探した（すべてあり）。
- 綴り違いの重複: `read_parquet` の `id`（`S/RES/%`）を `upper(regexp_replace(id,'\s','','g'))` で束ね、2 行以上あり本文が異なるものを数えた（75 番号）。差の型は 4 例の目視（S/RES/11(1946)、S/RES/426(1978)、S/RES/7(1946)、S/RES/761(1992)）。
- 仏語の行: 先頭 2 万字の英語の機能語（the、of、and…）と仏語の機能語（le、la、les、des…）の数の比。仏語が多い行を「仏語が過半」、仏語が英語の半分以上の行を「仏語がかなり混ざる」とした。簡易判定。
- 記号正規化のテスト: `python3 -I scripts/test_undocs.py`。
