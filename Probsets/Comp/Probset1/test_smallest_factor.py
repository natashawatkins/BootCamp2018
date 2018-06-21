from smallest_factor import *

def test_factor():
    assert smallest_factor(1) == 1    # test 1
    assert smallest_factor(10) == 2   # test even number
    assert smallest_factor(9) == 3    # test odd number
    assert smallest_factor(11) == 11  # test prime number