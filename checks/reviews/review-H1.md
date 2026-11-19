# レビュー H1: keyword-human-security / keyword-nexus / keyword-agency（un-docs 6cd1cf0）

対象: knowledge/keyword-{human-security,nexus,agency}-in-un-docs.md と checks/keywords-human-security-nexus-agency.md。
データ: documents.parquet（sha256 が checks/README.md の値 dd9edebc… と一致）。検索は scripts/undocs.py の connect()（正規化・重複除去・合冊除外）。公式原文は scripts/official.py（documents.un.org の PDF）で取得。届かなかった先は (3) に一覧。
抜き取り数: human security 約 20、nexus 約 20、agency 約 14。

## (1) 確認できた主張

### human security
- 803 文書、系列別（S/PV 495、A/PV 128、S/yyyy/n 96、A/RES 62、A/S 7、S/RES 2、S/PRST 3）: 再現。
- 期間別の 1,000 文書あたり（0.5/16.4/32.7/30.7/29.8/31.1/56.4）、分母（2,114/3,117/4,553/4,294/4,160/4,757/3,512）: 再現。
- 初出 S/PV.3514（1995-04-11）。公式 PDF で 3514th meeting, Tuesday, 11 April 1995、Mr. Lamamra (Algeria) の発言に "a new concept of human security based on economic prosperity and social well-being" と、核軍縮の完全廃絶に続く文脈: 一致。S/INF/72 の日付欄 1994-01-01（date_kind=other）が誤りという checks の注記も妥当。
- S/PV.3778（1997-05-21）: 最初の 2 件は公式 PDF で Mr. Jessen-Petersen（UNHCR 駐ニューヨーク連絡事務所長）の発言（"agencies such as ours"、"interface between human security…"、"to ensure human security if necessary"）。ジンバブエ（Mr. Sengwe）は発言者一覧に出るだけで、判定が外れたという記述は正しい。スウェーデン（Mr. Osvald）の "Large-scale attacks on human security" も確認。
- 式別件数: common understanding 5、Trust Fund 50（最初 S/PV.4422(Resumption 1)、2001-11-20。本体の S/PV.4422 には語がなく、Resumption 1 だけ。公式でも Resumption 1 に "Trust Fund for Human Security"）、Network 95（最初 S/PV.4139、2000-05-11。公式で Lucerne の Human Security Network に言及）、Friends 10、Commission/Now 6: 再現。
- S/RES 2 本（S/RES/2358 (2017)、2408 (2018)）の前文 "long-term human security for Somalis"、S/PRST/2005/9（2005-02-25、西アフリカ）、2006/38、2006/42: 再現。
- A/RES/60/1 第 143 項（公式で一致。"discussing and defining the notion of human security in the General Assembly"）、A/RES/64/291（2010-07-16。第 2 項は定義の合意を目指す継続の確認）、A/RES/66/290（2012-09-10、第 3 項 "Agrees that human security is an approach to assist Member States…"、公式で一致）。
- 発言国（speaker_counts.py）: 623 文書、日本 185、カナダ 63、チリ 56、スロベニア 46、オーストリア 38、タイ 36、スイス 29、コスタリカ 27。2015 年以降 212 文書で日本 69、タイ 23、スロベニア 20、チリ 13、オーストリア 12: 再現。
- 地理空間の語との共起 23 文書: 再現。
- 初期の A/RES（55/59 犯罪司法、55/206・57/267 国連大学の戦略計画の題名）: 本文で確認。

