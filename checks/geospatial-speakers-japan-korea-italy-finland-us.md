# 検査記録：地理空間の語を述べた発言者の国（日本、韓国、イタリア、フィンランド、米国）

データ: un-docs コミット 6cd1cf0。`scripts/undocs.py` の `connect`（記号の正規化、重複除去、合冊除外）。対象は系列 S/PV と A/PV で、次の式に当たる文書。

語の式（大文字小文字を無視。ただし GIS は大文字の語に限る）:

```
(?i)geo-?\s?spatial|geographic(?:al)?\s+information|\bGIS\b|remote[\s-]+sensing|earth[\s-]+observation|\bGGIM\b|Global\s+Geospatial\s+Information|\bcartograph(?:er|ers|ic|y)\b|satellite\s+(?:imagery|images?)
```

発言者の判定: `scripts/speaker_counts.py` の `HDR`（"Mr. X (Country):" の見出し。敬称に Count、Prof.、Father を足した）と `BOUND`（議長・事務総長などの見出し）を使い、語の位置の直前にある最後の見出しを発言者とした。

結果: 当たった文書 184、語の出現 203。発言者の国を特定できたのは 115 出現、特定できなかったのは 88 出現（67 文書。議長・事務総長の発言、見出しの崩れ、非国家の発言者を含むが、内訳は未確認）。

| 国 | 文書数 | 出現数 | 文書 |
|---|---|---|---|
| Japan | 1 | 9 | A/59/PV.37（2004-10-20） |
| Italy | 4 | 4 | S/PV.1565(OR)、S/PV.5667、S/PV.5736、S/PV.7196 |
| United States of America | 7 | 7 | S/PV.4701、S/PV.7253、S/PV.7353、S/PV.7394、S/PV.8119、S/PV.8543、S/PV.9436 |
| Republic of Korea | 0 | 0 | 見出しに該当なし |
| Finland | 0 | 0 | 見出しに該当なし |

他国で件数が目立つ見出し（文書数）: Russian Federation 8、Syrian Arab Republic 5、India 4、Ukraine 4、Iraq 4。

限界: 議長が自国の代表として述べた発言は、見出しが "The President" なので、この式では国に結び付かない（未確認）。EU など集団の代表としての発言は、国別には数えていない。語を `mapping` などに広げていない。決議案の提案国と第五委員会の発言は調べていない。
