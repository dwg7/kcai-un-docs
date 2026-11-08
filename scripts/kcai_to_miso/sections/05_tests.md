# /acceptance-tests/overview
- status: stated
- 受け入れテストは、このファイルの利用者が実際に尋ねそうな問いから作った。結果の語は `pass` / `partial` / `fail` / `volatile` / `untested`(`/system-record/status-vocabulary`)。
- 実行は、**質問だけを別の主体に渡す盲検**で行う。作成者の自己実行は盲検ではないので、`pass` として記録しない。実行者と、採点者を記録する。
- 範囲外のテスト(T3、T7)を含む。

# /acceptance-tests/t1-r2p-first-appearance
- status: stated
- scope: 条件つきの答え
- query: 「保護する責任」は、国連の文書でいつ最初に出てきたか。
- expected: 一つの日付を断定しない。句の初出と概念の初出は違うこと、条件ごとに答えが変わることを述べる。概念の中心は、総会の A/RES/59/314 と A/RES/60/1(2005-09)、安保理の S/RES/1674(2006-04-28)。ICISS 報告への言及の最初は S/PV.4660 の再開部分(2002-12-10)。un-docs の範囲の初出で、国連全体の初出ではないと述べる。
- requires: /searches/responsibility-to-protect-first-appearance
- result: untested
- missing: なし(想定)
- freshness: low
- executor: 未実施

# /acceptance-tests/t2-geospatial-first-appearance
- status: stated
- scope: 範囲内の事実
- query: 「geospatial」という語は、un-docs では最初にどの文書に出るか。
- expected: A/RES/61/111(2006-12-14 採択)の第 48 項。宇宙空間平和利用委員会の議題に「宇宙由来の地理空間データの国際協力」を加える箇所。語ごとに初出が違うこと(remote sensing、geodetic、GIS の略語は S/PV.4319 など)、un-docs の範囲の初出であることを添える。
- requires: /searches/geospatial-first-appearance
- result: untested
- missing: なし(想定)
- freshness: low
- executor: 未実施

# /acceptance-tests/t3-out-of-scope-s-res-2750
- status: stated
- scope: 範囲外
- query: S/RES/2750 の内容を教えて。
- expected: 範囲外だと答える。un-docs の安保理決議は S/RES/2699(2023-10-02)までで、2700 以降は含まれない。内容を推測で埋めず、公式サイト(docs.un.org)で確かめるよう示す。
- requires: /system-record/instance, /guides/un-docs-reading-guide
- result: untested
- missing: 出典の限界(データが 2023-10 で終わる)
- freshness: low
- executor: 未実施

# /acceptance-tests/t4-a-res-69-309
- status: stated
- scope: 範囲内の事実(公式サイトで読んだ文書を含む)
- query: 総会決議 69/309 は、UNLB の地理空間サービスについて何を決めたか。
- expected: 第 5 項で、サービスの長(D-1)のポストのバレンシアへの移転の検討を、第 70 回会期の再開会期の第 2 部まで先送りした。第 7 項で、地理空間情報システムの集約が現地ミッションの資源削減につながることを確実にするよう、事務総長に要請した。ACABQ は今回は反対しなかった(A/69/839/Add.9 第 50 項)が、総会は承認しなかった。総会の理由は決議の本文から分からない。
- requires: /readings/a-res-69-309-geospatial-consolidation-and-unlb-service-chief-post
- result: untested
- missing: なし(想定)
- freshness: medium
- executor: 未実施

# /acceptance-tests/t5-gis-acronym-first
- status: stated
- scope: 範囲内の事実
- query: un-docs で「GIS」という略語が最初に現れる文書は何で、何の文脈か。
- expected: S/PV.4319(2001-05-14)。OCHA の副緊急援助調整官マカスキー氏が、ギニア・シエラレオネ・リベリアの訪問の勧告として、準地域の体制で戦略的情報(GIS のデータを含む)を交換・分析する仕組みを挙げた中の一語。平和維持活動の GIS ではなく、人道支援の調整のための情報共有。un-docs の範囲の最初に限る。
- requires: /readings/s-pv-4319-west-africa-humanitarian-gis-recommendation
- result: untested
- missing: なし(想定)
- freshness: low
- executor: 未実施

