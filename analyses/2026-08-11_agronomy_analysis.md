# Yield & Practices Analysis — Unified Dataset (2026-08-11)

First repo-based analysis on the unified CSVs. All silage yields below are the
**70%-moisture standard column (`yield_70pct_tac`)** unless explicitly noted;
68%-basis records are already converted in that column (×1.0667). n = 147 corn
field-years (Hamstra 108, TeVelde 25, Correia 14), 2022–2026; wheat 18 records;
alfalfa 14 cuttings (2026). Practice fields (variety, planting date, sidedress,
lagoon inches) are populated only for 2025–2026 rows — everything older is
yield-only in the unified file (the practices exist in `drive_archive/`
workbooks; see §5). Confound warning applies throughout: **rotation, planting
date, and soil have never varied independently in this record.** Locked
decisions (rev. 2026-08-07) are respected absolutely.

---

## 1. Yield-lever quantification (unified dataset, 70% basis)

### 1.1 Crop slot: single-crop vs double-crop — the dominant managed lever

| Group | n | Mean T/ac @70% |
|---|---|---|
| Early single / single crop | 36 | **39.85** |
| Double-crop | 93 | **33.04** |
| (system not recorded: 2025 TeVelde + Correia) | 18 | — |

Within Hamstra only (same ranch, both systems every year, 2022–2025):
single 43.16 (n=11) vs double 33.04 (n=93) → **gap ≈ 10.1 T/ac @70%**
(by year: 2022 +13.0, 2023 +5.2, 2024 +12.0, 2025 +10.2). This matches the
rulebook's ~9 T slot penalty (86/50 heat at June-planting pollination).

Standardization refinement: on the as-recorded basis "every 40 T+ result was
single-crop." On the 70% column, five Hamstra double-crop field-years cross 40
(15-2023 41.0; 9, 18, 40, C1 in 2025 at 40.8–43.0). The ceiling story holds —
no double crop exceeds 43.0 while the single-crop mean is 43.2 and the top
singles run 45.4–48.4 — but the categorical claim should be retired in favor
of: **double-crop caps ~43 @70%; single-crop routinely exceeds it.**

### 1.2 Rotation position (dominant lever, thin explicit data)

`prior_crop` is populated for only 17 of 147 rows, so the 20-year rotation
finding rests on documented cases, not a dataset-wide regression:

- **Correia V15** (post-alfalfa yr 1/yr 2): 42.02 vs peer mean 32.80 (n=6) =
  **+9.2 T** in 2025; 38.90 vs 33.20 = **+5.7 T** in 2026. (Locked decisions
  quote +8.6/+4.9 vs ranch avg including V15; peer-excluded is the cleaner
  contrast.) Confounded with V15 being the heaviest ground (CEC 20.9).
- **Hamstra 9, 2026** (rotation behind it, per rulebook §3): 43.37 vs 39.67
  mean of the three matched 1718 fields planted the same week (29, 36, 24&25)
  = **+3.7 T** with variety and date controlled.
- **Correia V7, 2026** (post-alfalfa + pit sludge): 30.78, **−2.9 T below
  non-alfalfa peers** — the bump erased the moment salt was reintroduced.
  Mechanism is physical/salt-related, not fertility (locked §1, §4).

### 1.3 Variety (year-and-ranch controlled where possible)

| Comparison | n | Effect @70% |
|---|---|---|
| 1718 vs 2089, TeVelde 2025 | 6 vs 5 | 35.05 vs 33.26 → **+1.8 T** |
| 1718 vs 2089, TeVelde 2026 (all single-crop) | 11 vs 2 | 39.56 vs 37.97 → **+1.6 T** |
| 18986, TeVelde 18, 2026 | **1** | **48.11** — operation record; +8.5 over same-year 1718 mean, but n=1 on the ranch's best exchange chemistry (Ca%CEC 88–90) with sludge fertility. Trial-expand, do not bet on it. |
| 2089 vs 1718, Correia 2025 | 2 vs 4 | 36.01 vs 33.77 — **reversed**, but 2089 sat on the A-block and 1718 included rehab/salt fields; field identity confound, not a variety signal |
| Wheat: Pacheco vs 158, TeVelde 2025 | 8 vs 3 | 25.2 vs 23.5 → **+1.7 T** (moisture basis undocumented — direction reliable, magnitude soft) |

