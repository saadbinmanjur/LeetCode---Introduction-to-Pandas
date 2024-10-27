import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    return logins.loc[logins.time_stamp.dt.year == 2020].groupby('user_id').max().reset_index().rename(columns={'time_stamp':'last_stamp'})