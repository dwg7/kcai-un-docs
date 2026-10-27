---
id: un-open-gis-initiative-member-state-links
title: UN Open GIS Initiative と日本、韓国、イタリア、フィンランド、米国の関係：公式文書に無く、二次資料で分かること
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-27
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。S/PV.7802 の発言者の見出しと、「Open GIS」「Partnership for Technology in Peacekeeping」の検索。式は checks/un-open-gis-member-state-links.md
  - 国連 OICT 地理空間情報課のスライド「UN Open GIS Initiative Challenge & Opportunity」（2020-10、UN-GGIM アジア太平洋のウェビナーの資料。PDF を取得して全文を読んだ）
  - Fujimura ほか「Design and development of the UN Vector Tile Toolkit」（ISPRS Archives XLII-4/W14、FOSS4G 2019。PDF を取得して全文を読んだ）
  - OSGeo 国連委員会の wiki ページと、OSGeo の国連メーリングリスト 2016-11 の報告（WebFetch による要約。本文の直接の読みではない）
  - Brovelli ほか、ISPRS Archives XLII-4/W2（2017）の要旨
  - GPS World ほかの報道「Boundless partners with United Nations on UN Open GIS Initiative」（検索結果の要約のみ。本文は未取得）
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-27
related: [member-state-statements-on-geospatial-japan-korea-italy-finland-us, peace-operations-review-2026-implications-for-un-open-gis, sage-and-unite-aware-relationship, unlb-gis-function-in-budget-documents]
finding:
  - member-state-links-are-via-organizations-not-official-documents
  - korea-and-japan-links-are-best-documented
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書、安保理決議は 2699 まで。UN Open GIS Initiative は un-docs の文書に一度も出ない（`Open GIS` は 0 件）ので、この踏み跡の中身の大半は **un-docs の外の資料**（国連 OICT のスライド、学会論文、OSGeo の公開記録）による。

日本、韓国、イタリア、フィンランド、米国と UN Open GIS Initiative の関係は、総会・安保理の文書では確かめられない。確かめられるのは、**これらの国に拠点を持つ機関や企業が Initiative に参加した**という、二次的な記録である。Initiative の「貢献者」は国ではなく機関（財政、資材、技術、人員で支える組織）と定義されており、国の関与と読むのは適切ではない。

| 国 | 二次資料で分かる関係 | 強さ |
|---|---|---|
| 韓国 | 作業部会の長（HaeKyong Kang 氏が地理解析、Ki-Joune Li 氏がデータ収集〔共同議長も務める〕）、創設期の貢献者 OpenGDS、2016 年 11 月のソウルでの第 2 回ワークショップ、国土研究院（KRIHS）の 2020〜21 年のハイブリッド GIS 試験事業への参加。公式の安保理会議録では、韓国代表が 2016 年に第 3 回の技術パートナーシップのシンポジウムをソウルで開くと述べた（S/PV.7802） | 最も厚い |
| 日本 | 国土地理院（GSI）が国連ベクトルタイル・ツールキット（UNVT）の「主な貢献者」（2020 年のスライド）で、ツールキットを使って自らのベクトルタイルを試作した（2019 年の論文）。OSGeo 財団日本支部、農研機構（NARO）、民間企業が論文の共著者 | 厚い（ただし作業部会 1 つの中の 1 事業） |
| イタリア | 創設期の貢献者 GeoSDI、ミラノ工科大学（Brovelli 氏）が能力開発の作業部会を率いる、ブリンディジの国連グローバル・サービスセンター（UNGSC）が会合と計算機基盤を提供 | 厚い（ホスト国としての側面が強い） |
| 米国 | 創設期の貢献者 GeoSHAPE と OpenGeo Suite（米国のプロジェクト）、基盤は Boundless 社の Geoshape-Exchange で米国防総省が支援（OSGeo wiki の記述） | 中（企業と国防総省の事業としての記述。国の公式な関与の文書は未確認） |
| フィンランド | 2020 年のスライド 1 枚に、雲のない衛星画像の試験事業の「初期資金: フィンランド」、開発チームは GISPO とフィンランドの協力者、試験場は UNISFA、期間は 2020 年 10 月〜2021 年 3 月とある | 弱い（単一の資料。独立の裏づけは見つからなかった） |

