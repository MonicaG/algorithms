from problems.leetcode.q417_pacific_atlantic_water_flow import Solution


def test():
    sol = Solution()
    assert sol.pacificAtlantic([[1]]) == [[0, 0]]
    assert sol.pacificAtlantic([[1, 2]]) == [[0, 0], [0, 1]]
    assert sol.pacificAtlantic([[2, 1], [1, 2]]) == [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert sol.pacificAtlantic(
        [[2, 1, 3],
         [1, 2, 3]]) == [[0, 0], [0, 2], [1, 0], [1, 1], [1, 2]]
    assert sol.pacificAtlantic(
        [[1, 2, 2, 3, 5],
         [3, 2, 3, 4, 4],
         [2, 4, 5, 3, 1],
         [6, 7, 1, 4, 5],
         [5, 1, 1, 2, 4]]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert sol.pacificAtlantic(
        [[2, 1, 3],
         [4, 5, 1],
         [6, 2, 7],
         [7, 4, 1]]) == [[0, 2], [1, 1], [3, 0]]

    assert sol.pacificAtlantic(
        [[2, 1, 3],
         [4, 5, 1],
         [6, 2, 7],
         [7, 1, 1]]) == [[0, 2], [1, 1], [2, 0], [3, 0]]

    assert sol.pacificAtlantic(
        [[2, 1, 3],
         [4, 5, 1],
         [6, 5, 7],
         [7, 1, 1]]) == [[0, 2], [1, 1], [2, 0], [2, 1], [2, 2], [3, 0]]
