import mysql.connector
import pandas as pd

# Read the transformed CSV
df = pd.read_csv('transformed_coin_BinanceCoin.csv')

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',               # your MySQL username
    password='Vishnugermany@2016',  # your MySQL password
    database='crypto_data'     # database you created
)

cursor = conn.cursor()

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS coin_binancecoin (
    SNo INT,
    Name VARCHAR(50),
    Symbol VARCHAR(10),
    Date DATE,
    High DOUBLE,
    Low DOUBLE,
    Open DOUBLE,
    Close DOUBLE,
    Volume DOUBLE,
    Marketcap DOUBLE,
    Price_Diff DOUBLE
);
"""
cursor.execute(create_table_query)

# Insert DataFrame rows one by one
for _, row in df.iterrows():
    insert_query = """
    INSERT INTO coin_binancecoin (SNo, Name, Symbol, Date, High, Low, Open, Close, Volume, Marketcap, Price_Diff)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        int(row['SNo']),
        row['Name'],
        row['Symbol'],
        row['Date'],
        float(row['High']),
        float(row['Low']),
        float(row['Open']),
        float(row['Close']),
        float(row['Volume']),
        float(row['Marketcap']),
        float(row['Price_Diff'])
    )
    cursor.execute(insert_query, data)

# Commit changes and close connection
conn.commit()
print("✅ Data loaded successfully into MySQL.")

cursor.close()
conn.close()
