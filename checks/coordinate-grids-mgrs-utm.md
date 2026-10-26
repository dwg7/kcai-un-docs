# 検査記録：MGRS・UTM と座標・グリッドの周辺語（2026-10-26）

データ: un-docs コミット 6cd1cf0、`scripts/undocs.py` の規則（空白除去・大文字化・同記号 1 本・合冊除外。ユニーク記号 37,567）。件数は文書数（`regexp_matches(body, 式)`）。「最初」は日付の早い順（採択 > 配布 > その他）。実行は `search '<式>' --first 3` と、同じ `docs` ビューへの duckdb 検索（文脈の表示）。

## 語の表

| 式 | 件数 | 最初の文書 | 外れ方・読み |
|---|---|---|---|
| `\bMGRS\b` | 0 | - | 無い |
| `(?i)military\s+grid` | 0 | - | 無い |
| `\bUTM\b`（大文字小文字を区別） | 1 | S/2013/337 | Union Top Management という会社の略。無関係 |
| `(?i)\bUTM\b` | 11 | S/PV.37 | 1 件は上の会社。読んだ 8 件（S/PV.234、316、750/REV.1、2161、2643、2694、2981、S/INF/2/REV.1(III)）は、OCR の崩れ（"utmost" の分断など）。残り 2 件は文脈を読んでいない |
| `(?i)universal\s+transverse\s+mercator` / `transverse\s+mercator` | 0 / 0 | - | 無い |
| `\bUTM\s*(?:zone\|grid\|coordinate)` | 0 | - | 無い |
| `(?i)grid\s+coordinates?` | 1 | S/2015/302 | スーダンと南スーダンの安全非武装国境地帯の中心線の座標についての意見の不一致。座標系の名前は無い |
| `(?i)grid\s+references?` | 0 | - | 無い |
| `(?i)map\s+references?` | 12 | S/PV.544（1951） | 国連休戦監視機構（UNTSO）の報告などを引く発言の中の数字（例 `2070-2577`、`210600-294925`）。1951〜1970 年の会議録。座標系の名前は読んだ範囲に無い |
| `(?i)\bgrid\s+(?:system\|square\|zone\|line\|ref)` | 11 | A/519（1947） | 読んだ 8 件は電力網（power grid、smart grid）。2 件（A/519、A/RES/181(II)）は分割案の境界の記述にある「grid line 930/230」など。OCR で 930 と 230 が割れる（公式 PDF の A/RES/181(II) は 230） |
| `(?i)\b(?:palestine\|israel(?:i)?\|lebanese\|cassini\|lambert\|ordnance\s+survey\|national)\s+grid\b` | 6 | A/53/PV.38 | すべて電力網 |
| `\b\d{1,2}[C-HJ-NP-X][A-HJ-NP-Z][A-HJ-NP-V]\s?\d{4,10}\b`（MGRS 風の綴り） | 1 | S/2020/151 | 事件番号 `19MAG10987`。偽陽性 |
| `(?i)\b(?:northings?\|eastings?)\b` | 2 | S/PV.1247(OR) | 「74th Northings」（インドとパキスタンの停戦線の緯度の言い方か。未確認）と OCR の broadcasting |
| `(?i)geographic(?:al)?\s+coordinates?` | 48 | A/RES/49/28 | A/RES 27、S/yyyy/n 10、S/PV 4、A/PV 4、A/NN/L 1、S/INF 1、S/RES 1。大半は海洋法条約の海図・座標表の寄託、化学兵器施設の申告、紛争の調査報告 |
| `(?i)map\s+coordinates?` | 1 | S/2016/85 | 化学兵器禁止機関の事実調査団がシリアに求めた情報の一覧 |
| 上の 2 式の合計 | 49 | - | hfu の先の確認（49 件）と一致 |
| `(?i)\bcoordinates\b` | 371 | S/PV.2425(OR) | 動詞（「the Office coordinates ...」）が大量に混じる。S/ 系列・A/ の報告のうち、動詞らしい前後を正規表現で除いて 109 文書が残った（除き方が粗く、動詞が残る）。残った分の文脈は目で通した |
| `(?i)\bcoordinates?\s+(?:of\|are\|were\|at\|:)?\s*\d` | 12 | S/PV.2425(OR) | 12 件を全部読んだ。名詞は 6 件（S/PV.2425、S/2010/430、S/2015/517、S/2016/11、S/2017/904、S/PV.8645）、動詞と脚注番号は 6 件。S/2006/626 の「Coordinates of the targeted house: 108640/142900」は、コロンと数字の間に「of the targeted house」が入るため、この式に当たらない（式の外れ方） |
| `(?i)\d+\s*°\s*\d+\s*['’′]` | 14 | S/PV.1388(OR) | 度分秒。S/2011/111、2017/904、2018/732、2019/171、2019/691、2020/151、2020/840、2021/211、2021/777 は、制裁パネルや調査報告の数値座標。A/RES/38/99 など数件は OCR（`14 See F/CN.4/...` の脚注） |
| `(?i)\d+\s*°\s*[NSEW]\b` | 52 | S/PV.187 | OCR の崩れが混じる。内訳は分類していない |
| `(?i)\d+\s*degrees?\s*(?:and\s*)?\d+\s*minutes?` | 3 | S/PV.679（1954） | 発言の中で読み上げられた位置（S/PV.679、1388、2668） |
| `(?i)\blatitude\b` | 231 | S/PV.3 | 大半は「裁量の余地」の意味。座標の意味は S/PV.812（北緯 22 度）、814、815、1388、1488、2419、2541 など |
| `(?i)\blongitude\b` | 13 | S/PV.679 | 座標の意味が大半。S/PV.9345 は比喩 |
| `(?i)\bWGS[\s-]?(?:84\|1984\|72)\b` | 0 | - | 無い |
| `(?i)\bdatum\b` | 2 | S/PV.2156(OR) | 「所与の事実」「貧困線 poverty datum-line」。測地の意味は無い |
| `(?i)geodetic` | 27 | A/PV.1522（1967） | A/RES/66/231 以降の海洋法決議の "geodetic datums" の一文（A/RES/66/231、67/78、68/70、69/245 ほか。A/77/L.36 も）。A/RES/69/266 の測地基準座標系。ミッションの境界画定の「geodetic stations」（S/2007/695、S/2009/642） |
| `(?i)coordinate\s+(?:system\|reference)` | 4 | S/PV.2985 | 3 件は動詞 + system（"coordinate system-wide"）。A/69/PV.80 のみ測地の "coordinate reference frame" |
| `(?i)reference\s+(?:system\|frame)` | 36 | S/PV.564 | 測地以外（「準拠枠」の一般語）が大半。未分類 |
| `(?i)Gauss[\s-]*Kr[uü]ger` | 0 | - | 無い |
| `(?i)\bprojection\b` | 221 | A/RES/277(III) | 「投影（推計）」の意味。`map\s+projection` は 0 |
| `(?i)\bGPS\b` | 44 | S/1998/166/ADD.1 | `global positioning system` は 41。GPS 座標の言及は 2010 年代に増える（MONUSCO の集団墓地、国連の施設の位置、イラクとクウェートの行方不明者の捜索） |
| `(?i)\bGNSS\b` | 8 | S/INF/58 | 輸出管理品目の列挙（S/INF/58、S/RES/1454、2498、2551、2607）と、宇宙空間平和利用委員会の A/RES/59/2、60/99 |
| `(?i)\bEPSG\b`、`GeoJSON`、`shapefile`、`gazetteer`、`geo-?coordinat` | 0 | - | 無い |
| `(?i)\bKML\b` | 3 | A/35/PV.1 | OCR の崩れと、コンゴ民主共和国の RCD/KML（政治運動）。無関係 |
| `(?i)\bPCode\|p-code` | 1 | S/PV.2596(OR) | "pcode" は OCR の崩れ |
| `(?i)\bgeo-?reference` | 7 | A/RES/73/245 | 観光データ、災害対応データベース、海洋境界の地理参照（S/PV.9260(RESUMPTION1)） |
| `(?i)\bgeo-?locat` | 18 | S/2016/157 | MONUSCO の「Geolocation Threat Analysis Unit」（2017〜2021）、調査報告の位置特定 |