### nexus
- 834 文書、系列別（S/PV 481、S/yyyy/n 164、A/PV 83、A/RES 74、S/RES 13）: 再現。
- 期間別の 1,000 文書あたり（3.5/11.6/16.5/29.8/58.7/81.7）: 再現。
- 1958〜1986 年の「9 文書」: 日付つきは 8 文書（最初 S/PV.816、1958-04-18。最後 S/PV.2662、1986-02-13）、日付なしの A/PV.1643 を足すと 9。踏み跡の書き方は「日付のある」とは言っていないので許容範囲だが、(2) の軽微な点に記す。
- 安全保障と開発の式 141 文書、最初 S/PV.4081(Resumption 1)（1999-12-15、公式で "the nexus between peace and development"）: 再現。2015〜19 年 70: 再現。
- 気候と安全保障の最初 S/PV.5663(Resumption 1)（2007-04-17、公式で "energy-climate-security nexus" および "nexus between environmental degradation from climate change and increased conflict"）: 一致。件数 40 / 2020〜23 年 31 は再現できず（(3) 参照）。
- 人道・開発・平和の狭い式 147 文書、2015〜19 年 34、2020〜23 年 113: 再現。広い式 187 文書、2015〜19 年 48、2020〜23 年 134: 再現（ただし中身に問題あり、(2) 参照）。
- 「nexus between A and B」の組: 安全保障と開発 47（記録 46）、平和と開発 32（31）、平和と安全保障 27（26）、国際移住と社会開発 16、平和維持と平和構築 10〜14: 私の粗い式でほぼ一致（±1）。
- カザフスタン: 2015 年以降 350 文書、カザフスタン 59、日本 30、南アフリカ 18、ポーランド 17、ドイツ 14: 再現。引用 5 文書（S/PV.7351、7389、7533、7793、7847）はいずれもカザフスタンの発言に nexus が出る。ただし理事国就任（2017〜18 年）以前の会議（2014〜16 年）も含まれ、「理事国を務め」という記述は事実（今回は国連公式での任期確認はしていない）だが、引用 5 文書は理事国時代のものではない。
- 区切りを必須にした式が 91 文書、任意にした狭い式が 147 文書: 「4 分の 1 を取りこぼす」は 138→187 の比（広い式）として約 26%。数値は整合。

### agency
- 16,026 文書（un-docs 37,567 文書の 42.7%）、専門機関 9,735、IAEA 2,022、`the Agency` 1,222、人道・援助 1,856、情報・法執行 1,322: すべて再現。
- 行為主体性の高精度の式の期間別（2005〜09: 0.2、2010〜14: 0.5、2015〜19: 2.5、2020〜23: 10.3 / 1,000 文書）: 件数 1/2/12/36 から再現。
- 最初の例 S/PV.6005（2008-10-29、公式で "How can we harness the full force of women's agency in the peace and security sphere?"）: 式の当たりでも最古。
- S/PV.9276(Resumption 1) の "women's agency"（エチオピア）、A/RES/73/147 の "voice, agency and leadership"、S/PV.9381（2023-07-18）の "human agency and control are essential for nuclear weapons"（事務総長の発言）: 公式で確認。
- 目視の抜き取り（私の 15 件）: 行為主体性の意味 15 件。

## (2) 食い違い

### A. nexus: 人道・開発・平和のネクサスの「初出」と決議の例が誤り（重大）
- 踏み跡（nexus 要点の表）: 「初出 S/2012/42（2012-01-18）。安保理決議では S/RES/2065 (2012)、2097 (2013)」「2010〜14: 5」。決議での扱いの節も「S/RES/2065 (2012) 以降」「S/RES 4、S/PRST 2」。checks も同じ。
- 公式原文: S/2012/42、S/RES/2065 (2012)、S/RES/2097 (2013) の "nexus" はいずれも "the peace, security and development nexus"（シエラレオネの文脈）で、人道を含まない。S/INF/68 も確認なし。S/PV.7289（2014-10-28）は "women-peace-security nexus"。広い式（`(?:peace|humanitarian)…(?:development|security)…nexus`）が「平和・安全保障・開発」の綴りを拾っている。すなわち 2010〜14 年の 5 文書はすべて偽陽性。
- 正しい値（狭い式 `humanitarian…development…nexus|triple nexus`、147 文書）: 最初は S/PV.7561（2015-11-17、トルコ "humanitarian-development nexus"。公式で確認）、次いで A/70/PV.116 と A/RES/70/302（2016-09-09、"a strengthened humanitarian-development nexus"）。2010〜14 年は 0。安保理決議で人道・開発・平和のネクサスが明示されるのは S/RES/2612 (2021)（"humanitarian-development-peace triple nexus approach"）と S/RES/2656 (2022) の 2 本。S/PRST/2018/16 と S/PRST/2019/7 は "development, humanitarian, (human rights and) peace and security nexus" で、語順違いの類似形。
- 影響: 「トリプル・ネクサスを含む広い式」の 187 は、安全保障・開発のネクサス（141）と重なる。「右肩上がり」の説明は 2015 年以降の狭い式の値（34→113）でも成り立つが、「2012 年から」という起点は誤り。

