#!/usr/bin/env python3
"""Normalize silage yields to the repo standard: 70% moisture (30% DM).

yield_70pct_tac = yield_asreported * (1 - moisture_asreported) / 0.30

Common conversions:
  68% moisture (32% DM) -> x 32/30 (~1.0667)   [Hamstra 2024+ basis]
  65% moisture (35% DM) -> x 35/30 (~1.1667)   [TeVelde billing basis]
  70% moisture          -> x 1.0

Usage:
  python scripts/normalize_moisture.py 40.66 0.68     # single value
  python scripts/normalize_moisture.py --check        # recompute the corn CSV
"""
import csv, sys, os

STANDARD_DM = 0.30
CSV = os.path.join(os.path.dirname(__file__), "..", "data", "yield", "corn_silage_history.csv")


def to70(yield_asreported: float, moisture: float) -> float:
    """As-reported tons/ac at `moisture` -> tons/ac at 70% moisture."""
    return yield_asreported * (1 - moisture) / STANDARD_DM


def check_csv(path=CSV, tol=0.02):
    bad = 0
    with open(path) as f:
        for row in csv.DictReader(f):
            if not row["yield_asreported_tac"] or not row["moisture_asreported"]:
                continue
            expect = to70(float(row["yield_asreported_tac"]), float(row["moisture_asreported"]))
            got = float(row["yield_70pct_tac"])
            if abs(expect - got) > tol:
                bad += 1
                print(f"MISMATCH {row['ranch']} {row['field_id']} {row['year']}: "
                      f"stored {got} vs computed {expect:.2f}")
    print("OK — all rows consistent" if bad == 0 else f"{bad} mismatched rows")


if __name__ == "__main__":
    if "--check" in sys.argv:
        check_csv()
    elif len(sys.argv) == 3:
        y, m = float(sys.argv[1]), float(sys.argv[2])
        print(f"{y} T/ac @ {m:.0%} moisture = {to70(y, m):.2f} T/ac @ 70%")
    else:
        print(__doc__)
