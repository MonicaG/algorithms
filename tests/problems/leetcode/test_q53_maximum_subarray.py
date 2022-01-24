from problems.leetcode.q53_maximum_subarray import Solution


def test_solution():
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray([-5, -2, -8, -1, -7]) == -1
    assert sol.maxSubArray([5, 8, -15, -3, 7, 4, 2]) == 13
    assert sol.maxSubArray([6, -6, 3, 3]) == 6


def test_solutionKadaneAlgo():
    sol = Solution()
    assert sol.maxSubArrayKadaneAlgo([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArrayKadaneAlgo([1]) == 1
    assert sol.maxSubArrayKadaneAlgo([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArrayKadaneAlgo([-5, -2, -8, -1, -7]) == -1
    assert sol.maxSubArrayKadaneAlgo([5, 8, -15, -3, 7, 4, 2]) == 13
    assert sol.maxSubArrayKadaneAlgo([6, -6, 3, 3]) == 6


def test_solutionBruteForce():
    sol = Solution()
    assert sol.maxSubArray_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray_brute([1]) == 1
    assert sol.maxSubArray_brute([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray_brute([-5, -2, -8, -1, -7]) == 0
    assert sol.maxSubArray_brute([5, 8, -15, -3, 7, 4, 2]) == 13
    assert sol.maxSubArray_brute([6, -6, 3, 3]) == 6
    assert sol.maxSubArray_brute([]) == 0


def test_solution_original_kadane():
    sol = Solution()

    assert sol.kadane_original([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.kadane_original([1]) == 1
    assert sol.kadane_original([5, 4, -1, 7, 8]) == 23
    assert sol.kadane_original([-5, -2, -8, -1, -7]) == 0
    assert sol.kadane_original([5, 8, -15, -3, 7, 4, 2]) == 13
    assert sol.kadane_original([6, -6, 3, 3]) == 6
    assert sol.kadane_original([]) == 0

