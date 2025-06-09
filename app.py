import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Crypto Dashboard", layout="wide")

# DB connection
def get_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vishnugermany@2016',
        database='crypto_data'
    )
    query = "SELECT * FROM coin_binancecoin"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Load data
df = get_data()

# App Title
st.title("📊 Crypto Data Dashboard")

# Show dataframe
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Line Chart: Closing Price over Time
st.subheader("Closing Price Over Time")
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Close'])
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
ax.set_title('Binance Coin Closing Price')
st.pyplot(fig)

# Correlation heatmap
st.subheader("Correlation Heatmap")
corr = df[['High', 'Low', 'Open', 'Close', 'Volume']].corr()
fig2, ax2 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)
