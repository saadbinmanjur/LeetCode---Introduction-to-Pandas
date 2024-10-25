import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    pivoted = activity.pivot(index=["machine_id", "process_id"], columns='activity_type', values='timestamp')
    pivoted['processing_time'] = pivoted['end'] - pivoted['start']