# 検査記録：衛星画像の会合の個別読み（2026-10-26）

データ: un-docs コミット 6cd1cf0。`scripts/undocs.py` の規則。公式 PDF は `scripts/official.py`（Resumption は `S/PV.6151(Resumption1)` の綴りで届く）。

```sh
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)satellite\s+(imagery|images?)' --family S/PV   # 68 件（空白 1 個の式は 62 件）
python3 -I scripts/undocs.py --data ... show 'S/PV.8184' --grep '(?i)satellite'
python3 -I scripts/undocs.py --data ... search '(?i)Operational\s+Satellite\s+Applications'   # 18 件（全系列）
```

`satellite` の件数（生の本文）: 8184=1、8271=1、8324=2、8396=2、8739=1、8910=2、6151 主記録=0、6151(Resumption1)=2、7196=6。`UNOSAT|UNITAR` は 6151(R1)=2、7196=2、他は 0。地中レーダーは 8910 のみ 1。

報告（決議 2107 第 4 項）は S/2016/885 から S/2021/930 まで本文を読み、`satellite|imagery` の文脈を確認した。UNOSAT の語を含む S 系列は生データで 19 件（S/2013/337、S/2014/373、696、740、756、840、S/2015/206、368、468、S/2016/157、384、1093、S/2017/505、969、S/2018/171、S/2020/278、会議録 6151(R1)、7196、8589）。unosat.org は内容を取得できなかった。公式 PDF で照合した記号は各踏み跡の「確かめた度合い」に記す。
