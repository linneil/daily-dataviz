"""
IEA Emergency Oil Stock Releases — Data Compilation & Cleaning
Date: 2026-03-17
Source: International Energy Agency (IEA) press releases (all 6 collective actions)

Sources verified:
  - 1991: https://www.iea.org/about/oil-security-and-emergency-response
  - 2005: IEA press release — Hurricane Katrina response
  - 2011: https://www.iea.org/news/iea-makes-60-million-barrels-of-oil-available-to-market-to-offset-libyan-disruption
  - 2022 (x2): https://www.iea.org/news/iea-member-countries-agree-to-new-emergency-oil-stock-release-in-response-to-market-turmoil
  - 2026: https://www.iea.org/news/iea-member-countries-to-carry-out-largest-ever-oil-stock-release-amid-market-disruptions-from-middle-east-conflict
"""

import pandas as pd

# ── RAW DATA (compiled from IEA primary sources) ───────────────────────────
raw_data = [
    {
        "year": 1991,
        "release_date": "1991-01-17",
        "trigger_event": "Gulf War",
        "barrels_million": 17.3,
        "duration_days": 45,
        "brent_price_before_usd": 32.0,
        "notes": "First ever IEA collective action. 33.75mb authorised; 17.3mb delivered over 45 days."
    },
    {
        "year": 2005,
        "release_date": "2005-09-02",
        "trigger_event": "Hurricane Katrina",
        "barrels_million": 60.0,
        "duration_days": 30,
        "brent_price_before_usd": 67.0,
        "notes": "Response to Gulf of Mexico refinery and pipeline disruption."
    },
    {
        "year": 2011,
        "release_date": "2011-06-23",
        "trigger_event": "Libya Civil War",
        "barrels_million": 60.0,
        "duration_days": 30,
        "brent_price_before_usd": 115.0,
        "notes": "Libya lost ~1.3mb/d; IEA released 60mb over 30 days."
    },
    {
        "year": 2022,
        "release_date": "2022-03-01",
        "trigger_event": "Ukraine War (1st)",
        "barrels_million": 61.7,
        "duration_days": 30,
        "brent_price_before_usd": 97.0,
        "notes": "First release in response to Russia's invasion. Part of 182.7mb total."
    },
    {
        "year": 2022,
        "release_date": "2022-04-07",
        "trigger_event": "Ukraine War (2nd)",
        "barrels_million": 120.0,
        "duration_days": 180,
        "brent_price_before_usd": 104.0,
        "notes": "Largest single release at the time. 240mb authorised; 120mb from IEA members."
    },
    {
        "year": 2026,
        "release_date": "2026-03-11",
        "trigger_event": "Iran War",
        "barrels_million": 400.0,
        "duration_days": None,
        "brent_price_before_usd": 72.0,
        "notes": "Largest ever IEA collective action. Strait of Hormuz disruption. Brent peaked near $120/bbl."
    },
]

# ── CLEANING ───────────────────────────────────────────────────────────────
df = pd.DataFrame(raw_data)

# Standardise date
df["release_date"] = pd.to_datetime(df["release_date"])

# Rename to snake_case
df = df.rename(columns={
    "year": "year",
    "release_date": "release_date",
    "trigger_event": "trigger_event",
    "barrels_million": "barrels_released_mb",
    "duration_days": "duration_days",
    "brent_price_before_usd": "brent_price_before_usd",
    "notes": "notes"
})

# Add cumulative total
df = df.sort_values("release_date").reset_index(drop=True)
df["cumulative_released_mb"] = df["barrels_released_mb"].cumsum()

# Chart label: combine year and event for the 2022 dual releases
df["chart_label"] = df.apply(
    lambda r: f"{r['year']}\n{r['trigger_event']}", axis=1
)

# ── DATA QUALITY REPORT ───────────────────────────────────────────────────
print("=" * 55)
print("DATA QUALITY REPORT — IEA Emergency Stock Releases")
print("=" * 55)
print(f"Shape:           {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Date range:      {df['release_date'].min().date()} to {df['release_date'].max().date()}")
print(f"Null counts:\n{df.isnull().sum()}")
print()
print(f"Total released (all time): {df['barrels_released_mb'].sum():.1f} mb")
print(f"Mean per release:          {df['barrels_released_mb'].mean():.1f} mb")
print(f"Max single release:        {df['barrels_released_mb'].max():.1f} mb  ({df.loc[df['barrels_released_mb'].idxmax(), 'trigger_event']} {df.loc[df['barrels_released_mb'].idxmax(), 'year']})")
print(f"2026 as % of all previous: {400 / (df['barrels_released_mb'].sum() - 400) * 100:.0f}%")
print("=" * 55)
print(df[["release_date", "trigger_event", "barrels_released_mb", "brent_price_before_usd"]].to_string(index=False))

# ── SAVE CSV ───────────────────────────────────────────────────────────────
output_path = "cleaned_iea-emergency-releases_2026-03-17.csv"
df.to_csv(output_path, index=False)
print(f"\nSaved: {output_path}")
