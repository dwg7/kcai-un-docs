# 未完了の課題と、先送りしたレビュー（2026-10-26 時点）

クレジットの残りが少なくなったため、新規の調査を止め、いま書けている内容を `draft` のまま保存した。次の担当者（人または AI）が、この一覧から続ける。各項目は hfu の依頼の原文に近い形で書く。

## A. 依頼済みで、書きかけまたは未着手のもの

1. **2001 年の OCHA 準地域提案（S/PV.4319）のその後の実装**: 何が成功し、何が残り、何が失敗し、何が残らなかったか。実装パターンが生まれたか。（担当の成果は `knowledge/west-africa-2001-proposal-implementation-*.md`。無ければ未着手）
2. **SAGE まわり**: (a) 安保理で SAGE 由来のデータをめぐってどのような議論が行われたか（`sage-in-security-council-discussions`）、(b) 誰が SAGE にアクセスするか、メインフレーム化の仮説（`sage-access-and-who-sees-it`）、(c) SAGE と Unite Aware の関係を公式文書で確認し、何が違うと説明されているか、(d) dwg7 のラジオシリーズとの関連。S/2021/501（オランダの発言と Unite Aware の開始）の中身の確認。
3. **衛星画像の S/PV 個別の踏み跡**: `satellite-imagery-in-security-council-who-and-why` の型 1〜6 の会合ごと。各国が提示した具体的な情報内容の深掘り（ロシア 6、米国 3、英国 2…の内訳）。読み残した会合は各踏み跡の「確かめた度合い」を見る。
4. **地図課（Cartographic Section）の改称と S/PV.4310**: A/RES/69/308 の改称の背景・理由。S/PV.4310（2001-04-19）が Chief Cartographer／Cartographic Unit／Cartographic Section について何を言うか、任務付与の明文化。
5. **地図課／UNGIS／UNGSC の関係の変遷**を 1 本にまとめる（2007〜2009 年のブリンディジの GIS センターがニューヨークの地図課長の指示を受けていた件を含む）。
6. **UNLB の「地理情報システムセンター」設置提案に総会が 2006 年に留意した件**: 誰が提案したか（事務総長か。起草した部局は）、特定の加盟国の支持の明記、留意の着眼点。
7. **A/63/824 付録第 11 項**: UNGSC の当初のコンセプト。
8. **A/RES/69/309**（現地ミッションの GIS 資源が減ることを確実にする要請。UNLB の「Service for Geospatial, Information and Telecommunications Technologies」の長のポストの移転の検討を先送りした決議の留保事項）、**A/RES/70/288、72/287、73/310** をそれぞれ深掘り（各 1 本）。
9. **権威性の仮説**: A/RES/66/288（2012 年）の段階に比べ、地理空間情報の権威性は国連で低下しているように見える。そのメカニズムの推測と un-docs での個別の裏取り。
10. **日本、韓国、イタリア、フィンランド、米国**が地理空間情報の議題で言及した踏み跡（UN Open GIS Initiative との関係の確認を含む）。
11. **個別文書の踏み跡**: S/2018/945（Barkhane 部隊と MINUSMA、geospatial intelligence の合同作業部会。前身の「G5 サヘル」「地理空間情報」の誤りを正す）、S/2019/319、S/2019/787、S/2020/938、S/2020/952、S/2021/843、S/2021/1110、S/2023/3、S/PV.9039（ブチャの件は別の踏み跡）。
12. **MGRS／UTM**: 済み（`coordinate-grids-mgrs-utm-in-un-docs`、`un-operational-coordinate-formats`）。MGRS は un-docs に無く、運用文書の多くは 403 で届かなかった。届かなかった先の一覧は各 `checks/` を見る。
13. **国境画定への国連実務官の関与の推移、最初と最新の地図作成官の任命**: 済み（`boundary-demarcation-un-cartographer-involvement-timeline`、`first-and-latest-cartographer-appointments`、`state-positions-on-un-boundary-assistance`）。

