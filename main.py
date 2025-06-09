from extract import extract_data
from transform import transform_data
from load import load_data
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)

def run_etl():
    df = extract_data()
    df = transform_data(df)
    load_data(df, connection)
    print("✅ ETL Job Completed Successfully.")

if __name__ == "__main__":
    run_etl()
