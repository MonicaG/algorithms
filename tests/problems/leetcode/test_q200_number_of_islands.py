"""
Question at: https://leetcode.com/problems/number-of-islands/
My notes at: https://monica-granbois.gitbook.io/cs-theory-and-problems/problems/leetcode/200.-number-of-islands
"""

from problems.leetcode.q200_number_of_islands import Solution, Solution2


def test_solution_1():
    sol = Solution()
    assert sol.numIslands([["1", "1", "1", "1", "0"],
                           ["1", "1", "0", "1", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "0", "0", "0"]]) == 1
    assert sol.numIslands([["1", "1", "0", "0", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "1", "0", "0"],
                           ["0", "0", "0", "1", "1"]]) == 3
    assert sol.numIslands([["0", "0"],
                           ["0", "0"]]) == 0
    assert sol.numIslands([["0", "1"],
                           ["0", "1"],
                           ["0", "1"]]) == 1


def test_solution_2():
    sol = Solution2()
    assert sol.numIslands([["1", "1", "1", "1", "0"],
                           ["1", "1", "0", "1", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "0", "0", "0"]]) == 1
    assert sol.numIslands([["1", "1", "0", "0", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "1", "0", "0"],
                           ["0", "0", "0", "1", "1"]]) == 3
    assert sol.numIslands([["0", "0"],
                           ["0", "0"]]) == 0
    assert sol.numIslands([["0", "1"],
                           ["0", "1"],
                           ["0", "1"]]) == 1

