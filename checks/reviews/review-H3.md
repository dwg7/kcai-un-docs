# review-H3: 抜き取り検証（un80-oict-ungsc-2026-changes-for-geospatial、un-open-gis-initiative-member-state-links）

検証日 2026-11-19。公式原文は scripts/official.py（pdftotext は -layout なし）で取得。取得物は scratchpad/c/、外部資料は scratchpad/ext/。
un-docs の pin 版（6cd1cf0）は取得し、sha256 が dd9edebc…ad54f5 で一致することを確かめた。

## (1) 確認できた主張

### un80 の踏み跡（原文照合 18 件）

1. **A/80/400 第 192 項(b)(iv) の文言**: 確認。(iv) は "Allocative efficiencies"。項目 d は "Open-source technology solutions will not be supported; instead, activities will focus on awareness building instead of supporting global challenges that foster the development of solutions"。踏み跡の訳と一致する。
2. **A/80/400 第 250 項**: 確認。2026-01-01 付で P-5（Senior Legal Officer）と P-4（Geographic Information Officer）の廃止を提案。緩和策は "redistribute the GIS workload among the remaining GIS officers"。
3. **OICT のポスト 178→152**: 確認（表 190）。P-5 16→15、P-4 23→18、P-3 35→33、一般職・現地職員 87→69、廃止 26。
   - 表 192 の内訳は P-5 1、P-4 5、P-3 2、GS(PL) 3、GS(OL) 15。
   - 支援勘定 55→50 も確認（表 191）。
4. **OICT の予算額**: 確認（表 188、第 192 項）。2025 年承認 5,538 万 9,600 ドル、2026 年当初提案 5,538 万 2,300 ドル、改訂 4,784 万 4,900 ドル。どちらと比べても 13.6% 減。
   - 第 192 項(a) の「12 ポストをバレンシア 6、バンコク 6 に移す」も確認。
5. **A/80/7/Add.9 第 VIII.88〜89**: 確認。第 VIII.88 が (b)(iv) を引いて "focus on awareness-building rather than opensource support" と書く。第 VIII.89 が "broad adoption of open-source systems was not foreseen due to cost, operational complexities and risks" と書く。
6. **A/80/7/Add.9 第 VIII.91**: 確認。バレンシアの Enterprise Data Centre は digital hub に指定済み。UNICEF、UNICC、IOM を収容。
   - 第 VIII.92（バレンシアは第 3 層データセンター、バンコクは ESCAP のサービスデスク）、第 VIII.87（"where feasible" の理由、第 2 段階は 2027 年）、第 VIII.97（OICT と ERP 課の統合の検討）、第 VIII.110（第 29C 款の承認勧告）も確認。
   - 第 VIII.87 の評価は "proposed abolishments do not clearly reflect a strategic approach to improve ICT management" で、踏み跡の要約と整合する。
   - 表 VIII.18 に "(1) P-3 Geographic Information Officer" が Abolishment として載る。位置は Subprogramme 2 付近と読めるが、抽出が崩れていて確定できない。踏み跡自身の「小課は未確認」という留保は妥当。
7. **A/RES/80/253**: 確認。2026-04-15 採択（配布は 2026-04-17）。第 9 項が digital hubs の設置に留意し、第 54 項（事務総長報告）の追加の拠点の選定基準を支持し、既存の ICT 基盤の周りへの集約を奨励する。"open source" は 0 件。
8. **A/80/605**:
   - 「地理空間・情報・電気通信技術サービス」のポストは承認 123→提案 121 で一致。内訳は廃止 3（バレンシア G-6 が 1、ブリンディジ G-5 が 2）と、G-7 の流入 1 による差し引き 2 減。
   - 第 92 項（地理情報担当官 FS-6 を P-2 に再分類）、第 65 項（UN Maps は Unite Aware と Unite field remote infrastructure monitoring を支え、20 を超える現場アプリを geoenable）、第 69 項（MONUSCO での遠隔地理空間サービスの試験）、第 73 項、第 94〜95 項（バレンシアは "critical digital technology hub"）、第 27 項（収入 1,880 万ドル）も確認。
   - 総予算 5,550 万ドル（前年 5,790 万ドルから 240 万ドル、4.2% 減）、21＋2 ポスト廃止、付属書 II の 136→452 ポストも確認。
   - 発行日は 27 January 2026 で、2026-03-16 に "Reissued for technical reasons"。踏み跡の「2026-03-16 再発行」は正しい。
