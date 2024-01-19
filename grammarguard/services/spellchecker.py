from spellchecker import SpellChecker


def process_text(text):
    spell = SpellChecker()
    misspelled = spell.unknown(text.split())
    return misspelled