Historical double-crop table (as-recorded basis, from the rulebook): 1718 35.3
(n=5) > 2089 33.4 (n=32) > 1828 32.7 (n=44) > 1759 31.7 (n=21) > 1359 31.2
(n=22) > **1870 30.4 (n=55, phase out)**. Variety spread is 2–3 T; the slot
spread is ~10. **Slot beats seed.**

### 1.4 Planting-date gradient within 2026 — no gradient inside March

All 2026 plantings with dates fall in a Mar 11–25 window:

- TeVelde (n=14): slope +0.07 T/day, r = 0.10 (excl. field 18: +0.11, r = 0.24)
- Hamstra (n=4): slope −0.40 T/day, r = −0.47 (rotation-confounded by field 9)
- Correia (n=7): slope +0.47 T/day, r = 0.53 — **spurious**: V15/V5 (best
  ground) planted late-window, the A-block (weakest, unexplained 2026 drop)
  planted earliest.

**Within a two-week March window, planting date does not measurably move
yield.** The date lever is the *slot* (Feb–Apr vs June), consistent with the
killed hypothesis in locked §0 (days-to-silk moved ~1:1 with date; cold-soil
compression is dead). Do not chase 3–4 days in March; do keep fields out of
the June slot.

### 1.5 Ranch ceilings on the standardized basis

| Ranch | 2026 corn mean @70% (n) | 2026 max | All-record mean (n) |
|---|---|---|---|
| Hamstra (early singles only harvested) | **40.59** (4) | 43.37 | 34.35 (108) |
| TeVelde (all single-crop 2026) | **39.95** (14) | 48.11 | 37.43 (25) |
| Correia (7 early fields) | **34.01** (7) | 38.90 | 34.07 (14) |

Standardization narrows the Hamstra–TeVelde gap to ~0.6 T on 2026 singles
(the prior "40.6 vs 37.25" comparison mixed 68% and 32%-DM bases). **Correia
sits ~6 T below both dairies on the same operator, same varieties, same
window** — the soil bank (OM/CEC, no dairy-manure history) sets the ceiling;
fertility gets a field TO its ceiling, not past it. Caveat: Hamstra's 2026
mean is its four best (early) fields only; its double-crop 2026 fields were
still standing at data close.

---

## 2. Blueprint first tasks

### 2.a Ca%CEC vs yield across ranches — TeVelde computable, others blocked

Pairing `soil_panels.csv` base-saturation Ca with 2026 yields @70%:

- **Dixie core (n=9 pairs, 2025 pre-plant panel → 2026 yield): r = 0.80,
  slope ≈ 0.5 T per Ca%CEC point.** Adding the R-block (R1–R4 composite, R5,
  R14; n=12): r = 0.80. Excluding field 18 (18986 + sludge fertility, the
  extreme on both axes): **r = 0.54, slope ≈ 0.4 T/point** — the relationship
  survives its strongest point, weaker but present.
- Top three Ca%CEC fields (18, 20N, 12 at 77–90%) = top three yields; lowest
  (14 at 68.1%) landed mid-pack despite the biggest N bank on the panel (248
  ppm NO₃, 4.3% OM). Soluble Na% does NOT rank yields (18 was worst-Na and
  best-yield). Confirms the rev-3 intelligence finding on the actual numbers.
- **Cross-ranch check is blocked:** the 2026 Hamstra panels in the CSV carry
  Na%CEC but **no Ca%CEC**, and the Correia rows have CEC but no base
  saturation. Until those columns are filled from the raw PDFs, "Ca%CEC
  predicts yield" is proven on one ranch (two datasets) only. Field 7
  (Ca%CEC 59–63) remains the 2027 low-confidence field this predicts.

### 2.b Post-alfalfa bump re-estimated on the standardized basis

All Correia records are natively @70%, so the standardized re-estimate equals
§1.2: **+9.2 T (yr 1) and +5.7 T (yr 2) vs peers, ≈ 15 T cumulative on V15**
— slightly larger than the locked file's 10–13 T two-year figure because the
peer mean excludes V15 itself. Halve it if being conservative (CEC-20.9
confound); still the largest effect in the record. Supporting, not proof:
Hamstra's 2025 early trio 16/28/31N made 45.4–47.5 @70%, and field 16 carries
a documented post-alfalfa residual signature (547 lb N, June 2026) — but the
CSV does not record their 2025 rotation positions, so they stay out of the
estimate. **Per locked §3: the bump is physical, arrives with a K hole and NO
N surplus. No N cut on post-alfalfa ground — this binds the entire Hamstra
2027 pool and V4 in 2028. No alfalfa-return assumptions beyond V4 (2028).**

