import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    
    df = prices.merge(units_sold, on = 'product_id', how = 'left').loc[lambda x: (x.purchase_date.between(x.start_date, x.end_date)) | (x.purchase_date.isnull())]
    
    result = df.groupby('product_id').apply(lambda x: sum(x.price * x.units) / sum(x.units)).fillna(0).round(2).to_frame('average_price').reset_index()

    return result