"""
Data cleaning script — AI Token Cost Collapse (2022–2026)
Source: IntuitionLabs API Pricing Database; AI CERTs; NavyaAI Cost Report
Date: 2026-03-22
"""

import pandas as pd

# Load raw data (manually compiled from sources)
df = pd.read_csv("cleaned_ai-token-cost-collapse_2026-03-22.csv")

# Parse date column
df["release_date"] = pd.to_datetime(df["release_date"], format="%Y-%m")

# Rename to snake_case (already done)
# Filter to primary chart series only (budget/frontier per provider, no premium tiers)
chart_series = df[~df["model"].isin(["GPT-5.2 Pro", "Claude Opus 3", "Gemini 2.5 Pro",
                                      "Gemini 3.1 Pro", "Claude Opus 4.6", "xAI"])]

# Quality report
print("=== Quality Report ===")
print(f"Shape: {df.shape}")
print(f"Null counts:\n{df.isnull().sum()}")
print(f"Date range: {df['release_date'].min()} — {df['release_date'].max()}")
print(f"\nPrice range: ${df['input_price_per_million_usd'].min()} — ${df['input_price_per_million_usd'].max()}")
print(f"\nProviders: {df['provider'].unique()}")
print(f"\nKey stats:\n{df.groupby('provider')['input_price_per_million_usd'].describe()}")
print(f"\nOverall price decline (min/max): {df['input_price_per_million_usd'].max() / df['input_price_per_million_usd'].min():.0f}x")
