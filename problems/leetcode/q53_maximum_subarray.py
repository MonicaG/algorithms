"""
53. Maximum Subarray: https://leetcode.com/problems/maximum-subarray/

What I learned from this problem: I was on the right track to the optimal solution which is Kadane's Algorithm (see
 https://en.wikipedia.org/wiki/Maximum_subarray_problem). I should have taken extra time to look at my nested if
 statements. I knew it was bad, but just submitted anyway. If I stopped and looked closer, I think I could have
 simplified it closer to Kadane's Algorithm. I was happy I found the O(N) solution.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        This is my original answer to the problem
        """
        current_sum = nums[0]
        high_sum = current_sum
        for i in range(1, len(nums)):
            if current_sum < 0:
                if nums[i] > 0:
                    current_sum = nums[i]
                else:
                    current_sum = max(current_sum, nums[i])
            else:
                current_sum += nums[i]
            high_sum = max(current_sum, high_sum)

        return high_sum

    def maxSubArrayKadaneAlgo(self, nums: List[int]) -> int:
        current_sum = nums[0]
        high_sum = current_sum
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            high_sum = max(current_sum, high_sum)
        return high_sum

    def maxSubArray_brute(self, nums: List[int]) -> int:
        high_sum = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum < 0:
                    current_sum = 0
                high_sum = max(high_sum, current_sum)
        return high_sum

    def kadane_original(self, nums: List[int]) -> int:
        high_sum = 0
        current_sum = 0
        for i in nums:
            current_sum = max(0, current_sum + i)
            high_sum = max(high_sum, current_sum)
        return high_sum



