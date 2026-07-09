import os
from datetime import datetime


def create_folder(folder_path):
    """
    Create a folder if it does not already exist.
    """

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def save_dataframe(df, folder_path="outputs", file_prefix="news_sentiment"):
    """
    Save dataframe as CSV with timestamp.

    Example output:
    outputs/news_sentiment_20260709_142530.csv
    """

    create_folder(folder_path)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = os.path.join(folder_path, f"{file_prefix}_{timestamp}.csv")

    df.to_csv(file_path, index=False)

    return file_path


def get_sentiment_summary(df):
    """
    Create sentiment summary counts.

    Example:
    Positive: 8
    Neutral: 10
    Negative: 2
    """

    if "sentiment_label" not in df.columns:
        return {}

    summary = df["sentiment_label"].value_counts().to_dict()

    return summary


if __name__ == "__main__":
    import pandas as pd

    sample_df = pd.DataFrame({
        "title": ["Good market news", "Bad inflation news", "Normal update"],
        "sentiment_label": ["Positive", "Negative", "Neutral"]
    })

    print(get_sentiment_summary(sample_df))

    saved_path = save_dataframe(sample_df)
    print("Saved file:", saved_path)