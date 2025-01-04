import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    df1 = products[products.change_date <= '2019-08-16']
    df2 = products[products.change_date > '2019-08-16']
    df2.new_price = 10
    df2 = df2[~df2.product_id.isin(df1.product_id)]
    return pd.concat([df1,df2]).sort_values(by = 'change_date', ascending = False).drop_duplicates(['product_id'])[['product_id','new_price']].rename(columns = {'new_price' : 'price'})