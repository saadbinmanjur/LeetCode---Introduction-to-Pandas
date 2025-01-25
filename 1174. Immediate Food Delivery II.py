import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df=delivery.groupby("customer_id").min()
    df1=df[df["order_date"]==df["customer_pref_delivery_date"]]
    return pd.DataFrame({"immediate_percentage":[len(df1)/len(df)*100]}).round(2)