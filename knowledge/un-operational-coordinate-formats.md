---
id: un-operational-coordinate-formats
title: 決議より運用に近い国連の公開文書で、位置はどの座標表記で書かれるか（MGRS は見つかったか）
status: draft
verified_how: mixed
dataset_rev: 6cd1cf0
as_of: 2026-10-26
sources:
  - yuiseki/un-docs documents.parquet（コミット 6cd1cf0）。式と件数は checks/un-operational-coordinate-formats.md
  - S/2015/302、S/2016/85、S/2017/904、S/2018/732、S/2019/632、S/2020/840、S/2021/777、S/PV.544、S/PV.1162(OR)、S/PV.1320(OR)、S/PV.1449(OR)（un-docs の本文で文脈を読んだ。公式 PDF との突き合わせはしていない）
  - United Nations Military Peacekeeping-Intelligence Handbook（第 1 版、2019 年 5 月。国連平和活動局。中東和平プロセス担当国連特別調整官事務所（UNSCO）のサイトで公開）
  - UN Military Observers 研修教材の UNMO Report Templates（UNMO STM 2025）と Lesson 3.12（UNSCO のサイトで公開）
  - UN Military Peacekeeping-Intelligence Officers 研修教材（2020-04-15 版）第 1 部
  - UNOSAT OCHA-OPT-015（2024-07-06）
  - checks/un-operational-coordinate-formats.md
authors:
  - hfu の指示のもと、AI が実施・記述。AI 支援あり
reviewed_by: []
updated: 2026-10-26
related: [sage-situational-awareness-geospatial-enterprise, un-mission-gis-mentions-in-un-docs, geospatial-search-terms, satellite-imagery-in-security-council-who-and-why]
cites:
  - un-docs: 座標の語と表記の検索、文脈の確認
finding:
  - mgrs-not-found-in-un-docs-or-in-the-public-operational-documents-read
  - un-public-operational-documents-say-grid-reference-without-naming-the-grid
---

## 要点

> 範囲: un-docs ＝ 総会と安保理の英語文書（2023 年 10 月ごろまで）。安保理決議は S/RES/2699（2023-10-02）まで。ここでは un-docs の外の文書も数本読んだが、本文を読めた運用寄りの文書は下の表の 5 本（と UNOSAT の地図 1 枚を含む）だけで、国連全体の運用文書を代表しない。

hfu の問いは、決議より運用に近い準公式文書に、MGRS（Military Grid Reference System、NATO などの軍が使う格子による位置表記）が出る可能性があるか、である。結論は次のとおりである。

- **MGRS という語も、MGRS 形式の文字列も、見つからなかった。** un-docs では `MGRS`、`military grid`、`grid zone` の式がすべて 0 件で、MGRS 形式の文字列を探す式も 0 件だった。un-docs の外で本文を読めた 5 本の国連の文書（下の表）でも 0 件だった。
- **位置の表記は文書の種類で分かれていた。** 安保理に出る調査報告では度分秒の緯度経度、国連衛星センター（UNOSAT）の地図では投影法つきの UTM（Universal Transverse Mercator、メートル単位の平面座標）、平和維持の訓練用の様式では「grid reference」（格子の名前を書かない）だった。
- **「可能性が高い」は根拠を分けて言うべきである。** 国連の文書自身が MGRS を指定する文言は、読めた範囲に無い。根拠になりうるのは、様式が「grid reference」を求めること、地雷情報管理の道具 IMSMA が MGRS を最初から有効にしているとする検索結果の要約（本文は未取得）、各国軍が MGRS を使うこと、の三つだが、どれも国連の文書が MGRS を使うことを直接には示さない。
- 読めなかった文書が多い（末尾の一覧）。「見つからなかった」は、読めた文書と un-docs の範囲での話である。

## 詳しく

### 読めた文書と、位置の書き方

