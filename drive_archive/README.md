# Drive Archive — Past Records

Verbatim archive of the operation's Google Drive record folders, pulled in so
every past record is referenceable inside the repo. Scope: **agronomy /
field records only** — crop, soil, water, fertilizer/amendment, and mapping
records. Office/payroll/business files (wages, time cards, billing credits,
base-station configs) are intentionally excluded.

Structure mirrors the Drive folders:
- `hamstra/` — from Drive "Hamstra files"
- `tevelde/` — from Drive "Tevelde files"
- `correia/` — from Drive "Correia crop files"

## How each record is stored
- **`<file>.extract.md`** — a text/CSV extraction of the spreadsheet or PDF.
  This is the agent-referenceable copy of the data and exists for (almost)
  every file, regardless of the original's size.
- **`<file>`** (the original binary) — present when the source was small
  enough to embed. Large binaries (field-map PDFs, big scans) may have only
  the `.extract.md` plus a link in `MANIFEST.csv`; pull the original from
  Drive when the full-fidelity file is needed.
- **`MANIFEST.csv`** (per ranch) — index of every archived source file and
  which artifacts (binary / text extract) are present.

## Status (2026-08-11)
- **tevelde/** — complete (75 source files: 2024–2027 crop workbooks, soil
  sample PDFs, water-usage planners, gyp orders, field maps, crop planning).
  Mirrors Drive faithfully, including a nested `Tevelde/` subtree that Drive
  itself duplicates.
- **correia/** — complete (46 source files: 2020–2026 corn/wheat/alfalfa +
  almond/walnut workbooks, soil samples, water usage, gyp orders). Two
  purely financial sheets (crop buyers, wheat expenses) excluded per the
  agronomy-only scope.
- **hamstra/** — complete catalog (241 agronomy files in `MANIFEST.csv`,
  each with a Drive `view_url`), mirroring the tree (year folders 2010–2026,
  soil samples, nutrient management, pump data, field records). Text extracts
  captured for **all 147 modern `.xlsx` / PDF / `.doc` records** plus the
  data-bearing large soil-sample and corn-plot PDF scans. Office/payroll/
  equipment-admin files (wages, time cards, bill credits, base-station
  channels, tractor hours, equipment-setup folder) excluded per scope.

### Known gap — legacy `.xls` files
65 legacy `.xls` workbooks (mostly 2010–2013) are cataloged with working
Drive links but have **no text extract**: the Drive text tool cannot read the
old `application/vnd.ms-excel` format. Most of their content is superseded by
`Hamstra/Hamstra Corn Summary 2008-2026.xlsx` (extracted — the canonical
per-field yield/N/irrigation history back to 2008) and the per-year `.xlsx`
workbooks. To capture the `.xls` data at full fidelity, download the binaries
from Drive and convert locally with a spreadsheet library (`xlrd`) — a
follow-up pass can do this on request.

Also link-only (image scans, little text value): field-map PDFs/JPGs, well-
completion / WCR / linked-wells report scans. These carry a `view_url` in the
manifest.

Original source of record remains Google Drive under `Claude/`; this archive
is a point-in-time copy for reference and offline computation.
