from algorithms.dynamic_programming.fibonacci import fibonacci, fibonacci_memoization


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13


def test_fibonacci_memoization():
    assert fibonacci_memoization(0) == 0
    assert fibonacci_memoization(1) == 1
    assert fibonacci_memoization(2) == 1
    assert fibonacci_memoization(3) == 2
    assert fibonacci_memoization(4) == 3
    assert fibonacci_memoization(5) == 5
    assert fibonacci_memoization(6) == 8
    assert fibonacci_memoization(7) == 13
    assert fibonacci_memoization(30) == 832040
