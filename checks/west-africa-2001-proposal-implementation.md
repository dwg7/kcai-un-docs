# 2001 年の西アフリカ提案の実装追跡：確認の記録（途中で終了）

データ: yuiseki/un-docs 6cd1cf0。範囲は総会と安保理の英語文書。

## 実施したこと
- `python3 -I scripts/undocs.py --data $D show 'S/PV.4319' --grep '(?i)subregion|sub-region|GIS\b|information system'`: McAskie 氏の勧告の原文は「subregional capacity」「Geographical Information System (GIS)」。
- `show 'S/PV.4439' --grep '(?i)regional\s+office\s+for\s+west|OCHA|Office\s+for\s+the\s+Coordination'`: 該当 5 か所。
- `search '(?i)regional office for west africa' --by-year`: 5 件（S/2001/434、S/PV.4439、S/2019/549、S/PRST/2019/10、S/PV.8679）。OCHA 以外の文脈を含む。
- `search '(?i)Office for the Coordination of Humanitarian Affairs.{0,80}(regional|subregional) (office|support|capacity)'`: 0 件（本文の改行に空白が入るため、`\s+` を使わない式は取りこぼす）。
- 公式 PDF: S/2001/1128、S/2001/1129、S/2001/434 を取得。
- ウェブ: reliefweb.int と www.unocha.org は 403。unowas.unmissions.org/mandate は 404。

## 未完了
23 語（UNOWA、Regional Support Office、Humanitarian Information Centre、ReliefWeb、UNJLC、UNOSAT、Cartographic Section、GIS 等）の全文検索は、全件走査が終わらず結果を得ていない。式は `scratchpad` の q1.tsv にあり、再実行が必要。
