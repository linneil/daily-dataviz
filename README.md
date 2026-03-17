# Daily Data Visualization

One publication-ready interactive chart per day, built from real international news data.
Charts follow **Financial Times** or **Economist** style standards and are published as self-contained HTML files.

---

## How it works

Each morning at 08:00, Claude automatically:
1. Scans major news sources for the day's most significant story with quantitative data
2. Identifies and verifies downloadable datasets from authoritative sources (UN, World Bank, IEA, OECD)
3. **Pauses for approval** before downloading anything
4. Cleans the data with Python/pandas and produces a reproducible cleaning script
5. Generates a self-contained interactive HTML chart (no server needed)
6. Commits and pushes everything to this repository

---

## Chart Log

| Date | Topic | Data Source | Chart Type | Style | Link |
|------|-------|-------------|------------|-------|------|
| 2026-03-17 | IEA record 400mb emergency oil release — Iran War | International Energy Agency (6 press releases) | Horizontal bar | Economist | [View](https://linneil.github.com/daily_dataviz/2026-03-17_iea-emergency-releases/index.html) |
| 2026-03-17 | TSMC annual revenue 2013–2025 — Taiwan's AI chip boom | TSMC Annual Reports / SEC Form 20-F | Annotated bar | FT | [View](./daily-dataviz/2026-03-17_tsmc-revenue/index.html) |

### 2026-03-17 (②) — Why this chart?

Taiwan Semiconductor Manufacturing Company hit a $2 trillion market capitalisation milestone in February 2026 — making it arguably the most strategically important company in the global economy. TSMC manufactures over 90% of the world's most advanced chips (3nm and below), and its revenue trajectory maps almost perfectly onto the AI investment supercycle. Revenues surged from $20bn in 2013 to $116bn in 2025, a 15.7% compound annual growth rate. After a brief 4% dip in 2023 caused by a consumer-electronics inventory glut, the AI-driven rebound sent revenues up 25% in 2024 and a further 32% in 2025. In January 2026, a landmark US-Taiwan trade deal — cutting tariffs on Taiwanese goods from 32% to 15% and exempting semiconductors entirely — in exchange for $250bn in TSMC investments in US fabs cemented the chip sector's central role in geopolitics. The chart was made the same day as a separate chart on the IEA's record oil reserve release, together illustrating how Taiwan sits at the intersection of both the energy and technology crises reshaping the world order.

### 2026-03-17 — Why this chart?

On February 28, 2026, US and Israeli air strikes on Iran triggered the most severe energy supply shock since Russia's 2022 invasion of Ukraine. Iran's retaliation disrupted the Strait of Hormuz — the chokepoint through which a fifth of the world's oil and liquefied natural gas flows — sending Brent crude surging to near $120 per barrel before settling around $92. On March 11, the International Energy Agency responded by unanimously authorising the release of 400 million barrels from its members' strategic reserves: the sixth collective action in the IEA's 52-year history, and by far the largest. The release exceeds the combined total of all five previous interventions — and comes as the IEA simultaneously cut its global oil demand forecast by more than 1 million barrels per day for March and April. Whether the record release can stabilise prices hinges on how long the Strait of Hormuz remains disrupted.
