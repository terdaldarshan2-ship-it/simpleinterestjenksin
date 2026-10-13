from simpleinterest import simint

def test_simpleint_pos():
    assert simint(20000,8,12) == 19200

def test_simpleint_zer():
    assert simint(10000,7,0) == 0
    