9. **A/81/7**:
   - 第 VIII.82（5,253 万 7,300 ドル、5.3% 増）、第 VIII.89〜90（152 ポスト、再配置 8、移転 3、廃止 6 ポストの在職者の再配置、移転 7 ポストの費用 25 万 9,900 ドル）、第 VIII.91（空席 18、2 年以上が 5）、第 VIII.94（非ポスト 2,698 万 300 ドル、9.0% 増）を確認。
   - 第 VIII.96（GTA 2 件を 3 か月）、第 VIII.98（契約サービスの増加分を 5%、7 万 5,800 ドル削減）、第 VIII.86（統合の検討は 2028 年の提案へ）、第 VIII.87（100 超のデータセンター・サーバー室、4 機関の試験、2026 年末まで）も確認。
   - **第 VIII.105**: OICT は両方の利用者で、代替として "open-source tools where suitable" を検討。ACABQ は戦略的で持続可能な取り組みとベンダー・ロックインの回避を期待。第 VIII.85（UN Open Source Week と Mind the Open-Source Gap）、第 VIII.103（開放型・閉鎖型を指定しない）も確認。
10. **A/81/6 Sect.29C に open-source 語が 0 件**: 確認。正規表現 `(?i)open.?source|free software|FOSS` で 0 件。A/80/6 Sect.29C では表 29C.2 に "opensource" 表記を含む 4 件あり、年の欄は 2022 実績、2025 計画、2026 計画で踏み跡どおり（ページ画像で確認）。
    - 結果見出しの付け替え（A/80/6 の Result 1「革新的技術のパートナーシップ」→ A/81/6 の Result 1 は生成 AI、Result 3 は ICT 戦略の適用）も確認。
    - A/81/6 の "geographic" は目標(d)「standardized geographic information systems services」と、地理的移転の文の 2 か所のみ。A/80/6 は "geographic information systems services"（standardized なし）。
11. **データ**:
    - A/81/6 は 2026 年承認 4,987 万 4,900 ドル（表 29C.18）。
    - 2027 年の非ポスト増の内訳（障害者包摂 89.8 万、デジタル・ライブラリー 30 万、CRM と AI 11.95 万ドル）も確認。

### open-gis の踏み跡（照合 9 件）

1. **S/PV.7802（2016-11-07）**: 発言者は Mr. Oh Joon（Republic of Korea）で確認。"The Republic of Korea, in partnership with the Department of Field Support and Department of Peacekeeping Operations, is hosting the Third International Partnership for Technology in Peacekeeping Symposium this week in Seoul"。
2. **A/71/19 第 53 項と A/72/19 第 52 項**: 確認。どちらも国名を挙げない。正式名称は "United Nations Open Geographic Information System Initiative"。
3. **「Partnership for Technology in Peacekeeping」8 文書**: 再現。un-docs（pin 版）で 8 文書、記号も一致（S/PV.7802、8521、8534、8838、9181(RES1)、S/2021/501、732、868）。`open\s+GIS` は 0 件。
4. **ホスト国**: カザフスタン（S/PV.8521、8534、2019）と南アフリカ（S/2021/501、2022 年前半に開催予定）を確認。S/PV.8838 の韓国は閣僚級会合のホストで、India との MoU の発言も確認。
5. **FOSS4G 2025 の要旨**（WebSearch の結果）: "DWG 7"、"UN Smart Maps Group" が出る。ただし検索要約で、原文は未読。
6. **OSGeo メーリングリスト 2016-11**（原文を直接取得）: 次の点を確認。
   - 2016-11-07〜11 に Seoul City Hall で開催。主催は DFS とソウル市。
   - 貢献者は機関で、戦略委員会は貢献者 1 者 1 代表。共同議長は 3 人（UN 任命 1、選出 2）。
   - Spiral 1〜4 の長: Calamito（Boundless）、Brovelli、Hae Kyong Kang（Republic of Korea と明記）、Ki-Joune Li（Republic of Korea と明記）。
