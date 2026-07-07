import pandas as pd
orders = pd.read_csv("data/olist_orders_dataset.csv")
print(orders.shape)
print(orders.head())
print(orders.info())
miss_delivery = orders[orders['order_delivered_customer_date'].isnull()]
print(miss_delivery['order_status'].value_counts())