| 文書 | 日付・公開の度合い | 位置の書き方 | 読んだ位置 |
|---|---|---|---|
| UN Military Peacekeeping-Intelligence Handbook | 2019 年 5 月、国連平和活動局。UNSCO のサイトに PDF があり、公開 | 座標の形式を決める文言は無い | 9.4.3 に「At least two northing and easting cross markings」とある。重ね図を地図に正しく載せるための印で、座標の表記ではない |
| UNMO Report Templates | 2025 年の研修教材。UNSCO のサイトに docx があり、公開。研修用で、実際の様式ではないと断っている | 「grid reference」を求める。MGRS の語は無い | 緊急報告（Flash Report）の「Where」欄に「Provide grid reference of the location」と「Use the GPS as appropriate」とある。停戦違反報告（Cease Fire Violation Report）に「Grid Reference」欄がある |
| UNMO Lesson 3.12（報告の手続） | 2025 年 12 月作成。公開 | 形式は書かれない | 日報の指針の図に「COORDINATES」の見出しだけがある |
| UN Military Peacekeeping-Intelligence Officers 教材（第 1 部） | 2020 年 4 月版。Peacekeeping Resource Hub で公開 | 座標の形式の語は無い | 第 1 部（282 ページ）に該当語が 0 件。第 2・3 部と地図の付属書は未読 |
| UNOSAT の Gaza 損害評価地図 OCHA-OPT-015 | 2024 年 7 月 6 日。公開 | 投影つきの UTM | 地図の記載欄に「WGS 1984 UTM Zone 36N」とある（地図の描画用の投影法の記載で、地図に載る地点の表記は別に確かめていない） |
| 安保理に出る調査報告（un-docs） | 2017〜2021 年。公開 | 度分秒の緯度経度 | 下の「安保理文書に出る表記」 |

MPKI Handbook は、軍の情報要員が使う手引きである。情報の分析に「coordinate register」という記録簿（脅威の出来事を地域別に記す紙の台帳）を勧めるが、書き方の形式は定めない（Annex B to Chapter 7）。

### 安保理文書に出る表記（un-docs で確かめた）

- 度分秒の緯度経度: OPCW（化学兵器禁止機関）・国連合同調査メカニズムの報告 S/2017/904 の「36°24′51.12″N, 37°12′38.16″E」、OPCW 事実調査団の報告 S/2018/732 の「N 33° 34’ 24”, E 36° 23’ 41.1”」、決議 1874 の専門家パネルの中間報告 S/2020/840 と S/2021/777 の「39°9'19.66"N 127°36'26.85"E」など。度分の式に当たったのは 11 件で、網羅ではない。
- 「GPS coordinates」という語: 12 件。形式を書かないものを文脈で読んだ（S/2016/85、S/2019/632）。S/2019/632 は、クウェート側が提供した GPS 座標で埋葬地を発掘したと述べる。
- 「grid coordinates」: S/2015/302 の 1 件。スーダンと南スーダンの間のアビエ地域に関する事務総長報告の文書で、安全な非武装国境地帯の中心線と grid coordinates をめぐる当事者の不一致を述べる。格子の種類は書かれない。
- 古い「map reference」: 1951〜1968 年の会議録に、地図の格子の数字を述べる例がある。S/PV.544（1951）は「map reference 2070-2577」、S/PV.1162(OR)（1964）は「map reference 210600-294925」、S/PV.1320(OR)（1966）は「map reference 156-089」、S/PV.1449(OR)（1968）は国連休戦監視機構（UNTSO）の軍事監視員の報告を引いて「approximate map reference 74158705」と述べる。数字だけで、格子の名前や基準面は文書に出ない。

### MGRS が出る可能性についての根拠（直接の証拠とは分けて読む）

1. 直接の証拠はない。読めた国連の文書に MGRS の語は 0 件である。
2. 「grid reference」という語は、軍の地図読みの用語である。ただし様式は格子の名前を書かないので、MGRS か、国や地図ごとの格子かは、この文言からは決まらない。
3. 検索結果の要約では、地雷情報管理システム IMSMA の wiki が「WGS 1984 and MGRS are active after the installation」と述べるとされる。ページの取得は失敗しており、本文を読んでいない。
4. 米国の統合参謀本部の指示（CJCSI 3900.01）が MGRS を陸上部隊の報告の座標にすると述べる、とする要約が検索結果にあった。これは米国の文書であり、国連の運用がこれに従うことは示さない。
5. UNIBAM（国連歩兵大隊マニュアル）2020 年版が国の教範に代わるものではないと述べる、とする要約があった。兵員派遣国の教範が使われる余地を示唆するが、本文は未取得で、MGRS との関係は未確認である。

### 運用の道具について

SAGE（国連の事案データベース）の入力項目の座標形式、各ミッションの Joint Operations Centre（統合作戦センター）の手順書、Contingent-Owned Equipment マニュアルの GPS の条項は、公開の本文を取得できなかった。取得できなかった先は checks/un-operational-coordinate-formats.md に一覧がある。

