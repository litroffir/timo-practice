import pandas as pd

def clean(df):
    df = df.drop_duplicates(subset=["user_id", "item_id", "last_watch_dt"]).copy()
    df["last_watch_dt"] = pd.to_datetime(df["last_watch_dt"])
    df = df[df["total_dur"] > 0]
    return df.reset_index(drop=True)
