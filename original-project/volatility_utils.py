"""
volatility_utils.py
====================
Shared utility module for computing daily volatility from price data.

This module is used by both:
  - MLFinal.ipynb (numerical LSTM model)
  - Model_2_Sentiment_full (1).ipynb (sentiment model + merge for DNN)

The volatility is computed as the rolling standard deviation of log returns.
"""

import pandas as pd
import numpy as np
from typing import Optional


def compute_daily_volatility(
    price_csv_path: str = "price_data_raw.csv",
    start_date: Optional[str] = "2016-01-01",
    save_path: Optional[str] = "daily_volatility.csv",
    window: int = 21,
) -> pd.DataFrame:
    """
    Load raw price data and compute a simple daily volatility series.

    Parameters
    ----------
    price_csv_path : str
        Path to the raw price CSV file. Expected columns: Date, Open, High, Low, Close, Volume.
    start_date : str or None
        Filter data from this date onward (format: 'YYYY-MM-DD').
        Set to None to use all available data.
    save_path : str or None
        If provided, saves the resulting DataFrame to this CSV path.
    window : int
        Rolling window size (in trading days) for volatility calculation.
        Default is 21 (~1 month of trading days).

    Returns
    -------
    pd.DataFrame
        DataFrame with columns:
          - date : str (format 'YYYY-MM-DD')
          - volatility : float (realized volatility proxy)

    Notes
    -----
    - Volatility is computed as the rolling standard deviation of daily log returns.
    - The first `window` days after start_date will have NaN volatility and are dropped.
    - This is a simple realized volatility proxy. For more sophisticated measures,
      consider GARCH models, Parkinson range-based volatility, etc.
    """
    # Load prices
    df = pd.read_csv(price_csv_path)

    # Parse and sort dates
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    # Filter from the desired start date
    if start_date is not None:
        df = df[df["Date"] >= pd.to_datetime(start_date)].copy()

    # Sanity check for required columns
    if "Close" not in df.columns:
        raise ValueError("Expected a 'Close' column in price_data_raw.csv")

    # Compute daily log returns from Close
    df["log_return"] = np.log(df["Close"]).diff()

    # Rolling window volatility (realized volatility proxy)
    df["volatility"] = df["log_return"].rolling(window=window).std()

    # Build output frame
    out = df[["Date", "volatility"]].copy()
    out = out.rename(columns={"Date": "date"})

    # Normalize date format to YYYY-MM-DD string (for consistent merging)
    out["date"] = out["date"].dt.date.astype(str)

    # Drop rows where volatility is NaN (first `window` days)
    out = out.dropna(subset=["volatility"]).reset_index(drop=True)

    if save_path is not None:
        out.to_csv(save_path, index=False)

    return out


def load_daily_volatility(csv_path: str = "daily_volatility.csv") -> pd.DataFrame:
    """
    Convenience function to load pre-computed daily volatility.
    
    Parameters
    ----------
    csv_path : str
        Path to the daily_volatility.csv file.
    
    Returns
    -------
    pd.DataFrame
        DataFrame with columns: date (str), volatility (float)
    """
    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"]).dt.date.astype(str)
    return df


if __name__ == "__main__":
    # Convenience entry-point: run `python volatility_utils.py` to regenerate daily_volatility.csv
    dv = compute_daily_volatility()
    print("Saved daily volatility series to 'daily_volatility.csv'")
    print(f"Date range: {dv['date'].iloc[0]} to {dv['date'].iloc[-1]}")
    print(f"Total rows: {len(dv)}")
    print(dv.head(10))
