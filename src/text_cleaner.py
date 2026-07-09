import re
import html


def clean_text(text):
    """
    Clean raw news text for NLP processing.

    Steps:
    1. Convert HTML entities
    2. Remove HTML tags
    3. Convert text to lowercase
    4. Remove URLs
    5. Remove special characters
    6. Remove extra spaces
    """

    if text is None:
        return ""

    text = str(text)

    # Convert HTML entities like &amp; to normal text
    text = html.unescape(text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def clean_news_dataframe(df):
    """
    Add cleaned text columns to the news DataFrame.
    """

    df = df.copy()

    df["clean_title"] = df["title"].apply(clean_text)
    df["clean_description"] = df["description"].apply(clean_text)

    df["combined_text"] = (
        df["clean_title"] + " " + df["clean_description"]
    ).str.strip()

    return df


if __name__ == "__main__":
    sample_text = "Stock Market Today: AI stocks rally &amp; investors react! <b>Read more</b>"
    print("Original Text:")
    print(sample_text)

    print("\nCleaned Text:")
    print(clean_text(sample_text))