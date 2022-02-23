from typing import List
"""
Problem: https://leetcode.com/problems/non-overlapping-intervals/
Solution: https://monica-granbois.gitbook.io/cs-theory-and-problems/problems/leetcode/435.-non-overlapping-intervals
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        answer = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < end:
                answer += 1
                end = min(end, interval[1])
            else:
                end = interval[1]
        return answer
