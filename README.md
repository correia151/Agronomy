# Correia Field Intelligence

Field-intelligence system for Hamstra, TeVelde/Dixie Creek, and Correia
Custom Farming (Tulare County, CA). Cross-references Valley Tech soil
chemistry against 13+ years of per-field yield history to drive
fertilizer, amendment, and agronomic decisions.

- **rulebook/** — the rules that govern every recommendation. Start here.
- **ranches/** — per-ranch intelligence files (current state, field flags).
- **data/** — all measurements as CSV. Yield standardized to 70% moisture.
- **analyses/** — dated writeups. Append-only.
- **protocols/** — sampling and diagnostic SOPs.
- **deliverables/** — generated outputs (PDFs, order sheets) for agronomists.
- **scripts/** — parsing and analysis utilities.

GitHub is the system of record; Google Drive is the inbox/outbox. New
Valley Tech PDFs, lab reports, and yield workbooks arrive in Drive and get
parsed into this repo; deliverables export back out to Drive.

Agents: read CLAUDE.md before doing anything.

See MIGRATION_NOTES.md for what was migrated from Drive on 2026-08-11 and
what is still pending.
