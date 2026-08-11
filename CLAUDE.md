# CLAUDE.md — Correia Field Intelligence

You are working in the field-intelligence system for three Tulare County, CA
operations managed by Eric Correia: Hamstra (reference ranch), TeVelde /
Dixie Creek Dairy, and Correia Custom Farming. Crops: corn silage, wheat
silage, alfalfa. Soil analysis: Valley Tech lab.

## Read order — every session
1. This file
2. rulebook/correia_field_intelligence_rulebook.md  ← governs ALL recommendations
3. rulebook/locked_decisions_2026.md                ← decisions are LOCKED; do not relitigate
4. The relevant ranches/<ranch>/intelligence.md

## Hard rules
- All yield comparisons use the 70%-moisture standard column
  (yield_70pct_tac). Never mix moisture bases.
- Na%SPe (soluble) ≠ Na%CEC (exchangeable). Hamstra is saline, not sodic —
  leaching is the reclamation lever there; gypsum is for infiltration and
  Ca:Mg:Na balance. At TeVelde, sodium management IS the central lever.
- Alfalfa gypsum floor: 1 T/ac minimum regardless of lab rec; 1.5 T where
  Ca balance fails and sulfate is low.
- 75-unit UN-32 sidedress floor is conditional: waive on high-residual
  fields; keep on low-residual no-lagoon fields.
- Lagoon water past ~2 ac-in adds sodium, not yield.
- Valley Tech under-targets yield. Feed every crop to maximum potential.
- Do not edit files in analyses/ — add new dated files instead.
- Data corrections go in data/ CSVs with a commit message explaining why.

## What you may do autonomously
- Load CSVs, run Python analysis, produce charts and writeups in analyses/
- Parse new Valley Tech PDFs into data/soil/soil_panels.csv (keep raw PDF)
- Update ranch intelligence files when new data changes conclusions —
  note what changed and why in the commit message

## What requires Eric's confirmation
- Any change to rulebook/ or locked decisions
- Any fertilizer/amendment recommendation before it goes in a deliverable
- Deleting or restructuring data files

## Key people
- Steve Mendonca — Nutrien Porterville agronomist (Hamstra soil samples)
- Joe & Patrick O'Brien — Valley Tech CCAs (all operations)

## ET / weather
Open-Meteo archive API (https://archive-api.open-meteo.com/v1/archive),
Tulare coordinates (36.2077, −119.3473). CIMIS is not used — it runs
~200 GDD cooler per season and the harvest targets (2,500 GDD pre-May-1 /
2,800 GDD May-1-and-later) are calibrated to Open-Meteo.
