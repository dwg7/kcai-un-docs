# Draft: observations from reading yuiseki/un-docs (6cd1cf0) — NOT POSTED

Status: draft for hfu to review. Do not post without review.
Dataset: `yuiseki/un-docs`, revision `6cd1cf0`, `documents.parquet` (39,363 rows).
Written in plain English on purpose.

Thank you for publishing this dataset. It made it possible to check claims against the UN symbols. While reading it, we noticed several things that other readers may want to know. We list them with small reproduction queries. We did not check the PDFs for every case, and we say so below.

## 1. The same symbol can appear twice with different spacing

`S/RES/1 (1946)` and `S/RES/1(1946)` are two rows. After removing whitespace, `S/RES` has 2,699 distinct numbers (1 to 2699) in 4,248 rows. 1,548 numbers have two rows. For 75 of those numbers, the two bodies are different. The `pdf` column shows that the two spellings point to different source files, for example `en/pdfs/S/RES/426 (1978)/resolution.pdf` and `en/pdfs/S/RES/426(1978)/resolution.pdf`.

Examples of what we saw (we read the extracted text, not the PDFs):
- `S/RES/761 (1992)`: one row is a page from a "Resolutions and Decisions" volume with other text around it; the other row is an OCR of the stand-alone resolution.
- `S/RES/426(1978)`: one row has 4,219 characters (English); the other has 8,266 characters and the text is French.

Also `S/inf/72` vs `S/INF/72`, and `Add.3` vs `ADD.3`, appear as separate rows.

```sql
select upper(regexp_replace(id,'\s','','g')) k, count(*), count(distinct md5(body))
from read_parquet('documents.parquet') where id ilike 'S/RES/%' group by 1 having count(*)>1 and count(distinct md5(body))>1;
```

## 2. `lang = en` rows that are mostly French

We used a crude test (counts of common English and French function words in the first 20,000 characters). 82 rows have more French than English (S/PV 63, A/RES 14, and a few others), and about 1,800 rows have a lot of French (mostly S/PV from the 1950s and 1960s). The card says "Languages: en". This is probably the bilingual Official Records pages. It may be worth a note in the card, or a language-detection column. Our test is rough; we did not validate it by hand beyond a few rows.

## 3. The range ends at S/RES/2699

The card says 1945 to 2023. `S/RES` ends at 2699 (2023-10-02). `S/RES/2700 (2023)` to `S/RES/2723 (2024)` and later symbols are available as PDFs from the UN document system (we checked that the PDFs exist for 2700, 2701, 2710, 2720, 2721, 2722, 2723, 2750 and 2800). Also, 72 of the 90 missing `S/PV` numbers (1544–1548, 1624–1683 and 25 single numbers) have PDFs there (most under the `(OR)` form of the symbol, for example `S/PV.1544(OR)`). 18 numbers we could not find with the two symbol forms we tried. A short note in the card about the end of the range may help users.

## 4. Some date fields look wrong

The card explains that dates are checked against the year implied by the symbol. This cannot work for `S/PV`, which has no year in the symbol. Examples we saw:
- `S/PV.2411(OR)` has `date_other = 1965-01-01`, but `S/PV.2457(OR)` (a larger number) has 1982-11-09.
- `S/PV.1543(OR)` has 1963-12-26; its neighbours are around 1970.
- `A/RES/2778(XXVI)` has `date_other = 1970-12-16`. The text cites resolution 2733 C (XXV) of 16 December 1970; the resolution itself is from the 26th session (1971).
- `date_other` is `YYYY-01-01` in 277 `S/PV` rows and 123 `A/RES` rows. These look like year-only values.

## 5. Old General Assembly resolutions can contain neighbouring resolutions

For 1970s and 1980s `A/RES` rows, many bodies contain headings of other resolutions. Example: `A/RES/36/231` (scale of assessments) also contains `36/232` and `36/233`; a sentence about the "power and responsibility to protect members of their staff" is in 36/232. By a simple test (a heading `NN/NNN.` of another resolution inside the body), this affects 676 of 1,716 rows from the 1970s, 902 of 2,097 from the 1980s, 46 of 2,273 from the 1990s, and none after 2000. The official PDF for `A/RES/36/231` is also a book spread, so this seems to come from the source PDF, not from extraction.

## 6. A note on the card's OCR description

The card says the OCR documents are "mostly General Assembly supplements from around 1950". By symbol family, 1,532 of the 1,864 OCR rows are `A/RES` (82%). By decade, the OCR share is 20% for the 1980s (659 of 3,231) and 13% for the 1990s (732 of 5,641). This may simply mean the card describes the largest items, not the largest count. We mention it because it affects word searches in those decades.

## What we did not check
- We did not open the PDFs for items 1 and 2 beyond a few rows.
- Our French test (item 2) and our neighbour-heading test (item 5) are simple heuristics.
- We did not try to fix anything.

(No attribution line is needed in the final post; hfu decides how to present it.)
