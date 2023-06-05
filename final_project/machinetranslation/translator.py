"""
This module provides functions for translating text between En and Fr using MyMemoryTranslator.
"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translates English text to French using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    frenchText = translator.translate(english_text)
    return frenchText


def french_to_english(french_text):
    """
    Translates French text to English using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    englishText = translator.translate(french_text)
    return englishText
