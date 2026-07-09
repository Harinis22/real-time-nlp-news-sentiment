# Real-Time NLP News Sentiment Dashboard

## Project Overview

This project is a real-time Natural Language Processing dashboard built using Python and Streamlit.

It collects live news headlines from Google News RSS, cleans the text data, performs sentiment analysis, extracts trending keywords, and visualizes the results in an interactive dashboard.

## Key Features

- Real-time news headline collection
- Text preprocessing and cleaning
- Sentiment analysis using NLP
- Positive, Negative, and Neutral sentiment classification
- Keyword extraction using CountVectorizer
- Interactive Streamlit dashboard
- Plotly visualizations
- CSV export option
- GitHub-ready project structure

## Tech Stack

- Python
- Streamlit
- Pandas
- Requests
- TextBlob
- Scikit-learn
- Plotly
- Google News RSS

## Project Structure

```text
real-time-nlp-news-sentiment/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│
├── notebooks/
│
├── outputs/
│
├── src/
│   ├── news_fetcher.py
│   ├── text_cleaner.py
│   ├── sentiment_model.py
│   ├── keyword_extractor.py
│   └── utils.py
│
├── README.md
├── requirements.txt
└── .gitignore