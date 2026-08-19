[Uploading README.md…]()
# Dual-LSTM-Based Volatility Prediction

This project predicts **short-term stock volatility** (risk level) using:
- **Price patterns** from OHLCV
- **Financial news sentiment** extracted with **FinBERT**
- A **fusion model** combining both signals

---

## Overview
Price prediction is noisy and unstable. Volatility is a more meaningful target for risk-aware decisions.  
We ask: **Can price + news sentiment improve volatility prediction?**

---

## How to Run
Run the notebooks in order:

1. **Price model**
   - `Model_1_Price.ipynb`

2. **Sentiment pipeline + sentiment embeddings**
   - `Model_2_Sentiment.ipynb`

3. **Fusion model**
   - `Model_3_DNN.ipynb`

Make sure these files exist in the project root:
- `price_data_raw.csv`
- `news_data_raw.csv`
- `volatility_utils.py`

---

## Method
### Data & Label
- Price: daily **OHLCV** (`price_data_raw.csv`)
- News: raw news text (`news_data_raw.csv`)
- Label: rolling realized volatility (≈ **21-day** window), computed in `volatility_utils.py`
- Split: **time-based** (first 80% train, last 20% test; no shuffle)

### Models
- **Model 1 (Price-Only)**: LSTM on 60-day OHLCV sequences
- **Model 2 (Sentiment-Only)**:
  - News → FinBERT (neg/neu/pos)
  - Daily sentiment score = `pos - neg`
  - Aggregate to daily mean; missing-news days set to **0.0 (neutral)**
  - LSTM for forecasting / embeddings
- **Model 3 (Combined)**: fuse **price embedding (64-d)** + **sentiment embedding (64-d)** with a small DNN to predict volatility

---

## Repo Files
- `Model_1_Price.ipynb` — Price-only LSTM
- `Model_2_Sentiment.ipynb` — FinBERT sentiment + LSTM
- `Model_3_DNN.ipynb` — Fusion DNN
- `volatility_utils.py` — volatility label computation

---

## Contributions
- Malvin Julius malvinjulius12@gmail.com — study research, methodology design, result analysis, evaluation metrics, data curation  
- Richard Bryan Cuthbert richardbryancuthbert25@gmail.com — methodology design, study research  
- Yong-Jie Hu jerry940315@gmail.com — methodology design, study research  
- Ting-Yu Tsai willem.unit3@gmail.com — video presentation, research questions, results, conclusion  
- Nicholas Albert Aklin nicholasalbert2005@gmail.com — discussion, limitations, result analysis  
- Waylen Twensin Collin waylentc@gmail.com — methodology design, study research
