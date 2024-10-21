import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = products.merge(orders, on = 'product_id', how = 'left')
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    df = df[(df['order_date'].dt.month == 2) & (df['order_date'].dt.year == 2020)]
    df = df.groupby(['product_id', 'product_name'], as_index=False).agg({'unit':'sum'})
    
    return df[df['unit'] >= 100][['product_name', 'unit']]