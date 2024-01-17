from um import count

def test_um_at_idx_0():
    assert count("um") == 1
    assert count("Um, thanks") == 1
    assert count("Um hello, thanks") == 1
    assert count("UM, UM, HELLIO") == 2

def test_um_at_idx_middle():
    assert count("Hi, um, hello") == 1
    assert count("um..") == 1
    assert count("yummy") == 0
    assert count("yum") == 0

def test_um_at_idx_last():
    assert count("hi, um") == 1
    assert count("um, um, um") == 3