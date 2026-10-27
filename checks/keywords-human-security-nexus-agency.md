# キーワード調査の記録：human security、nexus、agency（2026-10-27）

un-docs（6cd1cf0）、`scripts/undocs.py`（記号を正規化、合冊除外、同じ記号は 1 本）。補助の集計スクリプトはスクラッチ（再現は下の式と `scripts/undocs.py search`、`scripts/speaker_counts.py`）。文書数は「語を含む文書の数」。5 年ごとの値は、日付のある文書を `date` の年で分けた。1,000 件あたりは、その期間の全文書（日付あり）で割った。

## 期間ごとの全文書数（日付あり）
1990〜94: 2,114／1995〜99: 3,117／2000〜04: 4,553／2005〜09: 4,294／2010〜14: 4,160／2015〜19: 4,757／2020〜23: 3,512（2023 年 10 月中旬まで）

## human security
| 式 | 文書数 | 注 |
|---|---|---|
| `(?i)human[\s-]+security` | 803 | S/PV 495、A/PV 128、S/yyyy/n 96、A/RES 62、A/S 7、S/RES 2、S/PRST 3。1,000 件あたり 1995〜99: 16.4、2000〜04: 32.7、2005〜09: 30.7、2010〜14: 29.8、2015〜19: 31.1、2020〜23: 56.4 |
| `(?i)common\s+understanding\s+(?:on\|of)\s+(?:the\s+notion\s+of\s+)?human\s+security` | 5 | A/64/PV.89、A/64/PV.107、A/66/PV.127 ほか |
| `(?i)trust\s+fund\s+for\s+human\s+security` | 50 | 最初 S/PV.4422(Resumption 1)（2001-11-20） |
| `(?i)human\s+security\s+network` | 95 | 最初 S/PV.4139（2000-05-11） |
| `(?i)friends\s+of\s+human\s+security` | 10 | 2007〜2010 年 |
| `(?i)commission\s+on\s+human\s+security\|human\s+security\s+now` | 6 | 最初 S/PV.4748（2003-04-30） |
- 最初の文書（S/INF を除く）: S/PV.3514（1995-04-11、アルジェリアの Lamamra 氏。公式の PDF で発言者を確認）。S/INF/72 は冊子（2017 年分を 2020 年に刊行）で、日付欄 1994-01-01 は誤り。
- S/PV.3778（1997-05-21）の最初の 2 件は、自動の見出し判定がジンバブエとしたが、公式の PDF では UNHCR の側の発言（「agencies such as ours」「as the High Commissioner said」）で、判定が外れた。3 件目はスウェーデン。
- 発言国（`scripts/speaker_counts.py`、見出し判定、623 文書、国を特定できなかった言及 251）: 日本 185 文書、カナダ 63、チリ 56、スロベニア 46、オーストリア 38、タイ 36、スイス 29、コスタリカ 27。2015 年以降（212 文書）は日本 69、タイ 23、スロベニア 20、チリ 13、オーストリア 12。
- A/RES の流れ: 55/59、55/206・57/267（国連大学の戦略計画の題名）、59/314・60/1（2005 年成果文書の第 143 項「人間の安全保障」）、64/291（2010）、66/290（2012-09-10。第 3 項「人間の安全保障は…アプローチ」）、以後は定型的な前文・本文。
- S/RES: 2358(2017)、2408(2018)（どちらもソマリア）。S/PRST: 2005/9、2006/38、2006/42。