## B. 先送りした独立レビュー（クレジットが戻ったら実施）

- 2026-10-26 午後に作った踏み跡のすべて（`s-pv-*`、`satellite-imagery-substitute-for-access-s-pv-readings`、`boundary-*`、`first-and-latest-*`、`state-positions-*`、`un-operational-coordinate-formats`、`coordinate-grids-*`、`un-document-symbols-primer`、`sage-*` の新規分、上の A の成果）。
- 過去のレビューで多かった誤り: 発言者の取り違え、同じ会合の別記号（(Resumption 1)）の混同、日付欄の誤り、綴り違い（geographic/geographical）、「未確認」と書いたが公式文書に理由があった例、推測の事実化。レビューはこれらを重点的に見る。
- 既存の踏み跡に反映すべき訂正: `satellite-imagery-in-security-council-who-and-why` の型 1 の発言者（S/PV.7932・8137 は事務総長、8353 は政務担当事務次長、IAEA 事務局長本人は 8500 だけ。4692 は IAEA のエルバラダイ事務局長。4707 は UNMOVIC の Blix 委員長）、`un-geospatial-organization-timeline` にレバノンのシェバア農地の地図作成官（S/2006/933）以外の境界画定の事例への参照、`un-docs-reading-guide` の「+478」は `S/<通し番号>`（1993 年までの形）の行数。

## C. そのほかの未着手

- C2「投票で賛成が多い決議」の抽出式の作り直し。
- ブランチ削除（`claude/bootstrap-un-docs`、`hfu/kcai-yuiseki-datasets` の `claude/youthful-goldberg-tq7dzs`）は、ここからはできない。GitHub の画面から hfu が行う。
- 届かなかった先（403 など）は回避していない。FOSS4G の要旨、UN Open GIS の公式サイト、peacekeeping.un.org、media.defense.gov（UNIBAM）、mineaction.org（平和維持活動の指針）、unowas.unmissions.org、www.un.org/geospatial/、E/RES/2011/24 の PDF。hfu が別の経路で取得できるなら、`handoffs/` に置く。

## D. 担当の最終報告から（記録。まだ踏み跡に反映していない訂正と所見）

### 衛星画像の S/PV（告発・平和維持の担当。10 本と横断の `satellite-imagery-claims-by-state-in-s-pv`）
- 23 会合を発言者の見出しで読み直し、公式の PDF と衛星の語の件数が全会合で一致した。
- ロシア 6 件は、自国の画像を示した例がなく、米国の画像の開示要求 3、英国が引いた画像への疑義 1、一般的な言及 2。画像を画面に映したのは S/PV.4701 のみ。場所・日付・公表元まで述べたのは 4701、7154、7253、9042、9436 の 5 会合。
- `satellite-imagery-in-security-council-who-and-why` に反映すべき訂正: S/PV.4707 の発言者は Blix 氏（UNMOVIC 委員長）。S/PV.7253 は米国のほか英国も述べた（議長を務めた英国代表の発言に NATO 公表の 8 月 21・23 日の画像）。英国は 7154、7253、9039 の 3 会合。「不明 1」はおそらく S/PV.9011 のゼレンスキー大統領（確証なし）。S/PV.6151 の衛星の語は `S/PV.6151 (Resumption 1)` の側にある。S/PV.6790 の発言者は加盟国でなく OHCHR の事務次長補、7391 は OSCE の議長、7395 と 7683 は監視団の長。
- 重複: `s-pv-6151-georgia-unosat-village-destruction` と `s-pv-6151-resumption-1-georgia-unosat-images` は内容が重なる。統合か整理が要る。
- 読まなかった会合（45）: 人権・人道 6201、7394、7418、7950、8133、8589、8609、9126。行方不明者 8531、8543、8606、8676、8975、9145、9253。査察 4714、5710。国境画定 4744、5956、6079。化学兵器 7269、8090、8785、9255。環境ほか 4194、8119、8906、9345、9381、9392。（ほかに、別の担当が読んだ分は各踏み跡を見る。）
- 会議録の外（ニューヨーク・タイムズ、JIT、CSIS、UNOSAT の報告）は未確認。

