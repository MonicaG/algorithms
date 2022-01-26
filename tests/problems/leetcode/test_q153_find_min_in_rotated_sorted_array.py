from problems.leetcode.q153_find_min_in_rotated_sorted_array import Solution


def test():
    sol = Solution()
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.findMin([11, 13, 15, 17]) == 11
    assert sol.findMin([1, 2, 3, 4, 5]) == 1
    assert sol.findMin([5, 1, 2, 3, 4]) == 1
    assert sol.findMin([4, 5, 1, 2, 3]) == 1
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([2, 3, 4, 5, 1]) == 1
    assert sol.findMin([1]) == 1
    assert sol.findMin([1, 2]) == 1
    assert sol.findMin([2, 1]) == 1
    assert sol.findMin([1, 2, 3]) == 1
    assert sol.findMin([3, 1, 2]) == 1
    assert sol.findMin([2, 3, 1]) == 1
    assert sol.findMin([-4, 0, 5, 23]) == -4
    assert sol.findMin([23, -4, 0, 5]) == -4
    assert sol.findMin([5, 23, -4, 0]) == -4
    assert sol.findMin([0, 5, 23, -4]) == -4
    assert sol.findMin([0]) == 0