## 詳しく

### Initiative とは（二次資料の範囲）

- 2016 年 3 月に始まった。国連のオープンソースの GIS 一式を作り、国連の運用の要件を満たすことが目的。2016 年の Initiative は 4 つの作業部会（Spiral）、2020 年のスライドでは 6 つ（ハイブリッド、能力開発、地理解析、データ収集、地理 AI、屋内 GIS）。DWG 7 という呼び方と「UN Smart Maps Group」の名は、これらの資料には出ず、2025 年の FOSS4G の要旨（`peace-operations-review-2026-implications-for-un-open-gis` が引く二次資料）にある。
- 運営は、戦略委員会（貢献者 1 機関につき 1 代表）、共同議長（国連が 1 人、戦略委員会が 2 人選ぶ）、技術助言グループなどからなる（OSGeo 国連メーリングリスト 2016-11 の報告の要約）。**貢献者は機関**で、オブザーバーは個人や機関である。
- 2020 年の OICT のスライドは、Initiative を実施する地理空間情報課（ニューヨーク）の位置づけとして、安保理、事務局、平和活動、UN-GGIM の共同事務局、加盟国への国境の技術支援などを列挙し、ハイブリッド GIS（商用とオープンソースの併用）の構想の中で、ウェブ地図 "Unite Aware" の名を挙げる。SAGE と Unite Aware の関係は `sage-and-unite-aware-relationship` を参照。

### 国ごとの詳細

- **韓国**: OSGeo の記録によれば、創設期の貢献者に OpenGDS（韓国）があり、2016 年 3 月に始まった地理解析（Hae Kyong Kang 氏）とデータ収集（Ki-Joune Li 氏）の作業部会の長は韓国の人。2016 年 11 月 7〜11 日の第 2 回ワークショップはソウル市庁舎で、第 3 回の国際技術パートナーシップのシンポジウム（国連現地支援局とソウル特別市が主催）の一部として開かれた。2020 年 10 月〜2021 年 3 月のハイブリッド GIS の試験事業の貢献者は KRIHS/Korea、UNGIS、UNGSC、WFP。公式側では、S/PV.7802（2016-11-07）で、韓国の呉俊（Oh Joon）代表が、韓国が現地支援局と平和維持活動局と共に第 3 回の国際技術パートナーシップのシンポジウムをソウルで開くと述べた（発言者は会議録の見出しで確かめた）。2021 年の S/PV.8838 にも、平和維持活動閣僚級会合を韓国で開く言及がある（発言者は未確認）。
- **日本**: 論文（2019）の著者は、国連地理空間情報課（ニューヨーク）、UNGSC（ブリンディジ）、OSGeo 財団日本支部、航空測量会社、農研機構、国土地理院の所属。ツールキットは 2017 年に Initiative の Spiral 4 の中で始まり、2018 年 12 月に FOSS4G Asia 2018 の基調講演で公開が発表された。GSI は自らのベクトルタイルの試作に使い、そのフィードバックでコードが改善された。農研機構は、農林水産省の公開データの農地区画のベクトルタイルを作った。2020 年のスライドは、UNGSC での地図配信と、**日本での防災の試験**を挙げ、主な貢献者を GSI Japan とする。
- **イタリア**: OSGeo の記録では創設期の貢献者に GeoSDI（イタリア）がある。ミラノ工科大学の Brovelli 氏は能力開発の作業部会を率い、同大学の e-learning 基盤で、国連職員向けの QGIS と PostGIS の講座が開かれた。技術会合は、ブリンディジの UNGSC で 2016 年 3 月と 2017 年 4 月に開かれた。UNGSC の職員は論文の共著者でもあり、計算機とネットワークの基盤を提供した。
- **米国**: OSGeo の wiki は、創設期の貢献者に GeoSHAPE と OpenGeo Suite（米国）を挙げ、第 1 作業部会のポータルは Boundless 社の Geoshape-Exchange を基にし、米国防総省が支援するとする。Boundless 社は 2018 年に国連と提携したと報じられた。いずれも企業と事業単位の記録で、米国政府の立場を述べた安保理・総会の文書は見つからなかった（`member-state-statements-on-geospatial-japan-korea-italy-finland-us` の米国の発言は、衛星画像の証拠としての言及で、Initiative とは別の話）。
- **フィンランド**: 2020 年の OICT のスライドの 1 枚だけが根拠。ウェブ検索では、この試験事業の資金元を裏づける別の資料は見つからなかった。

