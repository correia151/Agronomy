# Migration Notes — Drive → GitHub (2026-08-11)

Migration executed per the repo blueprint (`Correia Field Intelligence —
GitHub Repo Blueprint & Migration Map`, prepared 2026-08-11). GitHub is now
the system of record; Drive is the inbox/outbox.

## Migrated (authoritative versions, byte-for-byte from Drive)

| Repo file | Drive source |
|---|---|
| rulebook/correia_field_intelligence_rulebook.md | `Correia_Field_Intelligence_Rulebook.md` (31.4 KB copy in soil folder — the authoritative one) |
| rulebook/tevelde_agronomy_agent_rulebook.md | `TeVelde_Agronomy_Agent_Rulebook.md` |
| rulebook/locked_decisions_2026.md | `★ Correia_2026_LOCKED_DECISIONS_rev2.md` (rev2 = only version) |
| ranches/tevelde/intelligence.md | `TeVelde_Field_Intelligence_rev3.md` (rev3 = only version) |
| ranches/hamstra/intelligence.md | `Hamstra_Soil_Intelligence_2026.md` (rev2, created 8/7 14:08 — the authoritative copy) |
| ranches/hamstra/salt_management_protocol.md | `Hamstra_Salt_Management_Protocol.md` |
| ranches/hamstra/gypsum_x_yield_analysis.md | `Hamstra_Gypsum_x_Corn_Yield_Analysis.md` |
| ranches/hamstra/alfalfa_cutting_log_2026.md | `Hamstra_Alfalfa_2026_Cutting_Log.md` (narrative kept; data also in CSV) |
| analyses/2026_hamstra_vs_correia_comparison.md | `Hamstra_vs_Correia_2026_Comparison.md` |

## Built at migration (from data documented in the files above)

- **data/yield/corn_silage_history.csv** — 147 field-year records: Hamstra
  2022–2026, TeVelde 2025–2026, Correia 2025–2026. All rows carry
  `yield_asreported_tac` + `moisture_asreported` + computed
  `yield_70pct_tac` (70%-moisture standard). Verify with
  `python scripts/normalize_moisture.py --check`.
  *This is a partial build of the 318-record crown jewel — see Pending.*
- **data/yield/alfalfa_cuttings_2026.csv** — July 2026 dry chop, field 32
  entered with tons empty, "pending confirmation."
- **data/yield/wheat_silage_history.csv** — TeVelde 2025 per-field +
  Hamstra ranch averages 2016–2025. 2026 wheat never recorded (backfill).
- **data/soil/soil_panels.csv** — 61 rows from all Valley Tech panels
  tabulated in the knowledge files (Hamstra 07-30S163333/163335; TeVelde
  07-17S126819, 07-31S128625, 05-11S153673, Rosa 07-25S127449 +
  07-31S128628; Correia 07-30S163338, 07-20S161861 partials).
  `na_pct_spe` and `na_pct_cec` are separate columns — never blur them.
- **data/inputs/gypsum_applications.csv** — Hamstra fall-gyp history
  2021–2024 (field lists from the gypsum×yield analysis), fall 2026 Hamstra
  plan, Correia 2026 booked order (531 T / 493 ac), TeVelde 2026 plan.
- **data/water/well_registry.csv** + **ranches/tevelde/well_summary.md** —
  38 wells from `Bernard_Tevelde_Well_Summary_ALL`. **Note:** the Drive
  sheet is a *well registration* export (locations/GSA/APN), not water
  quality — the blueprint's `well_water_quality.csv` has no source data
  yet; well-water nitrate is still an open gap.
- **data/reference/field_registry.csv** — all three ranches, R1–R14
  renumbering, "Dairy" = R1–R4 (47 ac), fall 2026 rotation, 4th-yr stands.
- **data/reference/variety_registry.csv** +
  **data/reference/hamstra_2020_variety_trial.csv** — from
  `Hamstra Corn plot 2020` sheet (Pioneer local experiment, 11 hybrids).
- **data/reference/tevelde_2026_projected_harvest_dates.csv** — from
  `Dixie Creek Projected Harvest Dates.pdf`.
- **ranches/hamstra/diagnostics/fields_11_14_17_lagoon_valve_protocol.md**,
  **protocols/paired_sampling_protocol.md**,
  **protocols/soil_sampling_sops.md** — assembled from the salt protocol,
  locked decisions, and rulebook.
- **ranches/correia/intelligence.md** — roster + pointer; the authoritative
  Correia program is `rulebook/locked_decisions_2026.md`.

## Pending / not migrated

1. **`files hamstra.zip` / `files hamstra 2.zip`** — contain
   `Fall_2026_Gyp_Order.xlsx`, `2026_Hamstra_Gyp.xlsx`, and a rulebook copy.
   The xlsx files were not parseable through the Drive tooling (the
   comparison doc also flagged `2026_Hamstra_Gyp.xlsx` as "unreadable at
   time of writing"). The gypsum CSV was built from the documented tables
   instead. **Action: re-export or open these xlsx locally, verify nothing
   is double-booked against data/inputs/gypsum_applications.csv.**
2. **318-record corn silage history** — source workbooks (per-ranch
   field-intelligence workbooks, Wheat History, Year-by-Year sheets) not in
   the migrated set. The CSV currently holds the 147 documented records.
3. **Valley Tech raw PDFs** → `data/soil/raw/` — file as they are pulled
   from `Claude/Hamstra files/Hamstra Soil Samples/` (2011–present archive).
4. **Correia 8-page gypsum/fertility PDF** → `deliverables/`.
5. **Hamstra per-field wheat yields 2016–2025** — in source workbooks.
6. **Superseded Drive files were NOT trashed** (destructive; do manually):
   TeVelde rev1 `1DiL4VZRr3VhZej7Mzk8A--eKcvz4huUT`, rev2
   `1EMCt44YeDinu6BtqUYUWDt_C2vMSwRMt`; locked decisions 7/29
   `1GLq4i4yDcLrQn1FoVlSSYnAPmDauYxqQ` and 8/7
   `1rZpnU1PXkzyT2e_4PsyAG0EACdbxZxe7`; Hamstra intelligence rev1
   `1dCtkAecacudNof30eltEhUzm19PPnr_k`; root Google-Doc rulebook
   `1yeuBbvkDYK4eBUZEUsuNBlj91d3TAR2Ooy6YsLBc-HE`.
7. **`MOVED_TO_GITHUB.md` note in the Drive project folder** — not written
   (outward-facing; do manually or ask for it explicitly).
8. **Claude Project instructions** — update to reference this repo as
   system of record.

## First agent tasks worth running (from the blueprint)
1. Ca%CEC vs. yield regression across all three ranches on the unified CSV
2. Post-alfalfa bump re-estimate on the standardized moisture basis
3. Sidedress-rate response surface split by residual-N class
4. Field 11 post-harvest sample (after ~9/13) → first new panel parsed
   straight into soil_panels.csv
5. Fields 11/14/17 diagnostic results → paired-sample writeup in analyses/
