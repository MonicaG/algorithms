"""
See: https://leetcode.com/problems/top-k-frequent-elements/

Note: the problem defined the following constraints:
* 1 <= nums.length <= 10^5
* k is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.

So, error checking is not performed on nums and k.
"""

from collections import Counter
import heapq
import random
from typing import List


class Solution:
    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = sorted(freq.keys(), key=lambda n: freq[n], reverse=True)
        return result[:k]

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        # This is the case where nums is unique numbers, so everything has a frequency of 1.
        # Example nums=[1,2,3,4], k=4
        if len(nums) == k:
            return nums
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)

    def topKFrequent_bucket_sort(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        freq = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

    def topKFrequent_quick_select(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        counts = Counter(nums)
        unique_nums = list(counts.keys())

        def partition(left, right):
            pivot_index = (left + right) // 2
            unique_nums[right], unique_nums[pivot_index] = unique_nums[pivot_index], unique_nums[right]
            mark = left
            for i in range(left, right):
                if counts[unique_nums[i]] < counts[unique_nums[right]]:
                    unique_nums[i], unique_nums[mark] = unique_nums[mark], unique_nums[i]
                    mark += 1
            unique_nums[mark], unique_nums[right] = unique_nums[right], unique_nums[mark]
            return mark

        def select(left, right, kth_position):
            val = partition(left, right)
            if val < kth_position:
                select(val + 1, right, kth_position)
            elif val > kth_position:
                select(left, val - 1, kth_position)
            else:
                return

        k_position = len(unique_nums) - k
        select(0, len(unique_nums) - 1, k_position)
        return unique_nums[k_position:]