### IAEA・調査委員会の S/PV（8 会合）
- 述べたのは事務局の職員、機関の長、国連の機関の報告を引いた加盟国で、自国の画像を示した加盟国はいない。画像の撮影者・時期・解像度を述べた会合は無い。慎重な言い方（signatures consistent with、alleged、where possible）が目立つ。仮の整理で、安保理全体の傾向とは言えない。
- 未確認: A/HRC/25/CRP.1 の本文、IAEA 事務局長の報告（GOV/…）、S/PV.8500 のプレス声明の文言。

### 国境画定
- un-docs で地図作成官の「任命」を明記するのは S/2006/933（レバノン、シェバア農地）の 1 件。広く「国境の専門家の任命」なら S/22558（1991-05-02、un-docs に無い）が最初。2024 年以降の任命は確かめた範囲で見つからず（公式サイトに全文検索なし）。
- カメルーン・ナイジェリア混合委員会への国連の支援チームは継続中（最新は S/2025/864、2025-12-26）。
- 未解決: 1991〜93 年の主要文書（S/22558、S/24113、S/25811）は un-docs に無い。シェバア農地の 2007 年以降の成果と氏名。越境資源（石油、水）への国連実務官の関与の事例は un-docs で見つからず。総会（A/PV）の関連発言は系統的に探していない。

### MGRS／UTM
- un-docs に `MGRS`、military grid、WGS 84 は 0 件。`UTM` は会社名と OCR の崩れ。座標は座標系の名前なしに本文中の数値で現れる（度分秒、`map reference` の数字、「座標が合意された」の記述）。
- 国連の公開の運用文書（MPKI Handbook など）に MGRS の語は無い。軍事監視員の報告様式に「grid reference」の欄がある（格子の名前なし）。UNOSAT の地図は UTM Zone 36N を示す。
- 「MGRS が使われている可能性が高い」とする根拠（IMSMA、UNIBAM）は検索結果の要約だけで、本文は未取得。media.defense.gov（UNIBAM）、mineaction.org、mwiki.gichd.org は届かなかった。

### 行方不明者・国連の機関の S/PV（7 本と総括 `satellite-imagery-sessions-two-patterns-synthesis`）
- イラク・クウェートの行方不明者の会合（2018〜2021 年）で、UNAMI の特別代表とクウェートが画像に触れたのは各 1〜2 文。国と場所は決議 2107 (2013) 第 4 項に基づく事務総長報告（S/2018/683、S/2018/976、S/2019/632、S/2020/358）に出る。国連側の役割は、国連グローバル・サービスセンター（ブリンディジ）に画像の有無を問い合わせたこと（1990〜93 年の画像は無いとの回答）と、地中レーダーの研修。画像の分析は赤十字国際委員会。S/PRST/2019/1 は、フランス・英国・米国が ICRC に提供した情報を歓迎した。8 会合のどれも決定は出していない。
- S/PV.6151 と S/PV.7196 は加盟国の言及。ジョージアは UNOSAT の画像を「数十の村」としてだけ引き、ロシアの返答は触れていない。イタリアの 7196 の文は事業の記述で、成果は述べていない。
- `satellite-imagery-in-security-council-who-and-why` に反映すべき訂正: S/PV.6151 は (Resumption 1) の行だけが衛星の語に当たる（本体は 0 件）。S/PV.8906 は未確認。S/PV.8324 は「呼びかけ」でなく、呼びかけに応答があったという報告。S/PV.8910 の声明が述べるのは埋葬地の特定でなく 19 人の身元特定。S/PV.7196 は「確認している」でなく、事業が衛星画像を使って履行を確認すると述べる記述。検索式のメモ（空白をそのまま書いた式は 62 件、`\s+` は 68 件）。
- 読まなかった会合: S/PV.8531、8543、8606、8676、8975、9145、9253。S/PV.8589（2019-07-30、Lowcock 氏が UNOSAT のイドリブの比較を示した。型 5 の候補）の反応は未読。
- 届かなかった先: unosat.org（スクリプトの殻のみ）。documents.un.org は `S/PV.6151(Resumption1)`（空白なし）の記号なら取得できる。

