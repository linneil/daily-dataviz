# Daily Data Visualization

One chart a day. Each one built from real international news data, published as a self-contained interactive webpage.

This is a personal project in data journalism — turning the day's most important stories into clear, honest visualizations. Every chart is made from scratch using open data from sources like the UN, World Bank, IEA, and government statistics agencies. No templates. No dashboards. Just a story, a dataset, and a chart that earns its place on the page.

---

## Charts

| Date | Topic | Data Source | Chart Type | Link |
|------|-------|-------------|------------|------|
| 2026-03-17 | IEA record 400mb emergency oil release — Iran War | International Energy Agency (6 press releases) | Horizontal bar | [View](https://linneil.github.io/daily-dataviz/2026-03-17_iea-emergency-releases/index.html) |
| 2026-03-17 | TSMC annual revenue 2013–2025 — Taiwan's AI chip boom | TSMC Annual Reports / SEC Form 20-F | Annotated bar | [View](https://linneil.github.io/daily-dataviz/2026-03-17_tsmc-revenue/index.html) |
| 2026-03-18 | Lebanon: 1 million displaced in 16 days — Iran war fallout | UNHCR, IOM DTM, UNICEF, UN OCHA | Area chart | [View](https://linneil.github.io/daily-dataviz/2026-03-18_lebanon-displacement-2026/index.html) |
| 2026-03-19 | Taiwan's heat health crisis — illness rate doubles in 18 years | BMC Public Health (2025), Taiwan NHI database; Taiwan MOHW; CWA | Line chart | [View](https://linneil.github.io/daily-dataviz/2026-03-19_taiwan-heat-health-crisis/index.html) |
| 2026-03-20 | SaaS pricing models are shifting — per-seat down, agentic-based up | OpenView Partners; Growth Unhinged; Gartner | Grouped bar | [View](https://linneil.github.io/daily-dataviz/2026-03-20_saas-agentic-pricing-shift/index.html) |
| 2026-03-21 | Recursion Pharmaceuticals — TechBio paradigm, from $41 peak to $3 reckoning | Recursion IR; Crunchbase; MacroTrends; ARK Invest 13-F | Annotated area chart | [View](https://linneil.github.io/daily-dataviz/2026-03-21_recursion-techbio-timeline/index.html) |
| 2026-03-22 | The 99.7% collapse: AI token costs across frontier models, 2022–2026 | IntuitionLabs; AI CERTs; NavyaAI Cost Report | Log-scale multi-series line (D3.js) | [View](https://linneil.github.io/daily-dataviz/2026-03-22_ai-token-cost-collapse/index.html) |
| 2026-03-23 | The great nuclear reversal — EU and East Asia policy shifts, 2000–2024 | Our World in Data / Ember, Energy Institute | Heatmap (D3.js) | [View](https://linneil.github.io/daily-dataviz/2026-03-23_nuclear-policy-reversal/index.html) |

---

## Stories behind the charts

### 2026-03-23 — The great nuclear reversal

For a decade after Fukushima, nuclear power appeared to be in managed retreat. Germany accelerated its phase-out, reaching zero in April 2023. Japan shuttered its entire fleet; Taiwan began a slow wind-down. Yet 2025 marked a decisive turn. Japan's 7th Strategic Energy Plan authorised new reactor construction for the first time since 2011. South Korea's left-wing president — who had campaigned as a nuclear sceptic — confirmed two new large reactors, targeting 35.2 GWe of capacity by 2038. Sweden scrapped its "100% renewables by 2040" target and approved state loans for 5,000 MWe of new-build. Germany's Merz government, while keeping its own plants off, reclassified nuclear as climate-equivalent to renewables in EU policy. China's share appears static — a statistical illusion created by explosive demand growth: with 36 reactors under construction as of March 2026, its absolute nuclear capacity will within a decade exceed any country outside France.

### 2026-03-22 — AI tokens: the 400× price collapse

In November 2022, running a frontier AI model cost roughly $20 per million tokens. By February 2026, equivalent capability costs $0.05 — a 400-fold decline in under four years. The collapse was not gradual: it arrived in lurches. OpenAI's GPT-4 briefly spiked costs to $30 at launch, then efficiency gains and competition drove them down sharply. The January 2025 DeepSeek shock — open-source models priced at a fraction of incumbent rates — forced every major provider to accelerate cuts within weeks. Yet total enterprise AI bills are rising sharply: API spending grew from $500 million in 2023 to $8.4 billion by mid-2025. Cheaper tokens have not reduced demand. They have detonated it.

### 2026-03-21 — Recursion: the TechBio paradigm

Recursion Pharmaceuticals was founded on a bold thesis: that artificial intelligence and high-throughput biology could industrialise drug discovery at a scale no human team could match. The market believed it. After raising $436 million at its April 2021 IPO, the stock surged to an all-time high of $41.33 in July — a valuation that implied Recursion had already solved problems the pharmaceutical industry had wrestled with for decades. The deals followed: a $12 billion potential collaboration with Roche and Genentech in December 2021, a strategic $50 million investment from NVIDIA in July 2023, and the $688 million acquisition of UK rival Exscientia in 2024. Then came the reckoning. NVIDIA quietly exited its position in late 2025. Clinical setbacks accumulated. The stock hit an all-time low of $2.98 in February 2026 — a 92% decline from its peak. Yet in March 2026, Cathie Wood's ARK Invest began buying. The chart does not resolve the question of whether Recursion is a failed experiment or a paradigm waiting for its moment. It simply shows what the journey has cost.

### 2026-03-20 — SaaS pricing in transition

For two decades, selling software meant counting seats. How many users, how many licences — a simple, predictable model that powered the SaaS boom. That model is now under structural pressure. Survey data from OpenView Partners and Growth Unhinged shows the share of B2B software companies using per-seat pricing as their primary model has fallen from 37% in 2021 to just 15% in 2025. Over the same period, outcome-based and agentic pricing — where vendors charge for results or AI-agent actions rather than human users — climbed from 3% to 15%, reaching parity for the first time. Hybrid structures, mixing seats with usage, now make up the single largest category at 41%. The catalyst is AI: agents that complete tasks autonomously have no seat to bill. Gartner projects 40% of enterprise applications will embed agentic AI by end of 2026, up from under 1% in 2024. IDC forecasts that pure seat-based pricing will be obsolete for 70% of vendors by 2028. The shift is structural, not cyclical.

### 2026-03-19 — Taiwan: a sicker summer, every year

Taiwan recorded its hottest year since measurements began in 1897 in 2024 — an annual mean temperature of 24.97°C, 1.66°C above the century-long average. The health toll has tracked the mercury upward: a nationwide analysis of Taiwan's National Health Insurance database found the rate of heat-related illness more than doubled between 2000 and 2018, rising from 1.76 to 4.17 cases per 10,000 people. Since then the pace has only quickened — working-age hospital admissions surged a further 74% between 2022 and 2024 alone, from 1,622 to 2,829 cases, according to Taiwan's Ministry of Health and Welfare. On an island sitting at the subtropical intersection of rising sea-surface temperatures and dense urban heat islands, the trajectory shows little sign of reversing.

### 2026-03-18 — Lebanon: 1 million displaced

When US and Israeli forces launched Operation Epic Fury on February 28, 2026, Lebanon became an immediate casualty of a war it was not party to. Within 16 days, more than one million people had fled their homes — roughly one in five of Lebanon's 5.5 million population — making it one of the fastest mass displacement events of the decade. The pace was extraordinary: 700,000 in the first seven days alone. The area chart tracks the week-by-week surge in internally displaced persons as reported by UNHCR, IOM, and UNICEF, and sets it against the backdrop that 4.1 million Lebanese — 75% of the population — were already in humanitarian need before the war began. The chart shows not just a number, but the speed and relentlessness of a humanitarian crisis unfolding in real time.

### 2026-03-17 — TSMC: the $2 trillion chip company

Taiwan Semiconductor Manufacturing Company hit a $2 trillion market capitalisation milestone in February 2026 — making it arguably the most strategically important company in the global economy. TSMC manufactures over 90% of the world's most advanced chips (3nm and below), and its revenue trajectory maps almost perfectly onto the AI investment supercycle. Revenues surged from $20bn in 2013 to $116bn in 2025, a 15.7% compound annual growth rate. After a brief 4% dip in 2023 caused by a consumer-electronics inventory glut, the AI-driven rebound sent revenues up 25% in 2024 and a further 32% in 2025. In January 2026, a landmark US-Taiwan trade deal cemented the chip sector's central role in geopolitics.

### 2026-03-17 — IEA's record emergency oil release

On February 28, 2026, US and Israeli air strikes on Iran triggered the most severe energy supply shock since Russia's 2022 invasion of Ukraine. Iran's retaliation disrupted the Strait of Hormuz — the chokepoint through which a fifth of the world's oil and liquefied natural gas flows — sending Brent crude surging to near $120 per barrel before settling around $92. On March 11, the International Energy Agency responded by unanimously authorising the release of 400 million barrels from its members' strategic reserves: the sixth collective action in the IEA's 52-year history, and by far the largest. The release exceeds the combined total of all five previous interventions.
