import pytest

from fuel import convert,gauge

def test_convert():
     assert convert("0/1") == 0
     assert convert("3/4") == 75
     assert convert("4/4") == 100

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"

def test_exception():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")