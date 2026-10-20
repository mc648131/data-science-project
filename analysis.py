"""
CSI 300 Index Return Analysis
CISC7204 Practice 09 - Data Science Portfolio Project
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import os

# ---------- Configuration ----------
TICKER = "000300.SS"
START_DATE = "2021-01-01"
END_DATE = "2025-12-31"
FIG_DIR = "figures"

os.makedirs(FIG_DIR, exist_ok=True)
sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 120

# ---------- 1. Download data ----------
print(f"Downloading {TICKER} data from {START_DATE} to {END_DATE} ...")
data = yf.download(TICKER, start=START_DATE, end=END_DATE)
print(f"Downloaded {len(data)} trading days.\n")

# ---------- 2. Compute daily log returns ----------
data["log_return"] = np.log(data["Close"] / data["Close"].shift(1))
data = data.dropna()

mean_return = data["log_return"].mean()
std_return = data["log_return"].std()
annualized_vol = std_return * np.sqrt(252)

print(f"Mean daily log return : {mean_return:.6f} ({mean_return*100:.4f}%)")
print(f"Daily std deviation    : {std_return:.6f} ({std_return*100:.4f}%)")
print(f"Annualized volatility  : {annualized_vol:.4f} ({annualized_vol*100:.2f}%)\n")

# ---------- 3. Rolling 30-day volatility ----------
data["rolling_vol_30d"] = data["log_return"].rolling(window=30).std() * np.sqrt(252)

# ---------- 4. Maximum drawdown ----------
cumulative = (1 + data["log_return"]).cumprod()
running_max = cumulative.cummax()
drawdown = (cumulative - running_max) / running_max
max_drawdown = drawdown.min()
print(f"Maximum drawdown       : {max_drawdown:.4f} ({max_drawdown*100:.2f}%)\n")

# ---------- Figure 1: Daily returns histogram + KDE ----------
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.histplot(data["log_return"], bins=60, kde=True, color="steelblue", ax=ax1, stat="density")

# Overlay normal distribution for comparison
x = np.linspace(data["log_return"].min(), data["log_return"].max(), 200)
normal_pdf = (1 / (std_return * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_return) / std_return) ** 2)
ax1.plot(x, normal_pdf, color="crimson", linestyle="--", linewidth=2, label="Normal distribution")

ax1.set_title("CSI 300 Daily Log Return Distribution (2021–2025)", fontsize=13)
ax1.set_xlabel("Daily Log Return")
ax1.set_ylabel("Density")
ax1.legend()
plt.tight_layout()
fig1.savefig(os.path.join(FIG_DIR, "daily_returns_histogram.png"))
print(f"Saved: {FIG_DIR}/daily_returns_histogram.png")

# ---------- Figure 2: Rolling 30-day annualized volatility ----------
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(data.index, data["rolling_vol_30d"], color="darkorange", linewidth=1.5)
ax2.axhline(y=annualized_vol, color="gray", linestyle="--", alpha=0.7, label=f"Full-period annualized vol = {annualized_vol:.2%}")
ax2.set_title("CSI 300 Rolling 30-Day Annualized Volatility (2021–2025)", fontsize=13)
ax2.set_xlabel("Date")
ax2.set_ylabel("Annualized Volatility")
ax2.legend()
plt.tight_layout()
fig2.savefig(os.path.join(FIG_DIR, "rolling_volatility.png"))
print(f"Saved: {FIG_DIR}/rolling_volatility.png")

print("\nAnalysis complete. Both figures saved to figures/ directory.")