### B. nexus: 「水・エネルギー・食料」の 4 文書の内訳が誤り
- 踏み跡: 「A/63/PV.36（2008）」を初出とする。checks も「A/63/PV.36、S/PV.7818、S/PV.8517」。
- A/63/PV.36（2008-11-03）の文は "the nexus between food security, climate change, sustainable development and agriculture"（FAO、カリブ海）で、水・エネルギー・食料の組ではない。私の狭い式で当たる 4 文書は S/PV.7818（2016-11-22、"water-energy-food security nexus"）、S/PV.8517（2019-04-29、"Water-Energy Nexus"）、S/PV.8923(Resumption 1)、S/PV.9181(Resumption 1)。件数 4 は偶然一致するが、初出は S/PV.7818（2016）で、「ほとんど出ない」という結論は変わらない。

### C. nexus: 「テロと組織犯罪・薬物」の初出 A/55/PV.79 の意味
- 公式原文の A/55/PV.79（2000-12-01）の nexus は、紛争ダイヤモンドの違法取引と反政府勢力の資金（"nexus between illicit trafficking and transactions in rough diamonds and the sustaining of rebel groups"）と、組織犯罪と武器の違法取引（"its nexus with the illicit trade in arms"）。テロとの関連ではなく、「テロと組織犯罪」の意味の初出とは言い難い。「粗い式」と断りはあるが、初出として書くなら要点の表から外すか注を付ける。テロと組織犯罪の "nexus between terror…" 型で最初に当たるのは S/PV.4845(Resumption 1)（2003-10-16）（私の式 `nexus between (international )?terroris`、44 文書）。

### D. nexus: 表の「約 480」と合計の矛盾
- 187+141+86+40+4+480 = 938 > 834。意味の分類が重なる（広い式 187 と安全保障・開発 141 が重なる）ためで、表に「重なりを含む」と書かれていない。「上記以外 約 480」は引き算の値のようだが、再現手順がない。

### E. agency: 高精度の式の文書数 59 は再現できず 51
- 踏み跡・checks: 「59 文書」。checks にある式をそのまま RE2（duckdb）で実行すると 51 文書（2005〜09: 1、2010〜14: 2、2015〜19: 12、2020〜23: 36）。1,000 文書あたりの値（0.2/0.5/2.5/10.3）は 51 件で再現し、59 では 2020〜23 年が 10.3 にならない可能性が高い。59 は式を変える前の値と見られる（推測。未確認）。
- 「目視で 16 件を読み、機関の意味が 3 件、精度 80%」: 3 件の例に挙がる S/PV.991、S/PV.6805、A/61/PV.52 は、記録された式の当たり 51 件に含まれない。S/PV.991 の "collective agency" は 1960 年代の文書。記録された式の当たりを私が抜き取った 15 件はすべて行為主体性の意味で、機関の意味はなかった。「精度 80%」は別の式（広い式）の目視で、式と数値が対応していない。
- 「S/PV.9381 の「人間の行為主体性と管理」」は踏み跡の「文脈」の例として正しい（公式で確認）が、高精度の式には当たらない（"human agency" を含まない式のため）。「59 文書の文脈」と読めないよう、式の外の例だと書く。

### F. human security: 軽微
- 「1999〜2000 年の山」: 年別は 1999: 31、2000: 50、2001: 22。2000 年（50）が最大で整合。「2020 年代の山」は 2020〜23 年の 47/48/47/56。問題なし。
- `verified_how: mixed` だが、本文は「公式の PDF との突き合わせはしていない」とする A/RES/60/1、64/291、66/290 を、今回は公式で確認した（60/1 第 143 項、66/290 第 3 項。64/291 は un-docs の本文のみ読んだ）。
- S/PV.3514 の引用「経済的な繁栄と社会的な福祉に立脚した人間の安全保障の新しい概念」は要約で、原文は "ensuring the promotion of a new concept of human security based on economic prosperity and social well-being"。誤りなし。

