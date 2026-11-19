# 独立レビュー H2: 日本の人間の安全保障の踏み跡 / agency の行為主体性の分類

対象: knowledge/japan-statements-on-human-security-in-un-docs.md、knowledge/agency-agentive-use-by-meeting-type-in-un-docs.md
データ: scratchpad の documents.parquet（sha256 dd9edebc…ad54f5 が README の値と一致。読み取りのみ）。公式原文は scripts/official.py（docs.un.org / documents.un.org の PDF、届いた）で照合。
リポジトリのファイルは編集していない。作業用の出力はスクラッチ（…/scratchpad/w/jp.json、ag.json、loose.py、ag1.py）。

## (1) 確認できた主張

### 日本の踏み跡
- (a) 数: `python3 -I scripts/country_segments.py DATA Japan '(?i)human[\s-]+security'` で 185 発言・185 文書・361 出現。checks/japan-human-security-statements.tsv と全行が一致（diff なし）。ただし正規表現は `human[\s-]+security`（`human\s+security` だと 184 文書・359 で、S/PV.8900 の "human-security perspectives" が落ちる）。踏み跡の本文にも README にも、この式が書かれていない（checks/keywords-human-security-nexus-agency.md の式表にだけある）。
- 見出しの判定（Mr./Ms./Mrs. X (Japan):）: 185 発言の見出しは全て "Mr./Mrs. 氏名 (Japan)" 形（"(spoke in French/Spanish/Japanese…)" 付き 6 件を含む）。発言の中に別の発言者の見出し様の文字列（"Mr. X (…):" "The President:" など）が混ざるものは 0 件。別の国の発言を日本としている例は見つからなかった。「会議の終了・附属書・議題」語の後に出現が来る 16 件も、全て発言の中の語（annex 等の普通の語）だった。
- (b) 金額: S/PV.7247（2014-08-21、Mr. Yoshikawa (Japan)）に "Since 1999, Japan has contributed $390 million to the United Nations Trust Fund for Human Security." 公式 PDF にも同文、直前の見出しも Yoshikawa (Japan)。「累計 3 億 9,000 万ドル」「1999 年から」「2014 年」は正しい。
- 基金の他の金額・事業（un-docs と公式 PDF の両方で、発言者見出しも確認）: S/PV.4176 (Resumption 1) の $16 million（コソボ初等教育、Akasaka）、S/PV.4577 の $3 million（シエラレオネ、Motomura）、S/PV.5703 の "more than 50 projects"（Oshima）、S/PV.7527 の $2.5 billion（Minami）、S/PV.8234 の約 $18 million（Hoshino）、S/PV.6389 の four pillars（Kan）、S/PV.5834 の "initiator of the Friends of Human Security"（Takasu）、S/PV.7289 の "main pillars of human security"（Minami）、S/PV.3980 の小渕首相の引用（Takasu）、S/PV.8241 の "two main strategies"（Hoshino）。S/PV.4646 (Resumption 1) の約 $6 million（農業とコミュニティの復興、基金経由、Haraguchi）は un-docs で確認（公式は照合せず）。
- (c) S/PV.5898 (Resumption 1)（2008-05-27、Mr. Shinyo (Japan)）: "It does not in any way suggest military intervention, even as a last resort, and thus differs from the notion of the responsibility to protect." un-docs と公式 PDF が一致。踏み跡の言い換え（軍事介入を意味するものでは全くなく、保護する責任とは異なる）は妥当。「185 発言のうち responsibility to protect が出るのは 3 発言」も再現（S/PV.5703、S/PV.5898 R1、S/PV.7129）。S/PV.5703 は 2005 年サミットと決議 1674 を引く用法、S/PV.7129 は「peacekeepers' responsibility to protect children」で概念ではない、という説明も本文どおり。
- (d) S/PV.5264（2005-09-20、Mr. Oshima）: "For the first time in United Nations history, the concept of human security is reflected…2005 world summit outcome document… In paragraph 143" 一致（公式 PDF も同文、見出し Oshima (Japan)）。A/67/PV.23（2012-10-11、Mr. Kodama）: "Resolution 66/290 on human security, adopted by consensus in September, is another notable achievement" 一致（公式も）。A/64/PV.107（Takasu）: "first-ever draft resolution of the General Assembly on human security"、A/64/L.61、第 143 項、2006 年 10 月のフレンズ、"More than 140 Member States…seven meetings"、A/64/701、作業上の定義 "to protect the vital core of all human lives in ways that enhance human freedoms and human fulfilment" いずれも一致。
- その他、本文どおりと確認: S/PV.4748（原口、「1 May に報告書」）、S/PV.9257（Shino の三つの柱: 恐怖からの自由、欠乏からの自由、尊厳）、S/PV.9158 R1 の 79 の行動、S/PV.8949 の軍事費と人間の安全保障への投資、S/PV.6587 R1（Osuga、気候変動）、S/PV.9036 R1、S/PV.8923、S/PV.8900（"human-security perspectives"、Ishikane）、S/PV.6097（コソボ "test case"）。
- (e) 年代ごとの「発言の数」行: 17 / 34 / 49 / 24 / 20 / 41 が再現。主題語の表は式が書かれていないので、緩い式で再現を試みた結果、平和構築 97(104)、アフリカ 92(92)、女性 76(75)、難民 65(67)、子ども 64(64)、保健 53(51)、アフガニスタン 40(40)、テロ 38(37)、気候・災害 32(32)、民間人の保護 23(26)、コソボ 19(21)、食料 11(11)、ネクサス 16(16)。括弧内は踏み跡の値。式が違うため数件ずつずれるが、時期ごとの山の形は同じ。「フレンズ」は 9 文書、全て 2007〜2010。「保護とエンパワーメント」は式により 41〜43 文書（踏み跡の 43 と矛盾しない式あり）。
- 話者別の見出し数は Takasu 30、Ishikane 21、Haraguchi 18、Shino 10 を再現。

