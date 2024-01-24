import string

from spellchecker import SpellChecker


def spelling_check(text: str) -> str:
    spell = SpellChecker()
    misspelled = spell.unknown(spell.split_words(text))
    highlighted_text = " ".join(
        f'<span class="highlighted-word bg-[#FFCCCB] text-black" data-correct-word="{spell.correction(remove_nonletters(word.lower()))}">{word}</span>'
        if remove_nonletters(word.lower()) in misspelled
        else word
        for word in text.split()
    )
    return highlighted_text


def remove_nonletters(word: str) -> str:
    translator = str.maketrans("", "", string.punctuation)
    return word.translate(translator)


def count_word_frequency(text: str) -> dict:
    spell = SpellChecker()
    words = spell.split_words(text)
    result = dict()
    for word in words:
        word = word.lower()
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    return result
