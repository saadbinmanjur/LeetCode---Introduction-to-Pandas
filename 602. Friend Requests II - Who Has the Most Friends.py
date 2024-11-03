import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # Combine the requester_id and accepter_id directly as a Series
    combined_ids = pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']])
    
    # Count the frequency of each user ID and find the max count
    user_counts = combined_ids.value_counts()
    max_count = user_counts.max()
    
    # Filter the user IDs that have the maximum count and reset the index
    most_friends_df = user_counts[user_counts == max_count].reset_index()
    most_friends_df.columns = ['id', 'num']  # Rename columns for clarity
    
    return most_friends_df