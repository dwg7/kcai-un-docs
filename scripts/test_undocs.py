#!/usr/bin/env python3
"""記号の正規化のテスト（標準ライブラリと duckdb のみ）。python3 -I scripts/test_undocs.py"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import duckdb
import undocs

CASES = [
    ("S/RES/1 (1946)", "S/RES/1(1946)"),
    ("S/RES/1(1946)", "S/RES/1(1946)"),
    ("S/inf/72", "S/INF/72"),
    ("A/77/443/Add.3", "A/77/443/ADD.3"),
    ("S/PV.7505(Resumption1)", "S/PV.7505(RESUMPTION1)"),
    ("A/RES/2778 (XXVI)", "A/RES/2778(XXVI)"),
    ("S/RES/11 07(1997)", "S/RES/1107(1997)"),
]


class Normalize(unittest.TestCase):
    def test_python(self):
        for raw, want in CASES:
            self.assertEqual(undocs.normalize_symbol(raw), want, raw)

    def test_same_as_sql(self):
        con = duckdb.connect()
        for raw, want in CASES:
            got = con.execute("select upper(regexp_replace(?, '\\s', '', 'g'))", [raw]).fetchone()[0]
            self.assertEqual(got, want, raw)
            self.assertEqual(got, undocs.normalize_symbol(raw), raw)

    def test_spellings_collapse(self):
        self.assertEqual(undocs.normalize_symbol("S/RES/1 (1946)"), undocs.normalize_symbol("S/RES/1(1946)"))
        self.assertEqual(undocs.normalize_symbol("S/inf/72"), undocs.normalize_symbol("S/INF/72"))


if __name__ == "__main__":
    unittest.main()
