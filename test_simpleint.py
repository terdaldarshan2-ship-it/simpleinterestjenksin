
from simpleinterest import simint

def test_simint():
    assert simint(1000, 5, 2) == 100.0
    assert simint(2000, 10, 3) == 600.0

if __name__ == "__main__":
    test_simint()
    print("All tests passed!")
