# Soil Sampling SOPs

## Sampling order in the field operation sequence (Correia — operator confirmed)
```
soil sample → dry manure → disc ×2 → landplane/GPS level → gypsum → chisel
→ pre-irrigate (wheat) or disc + furrow (corn)
```
Samples are pulled **post-corn-harvest, BEFORE any amendment.** Every
post-harvest soil number is therefore an **annual trough** reading — post-crop,
pre-amendment. Interpret low K/P under a big crop accordingly (a field feeding
the crop, not starving it).

## Standard panel
Valley Tech, 0–18", one row per field (split N/S or E/W where the field is
split). Enter into `data/soil/soil_panels.csv`; file the raw PDF in
`data/soil/raw/` named `YYYY-MM-DD_ranch_field.pdf`.

**Always record which sodium number you are reading** — `na_pct_spe`
(saturation-paste, salinity) and `na_pct_cec` (exchangeable, sodicity) get
separate columns and must never be blurred. Sodic threshold: ESP > 15% or
SAR > 13.

## Depth-basis conversions (before crediting N)
- Valley Tech 0–18" basis: **ppm NO₃-N × 6 = lb N/ac**
- UC per-foot basis: **× 3.5**
- The lab's 75% leach-adjusted column uses × 3
- Reconcile the depth basis before crediting residual N.

## PSNT protocol
Sample the top foot at 6–12" corn (4–6 leaf), **before the first
lagoon-water application** — sampling after lagoon water confounds the read.

## Timing rules
- Post-harvest sample = next spring's pre-plant map (salt fields don't reset
  over winter — this year's panels predict next spring's emergence risk).
- **Ground going into or already in alfalfa never fires on the normal
  post-corn cycle** — sample explicitly at termination and mid-stand
  (locked-decisions: sample V4 during the 2027 alfalfa year, hard deadline).
- Re-sample **pre-plant, not post-harvest**, where a winter leach must be
  verified (spring EC is the only way to know the leach worked before
  committing the field).
- February EC walk with a handheld meter (Hanna GroLine class): top 6" at
  valve end and tail end of every corn field, ~20 min/field — flags the
  checks that get water-run Ca, no lab lag.
