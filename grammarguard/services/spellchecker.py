from spellchecker import SpellChecker


def spelling_check(text: str) -> str:
    spell = SpellChecker()
    misspelled = spell.unknown(spell.split_words(text))
    highlighted_text = " ".join(
        f'<span style="background-color: #FFCCCB;">{word}</span>'
        if word in misspelled
        else word
        for word in text.split()
    )
    return highlighted_text