## nexus
| 式 | 文書数 | 注 |
|---|---|---|
| `(?i)\bnexus\b` | 834 | S/PV 481、S/yyyy/n 164、A/PV 83、A/RES 74、S/RES 13。1,000 件あたり 1995〜99: 3.5、2000〜04: 11.6、2005〜09: 16.5、2010〜14: 29.8、2015〜19: 58.7、2020〜23: 81.7。1958〜1986 年は 9 文書（比喩的な普通の英語） |
| 人道・開発・平和のネクサス（式は下） | 187 | 最初 S/2012/42（2012-01-18）、S/RES/2065(2012)、S/RES/2097(2013)。5 年ごと 2010〜14: 5、2015〜19: 48、2020〜23: 134 |
| 安保・開発（`(?i)(?:security\|peace)[\s,/-]+(?:and\s+)?development[\s-]+nexus\|nexus\s+(?:between\|of)\s+(?:security\|peace)\s+and\s+development`） | 141 | 最初 S/PV.4081(Resumption 1)（1999-12-15） |
| 気候・安全保障（`(?i)climate[\s,/-]+(?:and\s+)?(?:security\|conflict\|peace)[\s-]+nexus\|nexus\s+(?:between\|of)\s+climate…`） | 40 | 最初 S/PV.5663(Resumption 1)（2007-04-17）。2020〜23 年に 31 |
| テロと組織犯罪・薬物（粗い式） | 86 | 最初 A/55/PV.79（2000-12-01） |
| 水・エネルギー・食料（`(?i)(?:water\|energy\|food)…nexus`） | 4 | A/63/PV.36、S/PV.7818、S/PV.8517 |
- 人道・開発・平和の式（OCR で区切りの落ちた綴りも拾う）: `(?i)humanitarian[\s,/–-]*(?:and\s+)?development[\s,/–-]*(?:and\s+)?(?:peace\w*)?[\s,/–-]*nexus|triple[\s,/–-]*nexus|(?:peace|humanitarian)[\s,/–-]*(?:and\s+)?(?:humanitarian|development|security)[\s,/–-]*(?:and\s+)?(?:development|peace\w*|humanitarian|security)?[\s,/–-]*nexus|nexus\s+(?:between|of)\s+(?:the\s+)?humanitarian`（広い式。187）。狭い式 `humanitarian…development…nexus|triple nexus` だけだと 1,000 件あたり 2015〜19: 7.1、2020〜23: 32.2（34 と 113 文書）。
- `nexus between A and B` の組（上位）: 安全保障と開発 46、平和と開発 31、平和と安全保障 26、テロと組織犯罪 24＋15＋14、国際移住と社会開発 16＋13、平和維持と平和構築 14、気候変動と安全保障 12＋7。
- 発言国（2015 年以降の `nexus`、350 文書）: カザフスタン 59（2017〜18 年の理事国。平和・開発の「close nexus」）、日本 30、南アフリカ 18、ポーランド 17、ドイツ 14。人道・開発・平和のネクサスを述べた国: 日本 16 文書、デンマーク 5、スペイン 4、ポルトガル 4、アイルランド 4、韓国 4。

## agency
| 式 | 文書数 | 注 |
|---|---|---|
| `(?i)\bagenc(?:y\|ies)\b` | 16,026 | 全体の 43%。ほとんどが「機関」の意味 |
| `(?i)\bspeciali[sz]ed\s+agenc\|\bUnited\s+Nations\s+agenc\|\bUN\s+agenc` | 9,735 | 機関 |
| `International\s+Atomic\s+Energy\s+Agency` | 2,022 | 固有名（大文字小文字を区別） |
| `\bthe\s+Agency\b`（大文字） | 1,222 | IAEA、UNRWA など固有名の略称 |
| `(?i)humanitarian\s+agenc\|aid\s+agenc\|relief\s+agenc\|donor\s+agenc` | 1,856 | 機関 |
| `(?i)intelligence\s+agenc\|law[\s-]+enforcement\s+agenc\|security\s+agenc` | 1,322 | 機関（情報機関、法執行機関） |
| **行為主体性の高精度の式**（下） | 59 | 取りこぼしが多い。1,000 件あたり 2005〜09: 0.2、2010〜14: 0.5、2015〜19: 2.5、2020〜23: 10.3 |
- 高精度の式: `(?i:women|girls|youth|young people|children|survivors|refugees|migrants|adolescents|individuals|people)(?:['’]s|s['’])\s+(?:own\s+)?agency\b|\bagency\s+of\s+(?i:women|girls|youth|young people|children|survivors|adolescents)\b|\b(?:autonomy|voice|empowerment|resilience|leadership|dignity|choice)(?:,|\s+and|,\s+and)\s+agency\b|\bagency(?:,|\s+and)\s+(?:autonomy|voice|empowerment|resilience|leadership|dignity|choice|participation)\b|\bsense\s+of\s+agency\b`（`agency` は小文字を区別）。
- 目視で 16 件を読んだところ、行為主体性の意味が 13 件、機関の意味が 3 件（S/PV.991 の "collective agency" は集団的機関、S/PV.6805 の "individual agency turf wars" は各機関の縄張り争い、A/61/PV.52 は曖昧）。精度はおよそ 80%。
- 最初の明確な例: S/PV.6005（2008-10-29、"women's agency in the peace and security sphere"）。
- より広い式（`human agency`、`local agency` など）は、機関の意味（"local agency"）や固有名への当たりが多く、使わなかった。`agency to act` も UNRWA などの "the Agency to act" に当たる。

## 地理空間の語との重なり（式 `(?i)geo-?\s?spatial|geographic(?:al)?\s+information|\bGIS\b|remote[\s-]+sensing|earth[\s-]+observation|satellite\s+imagery`）
同じ文書に両方が出る数: human security 23、nexus 29（うち人道・開発・平和 8）、行為主体性 2。偶然の同居が多く、内容のつながりは読んでいない。
