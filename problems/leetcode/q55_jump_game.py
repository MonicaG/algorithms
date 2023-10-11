from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest_index = len(nums) - 1
        prev_index = dest_index - 1
        for i in range(1, len(nums)):
            # Need to substract previous index from destination 
            # index to get the jump distance. 
            if nums[prev_index] >= dest_index - prev_index:
                # if the element can 'jump' to or beyond the destination index then a 
                # potential path has been found. Reset the destination index to this 
                # location. On the next loop it will check if this new destination
                # index is reachable
                dest_index = prev_index
                prev_index = dest_index - 1
            else:
                # the element cannot jump to this location. Try again with a previous
                # element
                prev_index = prev_index - 1

        # If destination index is set to 0 then a path was found to the start of the list. 
        # Hence there is a path to the end of the list    
        return dest_index == 0
