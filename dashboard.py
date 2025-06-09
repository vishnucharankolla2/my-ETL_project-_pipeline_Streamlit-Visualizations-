import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection details
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Connect to the database
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)

# Fetch data
df = pd.read_sql('SELECT * FROM crypto_prices', connection)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Close the connection
connection.close()

# 1️⃣ Line Chart — Closing price over time with moving average
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
plt.plot(df['Date'], df['Close'].rolling(window=7).mean(), label='7-Day MA', color='orange')
plt.title('Crypto Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2️⃣ Bar Chart — Top 5 highest closing prices
top_5 = df.nlargest(5, 'Close')
plt.figure(figsize=(8, 5))
plt.bar(top_5['Date'].dt.strftime('%Y-%m-%d'), top_5['Close'], color='green')
plt.title('Top 5 Highest Closing Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# 3️⃣ Pie Chart — Average distribution of Open, Close, High, Low prices
avg_values = df[['Open', 'Close', 'High', 'Low']].mean()
plt.figure(figsize=(7, 7))
plt.pie(avg_values, labels=avg_values.index, autopct='%1.1f%%', startangle=140)
plt.title('Average Price Type Distribution')
plt.tight_layout()
plt.show()
