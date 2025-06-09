import pandas as pd

def extract_data():
    file_path = "C:/Users/vishn/Documents/ETL_CRYPTO_PROJECT/coin_BinanceCoin.csv"
    return pd.read_csv(file_path)

