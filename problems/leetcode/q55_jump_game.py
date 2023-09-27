from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest_index = len(nums) - 1
        prev_index = dest_index - 1
        for i in range(1, len(nums)):
            if nums[prev_index] >= dest_index - prev_index:
                dest_index = prev_index
                prev_index = dest_index - 1
            else:
                prev_index = prev_index - 1
            
        return dest_index == 0
