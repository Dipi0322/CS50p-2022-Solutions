from plates import is_valid

def test_start():
    assert is_valid("AA222") == True

def test_length():
    assert is_valid("A") == False
    assert is_valid("OUTATIME") == False

def test_num():
    assert is_valid("CS05") == False
    assert is_valid("AA22") == True
    assert is_valid("AA22A") == False
    assert is_valid("50") == False

def test_punctuation():
    assert is_valid("AA!2") == False