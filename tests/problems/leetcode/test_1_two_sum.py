from problems.leetcode.q1_two_sum import Solution


def test_cache_solution():
    sol = Solution()
    assert sol.twoSum_cache([], 5) == []
    assert sol.twoSum_cache([11, 7, 2, 15], 9) == [1, 2]
    assert sol.twoSum_cache([5, 30, 1, 20, 2, 27], 25) == [0, 3]
    assert sol.twoSum_cache([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum_cache([3, 3], 6) == [0, 1]


def test_two_pointer_solution():
    sol = Solution()
    assert sol.twoSum_two_pointer([], 5) ==[]
    assert sol.twoSum_two_pointer([11, 7, 2, 15], 9) == [1, 2]
    assert sol.twoSum_cache([5, 30, 1, 20, 2, 27], 25) == [0, 3]
    assert sol.twoSum_two_pointer([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum_two_pointer([3, 3], 6) == [0, 1]
