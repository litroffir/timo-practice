import pandas as pd

def build_sequences(df, min_len=3):
    df = df.sort_values(["user_id", "last_watch_dt"])
    sequences = df.groupby("user_id")["item_id"].apply(list).reset_index()
    sequences["len"] = sequences["item_id"].apply(len)
    sequences = sequences[sequences["len"] >= min_len]
    return sequences
