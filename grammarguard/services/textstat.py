from textstat import textstat


def get_flesh_stat(text: str) -> float:
    return textstat.flesch_reading_ease(text)
