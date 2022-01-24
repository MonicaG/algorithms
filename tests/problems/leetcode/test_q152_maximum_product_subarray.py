from problems.leetcode.q152_maximum_product_subarray import Solution


def test():
    sol = Solution()
    assert sol.maxProduct([-2, 0, -1]) == 0
    assert sol.maxProduct([5, 3, -1, 2]) == 15
    assert sol.maxProduct([5, 3, -1, 2, -2]) == 60
    assert sol.maxProduct([5, 3, -1, 2, -2, -3, 6]) == 72
    assert sol.maxProduct([3, 2, 0, 5]) == 6
    assert sol.maxProduct([3, 2, 0, 5, 6, -1]) == 30
    assert sol.maxProduct([2, 3, -2, 4]) == 6
