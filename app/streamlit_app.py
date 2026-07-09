import sys
import os

# Allow Streamlit app to import files from src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.express as px

from src.news_fetcher import fetch_news
from src.text_cleaner import clean_news_dataframe
from src.sentiment_model import add_sentiment_columns
from src.keyword_extractor import extract_top_keywords, keywords_to_dataframe
from src.utils import save_dataframe, get_sentiment_summary


st.set_page_config(
    page_title="Real-Time NLP News Sentiment Dashboard",
    page_icon="📰",
    layout="wide"
)


st.title("📰 Real-Time NLP News Sentiment Dashboard")

st.write(
    """
    This dashboard collects real-time news headlines, cleans the text,
    applies NLP sentiment analysis, extracts trending keywords,
    and visualizes the results.
    """
)


# Sidebar inputs
st.sidebar.header("Search Settings")

query = st.sidebar.text_input(
    "Enter news topic",
    value="artificial intelligence"
)

limit = st.sidebar.slider(
    "Number of news articles",
    min_value=5,
    max_value=50,
    value=20,
    step=5
)

run_button = st.sidebar.button("Fetch and Analyze News")


if run_button:
    with st.spinner("Fetching real-time news and running NLP analysis..."):

        # Step 1: Fetch news
        news_df = fetch_news(query=query, limit=limit)

        # Step 2: Clean text
        cleaned_df = clean_news_dataframe(news_df)

        # Step 3: Add sentiment analysis
        final_df = add_sentiment_columns(cleaned_df)

        # Step 4: Extract keywords
        keywords = extract_top_keywords(final_df["combined_text"].tolist(), top_n=15)
        keywords_df = keywords_to_dataframe(keywords)

        # Step 5: Save output
        saved_file = save_dataframe(final_df)

    st.success(f"Analysis complete. Output saved to: {saved_file}")

    # Summary metrics
    st.subheader("Sentiment Summary")

    sentiment_summary = get_sentiment_summary(final_df)

    col1, col2, col3, col4 = st.columns(4)

    total_articles = len(final_df)
    positive_count = sentiment_summary.get("Positive", 0)
    neutral_count = sentiment_summary.get("Neutral", 0)
    negative_count = sentiment_summary.get("Negative", 0)

    col1.metric("Total Articles", total_articles)
    col2.metric("Positive", positive_count)
    col3.metric("Neutral", neutral_count)
    col4.metric("Negative", negative_count)

    # Sentiment chart
    st.subheader("Sentiment Distribution")

    sentiment_chart_df = final_df["sentiment_label"].value_counts().reset_index()
    sentiment_chart_df.columns = ["sentiment_label", "count"]

    fig_sentiment = px.pie(
        sentiment_chart_df,
        names="sentiment_label",
        values="count",
        title="Positive vs Neutral vs Negative News"
    )

    st.plotly_chart(fig_sentiment, use_container_width=True)

    # Keyword chart
    st.subheader("Top Trending Keywords")

    if not keywords_df.empty:
        fig_keywords = px.bar(
            keywords_df,
            x="keyword",
            y="count",
            title="Most Frequent Keywords in News Headlines"
        )

        st.plotly_chart(fig_keywords, use_container_width=True)
    else:
        st.warning("No keywords found.")

    # Sentiment score chart
    st.subheader("Sentiment Score by Article")

    fig_score = px.bar(
        final_df,
        x=final_df.index,
        y="sentiment_score",
        color="sentiment_label",
        hover_data=["title", "source"],
        title="Sentiment Score for Each News Article"
    )

    fig_score.update_layout(
        xaxis_title="Article Number",
        yaxis_title="Sentiment Score"
    )

    st.plotly_chart(fig_score, use_container_width=True)

    # Data table
    st.subheader("Analyzed News Articles")

    display_columns = [
        "title",
        "source",
        "published_at",
        "sentiment_score",
        "sentiment_label",
        "link"
    ]

    st.dataframe(final_df[display_columns], use_container_width=True)

    # Download button
    csv_data = final_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Results as CSV",
        data=csv_data,
        file_name="news_sentiment_results.csv",
        mime="text/csv"
    )

else:
    st.info("Enter a topic in the sidebar and click **Fetch and Analyze News**.")