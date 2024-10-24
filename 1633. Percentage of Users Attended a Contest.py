import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(users, register, on='user_id', how='right')
    df = df.groupby(['contest_id']).agg({'user_id': 'count'}).reset_index()
    df['percentage'] = (df['user_id'] / len(users) * 100).round(2)
    df = df.sort_values(['user_id', 'contest_id'], ascending=[False, True])[['contest_id', 'percentage']]
    return df