### agency の踏み跡
- 51 文書: checks/keywords-human-security-nexus-agency.md の高精度の式から human/individual/collective/moral を除いた式を全文書に適用して 51 文書、TSV の 51 行と完全に一致（過不足 0）。内訳（安保理の会合 18、決議・報告 19、事務総長報告 7、書簡 5、A/PV 2）と年別（2008:1、2012:1、2013:1、2015:2、2017:2、2018:4、2019:4、2020:7、2021:7、2022:12、2023:10）も TSV と一致。
- 本文を読み直して、行為主体性の用法で分類も妥当と判定した文書（17 件）: S/PV.6005（"women's agency in the peace and security sphere"）、S/PV.7857（"harness the agency of women"、スウェーデンの発言）、S/PV.8241（"voice, agency and leadership" 青年）、S/PV.8382（"young women's capacities, agency and leadership"）、S/PV.8403（"women's leadership, voice and agency"、スーダンの議題）、S/PV.8888（"voice and agency of Syrian women"）、S/PV.9126（"retain dignity and agency"、避難民）、S/PV.9257（"stereotypes about women's agency"）、S/PV.9260 R1（"voice and agency"、女性と女児、海面上昇）、A/67/PV.43（インド、"women's agency and empowerment"）、A/75/PV.58（"dignity and agency"、奴隷とされた人々）、S/2020/346（青年、書簡。本文は青年担当事務総長特使の説明を含む）、S/2022/258（IE グループの書簡、ミャンマー）、S/2021/383（アビエ、"women's agency in the Misseriya community"）、A/RES/75/284（"voice, autonomy, agency and leadership of women and girls"）、A/77/L.77（SGBV の被害者の "autonomy and agency"）、A/RES/73/153・A/RES/77/317 など。
- 「同じ定型の一文が繰り返される」: A/RES/73/147・75/159・77/196 は同題の「Intensification of efforts to end obstetric fistula」、73/153 は Child, early and forced marriage、73/195・76/266・77/176 の移住は "independence, agency and leadership" の同じ句。決議と報告の二重計上（A/RES/77/196 と A/77/456 など）も本文のとおり。
- 抽出は 2008 年が最初（S/PV.6005）という主張も、式の範囲内で一致。

## (2) 食い違い（該当文、正しい値、根拠）

### 日本の踏み跡

