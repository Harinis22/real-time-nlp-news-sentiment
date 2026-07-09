from sklearn.feature_extraction.text import CountVectorizer


def extract_top_keywords(texts, top_n=15):
    """
    Extract the most frequent keywords from a list of cleaned news texts.

    This uses CountVectorizer to:
    1. Remove common English stop words
    2. Count word frequency
    3. Return top keywords
    """

    if texts is None or len(texts) == 0:
        return []

    vectorizer = CountVectorizer(
        stop_words="english",
        max_features=100
    )

    word_matrix = vectorizer.fit_transform(texts)

    word_counts = word_matrix.sum(axis=0)

    keywords = []

    for word, count in zip(vectorizer.get_feature_names_out(), word_counts.tolist()[0]):
        keywords.append((word, count))

    keywords = sorted(keywords, key=lambda x: x[1], reverse=True)

    return keywords[:top_n]


def keywords_to_dataframe(keywords):
    """
    Convert keyword list into pandas-friendly format.
    """

    import pandas as pd

    return pd.DataFrame(keywords, columns=["keyword", "count"])


if __name__ == "__main__":
    sample_texts = [
        "stock market rises after positive earnings report",
        "ai stocks gain as investors show confidence",
        "market volatility increases after inflation report",
        "investors watch ai market and stock earnings"
    ]

    keywords = extract_top_keywords(sample_texts, top_n=10)

    print("Top Keywords:")
    for word, count in keywords:
        print(word, count)