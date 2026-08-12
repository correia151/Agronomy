#!/usr/bin/env python3
"""Query tool for the field-intelligence database (the data/ CSVs).

The database is the set of CSVs under data/ — git-versioned, agent-computable,
appended to as reports and field records arrive (see protocols/data_intake.md).

Usage:
  python scripts/db.py tables                       # list tables + row counts
  python scripts/db.py field <ranch> <field_id>     # everything about one field
  python scripts/db.py year <ranch> <year>          # everything from one season
  python scripts/db.py crop <crop_substring>        # rows mentioning a crop
Examples:
  python scripts/db.py field hamstra 9
  python scripts/db.py field correia V15
  python scripts/db.py year tevelde 2026
"""
import csv, os, sys, glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

def tables():
    out = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "**", "*.csv"), recursive=True)):
        with open(p, newline="") as f:
            rows = list(csv.DictReader(f))
        out[os.path.relpath(p, os.path.join(ROOT, ".."))] = rows
    return out

def norm(s):
    return str(s).strip().lower().replace("&", "").replace("-", "").replace(" ", "")

def match_field(row, ranch, fid):
    r = norm(row.get("ranch", ""))
    if r and r != norm(ranch):
        return False
    for col in ("field_id", "block", "sample_label", "well_label"):
        v = row.get(col)
        if v is None:
            continue
        nv, nf = norm(v), norm(fid)
        if nv == nf or nv.startswith(nf) or nf in nv.split(","):
            return True
    return False

def show(title, rows):
    if not rows:
        return
    print(f"\n## {title}  ({len(rows)} rows)")
    for row in rows:
        kv = ", ".join(f"{k}={v}" for k, v in row.items() if v not in ("", None))
        print("  -", kv)

def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    cmd = sys.argv[1]
    tbls = tables()
    if cmd == "tables":
        for name, rows in tbls.items():
            print(f"{name}: {len(rows)} rows")
    elif cmd == "field" and len(sys.argv) == 4:
        ranch, fid = sys.argv[2], sys.argv[3]
        print(f"# {ranch} field {fid}")
        for name, rows in tbls.items():
            show(name, [r for r in rows if match_field(r, ranch, fid)])
    elif cmd == "year" and len(sys.argv) == 4:
        ranch, year = sys.argv[2], sys.argv[3]
        print(f"# {ranch} {year}")
        for name, rows in tbls.items():
            hits = [r for r in rows
                    if norm(r.get("ranch", "")) == norm(ranch)
                    and any(str(year) in str(v) for v in
                            (r.get("year"), r.get("sample_date"), r.get("date"),
                             r.get("cutting_date"), r.get("planting_date")))]
            show(name, hits)
    elif cmd == "crop" and len(sys.argv) == 3:
        key = sys.argv[2].lower()
        for name, rows in tbls.items():
            show(name, [r for r in rows if key in str(r).lower()])
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
