# Soil-State Assessment — All Three Operations (2026-08-11)

**Prepared by:** soil-scientist agent · **Basis:** data/soil/soil_panels.csv (61 panel rows),
data/inputs/gypsum_applications.csv, data/water/lagoon_panels.csv, data/yield/corn_silage_history.csv,
drive_archive Valley Tech extracts (12-11S143167 Dec-2025; 2011 scans 08-29S725, 09-26S1029).
All values below are **measured Valley Tech numbers with sample dates** unless labeled *book*.
Yield comparisons on the stated basis per row; cross-ranch only at 70% std per CLAUDE.md.

**Data inventory:** Hamstra — 6 panels on file in CSV (all 07-30-26) + 13-field Dec-2025 report
(12-11S143167) in drive_archive only, **not yet parsed into soil_panels.csv**. TeVelde — 48 panel
rows, 2024-07 → 2026-05. Correia — 7 rows (07-20-26, 07-30-26), several partial. No tissue samples
on file (tissue_samples.csv empty).

---

## 1. Per-ranch soil state and binding constraint

### Hamstra — binding constraint: SALINITY (EC), not fertility, not sodicity
Fertility is banked everywhere sampled: Olsen-P 70–130, K 388–1,010 ppm, Zn 2.5–12.0 (six panels,
07-30-26). The money is in *not* over-applying. Exchange is Ca-dominant; Na 1.8–3.5 %CEC across all
six 2026 samples. Deviating fields:

| Field | Number (date) | Deviation |
|---|---|---|
| 29 | EC 2.02 (12-11-25) → **2.88** (07-30-26); ~392 lb residual N | Highest EC on ranch; going to **fall alfalfa** (threshold ECe ~2.0) |
| 23 | EC **3.20**, free lime 2.07% (12-11-25) | Ranch-high EC despite 2022+2024 gypsum; no 2026 resample |
| 24 | EC 2.92 (12-11-25) → 1.79 (07-30-26) | Recovered; cleanest Na on ranch (14.3 %SPe) |
| 25 | NO3-N ~39 lb, SO4-S **35 LOW**, B **<0.1 LOW**, EC 0.82 (07-30-26) | Mined tank — crop ran empty late season |
| 36N vs 36S | Residual N ~301 vs ~119 lb; Zn 2.5 vs 4.7 (07-30-26) | 2.5× fertility split inside one field; Zn at row-crop floor on N half |
| 9 | Na 30.2 → **18.5 %SPe** in 7 months (12-11-25 → 07-30-26) | Improving — leaching proof; first 40+ T crop (40.66 @68%) |
| 42 | K **303 ppm**, 5.5 %CEC (12-11-25) | 3rd-yr alfalfa mining K (~600 lb K2O/yr at 10 T removal, *book*) |
| 11 | EC 2.23, K 1,130 (12-11-25); **no 2026 sample** | Going to alfalfa this fall with no pre-plant panel |

### TeVelde / Dixie Creek — binding constraint: SODIUM LOADING + degraded exchange on Field 7
Soluble Na runs 15–53 %SPe operation-wide; Na>Ca in solution on 1S, 4N, 4S, 7N, 7S, 9N, 15 (2025),
16 (2025), R2, R4 (all measured, 2025–2026 panels). But the PROVEN ranch finding (two independent
datasets) is that **Ca%CEC predicts yield and soluble Na does not**: Field 18 carried the worst
soluble Na (44.6–49.6 %SPe, 07-17-25) on the best exchange (Ca 87.9–89.9 %CEC) and made the
operation record 45.1 T/ac @32% DM in 2026. Deviating fields:

| Field | Number (date) | Deviation |
|---|---|---|
| 7 | Ca%CEC **59.2–60.4** (07-31-25) → **62.9/69.2** (05-11-26); Na 51–53 %SPe (2025) | Only genuinely degraded exchange on the operation; leaching alone won't fix; 32.4 T in 2025 = low 1718 field |
| 14 | pH 6.0, **EC 5.76**, NO3-N 248 ppm, OM 4.34 (07-17-25) | Acidic + highest salts + huge N bank; lab called lime, not sulfur |
| 6S | **EC 3.49**, NO3-N 141 ppm (05-11-26) | Salt + nitrate load into 2027 corn; nitrate is a salt at emergence |
| 17E/W | Na **5.1/5.2 %CEC** (07-17-25) | Only samples on any ranch over the 5% ESP watch line |
| 18 | Panel is **pre-sludge** (07-17-25) | Current fertility/salt state unknown — resample before program |
| 12 | EC 23 subsoil / toxic Cl SW spot (05-02-24) → 41.3 T @32% (2026) | Reclamation arc complete; keep on maintenance |

