import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(visits, transactions, on = 'visit_id', how = 'left')
    df = df[df['transaction_id'].isna()]
    df = df.groupby(['customer_id'])['visit_id'].count().reset_index()

    return df.rename({'visit_id':'count_no_trans'}, axis = 1)