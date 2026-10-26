# 検査記録：地理空間の文書の地名・主題（2026-10-26）

対象: `geospatial` を含む 73 文書（`checks/geospatial-73-docs.tsv`）。

1. 国名・地域名: `geospatial` の各出現の前後 300 字を連結し、国名・地域名・国連の分類の一覧（約 150 語、`\b(...)\b`）に当たる語を文書ごとに集合にして数えた。結果（文書数）: developing countries 12、Brindisi 9、Italy 8、Iraq 7、Kuwait 3、least developed countries 2、そのほかは 1。
2. 主題: S/yyyy/n・S/PV・S/RES・S/INF の `geospatial` 文書（34 文書: S/yyyy/n 30、S/PV 2、S/RES 1、S/INF 1）の冒頭 3,000 字に、次の式のどれが当たるかを数えた: Iraq/Kuwait `paragraph 4 of Security Council resolution 2107|Kuwaiti|UNAMI|Iraq`、Mali/Sahel `MINUSMA|Mali\b|Sahel|West Africa|UNOWAS|AFISMA`、西サハラ `MINURSO|Western Sahara`、キプロス `UNFICYP|Cyprus`、レバノン `UNIFIL|Lebanon`、イエメン `UNMHA|Hodeidah|Yemen`、アビエ `UNISFA|Abyei`、ソマリア `UNSOS|AMISOM|Somalia|African Union peace support`、北朝鮮 `Democratic People|DPRK`、OPCW `OPCW|Organisation for the Prohibition of Chemical`、リビア `UNSMIL|Libya`。結果: 10 / 6 / 4 / 3 / 3(ソマリア) / 2(レバノン) / 2(北朝鮮) / 1(アビエ) / 1(OPCW) / 1(リビア) / 主題語なし 6。
3. 最初の窓だけの集計では、MINURSO の文書に `Western Sahara` が出ない（窓の外）。窓の集計は国名の把握に使わず、冒頭の主題語を使った。