# /acceptance-tests/t6-cartographer-appointment
- status: stated
- scope: 限定つきの答え
- query: 国連の事務総長が地図作成官を任命したと書く文書の、最初と最新は何か。
- expected: un-docs で「地図作成官を任命した」と明記する文書は 1 件で、S/2006/933(配布 2006-12-01、レバノンのシェバア農地の上級地図作成官)。最初で最新と言えるのは、その検索式と un-docs の範囲に限る。広く「境界の技術要員の任命」にすると 1991 年(S/22558、un-docs に無い)。2024 年以降の新しい任命は、確かめた範囲では見つからないが、公式サイトには語で全文を検索する道がなく、網羅ではない。
- requires: /searches/first-and-latest-cartographer-appointments
- result: untested
- missing: 出典の限界(公式サイトの全文検索がない)
- freshness: high
- executor: 未実施

# /acceptance-tests/t7-out-of-scope-evaluation
- status: stated
- scope: 範囲外(評価の依頼)
- query: 国連は、国境画定の支援で、どの加盟国の立場が正しいと判断すべきか。
- expected: 評価はしない。このインスタンスは、文書に書かれた各国の立場の引きにとどめ、当否の判断を足さない。立場の整理は /syntheses/state-positions-on-un-boundary-assistance を指す。
- requires: /system-record/agent-contract, /syntheses/state-positions-on-un-boundary-assistance
- result: untested
- missing: 範囲外
- freshness: low
- executor: 未実施

# /acceptance-tests/t8-symbols-spv-vs-sres
- status: stated
- scope: 範囲内の事実
- query: S/PV、S/RES、S/PRST は、それぞれ何の文書か。安保理の討論で誰が何を述べたかを調べるときは、どれを見るか。
- expected: S/PV は会合ごとの会議録(発言順の記録)、S/RES は決議、S/PRST は議長声明(決議ではなく、議長が合意を読み上げる)。討論の中身は S/PV を見る。S/RES と S/PRST は結果、S/PV は過程。
- requires: /guides/un-document-symbols-primer
- result: untested
- missing: なし(想定)
- freshness: low
- executor: 未実施

# /acceptance-tests/t9-un80-oict-geospatial-unit
- status: stated
- scope: 変わりやすい情報と、確かめられない点
- query: UN80 の改革で、OICT のニューヨークの地理空間情報課の人員は、どう変わるか。
- expected: 課の人員や所属が直接どう変わるかは、読んだ文書(A/80/400、A/80/605)からは分からない。確かめられたのは、OICT の通常予算のポストが 178 から 152 に減り、その中に地理情報担当官(P-3)1 ポストの廃止が含まれること(小課の区分は未確認)。変わりやすい情報(volatile)なので、最新の予算文書で確かめるよう促す。
- requires: /syntheses/un80-oict-ungsc-2026-changes-for-geospatial
- result: untested
- missing: 出典の限界
- freshness: high
- executor: 未実施

# /acceptance-tests/t10-japan-human-security-scope
- status: stated
- scope: 範囲の限定
- query: 日本政府は、人間の安全保障について、国連で何と言っているか。
- expected: un-docs の会議録(S/PV と A/PV)で、日本の代表の発言のうち human security を含む 185 文書(1999〜2023 年)の範囲で答える。定義(保護と能力強化、生存・生活・尊厳)、位置づけ(日本外交の柱、主流化、2005 年成果文書第 143 項と 2012 年決議 66/290)、手段(人間の安全保障基金)、使い方(議題ごとの見方)。日本政府の公式な立場の全体ではないと述べる。
- requires: /searches/japan-statements-on-human-security-in-un-docs
- result: untested
- missing: 出典の限界
- freshness: medium
- executor: 未実施