### G. 範囲の書き方
- 3 本とも範囲の注記は冒頭にあり、「国連全体」への拡張は見つからない。nexus の「一般に「ネクサス」から連想される使い方とずれる」は un-docs の範囲の話と読めるが、「国連の主要な議論ではない」（よくあるまちがいの節）は un-docs（総会・安保理の英語文書。ECOSOC や専門機関は含まない。水・エネルギー・食料は専門機関や ECOSOC の議論で多い可能性がある）に限ると明記したほうがよい。
- 発言者の取り違え、(Resumption 1) の混同、日付欄の誤り、綴り違いは、今回の抜き取りでは human security に限ればなし。nexus の 2012 年の文書群は「文書の取り違え」ではなく「語義の取り違え」。

## (3) 再現できなかった主張
- nexus「気候と安全保障」40 文書、2020〜23 年に 31: 私の再構成（checks の式が「…」で省略されているため）では 37 と 29。式が省略されており、完全な再現はできない。
- nexus「水・エネルギー・食料」の式（checks で「…」と省略）: 狭い式で 4 文書は当たるが、上記 B のとおり内訳が違う。
- nexus「テロと組織犯罪・薬物（粗い式）86」: 式が checks に書かれておらず再現できない。
- nexus 発言国の「人道・開発・平和のネクサスを述べた国: 日本 16、デンマーク 5…」: 式が広い式（偽陽性を含む）に依存する。再実行していない。
- agency 高精度の式 59 文書（51 で再現）、目視 16 件の精度 80%（上記 E）。
- agency 広い式の 684 文書: 式が checks に書かれておらず再現できない。
- nexus の「約 790 の「nexus between A and B」」: 私の粗い式で 600 件（493 文書）。数え方（文書数か出現数か）が書かれておらず再現できない。
- 届かなかった公式の記号: `S/PV.4422(Resumption 1)`（スペースあり、括弧のみ）は documents.un.org が 1,303 bytes の非 PDF を返した。official.py には空白なしの `S/PV.4422(Resumption1)` で届いた。到達できなかった先は他にない。
- 理事国の任期（カザフスタン 2017〜18 年）は国連公式で未確認。
- 公式の PDF と突き合わせていないもの: S/PV.9158 系、S/RES/2358/2408 の公式日付（un-docs の日付のみ）、A/RES/64/291 の公式本文。

## (4) 直し方の提案
1. nexus 要点の表と「決議での扱い」の節: 人道・開発・平和の初出を「S/PV.7561（2015-11-17、トルコの発言）。決議の明示は S/RES/2612 (2021)、2656 (2022)」に直し、2010〜14 年を 0 にする（件数は狭い式 147 で 2015〜19: 34、2020〜23: 113）。S/RES/2065 と 2097 は、人道を含まない「平和・安全保障・開発のネクサス」の例として安全保障・開発の行に移す。checks の式と注も修正する。広い式から `(?:peace|humanitarian)…security` の枝を除くか、「広い式は『平和・安全保障・開発』も拾う」と注記する。
2. 水・エネルギー・食料: A/63/PV.36 を外し、「初出 S/PV.7818（2016-11-22）」とする。A/63/PV.36 は「食料安全保障・気候変動・持続可能な開発・農業のネクサス」の例にとどめる。
3. テロと組織犯罪の初出: A/55/PV.79 の意味（紛争ダイヤモンド・武器取引）を注記するか、初出を S/PV.4845(Resumption 1)（2003-10-16）などに変える。式は checks に全文を書く。
4. 表の「約 480」と合計: 「分類は重なる。合計は 834 にならない」と書き、「上記以外」の数は再現できる式を添える。
5. agency: 「59 文書」を、記録した式で再現した 51 に直す（または 59 を出した式を checks に残す）。目視の 16 件と精度 80% は、どの式の当たりかを書き、S/PV.991、S/PV.6805、A/61/PV.52 が別の式の例であることを明記する。S/PV.9381 は式の外の例と書く。
6. nexus の「国連の主要な議論とみなす」の節: 「un-docs（総会・安保理）では」を足す。
7. 1958〜1986 年の「9 文書」: 「日付のある 8 文書＋日付なし 1 文書」と書く。
8. human security の `確かめた度合い`: A/RES/60/1 第 143 項と A/RES/66/290 第 3 項は公式の PDF と突き合わせ済み（2026-11-19 のレビューで確認）と更新する。reviewed への変更は hfu が判断する。
