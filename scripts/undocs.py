#!/usr/bin/env python3
"""yuiseki/un-docs（pin した版）を、正規化・重複除去・合冊除外つきで検索する。

使い方（データは scripts の外、リポジトリの外に置く。checks/README.md 参照）:
    python3 -I scripts/undocs.py --data /path/documents.parquet search '(?i)geo-?spatial' [--first N] [--by-year]
    python3 -I scripts/undocs.py --data ... show 'S/RES/1674(2006)' [--grep REGEX]

規則（docs: knowledge/un-docs-reading-guide.md）:
  * 記号は空白を除いて正規化する（sym）。同じ sym は 1 本にする（pdf を優先し、長い本文を採る）。
  * 総会決議の合冊（Vol. を含む記号）は除く。--keep-vol で残す。
  * 日付は date_adopted > date_distributed > date_other の順に採り、どれを採ったか（date_kind）を出す。
"""
import argparse
import re
import sys

import duckdb

FAMILY = """case
  when id like 'S/RES/%' then 'S/RES' when id like 'S/PRST/%' then 'S/PRST'
  when id like 'S/PV%' then 'S/PV' when id like 'A/RES/%' then 'A/RES'
  when regexp_matches(id,'^A/(\\d+/)?PV') then 'A/PV' when id like 'A/ES%' then 'A/ES'
  when id like 'A/S-%' or id like 'A/S/%' then 'A/S'
  when regexp_matches(id,'^S/\\d{4}/') then 'S/yyyy/n'
  when regexp_matches(id,'^A/\\d+/L\\.') then 'A/NN/L' when regexp_matches(id,'^A/\\d+/\\d+') then 'A/NN/n'
  when id ilike 'S/INF%' then 'S/INF' else 'other' end"""


def connect(path, keep_vol=False):
    con = duckdb.connect()
    vol = "" if keep_vol else "and id not ilike '%vol%'"
    con.execute(f"""
      create view docs as
      select * from (
        select id, regexp_replace(id,'\\s','','g') as sym, {FAMILY} as family, text_source,
               coalesce(date_adopted, date_distributed, date_other) as date,
               case when date_adopted is not null then 'adopted' when date_distributed is not null then 'distributed'
                    when date_other is not null then 'other' else null end as date_kind,
               body,
               row_number() over (partition by regexp_replace(id,'\\s','','g')
                                  order by (text_source='pdf') desc, length(body) desc, id) as rn
        from read_parquet('{path}') where true {vol}
      ) where rn = 1""")
    return con


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--keep-vol", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("regex")
    s.add_argument("--first", type=int, default=0, help="日付の早い順に N 件の記号を出す")
    s.add_argument("--by-year", action="store_true")
    s.add_argument("--by-family", action="store_true")
    s.add_argument("--family", help="系列を限る（例 S/RES）")
    h = sub.add_parser("show")
    h.add_argument("sym")
    h.add_argument("--grep")
    a = ap.parse_args(argv)
    con = connect(a.data, a.keep_vol)
    if a.cmd == "search":
        w = "regexp_matches(body, ?)" + (f" and family = '{a.family}'" if a.family else "")
        n = con.execute(f"select count(*), count(distinct md5(body)) from docs where {w}", [a.regex]).fetchone()
        tot = con.execute("select count(*) from docs").fetchone()[0]
        print(f"hits={n[0]} distinct_bodies={n[1]} of {tot} unique-symbol docs (合冊除外={'no' if a.keep_vol else 'yes'})")
        if a.by_family:
            for r in con.execute(f"select family, count(*) from docs where {w} group by 1 order by 2 desc", [a.regex]).fetchall():
                print("family", *r)
        if a.by_year:
            for r in con.execute(f"select substr(date,1,4) y, count(*) from docs where {w} group by 1 order by 1", [a.regex]).fetchall():
                print("year", *r)
        if a.first:
            for r in con.execute(f"select sym, date, date_kind, text_source, family from docs where {w} "
                                 f"order by date nulls last, sym limit {int(a.first)}", [a.regex]).fetchall():
                print("first", *r)
    else:
        sym = re.sub(r"\s", "", a.sym)
        r = con.execute("select sym, date, date_kind, text_source, length(body), body from docs where sym = ?", [sym]).fetchone()
        if not r:
            print("not found:", sym)
            return 1
        print(*r[:5])
        if a.grep:
            body = r[5]
            for m in re.finditer(a.grep, body):
                lo, hi = max(0, m.start() - 160), min(len(body), m.end() + 160)
                print("…" + re.sub(r"\s+", " ", body[lo:hi]) + "…")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
