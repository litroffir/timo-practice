import pandas as pd

def check_quality(df, items_df, users_df):
    issues = []
    if df[["user_id", "item_id"]].isna().any().any():
        issues.append("R1: пустые user_id или item_id")
    if (pd.to_datetime(df["last_watch_dt"]) > pd.Timestamp.utcnow()).any():
        issues.append("R2: даты в будущем")
    if (df["total_dur"] <= 0).any():
        issues.append(f"R3: total_dur <= 0: {(df['total_dur'] <= 0).sum()}")
    if not df["item_id"].isin(items_df["item_id"]).all():
        issues.append("R4: есть item_id, отсутствующие в items.csv")
    if not df["user_id"].isin(users_df["user_id"]).all():
        issues.append("R5: есть user_id, отсутствующие в users.csv")
    return issues
