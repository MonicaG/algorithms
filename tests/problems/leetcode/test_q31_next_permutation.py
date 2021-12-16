from problems.leetcode.q31_next_permutation import Solution


def test_solution():
    sol = Solution()
    nums = [1, 1, 5]
    sol.nextPermutation(nums)
    assert nums == [1, 5, 1]

    nums = [3, 2, 1]
    sol.nextPermutation(nums)
    assert nums == [1, 2, 3]

    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    assert nums == [1, 3, 2]

    nums = [5, 6, 3, 2, 4, 8, 6, 5, 3]
    sol.nextPermutation(nums)
    assert nums == [5, 6, 3, 2, 5, 3, 4, 6, 8]

