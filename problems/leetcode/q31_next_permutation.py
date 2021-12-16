
class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        peak_index = self.get_peak_index(nums)
        if peak_index > 0:
            self.swap_value(nums, peak_index)
        self.reverse(nums, peak_index)

    def swap_value(self, nums, peak_index):
        val_to_swap = nums[peak_index - 1]
        for i in range(len(nums) - 1, peak_index - 1, -1):
            if nums[i] > val_to_swap:
                nums[peak_index - 1], nums[i] = nums[i], nums[peak_index - 1]
                break

    def reverse(self, nums, peak_index):
        tail_index = -1
        for index in range(peak_index, (len(nums) + peak_index) // 2):
            nums[index], nums[tail_index] = nums[tail_index], nums[index]
            tail_index -= 1

    def get_peak_index(self, nums: [int]):
        peak_index = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                peak_index = i
                break
        return peak_index