### 2.c Sidedress response by residual-N class

From `fertility_programs.csv` + panel residuals + yields @70%:

| Class | Fields (residual basis) | Sidedress | Yield @70% |
|---|---|---|---|
| High-residual, zero sidedress | TeV 5 (54–122 ppm), 8 (31–44), 17 (76–83), R5 (no NO₃ on panel) | 0 u | **38.51 mean (n=4)** |
| Low/mod-residual, fed | TeV 20N (25 ppm), 10 (no panel) | 150 u | **39.30 mean (n=2)** |
| Low-residual, no lagoon | Correia V15 2025 (140 lb spring profile) | ~245 u total | 42.02 |
| Same field, cut | Correia V15 2026 | ~185 u total | 38.90 |

Read: **+0.8 T for 150 units on dairy ground** — below measurement noise;
matches the historical <75u = 31.2 vs 140u+ = 32.4 (as-recorded) finding.
On low-residual no-lagoon ground the V15 pair suggests ~3 T rode on ~60
units — confounded with year-2 rotation decay (one field-year cannot separate
them), but N was the only input that changed and the mass balance fits at
both ends. **Operational rule confirmed: don't buy N for yield on banked
fields; don't starve clean ones; PSNT before first lagoon water; 75-unit
floor waived on measured 300+ lb residual, kept on low-residual no-lagoon
ground.** Gap: Hamstra 16 (75u on 547 lb) and C1 (200u) have 2026 fertility
records but no 2026 yield rows — enter them at harvest close to extend this
table.

---

## 3. 2027 crop-plan draft — **DRAFT — pending Eric's confirmation**

### 3.1 Post-alfalfa pool: Hamstra 1, 2, 3, 4, C-3 (~158 ac of 4th-yr stands)

- **Terminate field 3 first** (weakest stand, 1.45 T/ac July cutting), then
  2, 1, 4, C-3 (1.67–1.74) as harvest scheduling allows.
- **Soil-sample all five at termination** (none has a panel newer than
  Dec-25). Request full base saturation — this also unblocks §2.a at Hamstra.
- **Variety/slot: 1718, earliest single-crop window (March, Feb pre-irrigated
  where ground allows).** The head start is wasted on late planting or weak
  genetics; never 1870 (or 1608 on this heavy-manure ground). These five are
  the only rotation-bonus acres of 2027 — the ~+9 T yr-1 effect (§2.b) is
  worth more than any input decision on the plan.
- **Nitrogen: NO automatic cut (locked §3).** Spring-profile each field,
  budget to the 40 T target (333 lb N) via the full mass balance. Expect
  large-but-variable residuals (16-style 300–550 lb is possible — waive the
  floor only on a measured number).
