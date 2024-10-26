import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby("reports_to", as_index=False).agg(reports_count=("employee_id","nunique"),average_age=("age","mean")).apply(lambda x: (x+1e-10).round(0)).rename(columns={"reports_to":"employee_id"}).merge(employees[["employee_id", "name"]],on="employee_id",how="left")[["employee_id","name","reports_count","average_age"]]
    return df