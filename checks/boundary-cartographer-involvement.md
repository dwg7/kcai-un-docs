# 検査記録：国境画定への国連の地図作成官の関与（2026-10-26）

対象: un-docs（コミット 6cd1cf0）の、記号の正規化・重複除去・合冊除外後の文書（`scripts/undocs.py` の `docs` ビュー）。関連の踏み跡は `knowledge/boundary-demarcation-un-cartographer-involvement-timeline.md`、`first-and-latest-cartographer-appointments.md`、`state-positions-on-un-boundary-assistance.md`。

## 1. 語ごとの文書数（正規表現は大文字小文字を区別しない）

| 式 | 文書数 | 備考 |
|---|---|---|
| `cartograph` | 73 | 年: 2000 年 4、2001 年 3、2002 年 1、2003 年 2、2004 年 2、2005 年 1、2006 年 5、2007 年 9、2008 年 2、2009 年 1、2011〜2022 年は各 0〜5。1950〜84 年の 18 文書は、比喩や他国の地図を指す発言で、国連の職員ではない |
| `\bcartographer` | 28 | 2000 年 3、2006 年 4、2007 年 7 |
| `boundary demarcation` | 38 | 1991〜94 年に 19 |
| `demarcat` | 1,019 | 2000 年以降は年に 12〜40 |
| `delimitation` | 384 | |
| `boundary commission` | 92 | 2002 年 15、2005 年 10 |
| `surveyor` | 16 | |
| `Cartographic Section` | 8 | 2001、2003（2）、2011、2013、2014（2）、2015 |
| `Chief Cartographer` | 3 | S/PRST/2000/21、S/PV.4160（再掲）ほか |

手順: 全文の走査は重く（メモリ超過で 1 回中断した）、広い式で部分集合を作ってから数えた。部分集合の式は `cartograph|demarcat|delimitat|boundary commission|surveyor|border commission|boundary delineation|boundary-making|boundary technical|technical (team|expert)s? .{0,80}(boundar|border)`（1,359 文書）と、`Blue Line|line of withdrawal|geodetic|geodesy|topograph|survey team|technical team|technical expert|shared natural resource|transboundary (water|aquifer|resource)|joint (development|management) (zone|area|authority)|Boundary Demarcation Commission|Joint Border Verification|…`（1,609 文書）。以下の語別の数え直しは、この二つの和集合に対して行った。

## 2. 年代別の頻度（1,000 文書あたり）

分母は、年ごとの un-docs の文書数（記号の重複除去後。日付の無い文書は含めない）を 5 年ごとに合計した値。

- A 式（国連の地図作成官を指す語）: `(united nations|\bUN\b) cartograph|(chief|senior) cartographer|Cartographic (Section|Unit)|cartographers? (from|of) the United Nations|United Nations Cartographer`
- B 式（名指しの境界委員会）: `Iraq.Kuwait Boundary Demarcation Commission|Eritrea.Ethiopia Boundary Commission|Ethiopia.Eritrea Boundary Commission|Cameroon.Nigeria Mixed Commission|Boundary Commission`

| 期間 | 文書総数 | A 式の文書数 | A 式 /1,000 | B 式の文書数 | B 式 /1,000 |
|---|---|---|---|---|---|
| 1990〜94 | 2,114 | 0 | 0.0 | 12 | 5.7 |
| 1995〜99 | 3,117 | 0 | 0.0 | 1 | 0.3 |
| 2000〜04 | 4,553 | 9 | 2.0 | 33 | 7.2 |
| 2005〜09 | 4,294 | 9 | 2.1 | 42 | 9.8 |
| 2010〜14 | 4,160 | 4 | 1.0 | 15 | 3.6 |
| 2015〜19 | 4,757 | 1 | 0.2 | 22 | 4.6 |
| 2020〜23 | 3,512 | 0 | 0.0 | 11 | 3.1 |

限界:
- 語が出ることは、国連の職員が関与したことを意味しない（A 式の 2011〜15 年の文書には、事務局の地図課の呼称や、地図の出典表記「Source: United Nations Cartographic Section」が含まれる）。
- 2015 年に地図課は Geospatial Information Section に改称された（A/RES/69/308）。A 式は新名称を含まないので、2015 年以降の低下の一部は名称の変更による。
- B 式の「Boundary Commission」は、エチオピア・エリトリア以外の委員会（1947〜57 年を除く期間でも）を含みうる。
- 年別の総数に、日付の無い 26 文書（`demarcat` 側）などは入らない。

## 3. 事例ごとに読んだ文書

- イラク・クウェート: S/PV.2981、S/PV.3108、S/PV.3224（公式 PDF）、S/22558（公式 PDF。un-docs に無い）、S/RES/773、806、833、S/PRST/1994/68（un-docs）。S/22558、S/25811（最終報告）、S/24113 は un-docs に無い（`replace(id,' ','') like 'S/22558%'` などで確認）。S/25811 の公式 PDF は画像のみで、文字が取れなかった（1 文字）。
- エチオピア・エリトリア: S/RES/1177、S/2000/1194、S/PV.4310、S/RES/1398、S/2008/630。UNMEE の報告に国連の地図作成官の語は見つけられなかった。
- レバノン: S/PRST/2000/21、S/2006/933、S/PRST/2006/52、S/PRST/2007/12、S/PRST/2007/29、S/PV.5667、5728、5736、S/2007/382、公式の S/2006/560、670、730、S/2007/392。2000 年の撤退線の確認の事務総長報告は、un-docs では S/2000/731 しか見つからず、地図作成官の語は無い。
- カメルーン・ナイジェリア: S/2004/298 以降の事務総長書簡（un-docs に 2004〜2021 年の 20 文書。`support team` と `Mixed Commission` の両方を含む S/yyyy/n）、議長の返信。公式サイトで S/2022/833、S/2024/43、S/2025/15、S/2025/864、S/2025/865。
- スーダン: S/RES/1812、1870、1919（UNMIS の技術・後方支援）、2046 以降の国境画定の記述。
- キプロス: S/2017/814。

## 4. 公式サイトの確認

- 公式の PDF の取得は `https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf` で届いた。S/PV.2981、3108、3224 は走査画像の文字認識で、`pdftotext` の既定の出力は語順が乱れた（-raw で読めた）。
- 国連デジタル図書館（digitallibrary.un.org）の検索は届いた。ただし書誌の検索で、全文の検索ではない。「Cameroon-Nigeria Mixed Commission support team」で、議長の返信 S/2005/529 から S/2025/865 までの一覧が得られた。「cartographer」では地図作成官の任命を示す結果は無かった。
- 届かなかった先: `unowas.unmissions.org`（403）、`www.un.org/geospatial/`（403）、`main.un.org/securitycouncil/…`（202、本文なし）。

## 5. 外れた・使えなかった検索

- `appoint…` と `cartograph…` の組み合わせ（前後 150 字）で当たった任命の文は、レバノンの 2006〜07 年の文書だけ。
- 「Cartographic Unit」の件数は、メモリの超過で数え終えなかった。S/PV.4227 に 1 件あることは確かめた。
- `joint (development|management) (zone|area|authority)` は 0 件。越境資源の共同開発区域の語は un-docs に無い。
