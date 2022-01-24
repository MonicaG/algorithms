from problems.leetcode.q33_search_in_rotated_sorted_array import Solution


def test_recursive():
    sol = Solution()
    assert sol.search_recursive([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search_recursive([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search_recursive([1], 0) == -1
    assert sol.search_recursive([1, 2, 3, 4, 5, 6, 7], 4) == 3
    assert sol.search_recursive([2, 1], 1) == 1
    assert sol.search_recursive([2, 1], 2) == 0
    assert sol.search_recursive([2], 2) == 0
    assert sol.search_recursive([1, 3], 3) == 1
    assert sol.search_recursive([3, 5, 1], 3) == 0
    assert sol.search_recursive([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
    assert sol.search_recursive([1, 2, 3, 4, 5, 6], 4) == 3
    assert sol.search_recursive([8, 1, 2, 3, 4, 5, 6, 7], 6) == 6


def test_iterative():
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    assert sol.search([1, 2, 3, 4, 5, 6, 7], 4) == 3
    assert sol.search([2, 1], 1) == 1
    assert sol.search([2, 1], 2) == 0
    assert sol.search([2], 2) == 0
    assert sol.search([1, 3], 3) == 1
    assert sol.search([3, 5, 1], 3) == 0
    assert sol.search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
    assert sol.search([1, 2, 3, 4, 5, 6], 4) == 3
    assert sol.search([1, 2, 3, 4, 5, 6], 7) == -1
    assert sol.search([8, 1, 2, 3, 4, 5, 6, 7], 6) == 6
