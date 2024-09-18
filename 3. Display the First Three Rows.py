import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    first_three_row = employees.head(3)
    return first_three_row