## 文脈を読んだ文書

- S/2006/626: 付属書の中の文に「Coordinates of the targeted house: 108640/142900」。座標系の名前は無い。公式 PDF（20 ページ、画像 0）でも同じ。
- S/2016/738、S/2016/888: 化学兵器禁止機関（OPCW）と国連の合同調査機構の報告。`N35.372950° E36.589800°` のような十進度の座標。タブレットの GPS アプリの表示、シリア政府が提供した座標、写真の解析で特定した位置。座標系の名前は読んだ範囲に無い。
- S/2016/847: アレッポの停戦の取り決め。「Russian-provided map の 31/15 の区画」（地図の格子の呼び名）と、添付地図の「geo-coordinates」。数値は文書本文に無い。
- S/2008/496、S/2008/630（エリトリア・エチオピア国境）: 境界は「声明に付属する座標」に従って画定された、という趣旨。数値は本文に無い（公式 PDF、5 ページでも無い）。
- S/2012/28、S/2014/6（カメルーン・ナイジェリア）: 「geographic coordinates の索引」が声明に含まれる、という予告。数値は本文に無い。
- S/2010/430（UNIFIL）: ブルーラインの「77 coordinates have been agreed; 57 markers」。数値は無い。
- S/2019/574（UNIFIL）: トンネル 3 本の座標をレバノン当局に渡した、という記述。数値は無い。
- S/INF/48、S/RES/778(1992) ほか: イラクとクウェートの境界の「precise coordinates」を画定する、という記述。数値は無い。
- S/2015/302 ほか UNISFA の報告: 中心線の座標（centreline coordinates）についての当事者の意見の不一致。

