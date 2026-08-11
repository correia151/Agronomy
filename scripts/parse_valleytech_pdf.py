#!/usr/bin/env python3
"""Parse a Valley Tech soil report PDF into data/soil/soil_panels.csv rows.

Workflow (per CLAUDE.md — this may be done autonomously):
  1. Drop the raw PDF into data/soil/raw/ named YYYY-MM-DD_ranch_field.pdf
  2. Run this script to extract text and draft rows
  3. Review the draft rows, then append them to data/soil/soil_panels.csv
  4. Commit both the PDF and the CSV rows together

Column discipline: na_pct_spe (saturation-paste, salinity) and na_pct_cec
(exchangeable, sodicity) are SEPARATE columns and must never be blurred —
this is the single most important lesson in the dataset.

Valley Tech layouts vary by report era, so extraction is semi-automatic:
the script dumps text per page; the header regexes below cover the common
0-18" panel layout. Extend PATTERNS as new layouts appear.

Requires: pdfplumber (pip install pdfplumber) or falls back to pdftotext.
"""
import re, sys, csv, subprocess, os

HEADER = ["ranch","field_id","sample_date","depth","lab","sampler","ph","ece","om_pct","cec",
 "ca_meq","mg_meq","k_meq","na_meq","ca_pct_cec","mg_pct_cec","k_pct_cec","na_pct_cec",
 "na_pct_spe","ca_spe","so4_ppm","no3_n_lb","p_ppm","k_ppm","zn_ppm","free_lime","sar","notes","source_pdf"]

PATTERNS = {
    "lab_no": re.compile(r"\b(\d{2}-\d{2}S\d{5,6})\b"),
    "sample_date": re.compile(r"[Ss]ampled[:\s]+(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})"),
    "ph": re.compile(r"\bpH\b[:\s]+(\d\.\d)"),
    "ece": re.compile(r"\bEC[e]?\b[:\s]+(\d+\.\d+)"),
}


def extract_text(pdf_path):
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    except ImportError:
        return subprocess.run(["pdftotext", "-layout", pdf_path, "-"],
                              capture_output=True, text=True).stdout


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    pdf = sys.argv[1]
    text = extract_text(pdf)
    print(text)
    print("\n--- detected fields ---")
    for name, pat in PATTERNS.items():
        m = pat.search(text)
        print(f"{name}: {m.group(1) if m else '(not found)'}")
    print("\nDraft a row per field/depth into data/soil/soil_panels.csv "
          f"with source_pdf set to the lab number and the PDF filed as "
          f"data/soil/raw/{os.path.basename(pdf)}")


if __name__ == "__main__":
    main()
