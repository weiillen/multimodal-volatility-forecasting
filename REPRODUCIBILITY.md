# Reproducibility Notes

## Original run order

Run the notebooks from inside `original-project/`:

1. `Model_1_Price.ipynb`
2. `Model_2_Sentiment.ipynb`
3. `Model_3_DNN.ipynb`

The notebooks use relative paths and expect the raw CSV files and `volatility_utils.py` in the same working directory.

## Generated intermediate files

### Model 1

The price notebook reads `price_data_raw.csv` and creates:

- `daily_volatility.csv`
- `lstm_embeddings.csv`
- `train_test_split_info.csv`

### Model 2

The sentiment notebook reads `news_data_raw.csv` plus the volatility output from Model 1 and creates:

- `news_preprocessed.csv`
- `news_summarized.csv`
- `news_with_sentiment_finbert.csv`
- `daily_sentiment.csv`
- `daily_features_for_dnn.csv`
- `daily_sentiment_embeddings.csv`
- `sentiment_train_test_split_info.csv`

### Model 3

The fusion notebook reads `lstm_embeddings.csv` and `daily_sentiment_embeddings.csv`. It can create:

- `best_dnn_model.pt`
- `price_only_model.pt`
- `sentiment_only_model.pt`
- `ablation_study_comparison.png`
- `attention_weights_analysis.png`

These generated intermediates and checkpoints were not included in the uploaded archive.

## Environment

The supplied project did not include pinned package versions. `requirements.txt` lists the packages imported by the notebooks, but it is not a lock file and cannot guarantee reconstruction of the original environment.

The sentiment notebook also requires:

- an internet connection for the FinBERT model download unless it is already cached;
- NLTK sentence-tokenization resources; and
- enough memory and execution time to process the news corpus.

## What was verified

- all three notebook files parse as valid notebook JSON;
- `volatility_utils.py` passes Python bytecode compilation;
- both CSV files load successfully with pandas;
- the stored notebook outputs and reported metrics remain present;
- the report is a readable five-page PDF; and
- every preserved artifact matches its source SHA-256 hash.

## What was not re-run

The complete training pipeline was not re-executed in the packaging environment. It depends on unpinned TensorFlow, PyTorch, Transformers, NLTK, Sumy, generated intermediate files, and a downloadable FinBERT checkpoint. The README therefore reports only results already stored in the uploaded notebooks and report.
