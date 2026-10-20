# CSI 300 Index Return Analysis

## Problem / Research Question

How has the CSI 300 (China Securities Index 300) performed over the past five years in terms of daily returns, volatility, and drawdown? Is there a noticeable difference in return distribution between bull and bear market regimes?

## Dataset Source & Usage Permissions

- **Source**: Yahoo Finance historical data for ticker `000300.SS` (CSI 300 Index)
- **Time Range**: 2021-01-01 to 2025-12-31
- **License / Usage**: Yahoo Finance historical price data is free for academic and personal analysis. This project uses only aggregated, non-proprietary index price data.
- **Citation**: Yahoo Finance. (2026). SSE CSI 300 Index (000300.SS) Historical Data.

## Methods & Tools Used

- **Language**: Python 3.10+
- **Data manipulation**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Data source**: yfinance (Yahoo Finance API wrapper)
- **Analysis approach**:
  - Daily log-return calculation
  - Rolling volatility (30-day) estimation
  - Maximum drawdown calculation
  - Return distribution comparison (histogram & KDE)

## Key Findings

1. **Average daily return** of the CSI 300 over 2021–2025 is slightly negative (~ -0.02% per day), reflecting a prolonged bear / sideways market.
2. **Annualized volatility** hovers around 18–20%, consistent with major emerging-market equity benchmarks.
3. The **largest drawdown** occurred during the 2022–2023 regulatory and property-sector downturn, exceeding -40% peak-to-trough.
4. Return distribution exhibits **fat tails** — extreme daily moves beyond ±3 standard deviations occur more frequently than a normal distribution would predict.

## One Limitation

This analysis uses only one broad-market index and does not control for macroeconomic variables (interest rates, GDP growth, policy shocks). Correlation with other asset classes (bonds, commodities, USD/CNY) is also excluded, so the findings describe price behavior but cannot explain causal drivers.

## How to Run the Analysis

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate    # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebook

```bash
jupyter notebook analysis.ipynb
```

Or run the Python script directly:

```bash
python analysis.py
```

The script will:
- Download CSI 300 data via `yfinance`
- Compute daily returns, rolling volatility, and drawdown
- Save two figures into the `figures/` directory:
  - `figures/daily_returns_histogram.png`
  - `figures/rolling_volatility.png`

## Repository Structure

```
data-science-project/
├── README.md
├── requirements.txt
├── analysis.ipynb       # Jupyter notebook (interactive)
├── analysis.py          # Equivalent Python script
└── figures/
    ├── daily_returns_histogram.png
    └── rolling_volatility.png
```

## Security Note

No passwords, API keys, or personal data are stored in this repository. The `yfinance` package uses public, unauthenticated endpoints.
