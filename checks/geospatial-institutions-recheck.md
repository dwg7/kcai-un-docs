# 検査記録：地理空間の機関の悉皆的な把握の確かめ直し（2026-10-26）

対象: hfu/kcai-yuiseki-datasets の `checks/un-docs-geospatial-institutions.tsv`（226 文書、コミット 1b0f565）。データは un-docs 6cd1cf0。

## 1. 集合の再現

式: `(?i:cartograph)|(?i:geo-?\s?spatial)|(?i:geographic(al)?\s+information\s+system)|\bGIS\b`（RE2 の語ごとの大文字小文字指定）。`undocs.connect(path, keep_vol=True)`（合冊を残す）で `regexp_matches(body, 式)` に当たる記号を正規化（空白除去・大文字化）した集合は 226 で、前身の TSV の `id` の集合と**両方向で一致**した。

最初の試行（誤り）: 式全体を `(?i)` で包んだため `\bGIS\b` が大文字小文字を無視し、290 文書（64 余計）になった。

## 2. 読み直し

- 「その他（自動）」54 文書: 各文書の最初の出現の前後 120 字を読んだ。
- M-ミッション 25 文書: 前後 210 字を読み、前身の要約と照合した。
- H-組織・U-UNLB の決議 10 本: 該当する項の前後 260 字を読み、公式の PDF と照合した。
- 変更・指摘した行は `un-docs-geospatial-institutions-recheck.tsv`（それ以外の行は変更なし）。

## 3. 検索語の漏れの調査

`UNOSAT`（4 文書）、`United Nations Satellite Cent`（0）、`\bSAGE\b`（1）、`(mapping|GIS|geospatial) (unit|section|centre|center|team|cell)`（1: S/PV.4507(RESUMPTION1) の Vulnerability Analysis and Mapping Unit）。`satellite imagery` の調査で書いた式 `UNITAR|…` は `unitary`（単一国家）に当たり、結果を使えなかった（大文字小文字を無視した式の誤り）。

## 4. ミッションの比率

式（ミッション名と長い正式名の約 50 語）を、S/yyyy/n・A/NN/n・S/INF の冒頭 900 字に当てて 1,045 文書、うち地図・GIS・地理空間の式に当たる文書が 21。前身の 23/1,180 とは完全には再現できなかった。

## 5. 公式サイトの原文との照合

取得: `https://docs.un.org/en/<記号>` のページは PDF を iframe で埋め込み、その実体は `https://documents.un.org/api/symbol/access?s=<記号>&l=en&t=pdf`（`scripts/official.py`）。`pdftotext`（読み順）で文にして、該当語の周辺を un-docs の本文と照合した。`-layout` の指定は 2 段組みの文書で段が混ざり、語が見つからないことがあった（A/RES/42/186 など）ため使わない。

一致を確かめた文書: A/RES/57/300、58/101、60/267、61/277、61/287、67/287、69/308、69/309、70/235、70/288、71/272、72/287、73/310、S/PRST/2000/21、S/RES/1398 (2002)、S/PRST/2007/29、S/2015/1025、S/2017/78、S/2017/1034、S/2017/454、S/2019/319、S/2019/352、S/2019/632、S/2020/133、S/2023/51、S/2014/130、S/2021/1110、S/2019/787、S/2023/3、S/PV.9039、S/PV.7802、S/PV.9389、S/2020/952、S/2018/945、S/2020/195、S/2014/515、S/2013/37、S/2018/110、S/2005/673。

届かなかった・照合できなかった: なし（取得に失敗した記号は無かった）。S/PV.4227、S/PV.4310、S/2000/1194 の本文、ほか多数は未照合。
