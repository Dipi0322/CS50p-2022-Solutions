from numb3rs import validate

def test_length():
    assert validate("255.255") == False
    assert validate("255.255.0.1.2") == False
    assert validate("127.234.7.9") == True

def test_range():
    assert validate("256.76.3.1") == False
    assert validate("145.3.6.8") == True
    assert validate("255.256.0.1") == False
    assert validate("255.255.512.0") == False

def test_number():
    assert validate("cat.cat.cat.cat") == False
    assert validate("255.cat.dog.0") == False