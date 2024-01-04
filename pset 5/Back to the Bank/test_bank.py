from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_h():
    assert value("Hey") == 20
    assert value("hey") == 20

def test_without_h():
    assert value("What's happening") == 100