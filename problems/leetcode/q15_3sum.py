from typing import List

"""
15 - 3Sum. This builds off of 2Sum problem that uses the two pointer solution. I found these posts helpful to understand
3Sum: https://en.wikipedia.org/wiki/3SUM and https://fizzbuzzed.com/top-interview-questions-1/

Below are two implementations. One that uses a set to handle the duplicates. The other handles duplicates by skipping
through duplicate numbers.

The idea behind the two pointer solution is:
- step 1: sort the array
- step 2: loop for the array. For each item, set a start and end (left and right) pointer. Summing the 3 numbers (the
current number from outer loop + the start pointer number+ the end pointer number) will give either less than zero, zero
or greater than zero. If it's zero we found a solution. If it is a positive value then we need to decrement the end 
pointer as we need the sum to be less (move down to zero). If it is a negative value then we increment the start pointer
as we need the sum to be greater (move up to zero).  
"""
class Solution:


    def threeSum_skip_dup_nums(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            a = nums[i]
            # skip duplicate numbers
            if i > 0 and a == nums[i - 1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                summ = a + b + c
                if summ == 0:
                    result.append([a, b, c])
                    # the while loops is what lets us use an array rather than a set to store the result (since
                    # duplicates are not allowed). Here duplicate numbers are skipped by.
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif summ > 0:
                    end -= 1
                else:
                    start += 1

        return result

    def threeSum_uses_set(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            a = nums[i]
            #skip duplicate numbers
            if i > 0 and a == nums[i - 1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                if a + b + c == 0:
                    result.add((a, b, c))
                    start += 1
                    end -= 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    start += 1
        return list(map(list, result))