## よくあるまちがい

- 「grid reference」を MGRS と読む。UNMO の様式は MGRS と書いていない。
- 地図の欄にある「UTM Zone 36N」を、MGRS を使っている証拠と読む。UTM は MGRS の土台だが、UNOSAT の記載は地図の投影法の宣言であり、地点の表記を MGRS にする宣言ではない。
- 「MGRS が 0 件」を「国連は MGRS を使わない」と読む。読めた文書が少なく、運用の内部文書（SOP）は公開されていないか、取得できなかった。
- 「northing and easting」を座標表記の規則と読む。MPKI Handbook の 9.4.3 は重ね図の位置合わせの印の説明である。
- un-docs の語の検索の件数を、運用での使用頻度と読む。un-docs は総会と安保理の英語文書である。
- `UTM` の 11 件を投影法の UTM と読む。確かめた 2 件は OCR の崩れと企業名で、投影法ではない。

## 確かめた度合い

- **un-docs を検索して確かめた**: 座標の語と表記の件数（式は checks/ に記録）。文脈を読んだのは 11 文書。検索語は大文字小文字の指定を式に書いた。度分秒の式は網羅ではない。
- **公式の原文で確かめた**: していない。S/ 番号の文書は un-docs の抽出テキストを読んだだけで、公式 PDF と突き合わせていない。
- **読んだだけ**: 上の表の国連の文書 5 本（WebFetch が保存した PDF／docx を文字にして語を検索した。MPKI Handbook は全 121 ページ、MPKIO 教材は第 1 部のみ、UNMO の様式と Lesson 3.12 は全体）と、UNOSAT の地図 1 枚。ページの様式や図に画像として入った文字は、文字抽出で拾えない可能性がある。
- **検索結果の要約だけ**: IMSMA、UNOSAT の他の地図、UNIBAM、CJCSI 3900.01、STANAG 2211。踏み跡の主張の根拠にしていない。
- **未確認**: SAGE の座標形式、各ミッションの SOP、UNIBAM・偵察部隊マニュアルなどの軍事ユニットのマニュアル、Aviation Manual の本文、COE マニュアル、UNIFIL・UNDOF・UNFICYP・MINURSO の公開の事案報告の座標、HDX の座標系の規約、UN Open GIS の資料。いずれも取得できなかった（403、503、502、接続不可）か、本文に届かなかった。

## 出典

- un-docs（コミット 6cd1cf0）: S/2015/302、S/2016/85、S/2017/904、S/2018/732、S/2019/632、S/2020/840、S/2021/777、S/PV.544、S/PV.1162(OR)、S/PV.1320(OR)、S/PV.1449(OR)。公式サイトの形式は `https://docs.un.org/en/<記号>`。
- United Nations Military Peacekeeping-Intelligence Handbook (MPKI HB), first edition, May 2019: https://unsco.unmissions.org/sites/default/files/2026-04/United%20Nations%20Military%20Peacekeeping%20Intelligence%20Officers%20-%20Scenario%20Based%20Exercise%20-%20Reference%20Materials%20MPKI%20Handbook.pdf
- UN Military Observers, UNMO Report Templates (UNMO STM 2025): https://unsco.unmissions.org/sites/default/files/2026-07/UN%20Military%20Observers%20-%20UNMO%20Report%20Templates.docx
- UN Military Observers, Module 3, Lesson 3.12 UNMO Reporting Procedures: https://unsco.unmissions.org/sites/default/files/2026-07/UN%20Military%20Observers%20-%20Module%203%20-%20Lesson%203.12%20UNMO%20Reporting%20Procedures.pdf
- UN Military Peacekeeping-Intelligence Officers training materials, 15 April 2020, Part 1: https://resourcehub01.blob.core.windows.net/training-files/Training%20Materials/038%20RTP-MIO/038-002%20UN%20MPKIO%20(Intel)%20Final%20Version%2015%20APR%202020_Part1.pdf
- UNOSAT, OCHA-OPT-015 Gaza Strip Comprehensive Damage Assessment, 6 July 2024: https://unosat.org/static/unosat_filesystem/3904/OCHA-OPT-015_UNOSAT_A3_Gaza_Strip_OPT_CDA_06072024.pdf
- checks/un-operational-coordinate-formats.md（式、件数、取得できなかった先、検索語）