D1. 「185 文書・361 出現」は、スクリプトの出力としては正しいが、日本の発言の全数ではなく、少なくとも 10 文書（約 21 出現）を落としている。
- 該当: 「要点」の範囲注記、「確かめた度合い」の「見出し判定は、日本の代表が議長や首脳として話す場合（"The President (…)"）…を拾えない。…誤って帰属した可能性は低い」。
- (i) 議長として話す日本の自国発言: 日本が議長国のとき（2006 年 10 月、2009 年 2 月、2010 年 4 月、2016 年 7 月、2017 年 12 月、2023 年 1 月）、国別の発言は見出しが "The President:" で、直後に "I shall now make a statement in my capacity as the representative of Japan." と続く。見出しは "The President (Japan):" ではなく、"The President:" なので、踏み跡の注意書きの形も外れている（この形の見出し "The President (Japan)" は un-docs に 0 件）。この区間に human security が出る文書: S/PV.5556 (Resumption 1)（2006-10-26、5 出現。基金 1999 年設立と "over 160 projects"）、S/PV.6080（2009-02-09、1）、S/PV.6302（2010-04-27、1）、S/PV.8129（2017-12-08、1）、S/PV.8144（2017-12-20、4。"the human security approach is highly relevant…"）、S/PV.9237（2023-01-09、1）、S/PV.9238（2023-01-10、2）、S/PV.9241（2023-01-12、外務大臣、1）、S/PV.9247（2023-01-24、1）。9 文書・約 17 出現。区間は次の見出しまでで見積もったので、S/PV.6080、6302、9238 は区間の終わりが曖昧（本文を読んで S/PV.5556 R1、8144、6302、9238 は日本の発言と確認）。
- (ii) 見出しの正規表現の取りこぼし: A/74/PV.41（2019-12-09）の "Mr. Mori (Japan) (spoke in Japanese; English interpretation provided by the delegation):" は、括弧の長さ上限 60 字を超え（約 70 字）、判定されない。4 出現（森元首相の人間の安全保障基金・委員会の発言）。"English text provided by the delegation"（Kan）は収まるので拾われる。
- 影響: 日本の議長国期（特に 2017 年 12 月、2023 年 1 月）の発言が欠け、2017〜2020 と 2021〜2023 の「発言の数」「ネクサス」「保健」などの表の値、「2023 年の安保理での発言（Ishikane 氏と Shino 氏が中心）」にも抜けがある。
- 誤帰属（他国の発言を日本にした）ではなく、見落とし（過少）の向き。

D2. 引用の記号に "(Resumption n)" が落ちている。S/PV.4049 (R3)、4087 (R1)、4176 (R1)、4646 (R1)、4877 (R1)、4990 (R1)、5100 (R1)、5766 (R1)、5898 (R1。ここだけ本文中で付いている)、6587 (R1)、9036 (R1)、9158 (R1) の 12 件。公式の `https://docs.un.org/en/S/PV.4176` は再開会合ではなく最初の部分に当たり、日本の発言はそこにない（S/PV.4176 の最初の部分では human security の最初の出現は事務次長の発言）。引用どおりに公式を開くと確かめられない。

D3. 「S/PV.6114、6341では、メキシコと共に共同議長を務めていると述べた」: 共同議長（co-chairs of the Friends of Human Security）と述べたのは S/PV.6341（Takasu）だけ。S/PV.6114（2009-04-29）は "together with Mexico, we are promoting the Friends of Human Security" で、共同議長とは言っていない。

D4. 「基金（Trust Fund）は 36 文書、2007〜2010 年は 17 文書」: 再現できる式が一致しない。`trust fund` 全体は 44 文書（2007〜2010 は 18）、`trust fund for human security` は 34（同 17）、`trust fund for human` は 35（同 17）。36 になる式は見つからなかった。「2017 年以降は数文書」は 2 文書（S/PV.8241、S/PV.9346）で、「数文書」より少ない。

D5. 「基金の言及の減少と、「アプローチ」「視点」「レンズ」という言い方の増加が同時に見える」: 増加は再現できない。human security の 60 字以内に approach/perspective/lens/viewpoint がある発言の割合は、1999〜2002: 12%、2003〜06: 18%、2007〜10: 55%、2011〜16: 25%、2017〜20: 40%、2021〜23: 20%。最大は 2007〜2010。"lens" は 1 文書（S/PV.8699）。時系列の主張としては支えられない（表現の式を決めて表を付けるべき）。

D6. 「Takasu 30、Ishikane 21、Haraguchi 18、Shino 10、Oshima 8」: Oshima は、"(spoke in French)" 付きの 2 件を含めると 10（素の見出しだけだと 8）。Osuga は 9（素の見出し 7）。数え方が人ごとに揃っていない。見出し全体で数えると Oshima 10、Shino 10、Osuga 9。

D7. 参考（誤りではないが注意）: 冒頭の「定義」は「1999 年から 2023 年まで一貫して」と書くが、2007〜2010 年は「保護とエンパワーメント」の定式が最多で、2011 年以降は発言の型が変わる（上の D5）。「一貫して」は強すぎる。

### agency の踏み跡

