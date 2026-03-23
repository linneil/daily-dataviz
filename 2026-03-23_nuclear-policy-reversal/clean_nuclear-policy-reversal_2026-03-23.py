import pandas as pd

# Load raw data
df = pd.read_csv('raw_nuclear-policy-reversal_2026-03-23.csv')
df.columns = ['entity', 'code', 'year', 'nuclear_share_pct']

# Target countries: EU + East Asia focus
target_countries = {
    'France': 'France',
    'Germany': 'Germany',
    'Sweden': 'Sweden',
    'Belgium': 'Belgium',
    'Finland': 'Finland',
    'Japan': 'Japan',
    'South Korea': 'South Korea',
    'China': 'China',
    'Taiwan': 'Taiwan',
    'United Kingdom': 'United Kingdom',
}

df_filtered = df[df['entity'].isin(target_countries.keys())].copy()

# Filter years: 2000–2024 (meaningful modern policy window)
df_filtered = df_filtered[(df_filtered['year'] >= 2000) & (df_filtered['year'] <= 2024)]

# Forward-fill missing values within each country
df_filtered = df_filtered.sort_values(['entity', 'year'])
df_filtered['nuclear_share_pct'] = (
    df_filtered.groupby('entity')['nuclear_share_pct']
    .transform(lambda x: x.ffill().fillna(0))
)

# Round to 1 decimal
df_filtered['nuclear_share_pct'] = df_filtered['nuclear_share_pct'].round(1)

# Pivot to wide format for inspection
pivot = df_filtered.pivot(index='entity', columns='year', values='nuclear_share_pct')

# Quality report
print('=== Quality Report ===')
print(f'Shape (long): {df_filtered.shape}')
print(f'Countries: {sorted(df_filtered["entity"].unique())}')
print(f'Year range: {df_filtered["year"].min()} – {df_filtered["year"].max()}')
print(f'Null count: {df_filtered["nuclear_share_pct"].isna().sum()}')
print()
print('=== Key stats (2024 nuclear share %) ===')
latest = df_filtered[df_filtered['year'] == 2024].set_index('entity')['nuclear_share_pct'].sort_values(ascending=False)
print(latest.to_string())
print()
print('=== Pivot (selected years) ===')
cols = [2000, 2005, 2010, 2011, 2015, 2019, 2022, 2023, 2024]
print(pivot[[c for c in cols if c in pivot.columns]].to_string())

# Save
df_filtered.to_csv('cleaned_nuclear-policy-reversal_2026-03-23.csv', index=False)
print('\nSaved: cleaned_nuclear-policy-reversal_2026-03-23.csv')
