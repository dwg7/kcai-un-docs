# S/2018/945 ほか 4 文書の確かめ（2026-10-26、dataset_rev 6cd1cf0）

- 公式の PDF: `scripts/official.py` で S/2018/945、S/2019/319、S/2019/787、S/2020/938 を取得（全て OK）。S/2018/945 は全文、他は geospatial の周辺と冒頭のみ読んだ。
- `python3 -I scripts/undocs.py --data … search '(?i)geospatial intelligence'` は 1 件（S/2018/945）。
- `search '(?i)Barkhane'` は 143 件（会議録を多く含む）。`search '(?i)operational support to the United Nations Multidimensional Integrated Stabilization'` は 1 件（S/2018/945）。他の号の報告第 N 号は un-docs では見つからなかった（式を替えた確認はしていない）。
- 日付: un-docs の S/2018/945 は 2018-06-28（date_kind=adopted）。公式の PDF では書簡 2018-10-19、配布 2018-10-25、口上書 2018-10-12。2018-06-28 は決議 2423 の採択日。
- `show S/2019/787 --grep geospatial` 相当で 2 か所（第 25、52 項）。S/2020/938 は第 22 項。S/2019/319 は第 53 項（Service for Geospatial, Information and Telecommunications Technologies）。