### Correia Custom Farming — binding constraint: SALT TRAJECTORY under the no-rotation baseline (locked)
Light, low-CEC ground (8–20.9), no manure history on most; genuinely deficient P/K/Zn — the one
ranch where dry fertilizer earns its keep. With alfalfa ended (locked §1), nothing resets the
profile; the six lagoon fields (V4, V5, V6, V7, V10, V11) accumulate Na + HCO3 every event.

| Field | Number (date) | Deviation |
|---|---|---|
| V7 | **EC 1.55, SAR 2.5** (ranch highs), soluble Ca:Na 1.47, pH 6.3, no free lime (07-30-26) | Sludge damage on unbuffered ground; Na 4.2 %CEC = still not sodic |
| V15 | K **131 ppm** (1.6 %CEC on CEC 20.9), post-38.9 T trough (07-30-26) | Alfalfa K bill — replacement budgeting, not %CEC-chasing (locked §3) |
| A1 | Na **4.4 %CEC** (ranch high), SAR 2.4, free lime high (07-20-26) | Fallow-leach winter planned; 2.0 T gyp booked |
| A4 | CEC **9.5**, K 10% / Mg 7.3% of CEC inverted (07-20-26) | Weakest ground; HOLD all inputs pending ~January farming decision (locked §8) |
| V8E | OM **0.92%**, K 140, P 19.2, Zn 1.2 (07-20-26) | Lowest OM on ranch; manure priority 1 |
| V14 | P **14.3** (worst on ranch), K 147, Zn 1.2 (07-20-26) | Rehabilitation field, 3-yr build |
| V6, V9–V13 | **No 2026 chemistry at all** | V6/V10/V11 are lagoon fields with no EC/SAR trend line (locked §13.6) |

---

## 2. Salinity vs sodicity — ranch by ranch (Na%SPe ≠ Na%CEC)

| Ranch | Soluble Na (%SPe) | Exchangeable Na (%CEC / ESP) | Verdict |
|---|---|---|---|
| Hamstra | 14.3–30.2 (2025–26 panels) | **1.8–4.4** measured, 19 samples Dec-25 + Jul-26 | **Saline-not-sodic — CONFIRMED.** Leaching is the lever; gypsum = maintenance Ca/SO4/infiltration only |
| Correia | 38.2–58 on V7/A1-block | **1.8–4.4** measured (07-20/07-30-26) | **Not sodic — RESOLVED** (locked §13). Same discipline as Hamstra |
| TeVelde | 15–53 — worst of the three | **Partial:** 3.0–5.2 %CEC on the 13 samples of 07-17S126819 only | **Open where it matters most** — see below |

**TeVelde detail — what is and is not proven.** The 07-17-25 panel (fields 3, 5, 8, 12, 14, 17,
18, 20N) measured Na 3.0–5.2 %CEC: that ground is saline-not-sodic, same as Hamstra. **But Na%CEC
is NOT on file for exactly the fields with the worst soluble sodium:** 7N/7S (51.3/53.2 %SPe),
1S (47.4), 9N (42.5), 15/16 (39.9–44.3), and the whole R-block (R2 53.1, R4 46.4). The 05-11-26
and 07-31-25 reports carry Ca%CEC but the Na%CEC column was not captured. Field 7's Ca%CEC of
59–63 leaves ~37–41% of the exchange as Mg+Na+K in unknown proportions — **7 could plausibly
carry elevated ESP; that is the one place on three ranches where genuine sodicity is still
possible.** Per rulebook §4.1 ⚠: do not size TeVelde gypsum as reclamation until the base-sat
numbers are in hand. Every "gypsum-first on 7" statement rests on the low-Ca%CEC finding, which
is solid; whether the counter-ion is Na (true reclamation job) or Mg (different problem) is not.

**Long-run stability check (drive_archive, Hamstra):** Field 24 Na 1.9 %CEC (09-26-11) → 1.8 %CEC
(12-11-25); Field 19 Na 1.5 %CEC (08-29-11) → 3.2 %CEC (12-11-25). Fifteen years of lagoon
irrigation has roughly doubled ESP on 19 but left it far below the 15% sodic threshold. Direction
confirms the rulebook's "low exchangeable Na is a state to maintain, not assume" — the transition
risk is real but slow. EC meanwhile oscillates (24: 1.35 in 2011 → 2.92 Dec-25 → 1.79 Jul-26) —
soluble salt moves with water management, the exchange barely moves. n=2 fields; indicative only.