### A/RES/69/309 の踏み跡（`a-res-69-309-geospatial-consolidation-and-unlb-service-chief-post`）
- 決議第 5 項は、技術サービス部長（D-1）のポストをバレンシアへ移す件の検討の先送りで、却下ではない。ACABQ（A/69/839/Add.9 第 50 項）は今回は移転に反対しないと書いていた。総会は第 4 項で、2 か所配置の包括的研究を再度求めた。
- 第 7 項は、集約の結果として現場ミッションの資源が減ることを確実にし、次の UNLB 報告で報告するよう求めた。ACABQ 第 44 項は現場の約 80% を遠隔化し、19 ポスト・職を廃止すると見込んでいた。決議第 7 項は ACABQ「第 46 項」を引くが、資源削減の期待を述べる文は第 47 項にある（項番号のずれ）。
- 未着手: A/RES/70/288、72/287、73/310 の各踏み跡（公式 PDF はスクラッチに取得済みだったが、リポジトリにはない。再取得は `scripts/official.py`）。権威性の仮説の踏み跡 `geospatial-authority-since-a-res-66-288-hypotheses`（定義、指標、個別の裏取りとも）。69/309 の未確認: A/69/733/Rev.1 の提案本体、第五委員会の審議（A/C.5/69/SR）、67/288 第 5 項、第 70 会期での移転のその後。

### 個別文書（S/2018/945、S/2019/319、S/2019/787、S/2020/938）
- S/2018/945 は事務総長の書簡（2018-10-19 付、配布 10-25。S/RES/2295 にもとづく）で、中身はフランス代表部の口上書（10-12 付、原文仏語）と Barkhane の報告第 21 号（期間 2018-06-01〜09-01、S/RES/2423 の第 41・53・70 項にもとづく。参照に DPKO とフランス軍事省の 2015-03-26 の技術的取決め）。地理空間は「情報」節の 1 文で、合同作業部会の計画があるとだけ書き、相手方・時期は無い。G5 サヘルは調整会合の出席者として出るだけ。
- S/2019/319（UNISFA、第 53 項）は設備保守の文脈のサービス名で、GIS 分析ではない。S/2019/787 は第 25 項（EU 支援で導入中）と第 52 項（JMAC の手順）、S/2020/938 は第 22 項（拡充）。3 本とも事務総長報告。
- 既存の踏み跡の訂正: un-docs の S/2018/945 の日付欄 2018-06-28 は誤り（S/RES/2423 の採択日）。`un-mission-gis-mentions-in-un-docs` の表も同じ日付。同表の MINURSO「のち米国も」は S/2020/938 第 22 項では確認できない（本文は「他の高解像度の衛星画像」）。
- 未着手: S/2020/952、S/2021/843、S/2021/1110、S/2023/3、S/PV.9039（geospatial の語の位置）の個別の踏み跡（担当が未完の場合）。S/RES/2423・2100 の該当項、フランス軍の他の号の報告、同時期の MINUSMA 報告、技術取決めの中身。

