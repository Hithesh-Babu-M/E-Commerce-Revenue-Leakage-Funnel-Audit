import pandas as pd 
import sqlite3 
orders_df= pd.read_csv("data\olist_orders_dataset.csv", encoding='latin1')
payments_df=pd.read_csv("data\olist_order_payments_dataset.csv",encoding='latin1')
conn = sqlite3.connect("sql/orders_dataset.db")
orders_df.to_sql("Orders",conn, if_exists="replace",index=False)
payments_df.to_sql("Payments",conn,if_exists="replace", index=False)
conn.close()
print("Data Loaded into Sql database.")
print("New Table Loaded Payments into Database.")