---

## 3. Amendment program review — booked fall-2026 vs chemistry vs cadence

Ledger: data/inputs/gypsum_applications.csv. Locked rates (Correia §6) are **not relitigated**.

| Booking | Chemistry check | Verdict |
|---|---|---|
| **Correia — all 9 rows** (A1 2.0, V5E/W 1.0, V7 1.0+leach, V8E 1.0+Tiger 400–500 lb, V8W 0.5, V14 1.0, V15 1.0) | Matches locked §6 line-for-line; no field sodic (Na 1.8–4.4 %CEC) so no reclamation target; V7/V15 1.0 recorded as deliberate operator override of lab 1.5/2.0 (locked §13.9) | **CONFIRM — agreement.** On lagoon ground gypsum rides with the leach or not at all (§1a) |
| **Correia A4 2.0 T (72 tons)** | Locked §8 says **HOLD — no inputs** until ~January decision, and 1.0 T (not 2.0) if farmed; order sheet still carries the 72 tons | **DISCREPANCY — order sheet stale.** Pulling A4 drops the order 531→457 T. Flag to Eric before booking finalizes |
| Hamstra 29 — 1.0 T + 0.3 T S | Alfalfa floor 1.0 (CLAUDE.md) over VT's 0.5; S justified: free lime 1.41% measured 07-30-26, only calcareous field in the set; but **S ahead of alfalfa conflicts with §4.4 "never ahead of alfalfa"** (rhizobia) | **CONFIRM gyp; FLAG the 0.3 T S** — either apply well ahead of seeding or defer to first corn return. Eric's call |
| Hamstra 36 — 1.0 T | Alfalfa floor; VT called 0.5 on 36S only, nothing on 36N | **CONFIRM** (floor governs both halves) |
| Hamstra 11 — 1.0 T | Booked **with no current panel** (last chemistry 12-11-25: EC 2.23); ledger itself says "pending post-harvest sample"; cadence fine (gypped 2022, 2024 → 2026 due) | **CONFIRM conditionally — sample first** (see §6) |
| Hamstra 25 — 1.5 T + 2 lb B | Fails Ca>2×(Mg+Na); SO4-S 35 LOW, B <0.1 LOW (07-30-26); matches VT 1.5. Above the §4.2 1.0 corn-ground standard, but CLAUDE.md's "1.5 where Ca balance fails and sulfate is low" covers it; 1.5 T ≈ 460 lb SO4-S closes the S hole | **CONFIRM** — chemistry-driven, both triggers measured |
| Hamstra 9 — 0.0 (skip) | Na 30.2→18.5 %SPe by leaching; Na 2.6 %CEC; SO4-S 101 adequate (07-30-26) | **CONFIRM skip** — nothing for gypsum to do |
| Hamstra 24 — 0.0 (skip) | Cleanest sample (Na 14.3 %SPe, 1.8 %CEC, SO4 68); gypped 2024, so 2026 is its cadence year — skip is a deliberate chemistry override of the every-other-year clock | **CONFIRM**, note it restarts the clock (next look 2028) |
| Hamstra 23 — nothing booked | EC 3.20 (12-11-25) after gypsum 2022+2024 — the ranch's own proof gypsum ≠ EC control | **CONFIRM absence** — correct per §4.2; the treatment 23 needs is a leach + resample |
| **TeVelde — no fall-2026 bookings** | 2026 pre-plant program applied (1.0 T standard, 2.0 on 7 & 9). VT's 05-11-26 report calls 0.5–2.0 T gyp + 0.2–1.0 T sulfur across 19 samples of 2027-corn ground; none in the ledger yet | **GAP — bookings missing**, and per §2 above the rates on the Na>Ca fields should wait on the %CEC numbers. Sulfur split checks out: S only on calcareous (1S, 2, 4N/S, 6S, 7N/S, 19E/W); lime-not-sulfur on acidic 14 and 16 (pH 6.0, 5.9) |

Cadence footnote: rulebook §9 open item stands — 2025 ledger entries for Hamstra 11, 14, 31N
still missing; long gaps elsewhere are rotation artifacts (no gyp in-stand or first year out).

---

## 4. Trend watch-list — what's moving the wrong way

