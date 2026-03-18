"""
Lebanon Displacement Crisis 2026 — Data Compilation & Cleaning
Date: 2026-03-18
Sources verified:
  - UNHCR Briefing Note: https://www.unhcr.org/us/news/briefing-notes/unhcr-almost-700-000-displaced-week-across-lebanon-crisis-deepens
  - UN News: https://news.un.org/en/story/2026/03/1167098
  - IOM DTM Lebanon: https://dtm.iom.int/lebanon
  - fundsforNGOs (IOM report): https://news.fundsforngos.org/2026/03/16/nearly-1-million-displaced-in-lebanon-iom-seeks-19-million/
  - Al Jazeera Day 17 update: https://www.aljazeera.com/news/2026/3/16/iran-war-what-is-happening-on-day-17-of-us-israel-attacks
"""

import pandas as pd

# ── RAW DATA (compiled from UNHCR, IOM, UNICEF, UN News situation reports) ─
raw_data = [
    {
        "date": "2026-02-28",
        "displaced_total": 0,
        "children_estimate": 0,
        "in_shelters": 0,
        "source": "Baseline — Operation Epic Fury begins",
        "event_label": "US-Israel strikes on Iran begin"
    },
    {
        "date": "2026-03-02",
        "displaced_total": 96000,
        "children_estimate": None,
        "in_shelters": None,
        "source": "UNHCR/OCHA",
        "event_label": "Israeli evacuation warnings issued across Lebanon"
    },
    {
        "date": "2026-03-05",
        "displaced_total": 280000,
        "children_estimate": None,
        "in_shelters": 40000,
        "source": "IOM DTM Lebanon",
        "event_label": None
    },
    {
        "date": "2026-03-08",
        "displaced_total": 560000,
        "children_estimate": None,
        "in_shelters": 85000,
        "source": "Lebanon government displacement platform",
        "event_label": "100,000 new registrations in a single day"
    },
    {
        "date": "2026-03-09",
        "displaced_total": 667000,
        "children_estimate": 200000,
        "in_shelters": 96000,
        "source": "UNHCR / Lebanon government",
        "event_label": "700k in first 7 days"
    },
    {
        "date": "2026-03-11",
        "displaced_total": 822000,
        "children_estimate": 300000,
        "in_shelters": 110000,
        "source": "UNHCR",
        "event_label": None
    },
    {
        "date": "2026-03-16",
        "displaced_total": 1000000,
        "children_estimate": 330000,
        "in_shelters": 128000,
        "source": "IOM",
        "event_label": "1 million milestone — 1 in 5 Lebanese"
    },
    {
        "date": "2026-03-18",
        "displaced_total": 1049328,
        "children_estimate": 340000,
        "in_shelters": 135000,
        "source": "UNHCR/IOM latest",
        "event_label": "Latest figure (today)"
    },
]

# ── CONTEXT DATA ──────────────────────────────────────────────────────────
LEBANON_POPULATION = 5_500_000
PRE_WAR_HUMANITARIAN_NEED = 4_100_000  # people needing aid before war started

# ── CLEANING ──────────────────────────────────────────────────────────────
df = pd.DataFrame(raw_data)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

# Derived columns
df["pct_of_population"] = (df["displaced_total"] / LEBANON_POPULATION * 100).round(1)
df["days_since_conflict"] = (df["date"] - pd.Timestamp("2026-02-28")).dt.days

# Forward-fill shelter counts (minor interpolation for missing values)
df["in_shelters"] = df["in_shelters"].fillna(method="ffill")

# ── DATA QUALITY REPORT ───────────────────────────────────────────────────
print("=" * 58)
print("DATA QUALITY REPORT — Lebanon Displacement 2026")
print("=" * 58)
print(f"Shape:              {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Date range:         {df['date'].min().date()} to {df['date'].max().date()}")
print(f"Null counts:\n{df[['displaced_total','children_estimate','in_shelters']].isnull().sum()}")
print()
print(f"Peak displaced:     {df['displaced_total'].max():,} ({df['pct_of_population'].max()}% of population)")
print(f"Days to 1 million:  16 days (Feb 28 → Mar 16)")
print(f"Pre-war in need:    {PRE_WAR_HUMANITARIAN_NEED:,} ({PRE_WAR_HUMANITARIAN_NEED/LEBANON_POPULATION*100:.0f}% of population)")
print(f"Lebanon population: {LEBANON_POPULATION:,}")
print("=" * 58)
print(df[["date", "displaced_total", "pct_of_population", "in_shelters", "source"]].to_string(index=False))

# ── SAVE ──────────────────────────────────────────────────────────────────
output_path = "cleaned_lebanon-displacement-2026_2026-03-18.csv"
df.to_csv(output_path, index=False)
print(f"\nSaved: {output_path}")
