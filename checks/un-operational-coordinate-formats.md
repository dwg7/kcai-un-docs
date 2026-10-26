# 検査記録：運用レベルの準公式文書と座標表記（MGRS／UTM／緯度経度）（2026-10-26）

データ: un-docs コミット 6cd1cf0（`scripts/undocs.py` の規則。37,567 文書、合冊除外）。un-docs の外の文書は、WebFetch が保存した PDF／docx を `pdftotext`（-layout なし）で文字にして検索した。保存先はスクラッチ（リポジトリ外）。

## 1. un-docs の検索（式と件数。大文字小文字は式の (?i) で指定）

実行は `python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '<式>' --first N --by-year`。

| 式 | 件数 | 読み |
|---|---|---|
| `MGRS` | 0 | |
| `(?i)\bmgrs\b\|military grid\|grid zone` | 0 | |
| `(?i)grid reference` | 0 | |
| `(?i)universal transverse mercator` | 0 | |
| `(?i)WGS[ -]?84` | 0 | |
| `(?i)\bSTANAG` | 0 | |
| `(?i)\bNATO standard` | 0 | |
| `(?i)map coordinates` | 0 | |
| `(?i)decimal degrees` | 0 | |
| `\b\d{1,2}[C-HJ-NP-X][A-HJ-NP-Z][A-HJ-NP-V]\s?\d{3,5}\s?\d{3,5}\b`（MGRS 形式の文字列） | 0 | 語がなくても、MGRS 形式の文字列は無い |
| `(?i)\bUTM\b` | 11 | 文脈を見た 2 件は、S/PV.2643（OCR の崩れ）と S/2013/337（企業名 Union Top Management）。投影法の UTM ではない。残り 9 件は文脈未確認（S/PV の 1946〜1991 年が大半で、OCR の崩れとみられるが未確認） |
| `(?i)\bUTM zone\|\bzone \d{1,2}[NS]\b` | 3 | S/PV.1162(OR)、S/PV.2699、S/PV.648。文脈は未確認 |
| `(?i)\bnorthing\|easting\b` | 3 | S/PV.1247(OR)、1260(OR)、1898(OR)。S/PV.1898(OR) の文脈は無関係な発言。ほかは未確認 |
| `(?i)map reference` | 11 | 1951〜1988 年の S/PV。文脈を読んだ 5 件は下の 3. |
| `(?i)grid coordinates` | 1 | S/2015/302（2015-04-29） |
| `(?i)\bgrid\b.{0,30}\bcoordinates?\|coordinates?.{0,30}\bgrid\b\|\bgrid ref\|map grid` | 1 | 同じ S/2015/302 |
| `(?i)\bGPS coordinates` | 12 | S/1998/166/ADD.1、S/2009/250、S/2016/85、S/2016/738、S/PV.7779、S/2016/1093、S/2017/45、S/PV.7951、S/PV.8527、S/2019/632、S/PV.8606、S/2023/6。文脈を読んだのは S/2016/85 と S/2019/632 のみ |
| `(?i)geographic(al)? coordinates` | 45 | 文脈は読んでいない |
| `(?i)latitude and longitude` | 1 | 文脈は読んでいない |
| `\b\d{1,3}\s?°\s?\d{1,2}\s?['′’]\s?\d{0,2}`（度分の表記） | 11 | S/PV.1388(OR)、S/2011/111、S/2017/904、S/2018/732、S/2019/171、S/2019/691、S/2019/711、S/2020/151、S/2020/840、S/2021/211、S/2021/777。文脈を読んだのは S/2017/904、S/2018/732、S/2020/840、S/2021/777 |
| `(?i)\bCoordinates?\b.{0,40}\b(UNIFIL\|UNDOF\|UNFICYP\|MINURSO)\b` | 0（出力は空） | |

注意: 度分の式は秒の記号の綴り（′ ″ ' ”）の揺れに弱く、網羅ではない。

### 文脈を読んだ文書（`show <記号> --grep`）

- S/2015/302（国連アビエ暫定治安部隊 UNISFA に関する事務総長報告。冒頭の本文の題は未確認）: 第 23 段落に、境界の「centreline and grid coordinates」をめぐる当事者の不一致がある。格子の種類は書かれていない。
- S/2016/85（OPCW 事実調査団の報告を送る書簡）: 聞き取りの「GPS coordinates」が画像と整合するとある。形式は書かれていない。
- S/2019/632: クウェート側が提供した「GPS coordinates」で埋葬地を発掘した、とある。形式は書かれていない。
- S/2017/904（OPCW・国連合同調査メカニズム、2017-10-26）: 「36°24′51.12″N, 37°12′38.16″E」の形式（度分秒、小数の秒）。
- S/2018/732（OPCW 事実調査団、2018-07-25）: 「N 33° 34’ 24”, E 36° 23’ 41.1”」の形式（度分秒）。
- S/2020/840、S/2021/777（決議 1874 により設置された専門家パネルの中間報告を、安保理議長が送る注記）: 「39°9'19.66"N 127°36'26.85"E」「40°01′44″N 125°16′27″E」の形式。
- S/PV.544（1951-05-02）: 「map reference 2070-2577」（4 桁＋4 桁）。S/PV.1162(OR)（1964-11-14）: 「map reference 210600-294925」（6 桁＋6 桁）。S/PV.1320(OR)（1966-11-15）: 「map reference 156-089」（3 桁＋3 桁）。S/PV.1449(OR)（1968-09-02）: 「approximate map reference 74158705」（8 桁の連なり）。いずれも数字だけで、格子の名前や基準面は文書に出ない。

