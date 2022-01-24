from problems.leetcode.q56_merge_intervals import Solution


def test_solution():
    sol = Solution()
    sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
    sol.merge([[1, 3], [2, 6], [4, 7], [8, 10], [15, 18]]) == [[1, 7], [8, 10], [15, 18]]
    sol.merge([[1, 3], [2, 3], [7, 9]]) == [[1, 3], [7, 9]]
    sol.merge([[1, 4], [2, 3]]) == [[1, 4]]
