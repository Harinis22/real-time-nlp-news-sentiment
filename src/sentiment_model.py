from textblob import TextBlob


def get_sentiment_score(text):
    """
    Return sentiment polarity score.

    TextBlob polarity range:
    -1.0 = very negative
     0.0 = neutral
    +1.0 = very positive
    """

    if text is None or str(text).strip() == "":
        return 0.0

    blob = TextBlob(str(text))
    return blob.sentiment.polarity


def get_sentiment_label(score):
    """
    Convert numeric sentiment score into readable label.
    """

    if score > 0.10:
        return "Positive"
    elif score < -0.10:
        return "Negative"
    else:
        return "Neutral"


def add_sentiment_columns(df):
    """
    Add sentiment score and sentiment label to dataframe.
    """

    df = df.copy()

    df["sentiment_score"] = df["combined_text"].apply(get_sentiment_score)
    df["sentiment_label"] = df["sentiment_score"].apply(get_sentiment_label)

    return df


if __name__ == "__main__":
    test_sentences = [
        "The stock market is rising and investors are optimistic.",
        "The company reported losses and the market is worried.",
        "The meeting happened today."
    ]

    for sentence in test_sentences:
        score = get_sentiment_score(sentence)
        label = get_sentiment_label(score)

        print("Text:", sentence)
        print("Score:", score)
        print("Label:", label)
        print("-" * 50)