## 2. un-docs の外の文書（取得と検索）

方法: WebSearch で候補を探し、WebFetch で取得した。WebFetch は PDF／docx を保存するので、`pdftotext` と zip 展開で本文を検索した。

| 文書 | 取得 | 検索した語 | 結果 |
|---|---|---|---|
| UN Military Peacekeeping-Intelligence Handbook（第 1 版、2019 年 5 月。PDF 121 ページ） https://unsco.unmissions.org/sites/default/files/2026-04/United%20Nations%20Military%20Peacekeeping%20Intelligence%20Officers%20-%20Scenario%20Based%20Exercise%20-%20Reference%20Materials%20MPKI%20Handbook.pdf | 取得できた | `MGRS`、`military grid`、`\bUTM\b`、`grid ref`、`\bgrid\b`、`coordinat`、`\bGPS\b`、`latitude`、`longitude`、`NATO`、`STANAG`、`WGS`、`datum`、`northing`、`easting`、`geospatial`、`\bGIS\b` | MGRS、UTM、grid、GPS、WGS、latitude、longitude、NATO はいずれも 0 件。`northing and easting` は 9.4.3（重ね図の書き方）に 1 か所。「coordinat」は調整の意味の語が大半 |
| UN Military Observers: UNMO Report Templates（UNMO STM 2025、docx） https://unsco.unmissions.org/sites/default/files/2026-07/UN%20Military%20Observers%20-%20UNMO%20Report%20Templates.docx | 取得できた | `grid`、`MGRS`、`UTM`、`coordinat`、`GPS`、`latitude`、`location` | 「grid reference」が複数の様式に出る（パトロール報告、緊急報告の手引き、停戦違反報告）。MGRS、UTM、緯度経度の語は 0 件 |
| UN Military Observers: Module 3 Lesson 3.12 UNMO Reporting Procedures（スライド 23 枚、PDF 作成 2025-12） https://unsco.unmissions.org/sites/default/files/2026-07/UN%20Military%20Observers%20-%20Module%203%20-%20Lesson%203.12%20UNMO%20Reporting%20Procedures.pdf | 取得できた | 同上 | 「COORDINATES」の見出し語が日報の指針の図に 1 回。形式の語は 0 件 |
| UN Military Peacekeeping-Intelligence Officers 研修教材（2020-04-15 版）第 1 部、282 ページ https://resourcehub01.blob.core.windows.net/training-files/Training%20Materials/038%20RTP-MIO/038-002%20UN%20MPKIO%20(Intel)%20Final%20Version%2015%20APR%202020_Part1.pdf | 取得できた（第 1 部のみ） | `\bgrid`、`MGRS`、`\bUTM\b`、`coordinat`（調整系を除く）、`\bGPS\b`、`latitude`、`map read`、`NATO` | 0 件。第 2・3 部と付属書 B（地図・様式の zip）は読んでいない |
| UNOSAT「OCHA-OPT-015 Gaza Strip Comprehensive Damage Assessment」（2024-07-06） https://unosat.org/static/unosat_filesystem/3904/OCHA-OPT-015_UNOSAT_A3_Gaza_Strip_OPT_CDA_06072024.pdf | 取得できた | `UTM`、`WGS`、`datum`、`projection`、`coordinate`、`MGRS` | 「Name: WGS 1984 UTM Zone 36N / GCS: GCS WGS 1984 / Datum: WGS 1984」。MGRS は 0 件 |
| DOS Aviation Manual のページ（2026-07-13 掲載） https://operationalsupport.un.org/en/media/1395 | ページのみ。PDF 本体は読めていない | | ページの本文に座標の語は無い（本文は PDF への案内のみ） |
| UN Geospatial「United Nations Peacekeeping Operations」地図のページ https://www.un.org/geospatial/node/2754 | ページのみ（2025-02-01） | | 座標の記述は無い。地図の PDF は読めていない |
| Peacekeeping Resource Hub の MPKIO 教材ページ https://peacekeepingresourcehub.un.org/en/training/rtp/MPKIO | ページのみ（2026-10-20 更新） | | 認証の案内は見えず、リンクは直接開く形。MGRS と grid reference の語は無い |
| OCHA IM Toolbox「Common Operational Datasets (CODs)」（2025-02-21 更新） https://humanitarian.atlassian.net/wiki/spaces/imtoolbox/pages/42045911/Common+Operational+Datasets+CODs | ページのみ | `WGS 84`、`EPSG:4326` | 取得した本文に座標系の記述は無い（下位ページは未取得） |

