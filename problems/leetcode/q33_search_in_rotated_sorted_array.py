from typing import List


class Solution:

    def search_recursive(self, nums: List[int], target: int) -> int:
        def recurse(left, right) -> int:
            if left > right:
                return -1
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    return recurse(mid + 1, right)
                return recurse(left, mid - 1)
            if nums[mid] >= target >= nums[left]:
                return recurse(left, mid - 1)
            return recurse(mid + 1, right)

        return recurse(0, len(nums) - 1)

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                # we are in an ordered part of the array:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # we are in an un ordered part of the array
                if nums[mid] >= target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1




