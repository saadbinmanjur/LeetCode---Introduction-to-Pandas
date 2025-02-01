import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['operation'] = stocks['operation'].apply(lambda x: -1 if x == 'Buy' else 1)
    stocks['price'] *= stocks['operation']
    return stocks.groupby("stock_name")["price"].sum().reset_index().rename(columns={"price":"capital_gain_loss"})