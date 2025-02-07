import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:

    adj = lambda x: stadium.id.diff().shift(x) == 1

    stadium = stadium[stadium.people > 99]

    return stadium[adj(0) & adj(1) | adj(-1) & adj(0) | adj(-2) & adj(-1)]