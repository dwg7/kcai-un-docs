# 検査記録：「立ち入れない場所の代替としての衛星画像」を S/PV の個別会合で読む（2026-10-26）

データ: un-docs コミット 6cd1cf0。`scripts/undocs.py` の規則。公式の PDF は `scripts/official.py`（documents.un.org の公開 API 経由）で取得し、`pdftotext`（-layout なし）で文字にした。取得物はリポジトリの外（スクラッチ）に置いた。

## 1. 対象会合の確認（un-docs）

```sh
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)satellite\s+(imagery|images?)' --family S/PV --first 80
```

68 文書のうち、対象の S/PV.4692、4707、7353、7575、7830、7932、8137、8353、8500 が含まれることを確認した。日付は un-docs の `date`（date_kind は other）で、2003-01-27、2003-02-14、2014-12-22、2015-12-10、2016-12-09、2017-04-28、2017-12-15、2018-09-17、2019-04-02。公式の PDF の表紙の日付と一致した。

## 2. 公式の PDF（取得できた）

```sh
for s in 4692 4707 7353 7575 7830 7932 8137 8353 8500; do
  python3 -I scripts/official.py --cache "$SCRATCH/pdf" "S/PV.$s" --grep 'satellite' --max 1 --width 60
done
python3 -I scripts/official.py --cache "$SCRATCH/pdf" 'S/2014/276' --grep '(?i)satellite' --max 12 --width 220
python3 -I scripts/official.py --cache "$SCRATCH/pdf" 'A/HRC/25/63' --grep '(?i)satellite' --max 3 --width 150
```

すべて `OK`（PDF が取得できた）。取得できなかったもの: `A/HRC/25/CRP.1`（OK と出たが本文は 254 字の表紙のみ。委員会の詳細報告の衛星画像の記述は読めていない）。

## 3. 発言者の見出しの特定

各会合のテキスト（空白を 1 つにつぶしたもの）から、見出しの式
`((The (Secretary-General|President|Acting President)|(Mr|Ms|Mrs|Dr|Sir|Dame|Baroness|Lord|Miss)\.? [A-Z][^:()]{1,50}?( \([^()]{2,70}\))?)( \(spoke in [A-Za-z]+\))?): `
で発言の開始位置を列挙し、衛星画像の語の位置の直前の見出しを発言者とした。式は見出しの綴りが変則（"Mr. ElBaradei:"、"The Secretary-General:" など）でも当たることを、各会合で目視した（式が取りこぼす見出しが無いか、発言者の列と開始位置の連続を確認）。

## 4. 語の件数（公式の PDF の本文、空白をつぶして数えた）

| 会合 | `(?i)satellite (imagery|images?)` | `(?i)\bimagery\b` | `(?i)\bsatellites?\b` | `(?i)remote (monitoring|analysis)` | `(?i)open-source` |
|---|---|---|---|---|---|
| S/PV.4692 | 3 | 3 | 3 | 4 | 0 |
| S/PV.4707 | 1 | 0 | 2 | 0 | 0 |
| S/PV.7353 | 1 | 1 | 1 | 0 | 0 |
| S/PV.7575 | 1 | 1 | 1 | 0 | 0 |
| S/PV.7830 | 1 | 0 | 1 | 0 | 0 |
| S/PV.7932 | 2 | 2 | 3 | 0 | 0 |
| S/PV.8137 | 1 | 1 | 1 | 0 | 0 |
| S/PV.8353 | 1 | 1 | 2 | 0 | 0 |
| S/PV.8500 | 1 | 1 | 1 | 0 | 1 |

読み方: `imagery` が `satellite imagery` より多いのは 4692 の 1 件（ブリクス氏の「aerial imagery」）。`satellite` が多いのは、7932 の「placement of a satellite in orbit」、8353 の「Sohae satellite launching site」、4707 の「satellites」（イラクの代表の発言。空中監視の手段の一つ）などの別の意味の語。

発言者ごとの出現:

- 7932: The Secretary-General（3777〜11418 字目）の段落のみ。
- 8137: The Secretary-General（3809〜10312 字目）の段落のみ。
- 8353: Ms. DiCarlo（3039〜7941 字目）の段落のみ。
- 8500: Mr. Amano（12854〜24797 字目）の段落のみ。
- 4692: Mr. ElBaradei（34298〜49812 字目）。別に Mr. Blix（4234〜34113 字目）が「aerial imagery」（U-2）に 1 回触れる。
- 7353: Ms. Power (United States of America)（36929〜50828 字目）。
- 7575: The President（Ms. Power が議長として、米国代表の資格で述べた部分。78071〜94543 字目）。
- 7830: Mr. Gilmour（24788〜34089 字目）。
- 4707: Mr. Blix（4481〜24746 字目）の段落。ElBaradei の開始は 24910 字目。

## 5. 他の理事国の反応の確認

- 画像の語を含む発言は上のとおりで、他の理事国の発言には出ない（式 `satellite|imagery`）。
- IAEA に触れる発言の確認（7932、8137、8500）: `IAEA|Atomic Energy Agency` の出現位置と、その直前の見出し。
- 人権の 3 回（7353、7575、7830）: 中国、ロシア、オーストラリアの冒頭の発言を通読。画像の真偽に触れる発言は無かった。

## 6. 決議・議長声明への反映の確認（un-docs）

```sh
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)satellite' --family S/RES --first 30
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)satellite' --family S/PRST --first 30
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)satellite\s+(imagery|images?)' --family S/RES
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)(imagery|remote sensing)' --family S/RES --first 30
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)(imagery|remote sensing)' --family S/PRST --first 30
python3 -I scripts/undocs.py --data "$SCRATCH/data/documents.parquet" search '(?i)aerial imagery' --family S/RES --first 20
```

結果:

- `satellite` を含む S/RES は 11 件（1382、1441、1454、2087、2202、2270、2321、2474、2498、2551、2607）。S/PRST は 1 件（S/PRST/2012/13。北朝鮮の人工衛星打ち上げの意味）。
- `satellite imagery|images` を含む S/RES は 0 件。S/PRST は 0 件。
- `imagery|remote sensing` を含む S/RES は 3 件（1441、2321、2474）。S/PRST は 0 件。
- `aerial imagery` を含む S/RES は 2 件（1441〔附属書の書簡〕、2321〔第 42 項〕）。
- 2087 と 2012 年の S/PRST は「satellite launching station」など、人工衛星の打ち上げの意味。1441 の `satellite` は通信手段（衛星電話、衛星回線）の意味。
- 北朝鮮関連の個別確認: S/RES/2356、2371、2375、2397（2017）に `satellite|imagery|aerial|remote sens` の語は無い（2356 と 2397 は `IAEA|Atomic Energy` で別の語句に当たる）。2270（2016）にも `imagery` は無い。

## 7. 見つけたこと（先行の踏み跡との差）

- S/PV.7932、8137 の発言者は事務総長、8353 は政務担当の事務次長。IAEA の事務局長が自分で述べたのは 8500 の天野氏と 4692 のエルバラダイ氏。
- S/PV.4707 の「2 枚の衛星画像が数週間離れて撮られた」の発言者は Mr. Blix（UNMOVIC の委員長）。
- S/PV.7353 の表紙は 2014-12-22 だが、ページの脚注の日付は 23/12/2014（会合の日付は 22 日と読む。un-docs の日付も 22 日）。
