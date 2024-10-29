import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.loc[(employees.salary < 30000) & (~employees.manager_id.isnull()),['manager_id', 'employee_id']]
    df = df.loc[~df['manager_id'].isin(employees.employee_id), ['employee_id']].sort_values(by='employee_id')
    return df