from problems.leetcode.q11_container_with_most_water import Solution


def test_max_area():
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    # The first and last elements make the greatest area
    assert sol.maxArea([1, 1, 5, 1, 1]) == 4
    # The max area has the smallest width (just 1 width distance), but the height makes it the greatest area
    assert sol.maxArea([1, 1, 6, 7, 1, 1]) == 6
