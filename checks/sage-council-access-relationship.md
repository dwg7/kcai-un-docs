# 検査記録：安保理での SAGE の言及、アクセス、Unite Aware との関係（2026-10-26）

データ: un-docs コミット 6cd1cf0（最新の日付は 2023-10-16）。`scripts/undocs.py`（記号の正規化、重複除去、合冊除外）。

## un-docs の検索（件数は文書単位）

| 式 | 件数 | 備考 |
|---|---|---|
| `\bSAGE\b` | 1 | S/2021/1110 のみ |
| `(?i)Situational\s+Awareness\s+Geo` | 4 | S/2021/501（改行をまたぐ）、S/PV.8838（Geospace）、S/2021/1110、S/PV.9389 |
| `(?i)Geospace` | 1 | S/PV.8838 |
| `(?i)Unite[\s-]*Aware` | 12 | 既存の記録と同じ。S/2021/501 は付属文書 2（運用支援局長）と 7（インド） |
| `(?i)radio\s+mining` | 3 | S/2021/501、S/2021/732、S/PV.9189 |
| `Source:\s*MON?[A-Z]+/[^.]{0,60}Joint Operations` | 0 | 出典表記の形（S/2025/779 の図 I）は範囲内に無い |
| `(?i)Joint\s+Operations\s+Cent(re|er)` | 77 | 一般的な語。SAGE との関係は個別に読んでいない |
| `(?i)peacekeeping[- ]intelligence` | 21 | 同上 |
| `(?i)Office\s+of\s+Information\s+and\s+Communications?\s+Technology` | 84 | 同上（一覧の確認のみ） |
| `(?i)(incident|events?)\s+(database|management\s+system)` | 7 | 例: S/2015/620 はリベリアの別の仕組み。SAGE と無関係と確認 |

注意: 式の空白を一つに固定すると、改行をまたぐ S/2021/501 の正式名が漏れる。最初の確認で `-1`（未検出）になり、`\s+` に直した。
`(?i)situational\s+awareness` は 294 件で一般語のため、SAGE の指標にならない。

## 発言者の確認（見出しの位置）

- S/PV.9389: 質問 = Baeriswyl（Switzerland）の発言内、答え = General Subramanian（UNMISS 部隊司令官）。
- S/PV.8838: SAGE = Kvalheim（Norway）。Unite Aware の 9 か所のうち、見出しで確かめたのは議長（インド）、Liimets（Estonia）、Thomas-Greenfield（米国）、Kimani（Kenya）、Kariuki（英国）、Kvalheim（Norway）。
- S/PV.8859 Raguttahalli、S/PV.9039 Tirumurti、S/PV.9090 Kumar、S/PV.9123 Kamboj（いずれもインド）。
- S/2021/501: 付属文書 43 = オランダ常駐代表部、付属文書 2 = 運用支援局長、付属文書 7 = インド。

## 公式サイト・国連のサイトから読んだ文書（un-docs の範囲外）

- `scripts/official.py` で取得: A/78/726（SAGE／Unite Aware: 第 41・158・185 項）、A/79/788（第 166・185 項）、A/79/724（第 74・75 項）、A/78/7（Unite Aware 1 か所）、A/77/489（SAGE・Unite Aware の語なし）、A/79/724/Add.12・A/79/830・A/78/731（語なし）。A/80/798（語なし）。
- 以前の作業で取得済みの特別委員会の報告 A/67/19〜A/80/19、A/72/573 のテキストを再検索。
- 国連のサイトの PDF: ft.dfs.un.org の Enterprise SAGE ファクトシート、unsco.unmissions.org の UNMO 研修資料、peacekeeping.un.org の警察部門の事業提案書（日付未確認）。IPI（2023-09）の PDF（二次）。

## 届かなかった先（すり抜けていない）

- www.un.org/en/node/234607、node/234458（HTTP 403）、node/224432（取得がタイムアウト）、www.un.org/en/unpdf/peace-and-security-2023-03（403）
- peacekeeping.un.org の技術戦略の研究論文（20210430_-_sa-pki_technologies_research_brief_final_clean.pdf、403）
- oios.un.org/file/7754/download（403）
- www.un.org/en/delegate/innovation-day-virtual-discussion-unite-aware（502）

## 未着手

- 2026/27 年度の予算案（A/80/…）と OICT の文書での SAGE／Unite Aware の記述。
- dwg7 のラジオシリーズの内容（与えられていない）。
- S/2021/501 のビデオ会議に対応する会議録の有無。
