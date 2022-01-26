"""
leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

notes: https://monica-granbois.gitbook.io/cs-theory-and-problems/problems/leetcode/153.-find-minimum-in-rotated-sorted-array

"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # short circuit for arrays with 1 element
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                # the array isn't rotated so return the left element
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # the mid point is on the right side of the rotation point, so items are sorted in ascending order.
                # Example: that part of the array will look like: [2, 3, 4, 5]
                if nums[mid] >= nums[mid - 1]:
                    # if the value immediately to the left of the mid is less than the mid value, then we can still find
                    # a min value to the left of the mid point. Adjust the right pointer to that place
                    right = mid - 1
                else:
                    # if the value immediately to the left of the mid point is greater than the mid point value, then
                    # we're at the rotation point. Return the mid value as it's the min value.
                    return nums[mid]
            else:
                # mid point is on the left side of the rotation point. So the min value will be somewhere to the right
                # of the mid point. Adjust the left point to that place.
                # Example: [5, 6, 7, 0, 1, 2, 3, 4]. If mid is at index 1 (value 6), then the min value is somewhere to
                # the right of mid
                left = mid + 1
