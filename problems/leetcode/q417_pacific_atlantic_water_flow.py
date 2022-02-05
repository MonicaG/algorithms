"""
Question 417: https://leetcode.com/problems/pacific-atlantic-water-flow/
Notes: https://monica-granbois.gitbook.io/cs-theory-and-problems/problems/leetcode/417.-pacific-atlantic-water-flow
"""
from typing import List, Set


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])

        # implemented dfs function here so I could make use of the heights, num_rows and num_cols variables. Passing
        # them in as parameters resulted in too many parameters.
        def dfs(row: int, col: int, prev_height: int, visited: Set):
            # Since we are doing the dfs from the outer edges and working in we need to reverse the heights logic.
            # we do heights[row][col] < prev_height as water in a low area on the inside of the matrix won't make it
            # over a high area on the outer side of the matrix. So, we just return in that case.
            if (row, col) in visited or row < 0 or row >= num_rows or col < 0 or col >= num_cols or \
                    heights[row][col] < prev_height:
                return

            visited.add((row, col))
            cell_height = heights[row][col]
            dfs(row + 1, col, cell_height, visited)
            dfs(row - 1, col, cell_height, visited)
            dfs(row, col + 1, cell_height, visited)
            dfs(row, col - 1, cell_height, visited)

        pacific = set()
        atlantic = set()
        for c in range(num_cols):
            # the top row of the matrix flows into the pacific
            dfs(0, c, heights[0][c], pacific)
            # the bottom row of the matrix flows into the atlantic
            dfs(num_rows - 1, c, heights[num_rows - 1][c], atlantic)

        for r in range(num_rows):
            # the left side of the matrix (column 0 in all rows) flows into the pacific
            dfs(r, 0, heights[r][0], pacific)
            # the right side of the matrix (last column in all rows) flows into the atlantic
            dfs(r, num_cols - 1, heights[r][num_cols - 1], atlantic)

        # the answer requires a matrix. Otherwise, we could have done a set intersection instead, which would have been
        # more efficient. i.e. result = atlantic & pacific
        result = []
        for r in range(num_rows):
            for c in range(num_cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
