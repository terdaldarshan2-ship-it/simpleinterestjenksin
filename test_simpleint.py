
from simpleint import simInt

def test_simint():
    assert simInt(1000, 5, 2) == 100.0
    assert simInt(2000, 10, 3) == 600.0

if __name__ == "__main__":
    test_simint()
    print("All tests passed!")
