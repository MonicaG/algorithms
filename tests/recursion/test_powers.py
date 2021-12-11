from algorithms.recursion import powers


def test_powers():
    assert powers.recursive_power(5, 0) == 1
    assert powers.recursive_power(5, 1) == 5
    assert powers.recursive_power(5, 2) == 25