7. **OSGeo wiki**（原文を直接取得）: 創設期貢献者 GeoSHAPE（USA）、OpenGeo Suite（USA）、OpenGDS（Republic of Korea）、OSGeo、GeoForAll、GeoSDI（Italy）を確認。
   - Brindisi での 2016-03-05〜10 の会合も確認。
   - "Geoshape-Exchange, developed by Boundless and supported by US DoD" は wiki の記述どおり。
8. **UNVT 論文（ISPRS XLII-4/W14、全文）**: 確認。
   - 著者の所属に UN Geospatial Information Section、UNGSC ブリンディジ、OSGeo Foundation Japan Chapter、NARO、国土地理院が入る。
   - 2017 年に Spiral 4 内で開始。2018-12 の FOSS4G Asia 事前ワークショップで、基調講演でリリースを発表。
   - GSI は "As a partner ... prototyping its vector tiles"、NARO は農地区画のタイル、UNGSC の計算・ネットワーク基盤提供。
9. **2020 年の OICT スライド**（un-ggim-ap.org の PDF 全文）: 確認。
   - ハイブリッド GIS 試験: "Contributors: KRIHS/Korea, UNGIS, UNGSC, WFP"、2020-10〜2021-03。
   - UNVT: "Leading contributor: GSI Japan"、"pilot explore on DRR in Japan"。
   - 雲なし画像: "Initial funding: Finland"、"GISPO with Finnish partners"、試験場 UNISFA、2020-10〜2021-03。
   - 能力開発の PostGIS 講座はミラノ工科大学と協力。

## (2) 食い違い