### 公式文書の側

- un-docs には `Open GIS` の語が無い。特別委員会の報告 A/71/19 第 53 項と A/72/19 第 52 項（un-docs の外。`peace-operations-review-2026-implications-for-un-open-gis` で確認）が Initiative に触れるが、国名は挙げない。
- 「Partnership for Technology in Peacekeeping」は un-docs の 8 文書に出る（S/PV.7802、8521、8534、8838、9181 の再開会合、S/2021/501、2021/732、2021/868）。ホスト国は、韓国（2016、S/PV.7802）、カザフスタン（2019、S/PV.8521 と 8534）、南アフリカ（予定、S/2021/501）などで、5 か国のうち韓国だけが出る。

## よくあるまちがい

- 「Initiative の貢献者」を「その国の政府の貢献」とみなす。貢献者の定義は機関で、国ではない。
- 日本の関与を GSI の1事業から「日本が Initiative を支えている」と一般化する。確かめられたのは UNVT という 1 つの事業である。
- フィンランドの資金を確定した事実として扱う。単一のスライドに基づく。
- 2020 年の 6 つの作業部会と、2025 年に出る DWG 7 を同じ番号体系と決める。番号の振り直しや増加の経緯は確かめていない。

## 確かめた度合い

- 読んだ: 2020 年の OICT のスライドと 2019 年の UNVT 論文は、PDF を取得して全文を読んだ。S/PV.7802 の発言者は、un-docs の本文の見出しで確かめた。Partnership for Technology in Peacekeeping の語の検索は un-docs で行った（件数と記号）。
- 要約のみ: OSGeo の wiki とメーリングリストの報告、2019 年の講演ページ、2017 年の論文の要旨は、取得ツールによる要約で確かめた（原文の細部は未確認）。
- **利害関係の注記**: 2019 年の論文の筆頭著者 H. Fujimura（国連地理空間情報課の所属）は、このリポジトリの管理責任者と同名に見える。同一人物かは本書では確かめておらず、Initiative への参加は、AGENTS.md の約束（個人として、公開できることだけ）の範囲で扱う。
- 未確認: Initiative の公式サイトと GitHub（以前の調査で 403）。各国の公式な拠出や取り決め。フィンランドの資金の独立した裏づけ。米国の「南方軍の担当者」が能力開発の作業部会に関わるという検索要約の記述（本文は未取得）。国際技術パートナーシップのシンポジウムの運営への、イタリア、日本、フィンランド、米国の関与。

## 出典

- 国連 OICT 地理空間情報課「UN Open GIS Initiative Challenge & Opportunity」（2020-10、UN-GGIM アジア太平洋ウェビナー）
- Fujimura et al., "Design and development of the UN Vector Tile Toolkit", ISPRS Archives XLII-4/W14（2019）
- OSGeo 国連委員会の wiki（wiki.osgeo.org/wiki/UnitedNations_Committee）、OSGeo 国連メーリングリスト 2016-11（lists.osgeo.org/pipermail/un/2016-November/000035.html）
- Brovelli et al., ISPRS Archives XLII-4/W2（2017）
- S/PV.7802、S/PV.8838、S/PV.8521、S/PV.8534、S/2021/501（`https://docs.un.org/en/<記号>`）
