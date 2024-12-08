import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first_day"] = activity.groupby(["player_id"])[["event_date"]].transform("min")
    activity["is_day"] = (activity.event_date - activity.first_day).dt.total_seconds() == 86400
    df = activity[activity["is_day"]]
    return pd.DataFrame({"fraction":[round(df.player_id.nunique() / activity.player_id.nunique(),2)]})