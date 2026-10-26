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
