"""
Question: https://leetcode.com/problems/product-of-array-except-self/

Take a way from this question: Remember that iterating through an array is O(N) providing we iterate once and then
iterate again after it. O(N)^2 is when the for loops are nested. So here, we multiply the left side of the array for
the given i. Then we iterate a second time from the end of the list and multiply with the results from the first step
to get the answer.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        tally = 1
        for i in range(len(nums) - 2, -1, -1):
            tally *= nums[i + 1]
            answer[i] = answer[i] * tally
        return answer
