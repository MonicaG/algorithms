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

    def productExceptSelf_multipleArrays(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        answer = [1] * len(nums)

        # [2, 3, 4, 5]
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        # left_Side = [1,2, 6, 24]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
            answer[i] = right[i] * left[i]
        # right = [60, 20, 5, 1]
        for i in range(len(nums)):
            answer[i] = left[i] * right[i]

        return answer


