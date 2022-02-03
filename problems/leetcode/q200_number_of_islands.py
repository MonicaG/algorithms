from typing import List, Set

"""
leet code question 200:  https://leetcode.com/problems/number-of-islands/
"""


class Solution:
    def __dfs(self, grid: List[List[str]], m: int, n: int, visited: Set):
        if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[m]) or grid[m][n] == "0" or (m, n) in visited:
            return
        visited.add((m, n))
        # In the standard DFS algorithm we usually have a for loop to iterate over the adjacent vertices list. Here, we
        # look in the surrounding cells instead.
        self.__dfs(grid, m + 1, n, visited)
        self.__dfs(grid, m - 1, n, visited)
        self.__dfs(grid, m, n + 1, visited)
        self.__dfs(grid, m, n - 1, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        visited = set()
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if (m, n) not in visited and grid[m][n] == "1":
                    num += 1
                    self.__dfs(grid, m, n, visited)
        return num


class Solution2:
    def __dfs(self, grid, m, n, i, j):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
            return
        grid[i][j] = "X"
        self.__dfs(grid, m, n, i - 1, j)
        self.__dfs(grid, m, n, i + 1, j)
        self.__dfs(grid, m, n, i, j + 1)
        self.__dfs(grid, m, n, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num += 1
                    self.__dfs(grid, m, n, i, j)

        return num