1. **Hamstra 29 — EC 2.02 → 2.88 in 7 months** (12-11-25 → 07-30-26), entering alfalfa (ECe
   threshold ~2.0, *book*). It made 39.33 T corn @68% at this EC, but a germinating alfalfa stand
   is not a wet-profile corn crop. **Sample/act:** fresh-water pre-irrigation as a real leaching
   set before seeding; hold lagoon water off through establishment; re-check EC at first cutting.
2. **Hamstra 23 — EC 3.20 (12-11-25), no 2026 read.** Two gypsum cycles did not stop the climb.
   **Sample:** post-harvest panel + deep cores (4–5 ft, EC/NO3/water table) to verify drainage
   before budgeting the leach.
3. **Hamstra 42 — K 303 ppm and falling under 3rd-yr alfalfa** (12-11-25; desired >400 on this
   ground, ranch range 437–1,240). **Sample:** before it returns to corn; SOP topdress already
   flagged in intelligence file (pending Eric).
4. **TeVelde 17E/W — Na 5.1/5.2 %CEC** (07-17-25): the only ESP readings above the 5% watch line
   on any ranch. Not sodic, but this is the transition indicator the rulebook says to maintain
   against. **Sample:** include 17 in the next base-sat panel; watch, no action yet.
5. **TeVelde 6S — EC 3.49 + 141 ppm NO3-N** (05-11-26) going into 2027 corn: salt + ~846 lb
   N-equiv is the seed-zone scald recipe. **Act:** fresh-water pre-irrigation (never Dixie manure
   water); skip/cut sidedress per §7 of the ranch file.
6. **Correia V7 — EC 1.55 / SAR 2.5** ranch highs (07-30-26). The locked program (1.0 T gyp +
   mandatory winter leach) is the treatment. **Sample: PRE-PLANT spring 2027, not post-harvest**
   — the only way to know the leach worked before committing the field (locked §4).
7. **Correia lagoon fields V6, V10, V11 — no chemistry on file, ever** (locked §13.6). V7 reached
   EC 1.55 without anyone watching it climb; these are the same water on the same clock.
8. **Hamstra 19 — ESP 1.5 (2011) → 3.2 (Dec-25)** and EC 1.30 → 2.50 over 15 years. Slow, still
   safe, but the only multi-decade drift measurable on the operation; keep it in the Dec panel.

Moving the RIGHT way, for the record: Hamstra 9 (Na 30.2→18.5 %SPe), Hamstra 24 (EC 2.92→1.79),
TeVelde 12 (toxic 2024 spot → 41.3 T 2026). Leaching + paired sampling are doing the work.

---

## 5. DRAFT nutrient/amendment recommendations — **PENDING ERIC'S CONFIRMATION**

**DRAFT — no rate below goes in a deliverable or on the ground until Eric confirms (CLAUDE.md).**
Locked Correia rates restated for completeness, not re-derived.

| Ranch / Field | DRAFT action | Justifying number (measured, date) |
|---|---|---|
| Ham 29 | 1.0 T gyp (alfalfa floor) + 1 lb B; **decide S timing** (0.3 T booked vs no-S-before-alfalfa rule); NO N-P-K | Free lime 1.41%, ~392 lb residual N, P 130, K 1,010 (07-30-26) |
| Ham 36 | 1.0 T gyp floor; 5 lb Zn on North half only; 1 lb B | Zn 2.5 N-half vs 4.7 S-half (07-30-26) |
| Ham 11 | Panel + valve-end paired samples FIRST; then 1.0 T gyp with a fresh-water leach set on valve-end checks pre-seeding | EC 2.23, K 1,130 (12-11-25); 300+ lb residual per intelligence file; no 2026 data |
| Ham 25 | 1.5 T gyp + 2 lb B this fall; next corn: keep 75-unit floor + sulfate-S at sidedress | Ca>2×(Mg+Na) fails; SO4-S 35, B <0.1, ~39 lb residual N (07-30-26) |
| Ham 9, 24 | No gypsum; no P/K/Zn | 9: Na 18.5 %SPe, SO4 101; 24: Na 14.3 %SPe, 1.8 %CEC (07-30-26) |
| Ham 23 | No gypsum; post-harvest leach 6–12 in clean water after drainage check; resample | EC 3.20 after 2022+2024 gyp (12-11-25) |
| Ham 42 | SOP (0-0-50) topdress in-stand; sample before corn return | K 303 ppm, 5.5 %CEC (12-11-25); ~600 lb K2O/yr removal (*book*) |
| TeV 7 | Hold the 2.0 T standing call but classify it "pending %CEC"; then leach after gypsum | Ca%CEC 59.2–63 (07-31-25, 05-11-26); Na%CEC unknown |
| TeV 2027-corn ground | Book VT's 05-11-26 gyp calls (0.5–1.5 T) at maintenance logic once %CEC verifies non-sodic; sulfur only on the calcareous list; lime-not-sulfur on 14, 16 | Na>Ca on 1S/4N/4S/7N/7S/9N; pH 6.0/5.9 on 14/16 |
| TeV 18 | Resample post-harvest before any fertility call | Current panel is pre-sludge (07-17-25); K 97–173, P 8.2–19.5 no longer believable |
| TeV 6S, 14 | Fresh-water pre-irrigation; cut/skip sidedress | EC 3.49/5.76; NO3-N 141/248 ppm (05-11-26 / 07-17-25) |
| Cor (all) | As locked §6: A1 2.0 + fallow leach; V5 1.0; V7 1.0 + mandatory leach, no Tiger; V8E 1.0 + Tiger 400–500 lb; V8W 0.5; V14 1.0; V15 1.0 | Locked 2026-08-07; Na 1.8–4.4 %CEC = no reclamation target |
| Cor A4 | **Pull the 72 tons from the order until the January decision**; if farmed: 1.0 T gyp, MgSO4 100–150 lb, 10 T manure max, never K-Mag | Locked §8; K 10%/Mg 7.3% CEC inversion (07-20-26) |
| Cor V15 | 2027: ~200 u sidedress + real water-run; 325–350 lb K2O replacement (manure-first); 10 lb Zn | 2025 vs 2026: ~240–250 u → 42.02 T vs ~185 u → 38.90 T; K 131 ppm; Zn 1.2 (07-30-26) |
| Cor V8E/V14/A1 | 10 lb Zn each (with V15, per locked §11) | Zn ≤1.2 ppm all four (07-20-26) |