A1. S/PV.9241 (Resumption 1)（2023-01-12）の当たりは、女性・青年・個人の行為主体性ではない。本文は Australia の発言 "the agency and leadership of regional institutions, such as the Pacific Islands Forum and ASEAN, are respected"（地域機関の自律性）。表では「そのほかの主題別（法の支配）」に入れ、本文の「読み取れること」（ジェンダーと青年に集中）の反例にもなっているが、記述されていない。「行為主体性の用法」としても、人の行為主体性（agency of persons）とは別の意味（機関・主体の自律）であり、51 に含めるなら区別して書く。誤判定ではなく、分類軸の欠落。

A2. S/2020/727（2020-07-21）を「主題は未確認（本文の語から保健・差別への対応と読める）」としているが、書簡の冒頭（"copy of the briefings provided by Ms. Pramila Patten, SRSG on Sexual Violence in Conflict; Ms. Angelina Jolie; Ms. Khin Ohmar … on behalf of NGO Working Group on Women, Peace and Security…"）から、紛争関連の性暴力・女性・平和・安全保障の討論の記録と読める。同種の S/2021/375（Patten、Mukwege 氏。TSV は紛争関連の性暴力）と同じ扱いにすべき。本文の「書簡 5 件」の保健の列は誤り。

A3. 年別（2019: 4、2022: 12、2023: 10）は、A/RES の日付に un-docs の date_kind=distributed（配布日）を使っているため、年がずれる。A/RES/73/153・73/147・73/195 は 2018-12-17〜19 採択で 2019 年とされ、A/RES/77/202・77/211 は 2022-12-15 採択で 2023 年とされている（本文の "adopted by the General Assembly on…" の行で確認）。採択日で数え直すと 2018 は 4→7、2019 は 4→1、2022 は 12→14、2023 は 10→8。年の山や「2022〜2023 年の件数」の議論は、この点に注意が要る（踏み跡は「同じ定型の一文が決議と報告の両方に出て件数を押し上げる」とは書くが、日付の種類には触れていない）。

A4. A/RES/77/211 と A/77/463/Add.2 の主題を「人権（デジタル環境の児童の権利）」としているが、決議の題名は "The right to privacy in the digital age"（議題 68(b)）。当たりは "the importance of privacy to children's agency, dignity and safety" の前文 1 か所で、児童の権利の決議ではない。題名で書くべき。A/RES/73/195 は「Global Compact for Safe, Orderly and Regular Migration」の承認の附属書の文で、76/266 は「Progress Declaration of the International Migration Review Forum」。同じ決議の繰り返しではなく、"independence, agency and leadership" の定型句が文書をまたいで引き継がれたもの（本文の「同じ定型の一文」は句としては正しいが、「決議」の連続としては正確でない）。

A5. 分母の不在の影響（本文は「分母を数えていない」と断っているが、効果を示せるので記録）: 単位が「文書」で、1 文書の 1 出現（S/PV.7857 は 524,000 字の会合で 1 出現、S/PV.8403 は 1 出現）でも 1 件に数えるため、会合の種類の「18 件」は議論の厚みを表さない。参考に un-docs で数えた概算: 2008 年以降の S/PV 3,764 文書のうち 18（0.5%）。議題が "Women and peace and security" の冒頭 5,000 字内にある S/PV は 72 文書で 10 が当たり（14%、粗い判定）。つまり WPS では当たりは約 14%、全会合では約 0.5% で、WPS への集中（濃縮）は数字で支えられる一方、WPS の会合の 86% は当たりなし。「ジェンダーと青年に集中」は定性的には妥当だが、「集中」は分母を置いて初めて言える。

A6. 会合の種類の分類の構造的な歪み: COVID-19 期のビデオ会議の記録は S/PV の逐語録ではなく「議長の書簡 S/2020/…」として配布される。S/2020/346（青年）、S/2020/727（性暴力）、S/2020/1084（WPS 20 周年）、S/2021/375（性暴力）は、実質は安保理の公開討論の記録で、「会合」ではなく「書簡」に入っている。2020〜2021 年の S/PV は 85 と 165 文書しかない。このため「安保理の会合 18」と「書簡 5」の区別、特に 2020〜2021 年の分布は記録形式の違いで決まっている。

A7. 二重計上と同一会合の分割: S/PV.9158 とその再開会合（同じ会合の二分冊）は 2 件に数えている（実質 1 会合）。決議の草案（A/77/L.77、L.81）と採択後の決議（A/RES/77/300、77/317）、決議と第三委員会報告（A/77/456 と A/RES/77/196 など）が別件に数えられている。19 件の「決議・決議案・報告」は、実質では約 10 の別個の決議（系列）。本文はこの点を一部書いている（決議と報告の両方）が、草案と決議の二重は書いていない。

