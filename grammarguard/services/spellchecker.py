import string

from spellchecker import SpellChecker


def spelling_check(text: str) -> str:
    spell = SpellChecker()
    misspelled = spell.unknown(spell.split_words(text))
    highlighted_text = " ".join(
        f'<span class="bg-[#FFCCCB] text-black">{word}</span>'
        if remove_nonletters(word.lower()) in misspelled
        else word
        for word in text.split()
    )
    return highlighted_text


def remove_nonletters(word: str) -> str:
    translator = str.maketrans("", "", string.punctuation)
    return word.translate(translator)
