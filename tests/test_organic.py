"""Test single word special case: organic."""
from itranslate import itranslate


def test_organic_es():
    """Test organic_es."""
    word = "organic"
    to_lang = "es"
    res = itranslate(word, to_lang=to_lang)
    assert len(res) > 4


def test_who_are_you():
    """Test who are you."""
    text = "who are you"
    # to_lang = "es"
    res = itranslate(text)
    assert "谁" in res

