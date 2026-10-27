# UN Open GIS Initiative と 5 か国：検索の記録（2026-10-27）

un-docs（6cd1cf0）、`scripts/undocs.py`。

| 式 | 文書数 | 注 |
|---|---|---|
| `(?i)open\s+GIS` | 0 | Initiative の名称は un-docs に無い |
| `(?i)partnership\s+for\s+technology\s+in\s+peacekeeping` | 8 | S/PV.7802、8521、8534、8838、9181(Resumption 1)、S/2021/501、S/2021/732、S/2021/868 |
| `(?i)GeoSDI\|OpenGDS\|KRIHS\|Boundless\|GeoSHAPE\|Politecnico\|OSGeo\|QGIS\|open[- ]source\s+(GIS\|geospatial)` | 103 | 先頭は 1948 年の S/PV。`QGIS` ではなく `Boundless` などの普通の英語（boundless）に当たる偽陽性が大半。文脈は読んでいない |
| `(?i)technology\s+(and\s+peacekeeping\s+)?symposium` | 0 | |

S/PV.7802（2016-11-07）の発言者: 該当文の直前の見出しは Mr. Oh Joon (Republic of Korea)。S/PV.8838 の India との覚書の発言者は見出しで特定できず（議長の発言と見られる）。

取得した資料（スクラッチに保存。リポジトリには入れていない）: 国連 OICT のスライド（un-ggim-ap.org の PDF、16 頁、pdftotext で全文）、UNVT 論文（ISPRS Archives の PDF、pdftotext で全文）。

届かなかった・読めなかった先: Initiative の公式サイト、github.com/UNopenGIS（以前の調査で 403）、FOSS4G 2018 の資料 PDF（503）、wiki.osgeo.org・lists.osgeo.org・media.ccc.de は WebFetch の要約のみ。
