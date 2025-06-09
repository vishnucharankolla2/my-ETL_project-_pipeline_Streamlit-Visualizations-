import pandas as pd

# Load the data
try:
    df = pd.read_csv('coin_BinanceCoin.csv')
except FileNotFoundError:
    print("❌ Error: 'coin_BinanceCoin.csv' not found in the current directory.")
    exit()

# Show the columns to confirm structure
print("✅ Columns found:", df.columns)

# Example transformation: Convert numeric columns
numeric_columns = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values in essential columns
df.dropna(subset=numeric_columns, inplace=True)

# Example: Create a new column for price difference
if 'High' in df.columns and 'Low' in df.columns:
    df['Price_Diff'] = df['High'] - df['Low']

# Save the transformed data to a new CSV
df.to_csv('transformed_coin_BinanceCoin.csv', index=False)

print("✅ Transformation complete. Output saved as 'transformed_coin_BinanceCoin.csv'.")
