from problems.leetcode.q53_maximum_subarray import Solution


def test_solution():
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray([-5, -2, -8, -1, -7]) == -1


def test_solutionKadaneAlgo():
    sol = Solution()
    assert sol.maxSubArrayKadaneAlgo([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArrayKadaneAlgo([1]) == 1
    assert sol.maxSubArrayKadaneAlgo([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArrayKadaneAlgo([-5, -2, -8, -1, -7]) == -1