---

## 6. Top 5 measurements to reduce uncertainty — ranked

1. **TeVelde full base-saturation (Na%CEC) on 7N, 7S, 1S, 9N, 15, 16, R2, R4** — the one place
   sodicity is still credible; sets gypsum-as-reclamation vs gypsum-as-maintenance across ~19
   fields of 2027 corn ground. Rulebook §13.1, still the highest-value unknown. Piggyback on
   panels already being pulled; ask Joe/Patrick O'Brien to report the AA-extract cation table.
2. **Hamstra 11 pre-plant panel + valve-end paired samples — before ground prep, this fall.**
   A salt-thinned alfalfa stand is a 4-year mistake; the field is booked for gypsum on no data.
3. **Correia V6/V10/V11 EC-SAR panels (+ V4 in-stand sample, 2027 hard deadline, locked §5).**
   Four lagoon fields with zero trend line under a no-rotation baseline; V7 is the cost of not
   watching.
4. **Correia V7 pre-plant resample, spring 2027** — the only read on whether the mandatory winter
   leach worked; decides 1.0 vs 1.5 T next cycle and whether the field can be judged.
5. **Deep cores (4–5 ft, EC/NO3/water table) under Hamstra 23 and Correia A1** before the winter
   leaching program is budgeted — leaching only works if water has somewhere to go (§4.3); also
   the drainage check that converts LR arithmetic from *book* to measured.

(Close behind: TeVelde 18 post-sludge resample; parse 12-11S143167 into soil_panels.csv so the
Hamstra trend baseline lives in the repo, not only in drive_archive.)

---

## Plain-language summary

Eric — the three ranches have three different problems and the data now proves it. Hamstra is
salty but healthy underneath: exchangeable sodium has sat at 2–4% for fifteen years, and field 9
just showed that water, not gypsum, moves the salt (30→18% soluble Na in seven months, first 40-ton
crop). The fall gypsum book is right except two questions: the 0.3 T sulfur on 29 ahead of alfalfa,
and field 11 being booked blind — sample it before ground prep. TeVelde's sodium is the worst of
the three, but the fields that carry it best are the ones with the strongest calcium on the
exchange (18 made 45.1 tons through the worst soluble Na on the ranch); the one open question that
matters is whether field 7 and the other Na-dominant fields are genuinely sodic — one lab table
from the O'Briens settles it, and TeVelde's fall gypsum should wait for it. Correia's book is
locked and the chemistry agrees with it; the two actions there are pulling A4's 72 tons off the
order until the January decision and getting first-ever panels on the lagoon fields (V6, V10, V11)
so the next V7 gets caught on the way up instead of after the crop pays for it.

*Append-only per CLAUDE.md. Sources cited inline; nothing in this file changes a locked decision.*
