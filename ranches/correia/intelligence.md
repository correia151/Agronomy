# Correia Custom Farming — Field Intelligence

**The authoritative per-field program for this ranch lives in
[`rulebook/locked_decisions_2026.md`](../../rulebook/locked_decisions_2026.md).**
Read it before issuing any Correia rate — do NOT re-derive rates from the raw
lab report. This file is the ranch roster and quick orientation only.

## Ranch character
The ranch where dry fertilizer actually earns its keep: light, low-salt soils
(EC 0.47–0.99 on the 2025 panels), lower CEC (8–17, V15 the lone heavy field
at 20.9), no dairy manure history — so P and K are genuinely deficient,
unlike the two dairies. Zinc low across most V/A fields. Residual nitrate LOW
— this ranch needs a full N program and the early-N floor genuinely applies.

## Water source map (drives everything downstream)

| Access | Fields |
|---|---|
| Lagoon water | V4, V5, V6, V7, V10, V11 |
| 20 T/ac dry manure (no lagoon) | A1, V8, V14, V15 |
| Neither | A4 |

## Field roster (see data/reference/field_registry.csv for detail)
- **Early corn 2026:** V15, V5, V14, V8, A1, V7, A4 (yields in
  data/yield/corn_silage_history.csv, 70% basis)
- **Double-crop:** V6, V9, V10, V11, V12, V13 — no 2026 chemistry on file
  (real exposure under the no-rotation baseline)
- **V4:** alfalfa 2025→2028, the LAST post-alfalfa corn field on the plan.
  Protected: fresh water only, no sludge ever, sample during the 2027
  alfalfa year (hard deadline).

## Headline rules (locked)
- No more alfalfa rotation — salt management is now the primary long-term lever.
- Gypsum is scheduled with a leach on lagoon ground, or not at all.
- Sludge/lagoon placement hard rule: nothing that puts salt back goes onto a
  field entering, inside, or within two years of exiting its alfalfa window.
- Post-alfalfa fields arrive with a K hole and NO nitrogen surplus — do not
  cut N; budget K up.
- Input program constraint: dry manure + 90% gypsum + Tiger 90 only. NO
  ammonium sulfate, NO ATS. Never Tiger 90 on the acidic zone (V7, V15).

## Primary soil reports
07-20S161861 (Maps 3/4/6/7, sampled 07-20-26) · 07-30S163338 (V7, V15,
sampled 07-30-26) · 04-17S115463 (V15 spring N profile 2025 — the evidence
that killed the post-alfalfa N-surplus rule). Panel rows in
data/soil/soil_panels.csv.
