from typing import List

"""
1. Two Sum: https://leetcode.com/problems/two-sum/

What I learned: The cache solution is the easiest approach for this question. However, the problem can also be solved 
using two pointers. The two pointers method is used for solving the Three Sum problem.  See the method below for a 
description of how the two pointers work.  
"""


class Solution:

    def twoSum_cache(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cache:
                return [cache[diff], i]
            else:
                cache[nums[i]] = i
        return []

    def twoSum_two_pointer(self, nums: List[int], target: int) -> List[int]:
        """
        The idea is to sort the array. Then have two pointers, left and right. Add the two pointers together. If the
        result is greater than the target value, then we need to move the right pointer to the left (and hence resulting
        in a smaller sum the next time). If the result is less than the result, then the left pointer needs to move to
        the right. If the summation equals then we found the target.

        Example: input = [11, 7, 2, 15], target = 9
        first sort: [2, 7, 11, 15]
        left = 0 (start of the array)
        right = 3 (end position of the array
        input[left] + input[right] = 2 + 15 = 17
        17 > 9
         right = 2
        input[left] + input[right] = 2 + 11 = 13
        13 > 9
        right = 1
        input[left] + input[right] = 2 + 7 = 9 found solution!
        """
        # this gets us index and value for the elements in nums. We need to do this so we have the original location of
        # the value after the sorting is performed
        sortd = enumerate(nums)
        # now sort based on the value
        sortd = sorted(sortd, key=lambda x: x[1])
        left = 0
        right = len(sortd) - 1
        while left < right:
            # need position 1 here to get the value
            summ = sortd[left][1] + sortd[right][1]
            if target == summ:
                # need position 0 here to get the location. The min,max is done here to ensure
                # value is returned with the lowest position listed first.
                return [min(sortd[left][0], sortd[right][0]), max(sortd[left][0], sortd[right][0])]
            elif summ < target:
                left += 1
            else:
                right -= 1
        return []
