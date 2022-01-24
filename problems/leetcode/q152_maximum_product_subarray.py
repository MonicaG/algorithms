from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_product = nums[0]
        max_product = nums[0]
        min_product = nums[0]
        for i in range(1, len(nums)):
            prev_current_product = current_product
            current_product = max(min_product * nums[i], current_product * nums[i], nums[i])
            min_product = min(min_product * nums[i], prev_current_product * nums[i], nums[i])
            max_product = max(max_product, current_product)
        return max_product