- **Potassium: budget UP** — 4 years of alfalfa removal (~600 lb K₂O/ac/yr at
  10 T) mines the exchange even on high-K Hamstra ground; check panels at
  termination (field 42's 303-ppm-and-falling is the template).
- **Gypsum: none first year out of alfalfa** (cadence rule — rotation
  artifact, not a missed pass). No sulfur ahead of or on new stands.
- Fall 2026 seedings (11, 29, 36): fresh-water leach the seedbed before
  planting (11's valve-end checks especially; field 9 proved leaching works
  here), no lagoon through establishment, field 11 pre-plant sample still
  outstanding.

### 3.2 Correia V15 / V5 programs (per locked decisions — restated, not relitigated)

- **V15 (yr 3 post-alfalfa): target 36–38 T, not 40.** Run the 2025 N
  program: **~200 units at sidedress + a real 40–50u water-run** (not 150 +
  2×17.5u); spring-profile first. Full 20 T manure (queue priority 2), K
  replacement basis ~325–350 lb K₂O against removal — stop chasing the %CEC
  floor. Zinc 10 lb. 1.0 T gypsum as booked (infiltration insurance — first
  ton to cut if the order trims; watch winter water advance). **Never
  Tiger 90** (pH 6.6).
- **V5: harvest timing is the whole lever.** 2026 cut 7 days short of the
  2,500-GDD target and still made 37.26 on the cleanest chemistry. Let it run
  4–5 more days in 2027; chop on moisture (32–38% DM, target ~35%), not the
  calendar. No fertility change indicated. (Same instruction applies to V8,
  −8 days in 2026.)
- Rest of ranch per locked file: V8 East manure priority 1 + MAP band +
  Tiger 90 400–500 lb; skip V8 West entirely; V14 full rehab program with
  sulfur at sidedress (its sulfate is low); V7 = 1.0 T gyp + **mandatory
  winter leach** + pre-plant re-sample, no fertility dollars; A4 HOLD until
  the ~January farming decision; V4 protected (fresh water only, no sludge,
  **sample during the 2027 alfalfa year — hard deadline**).

### 3.3 Harvest-timing rule (all ranches)

GDD targets on Open-Meteo Tulare (36.2077, −119.3473), 86/50 method: **2,500
GDD for pre-May-1 plantings, 2,800 for May-1-and-later. Do not use CIMIS**
(~200 GDD cool per season against these calibrated targets). TeVelde V5/V8
2026 (−180–200 GDD) is the standing example of the cost. Confirm with
whole-plant moisture before the chopper moves.

### 3.4 Strip trials worth running in 2027 (trial discipline: one variable, split field, one scale ticket per half)

1. **Sidedress-rate strip on a measured high-residual field** (a Hamstra
   post-alfalfa pool field after spring profile, or TeVelde 6S at ~141 ppm):
   0/75/150u strips, same variety. Directly prices the floor policy — §2.c
   currently rests on n=4 vs n=2 across different fields.
2. **18986 vs 1718 split field at TeVelde** on ordinary (not field-18)
   chemistry. Converts the 45.1 n=1 into a decision before any acreage bet.
3. **Winter-slot dicot trial:** pea or pea-triticale in place of wheat on one
   continuous double-crop Hamstra field, corn yield measured 2027. The only
   grass-break lever available now that alfalfa is ending; costs one field's
   wheat tonnage to test the corn return.
4. **Deep-rip one field (V7 or A4) before committing the ranch** (locked §1)
   — probe first; rip only if the penetrometer finds a pan.
5. **Sulfur-at-sidedress on Hamstra 25** (S LOW, B LOW, ran dry 2026): keep
   the 75u floor + sulfate S there; cleanest test of the S finding on the
   reference ranch. (Note: Hamstra's AS/ATS status differs from Correia's
   locked no-AS/ATS constraint, which is Correia-only.)
6. **No-gyp check strip on one uniform maintenance-rate field** — the
   standing unfalsifiable-input discipline; gypped-vs-not was dead even
   (33.3 vs 33.4) in the 2025 continuous-field comparison.

---

## 4. Irrigation recommendations

### 4.1 Cadence by ground type (ET-based, Open-Meteo)

- Corn Kc ~0.3 → 1.15–1.2 at canopy closure; peak July ETc ~0.33–0.40 in/day;
  flood sets ~4–5 ac-in (fresh ≈ 5 ac-in/set per the Hamstra workbook legend).
- **High-AWC / high-CEC ground (Hamstra heavies, V15 at CEC 20.9): 10–12 day
  cadence holds.**
- **Light ground (CEC ~9–13: A4 9.5, V7 13.3): usable water ~1.6–2 in →
  8 sets at 8–9 days, not 6 at 11–12.** A4's 12-day gap (5/18→5/30) running
  into silk is the standing example — the one field where the fixed-interval
  critique survived (locked §0).
- **Intolerant windows: V12–V17 (ear size, kernel rows) and silk.** Shorten,
  never stretch, the interval there; high-yield fields carry water ~3.5 days
  longer into grain fill (terminal dry-down finding).

### 4.2 Lagoon-water sequencing discipline

- **Sequence rule: manure water EARLY in pre-irrigation; FRESH water as the
  last pass before planting** — the fresh flush pushes salt below the seed
  zone. Never pre-irrigate with manure water alone (TeVelde 18 fresh-flush
  success vs "irrigated manure water only and got burnt coming up").
- **Past ~2 ac-in lagoon adds sodium, not yield.** Every event ≈ 70 lb avail
  N + 98 lb K₂O + **32 lb Na** per ac-in (1.25 ac-in event ≈ 88 lb N, 40 lb
  Na). Credit the N in the sidedress math; ledger the Na.
- **No lagoon on new alfalfa through establishment** (11, 29, 36 this fall;
  V4's stand — stop or dilute if running), none on orchard blocks, no
  dormant-season manure water ahead of winter rain (Dairy General Order).
- **On lagoon ground, gypsum is scheduled with a winter leach or not at all**
  (locked §1). Protect the February fresh pre-irrigation as a real leaching
  set (V15 2/26/25, 2/9/26; Hamstra 9's Jan set cut Na 30.2→18.5 %SPe). V7's
  2026-27 leach is mandatory. Verify Greater Kaweah's ET-billing treatment of
  winter leach water before building the program on it (locked open gap #2).
- PSNT before the first lagoon event, every field, every year.

### 4.3 What to log in `data/irrigation/irrigation_events.csv` (3 rows today)

Log **every set, every field**, in the existing schema — one row per event:
`date` (actual, not planned) · `water_source` (fresh / lagoon_blend / sludge)
· `total_ac_in` (measured or the 4–5 ac-in set default, flagged which) ·
`lagoon_ac_in` (the 1.25 ac-in "\*" events; sludge loads too) · `method` ·
`event_type` (pre_irrigation / in_season / water_run_n / winter_leach) ·
`notes` (UN-32 units on water-runs — the workbook `*`/`**` legends changed
meaning between 2025 and 2026 and this column kills that ambiguity; crop
stage at the set, e.g. V12/silk). The 2026 workbook irrigation-date grids can
backfill this season in one pass. With one year logged, next year's analysis
can correlate interval length × stage and lagoon inches × Na trend × yield —
the correlations this report cannot run today.

---

## 5. Data gaps blocking better analysis — ranked by value

1. **Migrate practice columns for pre-2026 field-years** (variety, plant
   date, sidedress units, lagoon events sit in `drive_archive/` corn
   workbooks — verified against the 2025 Hamstra extract — but are blank in
   the unified CSV for 130 of 147 rows). Unblocks variety × slot × year
   regression on the full record instead of 2-year slices.
2. **Populate `prior_crop` / rotation position for all field-years.** The
   operation's dominant lever currently rests on 3 documented cases (§1.2).
   Eric's memory + the year-by-year workbooks can rebuild most of it.
3. **Ca%CEC (full base saturation) for Hamstra and Correia panels** — blocks
   the cross-ranch test of the best yield predictor found so far (§2.a).
   Cheap: it's on the raw Valley Tech PDFs or one lab request.
4. **2026 wheat yields — never entered** (Hamstra note says backfill from
   scale tickets; TeVelde 750 ac cut Apr–May 2026). Half the double-crop
   ledger is missing, so slot economics (corn gain vs wheat loss) can't be
   priced.
5. **Irrigation event log** (§4.3) — 3 rows today; the water-to-yield
   correlation is impossible until this exists.
6. **Missing 2026 yield rows for fields with fertility records** (Hamstra 16
   @75u/547 lb, C1 @200u; Hamstra 2026 double-crop harvest when chopped;
   TeVelde R1–R4 per-field split of the composite).
7. **V4 sampling during the 2027 alfalfa year** — locked hard deadline; not a
   modeling gap but the single most consequential scheduled measurement.
8. **Acres for pre-2025 records** — all historical means here are unweighted
   field means, not production-weighted; acreage columns would fix that.
9. **TeVelde field 10 soil panel; field 18 post-sludge resample; Hamstra 11
   pre-plant sample** — each blocks one named 2027 decision.

### The three measurements that most reduce uncertainty

1. Spring N profiles on all five Hamstra post-alfalfa fields (sets the whole
   2027 N program and tests the no-surplus rule at n=5 instead of n=1).
2. Full base saturation on every 2027 panel, all three ranches (tests the
   Ca%CEC ceiling model where it matters).
3. One season of complete irrigation logging (§4.3).

---

*All recommendations in §3–4 are DRAFTS pending Eric's confirmation. Sources:
`data/yield/corn_silage_history.csv` (70% column), `wheat_silage_history.csv`,
`alfalfa_cuttings_2026.csv`, `data/inputs/*.csv`, `data/soil/soil_panels.csv`,
`data/reference/*.csv`, ranch intelligence files rev. 08-07/08-08,
`rulebook/locked_decisions_2026.md` rev. 08-07, and the 2025 Hamstra corn
workbook extract in `drive_archive/` (practice verification only).*
