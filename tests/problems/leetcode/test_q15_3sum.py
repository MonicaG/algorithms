from problems.leetcode.q15_3sum import Solution


def test_solution_skip_duplicates():
    sol = Solution()
    assert sol.threeSum_skip_dup_nums([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum_skip_dup_nums([]) == []
    assert sol.threeSum_skip_dup_nums([0]) == []
    assert sol.threeSum_skip_dup_nums([-25, -10, -7, -3, 2, 4, 8, 10]) == [[-10, 2, 8], [-7, -3, 10]]



