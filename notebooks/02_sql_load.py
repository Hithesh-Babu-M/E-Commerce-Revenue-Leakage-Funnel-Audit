import pandas as pd 
import sqlite3 
df= pd.read_csv("data\olist_orders_dataset.csv", encoding='latin1')
conn = sqlite3.connect("sql/orders_dataset.db")
df.to_sql("Orders",conn, if_exists="replace",index=False)
conn.close()
print("Data Loaded into Sql database.")
print(df.shape)