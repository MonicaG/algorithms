from typing import List


class Solution:

    def search_recursive(self, nums: List[int], target: int) -> int:
        # re-implemented the iterative solution as a recursive solution.
        def recurse(left, right) -> int:
            if left > right:
                return -1
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > nums[right]:
                if target > nums[mid] or target < nums[left]:
                    return recurse(mid+1, right)
                else:
                    return recurse(left, mid - 1)
            else:
                if target < nums[mid] or target > nums[right]:
                    return recurse(left, mid - 1)
                else:
                    return recurse(mid + 1, right)
        return recurse(0, len(nums) - 1)

    def search(self, nums: List[int], target: int) -> int:
        # [7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] > nums[right]:
                # in the left side of the array
                if target > nums[mid] or target < nums[left]:
                    # Example: [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
                    # Assume mid point is index 2 (value 7). We need to search to the right of the mid point for the
                    # cases: 1) the target is greater than the mid (i.e. target is 9) or 2) the target is less than
                    # the mid point, but the value is actually on the right side of the array (i.e. target is 3)
                    left = mid + 1
                else:
                    # This scenario is reached when we just need to search the left side of the array. This occurs when
                    # the target value is less than or equal to the mid point and the target is on the left side of the
                    # array (i.e. target is 6)
                    right = mid - 1
            else:
                # in the right side of array
                if target < nums[mid] or target > nums[right]:
                    # Example: [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
                    # Assume mid point is index 8 (value 3). We need to search to the left of the mid point for the
                    # cases: 1) target is less than the mid (i.e. target is 0) or 2) the target is greater than the mid
                    # point, but the value is actually on the left side of the array (i.e. target is 6)
                    right = mid - 1
                else:
                    # This scenario is reached when we need to search just the right side of the array. This occurs when
                    # the target value is greater or equal to the mid point value and the target is on the right side of
                    # the array (i.e. target 4).
                    left = mid + 1
        return -1
