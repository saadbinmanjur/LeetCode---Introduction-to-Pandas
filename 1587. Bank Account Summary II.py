import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(users, transactions, on='account', how='inner')
    df = df.groupby(['account', 'name'])[['amount']].sum().reset_index()
    df = df.loc[df.amount > 10000][['name', 'amount']]
    df.rename(columns = {'amount': 'balance'}, inplace=True)
    return df