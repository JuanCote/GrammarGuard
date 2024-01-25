from textblob import TextBlob


def get_sentiment_analysis(text: str) -> TextBlob.sentiment:
    return TextBlob(text).sentiment
