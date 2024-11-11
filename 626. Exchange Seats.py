import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    l = len(seat)
    for i in range(1, l, 2):
        seat.iloc[i-1, 1], seat.iloc[i, 1] = seat.iloc[i, 1], seat.iloc[i-1, 1]
    return seat