| # | 該当文（踏み跡） | 正しい値 | 根拠 |
|---|---|---|---|
| D1 | un80「エンティティが運営するデータセンターとサーバー室の数の目標を、2026 年の 102 から 2027 年の 92 に減らす（図 29C.III）」 | 実績 102 は 2023、2024、2025 年（3 年とも）。計画は 2026 年も 2027 年も 92。「2026 年の 102」は誤り。 | A/81/6 Sect.29C 14/36 頁の図 29C.III（ページ画像で確認）。テキスト抽出では数値が並んでしまい読めない。 |
| D2 | un80 の時系列表「2025 年 10 月 A/80/400」 | A/80/400 の配布日は 2025-09-04（Distr.: General 4 September 2025）。 | A/80/400 の表紙。 |
| D3 | un80 の時系列表「2025 年 12 月 A/80/7/Add.9」 | 初版 2025-11-26、2025-12-12 に技術的理由で再発行（"Reissued for technical reasons"）。12 月は再発行の日付。 | A/80/7/Add.9 の表紙。 |
| D4 | un80「数値の食い違い」が未解明のまま（4,784 万と 4,987 万） | 下記 D4 の説明を参照。 | A/80/400 表 188、A/81/6 表 29C.13・29C.18、A/81/7 第 VIII.82・VIII.94。 |
| D5 | un80「ACABQ の評価（第 VIII.87 項）: OICT の措置は「…明確には示していない」」 | 評価の対象は OICT の措置全般でなく「提案された廃止（proposed abolishments）」。 | A/80/7/Add.9 第 VIII.87。 |
| D6 | un80「支援勘定は 6 か月分で 1,506 万 8,700 ドル」 | 第 192 項の本文は $15,068,900、表 189 は 15 068.7（千ドル）。原文の中で食い違っている。 | A/80/400 第 192 項と表 189。 |
| D7 | un80 の「確かめた度合い」の未確認に「A/80/6 の成果の表（どの年の欄か）」 | 確認できた（2022 実績、2025 計画、2026 計画）。本文の表と未確認の記述が内部で矛盾している。 | A/80/6 Sect.29C 表 29C.2。 |
| D8 | un80「A/81/7 第 VIII.93、VIII.96、VIII.98、VIII.100 項」を契約サービス 5% と GTA 3 か月の根拠として一括して挙げる | VIII.93 は「ポスト資源の承認勧告」で、削減とは別。5% 削減は VIII.98、GTA 3 か月は VIII.96、承認の結論は VIII.100。 | A/81/7。 |
| D9 | open-gis「S/PV.7802 で韓国代表が…シンポジウムをソウルで開くと述べた」 | 発言は "is hosting ... this week in Seoul"。すでに開催中の週。 | S/PV.7802。 |
| D10 | open-gis「国連現地支援局とソウル特別市が主催」と「韓国が現地支援局・平和維持活動局と共に開く」を並べる | 二つの資料で主催者の表現が違う。OSGeo 報告は DFS が主催でソウル市と協力、S/PV.7802 は韓国が主催国で DFS と DPKO と協力。踏み跡はそのまま並べており矛盾の指摘がない。 | OSGeo ML 2016-11 と S/PV.7802。 |
| D11 | open-gis 表の韓国「共同議長も務める」 | 正しいが、もう一人の共同議長 Juan Hurtado（GeoSHAPE、米国）を落としている。2020 年のスライドの共同議長は Ki-Joune Li、Maria Brovelli、Kyoung-Soo Eom。 | OSGeo wiki と 2020 年のスライド。 |
| D12 | open-gis「Brovelli 氏が能力開発の作業部会を率いる」をイタリアの強さに入れる | 原文は OSGeo と GeoForAll を代表して Spiral 2 を率いる。2020 年のスライドでは共同議長。 | OSGeo ML 2016-11 と 2020 年のスライド。 |
| D13 | open-gis の要点「un-docs の文書に一度も出ない（`Open GIS` は 0 件）」 | `Open GIS` は 0 件で再現するが、正式名 "Open Geographic Information System" で検索した記録がない。この語も un-docs で 0 件（`open\s+geographic\s+information`）だった。結論は変わらないが、検索語の表に載せるべき語。 | un-docs 検索。 |
| D14 | open-gis の A/71/19、A/72/19 を「特別委員会の報告」とし、年を 2016、2017 年とする書き方（本文は年を書かず） | A/71/19 は 2017 年の実質会期（2017-02-21〜03-17）、A/72/19 は 2018 年の会期。 | 両文書の表紙。 |

**D4: A/80/400 の改訂 4,784 万ドルと A/81/7 の 2026 年承認額 4,987 万ドルの関係。**
- 差は **203.0 万ドル**（49,874.9 − 47,844.9 = 2,030.0 千ドル）。
- 構成を A/80/400 表 188 と A/81/6 表 29C.13（2026 approved 列）で突き合わせると次のとおり。
  - 他の費目はすべて同額（契約サービス 14,819.6、一般運営費 6,769.1、備品 1,374.5、消耗品 65.0）。
  - ポスト費: 改訂 23,101.4 → 承認 25,111.5（＋2,010.1）。
  - その他職員費: 1,449.9 → 1,513.0（＋63.1）。
  - 旅費: 154.1 → 110.9（−43.2）。
  - 合計は＋2,030.0。
- ポスト数は同じ 152 なので、ポスト費の増は数ではなく費用の見積りの違い。
- 手がかりは A/81/6 第 29C.60 項。UN80 の再配置はバンコクとバレンシアへの移転日がずれており、2026 年はニューヨークとの部分年の両方の費用を承認した（バンコク 5 ポストは 2026-03-01、07-01、10-01 付、P-4 のバレンシアは 06-01 付）。
- 総会の最終決議がポスト費をどう決めたかを直接示す文は、読んだ範囲に見つからなかった。**理由は「部分年の費用の計上（推定）」まで。確定ではない。**
- 踏み跡の本文は 4,784 万の「2026 年の通常予算」と、A/81/7 の「2026 年の承認額」を、同じ「2026 年」として並べている。両者が別の量であることを明記すべき。
- 5.3% 増（第 VIII.82）の基準は 4,987 万 4,900 ドルであり、4,784 万ではない。
- 実際に 4,784 万から見れば、2027 年の提案 5,253.7 万ドルは 9.8% 増。踏み跡の「UN80 で減らした水準から小幅に戻る」は方向は合うが、幅は 5.3% でなく約 9.8%。

