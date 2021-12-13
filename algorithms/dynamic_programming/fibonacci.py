def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


def fibonacci_memoization(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-2) + fibonacci(n-1)
    return memo[n]
