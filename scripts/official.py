#!/usr/bin/env python3
"""公式サイトの原文（PDF）を取得して文字にし、語の周辺を出す。

docs.un.org/en/<記号> のページが埋め込む documents.un.org の公開 API（ブラウザが読むのと同じ経路）を使う。
pdftotext が要る。取得物は --cache（リポジトリの外）に置く。使い方:
    python3 -I scripts/official.py --cache DIR 'S/RES/1674(2006)' --grep 'responsib' [--width 150]
結果の 1 行目に、取得できたか（bytes、ページ数）を出す。届かないときは "UNREACHABLE" と出る（すり抜けない）。
"""
import argparse, re, subprocess, sys, urllib.parse, urllib.request
from pathlib import Path

def fetch(sym, cache, lang="en"):
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", sym)
    pdf = Path(cache) / f"{safe}.{lang}.pdf"
    if not pdf.exists():
        url = "https://documents.un.org/api/symbol/access?" + urllib.parse.urlencode({"s": sym, "l": lang, "t": "pdf"}, safe="/()")
        req = urllib.request.Request(url, headers={"User-Agent": "kcai-un-docs (reading official text)"})
        data = urllib.request.urlopen(req, timeout=90).read()
        if not data.startswith(b"%PDF"):
            raise RuntimeError("PDF ではない応答（%d bytes）" % len(data))
        pdf.write_bytes(data)
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    return pdf, txt

def main(a):
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", required=True)
    ap.add_argument("sym")
    ap.add_argument("--grep")
    ap.add_argument("--width", type=int, default=150)
    ap.add_argument("--max", type=int, default=6)
    o = ap.parse_args(a)
    Path(o.cache).mkdir(parents=True, exist_ok=True)
    try:
        pdf, txt = fetch(o.sym, o.cache)
    except Exception as e:
        print(f"UNREACHABLE {o.sym}: {e}")
        return 2
    flat = re.sub(r"\s+", " ", txt)
    print(f"OK {o.sym} pdf={pdf.stat().st_size}B chars={len(flat)}")
    if o.grep:
        for i, m in enumerate(re.finditer(o.grep, flat)):
            if i >= o.max: break
            print("…" + flat[max(0, m.start() - o.width): m.end() + o.width] + "…")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