## 3. 検索結果の見出しだけを見た（本文は読んでいない）文書

これらは WebSearch の要約文にだけ現れた。本文を確かめていないので、踏み跡では「読んだだけ（検索結果の要約）」より弱い扱いにする。

- IMSMA の座標系の説明（GICHD の wiki）: 「WGS 1984 and MGRS are active after the installation」とする要約。ページの取得は 502 で失敗した。
- UNOSAT のほかの地図: 「WGS 1984 UTM Zone 43N」（2019 年、パキスタン）、「UTM zone 46N」（2015 年、ミャンマー）とする要約。
- UNIBAM（国連歩兵大隊マニュアル）2020 年版: 国の教範に代わるものではない、とする要約。本文は取得できなかった。
- 米国統合参謀本部の指示 CJCSI 3900.01（米国の文書）: MGRS を陸上部隊の報告の座標にすると述べるとする要約。国連の文書ではない。
- NATO の STANAG 2211: WGS 84 を標準とする、とする要約（現在は失効の表示）。

## 4. 届かなかった先（回避していない）

| 先 | 結果 |
|---|---|
| unsco.unmissions.org の PDF を curl で直接 | 403（CloudFront）。WebFetch 経由で取得できた |
| media.defense.gov（国連平和維持活動の軍事ユニットのマニュアル 2012 年版の写し。UNIBAM Vol I・II、Military Reconnaissance Unit Manual） | 403（Akamai の Access Denied）、WebFetch でも 403 |
| pksoi.armywarcollege.edu（UNIBAM 2020 年版、Reconnaissance Unit Manual、Aviation Unit Manual のページ） | curl は接続リセット、WebFetch は 503 |
| www.mineaction.org（Policy on Peacekeeping-Intelligence 2019、Guidelines on Technical PKI 2025、SOP on Integrated Reporting 2019、deployment_3.1 の PDF） | curl は TLS 検証失敗または接続リセット、WebFetch は 503。検証は無効にしていない |
| peacekeeping.un.org、www.un.org/geospatial/（トップ）、unifil.unmissions.org、operationalsupport.un.org の COE マニュアルのページ、www.securitycouncilreport.org | curl で 403 |
| github.com/unopengis | 403 |
| mwiki.gichd.org（IMSMA の座標系） | 502 |
| data.humdata.org の検索ページ | WebFetch で 403 |
| web.archive.org | WebFetch が取得を許可せず。webarchive.unesco.org の写しは取得先が混雑で応答なし |
| resourcehub.dppa-dpo.org、maps.un.org、dag.un.org | 接続できず（000） |
| research.un.org/en/peacekeeping-documents | 404 |

## 5. 検索語（WebSearch）

`United Nations peacekeeping MGRS Military Grid Reference System UN military manual`／`UN Peacekeeping-Intelligence Handbook pdf dpo grid coordinates`／`UNIFIL technical report incident grid reference OR UTM coordinates Blue Line`／`United Nations Infantry Battalion Manual map reading OR grid reference OR MGRS peacekeeping`／`UN Military Reconnaissance Company Manual OR Reconnaissance Unit Manual … navigation GPS grid`／`UN peacekeeping Aviation Manual coordinates WGS 84 degrees minutes`／`UNOSAT product map Coordinate System WGS 1984 UTM zone damage assessment`／`IMSMA coordinate format MGRS UTM latitude longitude`／`DPO DOS Geospatial Information policy … MGRS OR UTM OR WGS 84`／`MINURSO ceasefire violation coordinates UTM OR grid OR MGRS`／`Contingent-Owned Equipment manual GPS`／`UN Open GIS initiative github … MGRS OR UTM`／`HDX OCHA Common Operational Datasets … WGS 84 EPSG:4326`／`Unite Aware OR SAGE … incident reporting location coordinates MGRS OR lat/long`／`UN Joint Operations Centre handbook … grid reference OR coordinates`／`UN Military Observers specialised training materials … map reading … MGRS`／`United Nations Military Staff Officers specialised training materials MGRS`。

見つからなかったもの: UNIFIL・UNDOF・UNFICYP・MINURSO の停戦線や違反の座標を載せた公開文書（検索結果は地名の記述だけ）、SAGE の入力項目の座標形式、Contingent-Owned Equipment マニュアルの GPS 条項（2023 年の米国の提案文書だけが見つかった）、UN Open GIS の GitHub の資料。
