import pandas as pd 
import sqlite3
orders= pd.read_csv("data/olist_orders_dataset.csv", encoding='latin1')
date_cols=['order_purchase_timestamp', 'order_approved_at','order_delivered_carrier_date', 'order_delivered_customer_date','order_estimated_delivery_date']
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col])
    
print(orders.dtypes)

orders['delivery_delay_days']= orders['order_delivered_customer_date']- orders['order_estimated_delivery_date']
orders['delivery_delay_days'] = orders['delivery_delay_days'].dt.days
print(orders['delivery_delay_days'].head())
print(orders['delivery_delay_days'].dtype)
print(orders['delivery_delay_days'].mean())
late_deliveries=orders[orders['delivery_delay_days']>0]
late_rate= len(late_deliveries)/orders['delivery_delay_days'].notna().sum() *100
print(f"Late delivery rate: {late_rate:.2f}%")
conn = sqlite3.connect("sql/orders_dataset.db")
orders.to_sql("OrdersWithDelay",conn,if_exists="replace",index=False)
conn.close()
print("Orders with delay column exported to database.")