## 公式 PDF との照合（図・付属書の欠落）

取得経路: `scripts/official.py`（documents.un.org）。キャッシュはスクラッチ。

- S/2019/691（142 ページ）: 度分秒の座標 10 か所が、公式 PDF の本文テキストと un-docs で同じ（図の説明文の座標を含む）。公式 PDF には 104 個の画像があり、図 III（ナムポの衛星画像）の画像内の注記は、目視で確かめた範囲では画像の一部で、本文テキストには入らない。画像内の注記の中身は読めていない。
- S/2016/738（98 ページ）: 座標は本文に文字で入る。ロゴ以外の画像は無い。
- A/RES/181(II)（22 ページ）: 全ページが画像（スキャン）で、文字は OCR の層。付属の地図は画像で、文字に入らない。境界の記述の「grid line」の数字は OCR の誤りを含みうる（A/519 は 930、A/RES/181(II) は 230）。
- S/2006/626: 画像 0。座標は本文に入る。

## un-docs の外（web 検索。届く範囲）

- 「UNIFIL Blue Line coordinates UTM MGRS」の検索: UNIFIL のページ（markers、GIS 座標）が出るが、UTM・MGRS の語は確認できなかった。UNIFIL の個別ページ `unifil.unmissions.org/working-unifil-laf-confirms-8-new-blue-line-points` は WebFetch で 404。
- 「United Nations peacekeeping MGRS」の検索: 国連の地理空間情報課の地図の一覧などが出るが、MGRS の語は確認できなかった。
- 未実施: UNMEER の文書、ミッションの予算文書の全文検索（un-docs の外の全文検索の手段が無い）、国連地理空間情報課の技術標準の本文。
