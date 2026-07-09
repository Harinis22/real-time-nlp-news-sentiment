import requests
import pandas as pd
from datetime import datetime


def fetch_news(query="artificial intelligence", limit=20):
    """
    Fetch real-time news headlines using the GNews public RSS endpoint.

    This does not require an API key.
    It collects:
    - news title
    - short summary
    - source
    - published date
    - article link
    """

    url = "https://news.google.com/rss/search"

    params = {
        "q": query,
        "hl": "en-US",
        "gl": "US",
        "ceid": "US:en"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    import xml.etree.ElementTree as ET

    root = ET.fromstring(response.content)

    articles = []

    for item in root.findall(".//item")[:limit]:
        title = item.findtext("title", default="")
        link = item.findtext("link", default="")
        published = item.findtext("pubDate", default="")
        source = item.findtext("source", default="Unknown")

        description = item.findtext("description", default="")

        articles.append({
            "query": query,
            "title": title,
            "description": description,
            "source": source,
            "published_at": published,
            "link": link,
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    df = pd.DataFrame(articles)

    return df


if __name__ == "__main__":
    news_df = fetch_news(query="stock market", limit=10)
    print(news_df.head())