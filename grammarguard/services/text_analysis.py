from .spellchecker import count_word_frequency, spelling_check


def analyze_text(text: str) -> dict:
    analysis_result = {
        "words_count": count_words(text),
        "letter_count": letter_count(text),
        "characters_count": len(text),
        "characters_count_without_space": len([x for x in text if x != " "]),
        "sentences": sentences_count(text),
        "original_text": text,
        "highlighted_text": spelling_check(text),
        "word_frequency": count_word_frequency(text),
    }
    return analysis_result


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def letter_count(text: str) -> int:
    letters = [char for char in text if char.isalpha()]
    return len(letters)


def sentences_count(text: str) -> int:
    text = text.replace("!", ".").replace("?", ".")
    senteces = text.split(".")
    filtered_sentences = [item for item in senteces if item.strip()]
    return len(filtered_sentences)
