# Paired Sampling Protocol — Standard Diagnostic Design

The standard way this operation isolates a real spatial problem: **sample the
bad area against an adjacent good area on the same field, same day, same
depths** — never against book values.

## Design
1. Identify the problem area (scald, stand failure, ponding check, chronic
   short corn) and a visually good reference area on the same field.
2. Sample both at **two depths minimum** — 0–6" and 6–24" for seed-zone salt
   questions; 0–18" plus deep cores (4–5 ft) when leaching feasibility or
   water table is in question.
3. Where the crop is standing, pull **tissue with Na/Cl** from both areas.
4. Same lab (Valley Tech), same panel, one submission — differences are then
   attributable to the ground, not the method.
5. File the raw PDF in `data/soil/raw/` (named `YYYY-MM-DD_ranch_field.pdf`)
   and enter one row per area per depth in `data/soil/soil_panels.csv`
   (keep `na_pct_spe` and `na_pct_cec` separate — never blur them).
6. Write the interpretation as a new dated file in `analyses/` — append-only.

## Proven results
- **TeVelde field 12 (May 2024, 05-02S83635):** NW ok / SW bad / East good.
  Bad area: pH 8.8–9.4, EC 6.6 surface / 23.0 subsoil, Na 22–72 meq/L,
  toxic chloride (37–115 meq/L), K to 6,670 ppm, buried anaerobic OM.
  Good area beside it: EC 1.8, normal profile. Lab: 10T gyp + 2T sulfur +
  leach (3 ft water per ft root zone). Two seasons later: **41.3 T/ac @32%
  DM — #2 on the ranch.** Textbook confirmation the design isolates real
  spatial problems, and that aggressive amendment + leaching pays within the
  rotation cycle.
- **Hamstra field 9:** Na 30.2 → 18.5 %SPe in seven months of leaching →
  first 40+ T crop on the ranch.

## Active applications
- Hamstra fields 11/14/17 (+16) valve-end diagnostic — see
  `ranches/hamstra/diagnostics/fields_11_14_17_lagoon_valve_protocol.md`
