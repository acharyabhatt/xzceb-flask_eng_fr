"""
This module provides functions for translating text between En and Fr using MyMemoryTranslator.
"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translates English text to French using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text
