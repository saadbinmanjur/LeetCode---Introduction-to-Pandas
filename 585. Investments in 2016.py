import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    res = insurance.drop_duplicates(subset=['lat', 'lon'], keep=False)
    need = insurance.groupby('tiv_2015').pid.count().reset_index()
    need = need[need['pid'] >= 2]
    need['pid'] = 1
    res = res.merge(need.rename(columns={'pid': 'coef'})).fillna(0)[['tiv_2016', 'coef']]
    res['tiv_2016'] *= res['coef']
    return pd.DataFrame([res['tiv_2016'].sum()], columns=['tiv_2016']).round(2)