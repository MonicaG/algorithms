from typing import List

"""
56. merge intervals: https://leetcode.com/problems/merge-intervals/
What I learned: to merge items, add first item to the result. Then iterate through the list and either update the tail 
item in the result or append a new item to the result. This is easier than trying to handle the merge by taking two 
items from the array, merging  them and then inserting into the array. Which was convoluted when I needed to then 
compare the merged item to the next item in the array.
I figured out that I needed to sort the array in order to compare the items. 
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x:(x[0], x[1]))
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(intervals[i][1], result[-1][1])]
            else:
                result.append(intervals[i])
        return result
