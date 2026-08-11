#!/usr/bin/env python3
"""Pull daily weather / ET0 / GDD from the Open-Meteo archive API for Tulare.

CIMIS is NOT used — it runs ~200 GDD cooler per season and the harvest
targets (2,500 GDD pre-May-1 / 2,800 GDD May-1+) are calibrated to Open-Meteo.

GDD formula (corn 86/50): max((min(Tmax,86) + max(Tmin,50))/2 - 50, 0)

Usage:
  python scripts/fetch_et.py 2026-03-16 2026-07-21          # GDD + ET0 summary
  python scripts/fetch_et.py 2026-03-16 2026-07-21 --csv out.csv
"""
import sys, json, csv, urllib.request, urllib.parse

LAT, LON = 36.2077, -119.3473  # Tulare (per Correia Corn Irrigation Scheduler)
API = "https://archive-api.open-meteo.com/v1/archive"


def fetch(start, end):
    params = urllib.parse.urlencode({
        "latitude": LAT, "longitude": LON,
        "start_date": start, "end_date": end,
        "daily": "temperature_2m_max,temperature_2m_min,et0_fao_evapotranspiration,precipitation_sum",
        "temperature_unit": "fahrenheit",
        "precipitation_unit": "inch",
        "timezone": "America/Los_Angeles",
    })
    with urllib.request.urlopen(f"{API}?{params}") as r:
        return json.load(r)["daily"]


def gdd_86_50(tmax, tmin):
    return max((min(tmax, 86) + max(tmin, 50)) / 2 - 50, 0)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    start, end = sys.argv[1], sys.argv[2]
    d = fetch(start, end)
    rows, cum = [], 0.0
    for i, day in enumerate(d["time"]):
        g = gdd_86_50(d["temperature_2m_max"][i], d["temperature_2m_min"][i])
        cum += g
        rows.append([day, d["temperature_2m_max"][i], d["temperature_2m_min"][i],
                     round(g, 1), round(cum, 1),
                     d["et0_fao_evapotranspiration"][i], d["precipitation_sum"][i]])
    if "--csv" in sys.argv:
        out = sys.argv[sys.argv.index("--csv") + 1]
        with open(out, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["date", "tmax_f", "tmin_f", "gdd_86_50", "gdd_cum", "et0_mm", "precip_in"])
            w.writerows(rows)
        print(f"wrote {out} ({len(rows)} days)")
    et0_total_mm = sum(x for x in d["et0_fao_evapotranspiration"] if x is not None)
    print(f"{start} → {end}: {cum:.0f} GDD (86/50), "
          f"ET0 {et0_total_mm:.0f} mm ({et0_total_mm/25.4:.1f} in), "
          f"precip {sum(x for x in d['precipitation_sum'] if x is not None):.2f} in")


if __name__ == "__main__":
    main()