### 個別文書（S/2020/952、S/2021/843、S/2021/1110、S/2023/3、S/PV.9039）— 5 本作成済み
- S/2021/1110 は SAGE を第 23 項の 1 文だけで名指す。第 III 節 C「民間人の活動の管理」の冒頭近くにあり、件数 989→343 への但し書き。図・表・出典表記はない。S/2020/952 は `geospatial` 1 件（第 39 項）。S/2021/843 は 1 件（第 32 項、EU と米国の二国間支援による画像）。S/2023/3 は SAGE も `geospatial` も無く、行方不明者委員会の Web 型 GIS の 1 文のみ。S/PV.9039 は `geospatial` が 0 件で、ディカルロ氏が `geographic information system` に触れ、インドが Unite Aware を挙げた。
- 修正点: `sage-situational-awareness-geospatial-enterprise` の「見直しが差の一因かもしれない」は、原文の "may partly explain"（一部）より強い。
- 未完了: 同種報告との比較（S/2019/787、S/2020/938、S/2020/476、S/2021/635、S/2022/533 は読んでいない）。S/2020/952 の後半、S/2021/843 の第 59 項、S/2023/3 の第 50〜51 項は流し読みで未確認。S/PV.9039 と S/PV.8838 などの同種会合の比較。

### UNLB の GIS センター提案（`unlb-gis-centre-proposal-2006-origin-and-considerations`）と A/63/824（`a-63-824-annex-iii-para-11-gis-centre-direction`）
- 2006 年: 決議 60/267 第 3 項は GIS センターの提案に「留意」しただけ（承認は 61/277 の P-4 センター長ほか）。提案は事務総長報告 A/60/715 第 9〜10 項。起草部署は文面で特定できない（本文に DPKO が提案と書く箇所はある。課の特定は推測）。イタリアなど加盟国の支持の明記は読んだ文書に無い。
- ACABQ A/60/787 第 29・31 項は、費用便益分析と、現場・基地・本部の責任分担の明確化を要求。重複の懸念は 2007 年の A/61/852/Add.14 第 28〜31 項（DPKO は重複しないと説明、計画を要求、臨時の職を勧告）。
- **訂正**: A/63/824 は UNGSC の報告ではなく、UNLB の 2009/10 年度予算。附属書 III 第 11 項は「GIS センターは UNLB が管理し、指示はニューヨークの DFS の地図課長から」と述べる。UNGSC の当初のコンセプトは、この文書からは読めない。依頼 7（UNGSC の当初構想）は、別の文書（A/64/ の事務総長報告、決議 64/269、A/62/ の現場支援戦略）で調べ直す必要がある。
- 未着手: 上記の UNGSC 構想と ACABQ・加盟国の懸念、A/C.5/60/SR.65-66 と A/60/PV.92 のイタリアの発言、A/61/752 第 89〜93 項の通読、A/61/852/Add.14 第 32 項、61/277 で P-4 をポスト承認した理由、3 本目の踏み跡。

### S/PV.4310（`s-pv-4310-cartographic-section-and-chief-cartographer`）
- 「Chief Cartographer」と「Cartographic Unit」は S/PV.4310 に無い。地図課に触れるのは 2 か所で、ゲエノ事務次長の "the office of the Chief of the Cartographic Section" と、アニャビ事務次長補の "the Cartographic Section"。どちらも DPKO の職員の発言で、加盟国は触れていない。内容は、エチオピア・エリトリア国境委員会の後方支援費用を見積もるため、地図課長室の班がアスマラで現地調査中、という報告。任務の根拠として決議・報告の項を挙げる発言は無い。
- un-docs の件数: 「Chief Cartographer」は S/PRST/2000/21、S/PV.4160、S/INF/56 の 3 件。「Cartographic Unit」は S/PV.4227 の 1 件。「Cartographic Section」は 8 件。「Geospatial Information Section」は 4 件。
- 反映すべき訂正: `un-geospatial-organization-timeline` の 2001-04-19 の行は「未照合」でなく照合済み。役職名は "Chief of the Cartographic Section"。
- 未着手: A/RES/69/308 の改称の理由（決議本文、第五委員会報告、ACABQ 報告、事務総長の予算案）、`a-res-69-308-renaming-cartographic-section`、`cartographic-section-ungis-ungsc-relationship-evolution`、決議 1177/1298/1344、S/PV.4227、S/PV.4160、S/2000/1194、S/PRST/2000/21 の用例の年表。

