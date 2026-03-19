"""
Taiwan Heat Health Crisis — Data Cleaning Script
Date: 2026-03-19

Data sources:
- HRI incidence rate (2000–2018): BMC Public Health (2025),
  "Epidemiological characteristics of heat-related illness: a nationwide study in Taiwan"
  https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-24344-1
  Confirmed endpoints: 2000 = 1.76/10,000, 2018 = 4.17/10,000 (101,614 patients)
  Intermediate years: linearly interpolated from published "gradual increase" trend

- MOHW working-age hospitalizations: Taiwan Ministry of Health and Welfare
  (reported via Taipei Times, April 2025)
  2022 = 1,622 cases, 2024 = 2,829 cases (+74.4%)

- Taiwan annual mean temperature: Central Weather Administration (6 centennial stations)
  2020 = 24.91°C, 2023 = 24.26°C, 2024 = 24.97°C (century average ≈ 23.31°C)
"""

import pandas as pd
import json

# ── HRI incidence rate, nationwide, all ages ──────────────────────────────
# Linear interpolation between confirmed anchor points
# slope = (4.17 - 1.76) / 18 = 0.13389 per year
years_bmc = list(range(2000, 2019))
rate_2000 = 1.76
rate_2018 = 4.17
slope = (rate_2018 - rate_2000) / 18.0
hri_rates = [round(rate_2000 + slope * i, 2) for i in range(19)]

df_hri = pd.DataFrame({
    "year": years_bmc,
    "hri_rate_per_10k": hri_rates,
    "source": ["BMC Public Health (2025) — confirmed"] +
              ["BMC Public Health (2025) — interpolated"] * 17 +
              ["BMC Public Health (2025) — confirmed"]
})

# ── MOHW working-age hospitalizations (19–64) ────────────────────────────
df_mohw = pd.DataFrame({
    "year":  [2022, 2024],
    "hri_cases_working_age": [1622, 2829],
    "source": ["Taiwan MOHW", "Taiwan MOHW"]
})

# ── Taiwan annual mean temperature (CWA, 6 centennial stations) ──────────
df_temp = pd.DataFrame({
    "year":    [2020, 2023, 2024],
    "mean_temp_celsius": [24.91, 24.26, 24.97],
    "anomaly_vs_century_avg": [1.60, 0.95, 1.66],
    "note": [
        "Previous record (until 2024)",
        "6th highest on record",
        "All-time record since 1897"
    ]
})

# ── Quality report ────────────────────────────────────────────────────────
print("=== HRI incidence rate dataset ===")
print(df_hri.to_string(index=False))
print(f"\nShape: {df_hri.shape}")
print(f"Year range: {df_hri.year.min()} – {df_hri.year.max()}")
print(f"Rate range: {df_hri.hri_rate_per_10k.min()} – {df_hri.hri_rate_per_10k.max()}")

print("\n=== MOHW working-age hospitalizations ===")
print(df_mohw.to_string(index=False))
pct_change = (2829 - 1622) / 1622 * 100
print(f"2022→2024 change: +{pct_change:.1f}%")

print("\n=== Taiwan annual temperature (confirmed years) ===")
print(df_temp.to_string(index=False))

# ── Save ──────────────────────────────────────────────────────────────────
df_hri.to_csv("cleaned_taiwan-heat-health-crisis_2026-03-19.csv", index=False)
print("\nSaved: cleaned_taiwan-heat-health-crisis_2026-03-19.csv")
