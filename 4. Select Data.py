import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    stu_id = students[students['student_id'] == 101][['name', 'age']]
    return stu_id