import sys
import pandas as pd
sys.path.append("/content/drive/MyDrive/sasrec/src")

from data_quality import check_quality
from data_preprocessing import clean
from feature_engineering import build_sequences

def run(batch_path, items_path, users_path, out_path):
    df = pd.read_csv(batch_path)
    items_df = pd.read_csv(items_path)
    users_df = pd.read_csv(users_path)

    issues = check_quality(df, items_df, users_df)
    if issues:
        print("Нарушения:", issues)

    df = clean(df)
    sequences = build_sequences(df)
    sequences.to_csv(out_path, index=False)
    return sequences

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
