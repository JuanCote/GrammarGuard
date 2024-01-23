from spellchecker import SpellChecker


def spelling_check(text: str) -> str:
    spell = SpellChecker()
    misspelled = spell.unknown(spell.split_words(text))
    highlighted_text = " ".join(
        f'<span class="bg-[#FFCCCB] text-black">{word}</span>'
        if word.lower() in misspelled
        else word
        for word in text.split()
    )
    return highlighted_text
