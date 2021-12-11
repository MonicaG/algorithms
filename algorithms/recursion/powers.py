def recursive_power(a, n):
    """Assumptions:
    a: a non-zero natural number
    n: a non-negative integer
    """
    if n == 0:
        return 1
    else:
        return a * recursive_power(a, n - 1)

