from algorithms.recursion import factorial


def test_factorial():
    assert factorial.factorial(0) == 1
    assert factorial.factorial(1) == 1
    assert factorial.factorial(2) == 2
    assert factorial.factorial(3) == 6
    assert factorial.factorial(4) == 24
    assert factorial.factorial(5) == 120
