from twttr import shorten

def test_lower_case():
    assert shorten("yoo-hoo-yoi") == "y-h-y"

def test_upper_case():
    assert shorten("PYTHON") == "PYTHN"

def test_mixed():
    assert shorten("Cs50-PYThOn") == "Cs50-PYThn"

def test_main_input():
    try:
        assert shorten(None) == None
    except TypeError:
        pass

def test_punctuation():
    assert shorten("CS50!") == "CS50!"