## (3) 再現できなかった主張

- 日本の踏み跡: 主題語の表の個々の値（式が書かれていない。緩い式で ±3 程度の差。完全一致は不可）、「基金は 36 文書」（D4）、「アプローチ・視点・レンズの増加」（D5）。
- 日本の踏み跡: 「185 発言のうち、語の周辺を全件読んだ」は、レビューでは検証できない（本人の作業記録のため）。読んだ範囲外に D2、D3 のような引用のずれがあることから、全件読了の記述は強すぎる可能性がある。
- 公式 PDF との照合は、本レビューで次を行った: S/PV.7247、5898 R1、5264、A/67/PV.23、A/64/PV.107、S/PV.8234、7527、5703、6389、4176 R1、5834、7289、4577、3980、8241（見出しと該当文の両方、15 件）。S/PV.4646 R1、A/74/PV.41、S/PV.8144、5556 R1 などは un-docs のみ（公式は照合せず）。公式との不一致は見つからなかった。
- agency: 「語の周辺の文は、各文書の最初の出現だけを読んだ」（本文の注）は、レビューでは検証できない。A1 のように、最初の出現が人の行為主体性でない例がある（S/PV.9241 R1 の最初の出現は地域機関）。

## (4) 直し方の提案

日本の踏み跡
1. 範囲注記と「確かめた度合い」を直す。"見出し判定は議長の自国発言を拾えない" は、実際の形を書く（見出しは "The President:" で、直後に "in my capacity as the representative of Japan"）。この区間を足すか、少なくとも日本が議長国だった月（2006-10、2009-02、2010-04、2016-07、2017-12、2023-01）を別枠で数える。
2. scripts/speaker_counts.py の HDR の括弧の上限（60 字）を 200 字に上げる（A/74/PV.41 の Mori が拾える。loose.py で試して、追加は A/74/PV.41 のみ）。議長の自国発言用に「"The President:" の直後に 'capacity as … representative of Japan' がある区間」を別途判定する。直したら 185/361 を更新（概算で 195 文書・約 382 出現）し、TSV を作り直す。
3. 引用の記号に (Resumption n) を戻す（D2 の 12 件）。公式の URL は `https://docs.un.org/en/S/PV.4176(Resumption1)` 形式で開く。
4. S/PV.6114 の「共同議長」を「メキシコと共にフレンズを推進」に直す（D3）。
5. 基金の文書数は、式を書いて数え直す（例: `(?i)trust fund for human` なら 35、2007〜2010 は 17）。主題語の表は、各行の式を checks/ に書く。
6. 「アプローチ・視点・レンズの増加」の一文は、表を付けるか削る（D5）。「一貫して」を、時期ごとの強調の違いを入れた書き方に直す。
7. 話者の件数は、素の見出しか、変種を含めるかを決めて揃える（D6）。

agency の踏み跡
1. S/2020/727 の主題を「紛争関連の性暴力・WPS」に直し、書簡の列から「保健」を除く（A2）。TSV の「主題は未確認」も直す。
2. S/PV.9241 R1 の当たりが「地域機関の agency and leadership」であることを注記し、「人の行為主体性」と「機関・主体の自律」を分ける列を足す（A1）。
3. 年別は採択日（"adopted by the General Assembly on …"）で数え直すか、「配布日による」と明記する（A3）。
4. A/RES/77/211 と A/77/463/Add.2 の主題を決議の題名（デジタル時代のプライバシーの権利）にそろえる（A4）。移住の 3 件は「定型句の引き継ぎ」と書く。
5. 分母: WPS（および性暴力、青年）の会合の総数を、議題の見出しで数えて、当たりの割合を表にする（概算は A5。粗い判定なので、議題の見出しの抽出式を決める）。単位を「文書」でなく「1 会合・1 決議系列」に揃える（A7）。
6. COVID 期の議長書簡の 4 件は「会合の記録（書簡形式）」と注記し、2020〜2021 年の会合の種類の集計を分けて読めるようにする（A6）。
7. 「最初の出現だけ読んだ」限界を、判定の根拠として、少なくとも全 51 件の当たりの文を 1 行ずつ TSV に残す列（根拠の句）を足す（レビューで 17 件を読んだ範囲で、機関の意味は 0 件、人以外の主体は 1 件）。
