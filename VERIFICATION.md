# Verification Record

Verification was performed without editing the original artifacts.

## Structural checks

- Jupyter notebooks parsed successfully: 3/3
- Python utility passed `py_compile`: 1/1
- PDF report opened successfully: 5 pages
- Embedded preview figures extracted successfully: 8

## Data checks

| File | Rows | Columns |
|---|---:|---:|
| `price_data_raw.csv` | 13,642 | 7 |
| `news_data_raw.csv` | 2,247 | 4 |

Price columns:

```text
Date, Open, High, Low, Close, Adj Close, Volume
```

News columns:

```text
Date, Url, Text, Mark
```

## Stored-output checks

The following values were found in the unchanged notebook outputs:

- final sequence dataset: 1,954 samples;
- split used by the fusion notebook: 1,563 train, 190 validation, 201 test;
- 64 price embedding dimensions and 64 sentiment embedding dimensions;
- 44,995 parameters in the combined dual-branch model;
- combined-model MAPE: 14.96%;
- combined-model RMSE: 0.005608; and
- first two price-embedding principal components: approximately 98.6% explained variance.

## Integrity

See `ORIGINAL_FILE_MANIFEST.tsv` for per-file hashes and original-to-portfolio path mapping.
