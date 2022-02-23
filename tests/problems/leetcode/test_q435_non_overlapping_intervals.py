from problems.leetcode.q435_non_overlapping_intervals import Solution


def test():
    sol = Solution()
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    assert sol.eraseOverlapIntervals([[3, 4], [1, 4]]) == 1
    assert sol.eraseOverlapIntervals([[3, 4], [1, 3]]) == 0
    assert sol.eraseOverlapIntervals([[6, 10], [5, 7], [7, 9]]) == 1
    assert sol.eraseOverlapIntervals([[6, 10], [5, 7], [7, 9], [8, 11]]) == 2
    assert sol.eraseOverlapIntervals([[5, 20], [7, 10]]) == 1
    assert sol.eraseOverlapIntervals([[6, 10], [7, 9]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2], [2, 7], [2, 9]]) == 3
    assert sol.eraseOverlapIntervals([[1, 20], [3, 5], [7, 10], [12, 15]]) == 1
