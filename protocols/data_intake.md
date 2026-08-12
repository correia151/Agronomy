# Data Intake Protocol — how new records enter the database

The database is the set of CSVs under `data/`. Every new report, yield, or
field event gets appended to the right table, committed with a message saying
what arrived and from where. **Append, don't rewrite** — corrections get their
own commit explaining why (per CLAUDE.md).

Query it anytime: `python scripts/db.py field hamstra 9`

## Where each kind of record goes

| When you receive… | Do this |
|---|---|
| **Valley Tech soil report (PDF)** | File PDF in `data/soil/raw/` as `YYYY-MM-DD_ranch_field.pdf`; add one row per field per depth to `data/soil/soil_panels.csv` (keep `na_pct_spe` and `na_pct_cec` separate — never blur). `scripts/parse_valleytech_pdf.py` helps extract. |
| **Tissue / leaf sample** | Row in `data/soil/tissue_samples.csv`. July leaf samples for almonds/walnuts; corn ear-leaf at silk. |
| **Corn or wheat silage yield** | Row in `data/yield/corn_silage_history.csv` / `wheat_silage_history.csv` with `yield_asreported_tac` + `moisture_asreported`; compute `yield_70pct_tac` (× (1−moisture)/0.30). Verify: `python scripts/normalize_moisture.py --check`. |
| **Alfalfa cutting (hay sale sheet)** | Row per field in `data/yield/alfalfa_cuttings_2026.csv` (new file per year: `alfalfa_cuttings_YYYY.csv`). |
| **Almond / walnut harvest** | Row in `data/yield/orchard_history.csv` (state yield units — kernel lb, in-shell, tons). |
| **Irrigation set / water run** | Row in `data/irrigation/irrigation_events.csv`: date, source (fresh/lagoon/blend), total ac-in, lagoon ac-in, event type (pre_irrigation / in_season / leaching / water_up). **Lagoon inches are the sodium ledger — record them even when total is estimated.** |
| **Lagoon or well water test** | Row in `data/water/lagoon_panels.csv` (note draw depth!) or well data per `data/water/well_registry.csv`. |
| **Gypsum / sulfur / lime applied or ordered** | Row in `data/inputs/gypsum_applications.csv` (`applied` true/false distinguishes done vs booked). |
| **Fertilizer event (sidedress, water-run, starter)** | Row in `data/inputs/fertility_programs.csv` with date, product, rate, units. |
| **Planting / variety assignment** | Update the field's row in `data/reference/field_registry.csv`; planting date goes on the yield row at harvest, or in notes meanwhile. |
| **New field / renumbering / acreage change** | `data/reference/field_registry.csv`, with the old name in `aliases`. |

## Rules that keep the database analyzable
1. **State the moisture basis on every silage yield.** 70%-standard column is
   the only cross-comparable number (CLAUDE.md hard rule).
2. **Dates ISO (`YYYY-MM-DD`)**, field IDs from `field_registry.csv` (aliases
   listed there), rates per acre.
3. **Measured vs book:** if a number is an estimate or UC default, say so in
   `notes`. Analysis treats them differently.
4. **Keep the raw source.** PDFs into `data/soil/raw/` or `data/water/raw/`;
   spreadsheets that arrive by email can go into `drive_archive/` inbox
   folders. The CSV row cites its source.
5. **Trough discipline:** post-harvest soil samples are annual troughs
   (post-crop, pre-amendment) — enter the sample date so the analysis knows.

## The learning loop
Once new data is in, run the agents (see `.claude/agents/`):
- **soil-scientist** — reads new panels against history; flags trends
  (EC/SAR creep on lagoon fields, K mining under alfalfa, Ca%CEC shifts).
- **agronomist** — correlates yields against practices (planting date,
  variety, rotation position, N budget, irrigation cadence, harvest timing)
  and drafts next-season recommendations.
Their writeups go in `analyses/` (dated, append-only). Recommendations become
deliverables only after Eric confirms (CLAUDE.md).
