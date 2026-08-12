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
The bulk download ran as three background workers and was interrupted by an
API session limit partway through:
- **tevelde/** — complete (75 source files: 2024–2027 crop workbooks, soil
  sample PDFs, water-usage planners, gyp orders, field maps, crop planning).
  Mirrors Drive faithfully, including a nested `Tevelde/` subtree that Drive
  itself duplicates.
- **correia/** — complete (46 source files: 2020–2026 corn/wheat/alfalfa +
  almond/walnut workbooks, soil samples, water usage, gyp orders). Two
  purely financial sheets (crop buyers, wheat expenses) were excluded per
  the agronomy-only scope.
- **hamstra/** — **incomplete.** Only `Gyp field dates.xlsx` was captured
  before the limit hit. The full Hamstra tree (year folders 2010–2026, soil
  samples, field maps, crop workbooks) still needs to be pulled — office
  files there (wages, time cards, bill credits, base-station channels,
  equipment setup) will be excluded. Resume after the API limit resets.

Original source of record remains Google Drive under `Claude/`; this archive
is a point-in-time copy for reference and offline computation.