## (3) 再現できなかった主張

- **un80**
  - 表 VIII.18 で地理情報担当官（P-3）が属する小課。文書の抽出が崩れ、Subprogramme 2 に見えるが確定できない（踏み跡も未確認と書く）。
  - 「A/81/6 の付属書 II に地理空間情報課の名が出ない」。全文の `geospatial|GIS|Geographic Information Officer` は 0 件だったが、付属書 II が表の画像なら文字検索の対象外。表を目視していない。
  - イタリア外務省の「19 ポスト」。外部資料で未確認、踏み跡も未確認と書く。
- **open-gis**
  - OSGeo の技術会合「2017 年 4 月ブリンディジ」。取得した wiki とメーリングリストには 2016-03 のみ。
  - Brovelli ほか ISPRS XLII-4/W2（2017）。URL の推測が 404 で、要旨は読めなかった。
  - 米国「南方軍の担当者」の記述（検索要約）。
  - Initiative の公式サイトと GitHub（下記の一覧）。
  - FOSS4G 2025 の要旨の原文。検索要約のみ。
  - S/PV.8838 で India との MoU を述べた発言者は特定しなかった。

### 届かなかった先の一覧（回避していない）

| 先 | 結果 |
|---|---|
| `https://github.com/UNopenGIS` | HTTP 403 |
| GPS World の Boundless 記事（`gpsworld.com/boundless-partners-...`） | HTTP 403 |
| ISPRS Archives XLII-4/W14/87（推測した URL） | HTTP 404（正しい論文は /57/ にあり取得できた） |
| ISPRS Archives XLII-4/W2/7/2017（推測した URL） | HTTP 404 |
| official.py による A/81/6、A/80/6（款を付けない記号） | PDF でない応答（1,303 bytes）。`A/81/6(Sect.29C)` の形では取得できた |
| スライドの推測 URL（un-ggim-ap.org） | HTTP 404（検索で得た正しい URL では取得できた） |

## open-gis: 二次資料の書き方と強さの順位の評価

**二次資料を事実のように書いていないか。**
- 全体として、出典を「OSGeo の記録によれば」「OSGeo wiki の記述」と区別している。国と機関を混同しない注意（貢献者は機関）も本文に明記されている。
- 弱い点は 3 つ。
  1. 表と要点の「韓国 >…」の順位表が、機関の参加の厚さを国の関与の強さの順位として読ませる。
  2. OpenGDS を「韓国」の行に、GeoSDI を「イタリア」の行に入れているが、いずれも企業や団体である。国の公式な関与とは別。
  3. Brovelli 氏を「ミラノ工科大学」としてイタリア行に入れているが、Initiative での役割は OSGeo と GeoForAll の代表（D12）。