### SAGE（`sage-in-security-council-discussions`、`sage-access-and-who-sees-it`、`sage-and-unite-aware-relationship`）
- un-docs では、SAGE は「技術名」「運用の説明」「報告の数字への注意」として出るだけで、安保理が SAGE のデータを議論した例は無い。「理事国が SAGE にアクセスしている」は支持も否定もできない。アクセス規則を述べた文書は読んだ範囲に無く、「閉じたシステム」は確かめられていない。
- 国連のファクトシート（2015 年ごろ。日付は PDF の属性のみ）は SAGE の想定利用者を JOC・JMAC・U2・U3・保安要員、共有先を「他ミッションと本部」と書く。特別委員会は A/71/19 第 53 項と A/72/19 第 52 項で SAGE と Open GIS を別々の取り組みとして並べただけで、両者の関係を述べる文書は無い。dwg7 のラジオシリーズの内容は与えられておらず、未確認。
- SAGE と Unite Aware: 置き換えを述べたのは S/PV.9389 の UNMISS 部隊司令官 1 人。A/78/726 第 158 項は「Unite Aware SAGE」と書く。A/79/788 第 185 項は Unite Aware の計画が「SAGE データベースを使って」事件を記録すると書く。2025 年の研修資料は「UA Sage」を Unite Aware の応用の一つとする。「可視化の層」という整理は文書に合わない。
- `sage-situational-awareness-geospatial-enterprise` に反映すべき訂正: S/2021/501 は S/PV ではなく議長（中国）の書簡。オランダの発言は付属文書 43 の書面声明。「Unite Aware を MINUSCA で始めた」は別の発言者（付属文書 2、運用支援局長）。インドの拠出 164 万ドルは付属文書 7。S/PV.9389 の発言者は「あるミッションの代表」でなく UNMISS の部隊司令官 Subramanian 中将（スイスの AI の質問への答え）。A/78/726 第 41・158・185 項、A/79/788 第 166・185 項、A/79/724 第 74 項を追記できる。
- 未着手: 2026/27 年度の予算案（A/80/…）と OICT の文書、S/2021/501 のビデオ会議の会議録の有無。届かなかった先: un.org/en/node/234607 ほか、oios.un.org/file/7754、peacekeeping.un.org の技術戦略の研究論文。

### 日本、韓国、イタリア、フィンランド、米国の言及（`member-state-statements-on-geospatial-japan-korea-italy-finland-us`）
- S/PV と A/PV の 184 文書（203 出現）を、見出し判定（`scripts/speaker_counts.py`）で分けた。国を特定できたのは 115 出現、特定できなかったのは 88 出現（67 文書）。
- 日本は A/59/PV.37（2004、地球観測サミット）の 1 文書。イタリアは 4 文書（国連の地図作成者への評価、UNITAR と衛星画像の事業など）。米国は 7 文書（衛星画像を証拠や支援として述べた発言）。韓国とフィンランドは 0。ほかの目立つ国（出現数）はロシア 8、シリア 5、インド 4、ウクライナ 4。
- UN Open GIS Initiative と各国の関係は調べていない（「未確認」。「無い」とは断定していない）。
- 未着手: 2 本目 `un-open-gis-initiative-member-state-links`（A/71/19 等、FOSS4G、公開ページ）。88 出現の発言者不明の内訳（議長が自国代表として述べた発言を含む）。A/RES の提案国、第五委員会、UN-GGIM と日本、ブリンディジ UNLB とイタリアの公式文書。公式 PDF との照合。A/59/PV.37 の議題名。
