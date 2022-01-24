from typing import List


def binary_search(nums: List[int], target: [int]) -> int | None:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def binary_search_recursive(nums: List[int], target: [int]) -> int | None:
    def recursive(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return recursive(mid + 1, right)
        else:
            return recursive(left, mid - 1)

    return recursive(0, len(nums) - 1)
