from typing import List
"""
 11: Container With Most Water - https://leetcode.com/problems/container-with-most-water/
 What I learned: I did the brute force solution to start with. This solution timed out as I expected it would. But,
 my math worked out, which showed I understood that part of the problem. I looked at the hint next. I implemented a 
 two pointer solution.
 
 The idea is to set a left pointer to the start of the array and the right pointer to the end of the array.
 The area is then calculated based on the formula:
 area = right - left * min(height[left], height[right])
 
 So, on the first iteration, the width (right - left) is the greatest. It is then multiplied by the shortest height,
 of height[left] and height[right] (heights are stored in the heights array, i.e. height[n]).
 
 However, there could be a greater area, if there is a larger height in the array. So, we need to move the left or
 right pointer (depending on which is the smaller one). By moving the smaller one, we are attempting to find a larger
 height, that could cause the area to be greater despite the smaller width.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

    # def maxAreaBruteForce(self, height: List[int]) -> int:
    #     max_area = 0
    #     for i in range(len(height) - 1):
    #         for j in range(i + 1, len(height)):
    #             x = j - i
    #             y = min(height[i], height[j])
    #             area = x * y
    #             max_area = max(max_area, area)
    #     return max_area
