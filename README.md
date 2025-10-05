# Financial Data Analysis: Stocks & Cryptocurrencies

## Project Overview

This repository contains a comprehensive analysis of multiple financial assets, including **cryptocurrencies, US tech stocks, and major Indian stocks**.

The main objective is to explore **price trends, returns, volatility, risk, correlations, and monthly patterns** to understand asset performance and diversification potential.

The analysis is implemented using **Python** with libraries such as `pandas`, `matplotlib`, and `seaborn`. Data collection is performed using **yfinance** for stocks and **CryptoCompare API** for cryptocurrencies. The project is modular, with data collection, cleaning, exploration, and risk-return analysis organized in separate notebooks.

---

## Repository Structure

```
stock-vs-crypto-risk-return-analysis/
├── data/
│   ├── Raw_Data/
│   │   ├── raw_crypto.csv
│   │   ├── raw_stocks.csv
│   │   └── stocks_wide.csv
│   └── clean_data/
│       ├── clean_crypto.csv
│       ├── clean_stocks.csv
│       └── merged.csv
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── data_cleaning.ipynb.ipynb
│   ├── data_collection.ipynb
│   ├── exploratory_data_analysis.ipynb
│   ├── analysis.ipynb
│   └── stock_vs_crypto_analysis.ipynb
├── results/
│   ├── risk_return_analysis/
│   │   ├── best_asset.png
│   │   ├── correlation_matrix.csv
│   │   ├── drawdown_*.png
│   │   ├── risk_return_extended.csv
│   │   ├── risk_return_tradeoff.png
│   │── cleaned_prices.csv
│   │── correlation_matrix.png
│   │── daily_returns.csv
│   │── daily_returns_distribution.png
│   │── monthly_returns.png
│   │─ normalized_prices.png
│   │── prices.png
│   │── returns_comparison.png
│   │── rolling_volatility.png
│   └── summary_statistics.csv
└── README.md
```

---

## Notebooks Description

| Notebook                          | Description                                                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data_collection.ipynb`           | Collects historical price data for all assets using **yfinance** for stocks and **CryptoCompare API** for cryptocurrencies.                                 |
| `data_cleaning.ipynb`             | Cleans, formats, and reshapes raw data into pivot/wide format.                                                                                              |
| `exploratory_data_analysis.ipynb` | Performs basic EDA: summary statistics, distributions, and missing value analysis.                                                                          |
| `risk_return_analysis.ipynb`      | Calculates daily returns, volatility, cumulative returns, drawdowns, Sharpe ratios, and generates visualizations.                                           |
| `stock_vs_crypto_analysis.ipynb`  | Converts the wide dataset into **long format** for advanced analysis: per-asset calculations, cumulative returns, rolling statistics, and monthly heatmaps. |

> **Note:** Duplicate notebook `data_cleaning.ipynb.ipynb` is an intermediate save and can be ignored.

---

## Data Formats

1. **Wide/Pivot Format (Cleaned Data)**

   * Each asset has its own column.
   * Used for reference and column-wise calculations.
   * Example:

   | time       | BTC   | ETH  | XRP  | AAPL | AMZN | ... |
   | ---------- | ----- | ---- | ---- | ---- | ---- | --- |
   | 2024-01-01 | 17000 | 1200 | 0.35 | 180  | 130  | ... |

2. **Long Format (Used in `stock_vs_crypto_analysis.ipynb` )**

   * Columns: `time`, `Ticker`, `Close`, `Return`, `Year`, `Month`
   * Enables per-asset operations, cumulative returns, and monthly heatmaps.

---

## Analysis Summary

1. **Price Trends**

   * Maximum, minimum, and average prices per asset.
   * Combined and individual plots of asset price movements.

2. **Returns Analysis**

   * Daily returns, mean returns, and volatility.
   * Identification of highest-return and most volatile assets.

3. **Sector / Group Comparisons**

   * Comparison of **cryptos, US tech stocks, and Indian stocks**.
   * Cumulative returns plots to visualize long-term growth.

4. **Risk & Drawdown**

   * Cumulative returns and drawdowns per asset.
   * Maximum drawdown and Sharpe ratio calculations.

5. **Correlation & Diversification**

   * Correlation matrix of asset returns.
   * Heatmaps for visual analysis.

6. **Rolling Statistics**

   * 90-day rolling volatility and returns for selected assets.

7. **Monthly / Yearly Trends**

   * Monthly average returns visualized in heatmaps.
   * Captures seasonal or periodic patterns in returns.

---

## Outputs & Visualizations

* **Best Asset:** `best_asset.png` shows the asset with highest average return.
* **Drawdowns:** Individual drawdown plots (`drawdown_*.png`) for all assets.
* **Correlation Matrix:** `correlation_matrix.csv` and `.png` visualize inter-asset correlations.
* **Risk-Return Tradeoff:** `risk_return_tradeoff.png` compares return vs volatility.
* **Daily Returns Distribution:** `daily_returns_distribution.png` shows return distributions.
* **Monthly Returns Heatmaps:** `monthly_returns.png` visualizes month-wise performance.
* **Normalized Prices & Returns Comparison:** `normalized_prices.png` and `returns_comparison.png`.
* **Rolling Volatility:** `rolling_volatility.png` tracks short-term risk trends.

---

## Usage

1. Run `data_collection.ipynb` to fetch updated datasets using **yfinance** for stocks and **CryptoCompare API** for cryptocurrencies.
2. Clean and reshape raw data using `data_cleaning.ipynb`.
3. Explore distributions and summary statistics using `exploratory_data_analysis.ipynb`.
4. Analyze risk, returns, and generate plots with `risk_return_analysis.ipynb`.
5. Use `stock_vs_crypto_analysis.ipynb` for **long-format analysis**, including monthly heatmaps and per-asset cumulative returns.
6. All plots and CSV outputs are saved in `results/risk_return_analysis/`.

---

## Key Financial Terms

* **Closing Price:** Last traded price for the day.
* **Return:** Daily percentage change in price.
* **Volatility:** Standard deviation of returns, indicating risk.
* **Cumulative Return:** Growth of investment over time.
* **Drawdown:** Peak-to-trough decline in value.
* **Sharpe Ratio:** Risk-adjusted return.
* **Correlation:** Relationship between asset returns.
* **Rolling Statistics:** Metrics over a moving window (e.g., 90-day volatility).

---

## Conclusion

This repository provides a **structured framework** to analyze multiple financial assets, evaluate risk-return characteristics, and visualize trends. It can be extended to include:

* Additional assets or markets
* Advanced risk metrics
* Predictive financial modeling
* Portfolio optimization
