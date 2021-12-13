from algorithms.recursion.powers import recursive_power


def test_powers():
    assert recursive_power(5, 0) == 1
    assert recursive_power(5, 1) == 5
    assert recursive_power(5, 2) == 25