**順位（韓国 > 日本 ≒ イタリア > 米国 > フィンランド）の根拠の強さ。**
- **韓国が最上位**: 妥当。作業部会 2 つの長、OpenGDS、共同議長、KRIHS の試験事業、国連会議録での主催国発言（S/PV.7802、公式文書での裏づけは 5 か国で唯一）。ただし公式側は「シンポジウム開催」の一点で、Initiative そのものへの言及ではない。
- **日本**: UNVT 論文（全文で確認）と 2020 年のスライドの "Leading contributor: GSI Japan" の二点で、根拠は強い。ただし論文の共著者に国連職員が筆頭で入り、1 事業に限る。
- **イタリア**: 会合のホスト（ブリンディジの UNGSC）は国連の施設であって、イタリア政府の関与とは言えない。GeoSDI の創設貢献者と、Brovelli 氏の共同議長（2020 年）は事実。「ホスト国としての側面が強い」の注記は適切だが、順位は日本と同格より低くも高くもなり得る。
- **米国**: 順位は妥当だが、共同議長の一人 Juan Hurtado（GeoSHAPE、米国）と Spiral 1 の長（Boundless）を落としているので、実態より弱く見える。DoD の支援は wiki の一文で、一次資料でない。
- **フィンランド**: 「弱い（単一の資料）」とされるが、**国名で資金を特定した記述はこの行だけ**。しかも資料は OICT（国連側）自身のスライドで、「二次資料」と呼ぶのは正確でない。「裏づけが 1 点」と「関与が弱い」は別の軸。
- 結論: 順位は「資料の厚み」の順としては概ね支持できるが、「関係の強さ」の順位として読むと誤導的。軸を明示すべき。

## (4) 直し方の提案

**un80**
1. D1: 「2026 年の 102 から 2027 年の 92」を「2023〜2025 年の実績 102 から、2026 年と 2027 年の計画 92」に直す。
2. D2、D3: 時系列表の「2025 年 10 月」を「2025 年 9 月（9 月 4 日配布）」に、「2025 年 12 月」を「2025 年 11 月（26 日配布、12 月 12 日再発行）」に直す。
3. D4: 要点 2 と「詳しく」に、次の趣旨の 1〜2 文を足す。
   - 改訂見積り 4,784 万ドルは 2026 年の事務総長の提案であり、A/81/6 と A/81/7 の 2026 年承認額 4,987 万 4,900 ドルとは別の量である。
   - 差 203.0 万ドルはポスト費（＋201.0 万）、その他職員費（＋6.3 万）、旅費（−4.3 万）で、ポスト数は 152 で同じ。
   - 理由は、再配置の部分年の費用が A/81/6 第 29C.60 項に現れることまでは言えるが、確定はしていない。
   - 「5.3% 増」は 4,987 万基準、4,784 万基準なら約 9.8% 増。
4. D5: 「OICT の措置」を「提案された廃止」に直す。D6: 1,506 万 8,700 と 1,506 万 8,900 の両方を原文の食い違いとして注記する。D7: 未確認の項目から「A/80/6 の成果の表」を外す。D8: 根拠の項番を VIII.96（GTA）、VIII.98（5%）、VIII.100（結論）に分ける。
5. 表 VIII.18 は小課の抽出が崩れていることの注記を残し、ページ画像で確かめるのが確実（今回は未実施）。
6. A/81/6 付属書 II の確認は、文字検索の 0 件でなく、画像の目視まで済ませたかを分けて書く。

**open-gis**
7. D9、D10: S/PV.7802 は「開催中の週と述べた」に直し、主催者の表現が資料で違う旨を 1 文足す。
8. D11、D12: 共同議長（2016 年は Hurtado、Li、Eom、2020 年は Li、Brovelli、Eom）を書き、米国の行にも反映する。Brovelli 氏は「OSGeo と GeoForAll の代表」と書く。
9. D13: `checks/un-open-gis-member-state-links.md` の式の表に `open\s+geographic\s+information`（0 件）を追加する。A/71/19 と A/72/19 が実際に使う名称であることも書く（再利用しやすい同義語の表になる）。
10. 順位表の「強さ」の列を、軸ごとに分けるか、列名を「資料の厚み」に変える。フィンランドは「国名で資金を明記した唯一の記述（国連 OICT のスライド）。ただし単一資料」と書く。
11. `verified_how: mixed` の内訳に、今回確認できた一次寄りの資料（OSGeo wiki と ML、UNVT 論文、2020 年のスライド）の取得日と URL を書く。OSGeo wiki と ML は今回、直接取得で読めた（要約ではない）。
12. 利害関係の注記は適切（筆頭著者 H. Fujimura と管理責任者の同名の可能性）。FOSS4G 2025 の要旨の話者も同名に見える（検索要約）ので、同じ注記に含めるとよい。
