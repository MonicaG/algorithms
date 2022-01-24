from problems.leetcode.q41_product_of_array_except_self import Solution


def test_solution():
    sol = Solution()
    nums = [2, 3, 4, 5]
    assert sol.productExceptSelf(nums) == [60, 40, 30, 24]

    nums = [1, 2, 3, 4]
    assert sol.productExceptSelf(nums) == [24, 12, 8, 6]

    nums = [-1, 1, 0, -3, 3]
    assert sol.productExceptSelf(nums) == [0, 0, 9, 0, 0]


def test_solution_mult_array():
    sol = Solution()

    nums = [2, 3, 4, 5]
    assert sol.productExceptSelf_multipleArrays(nums) == [60, 40, 30, 24]

    nums = [1, 2, 3, 4]
    assert sol.productExceptSelf_multipleArrays(nums) == [24, 12, 8, 6]

    nums = [-1, 1, 0, -3, 3]
    assert sol.productExceptSelf_multipleArrays(nums) == [0, 0, 9, 0, 0]
    