from typing import List
# Short circuit BubbleSort implementation. If no elements are swapped then we know the list is sorted.
# In this case we do not need to do anymore passes of the array and can exit the algorithm
def bubble_sort(nums: List[int]):
    did_swap_elements = True
    # subtract one here so we don't have to worry about index out of bounds error when using the right_item_index below
    end_range = len(nums) - 1
    while did_swap_elements:
        did_swap_elements = False
        for left_item_index in range(end_range):
            right_item_index = left_item_index + 1
            if nums[left_item_index] > nums[right_item_index]:
                nums[left_item_index], nums[right_item_index] = nums[right_item_index], nums[left_item_index]
                did_swap_elements = True
        # end_range is decremented because we know the tail end is sorted, so no need to operate on it again.
        end_range -= 1
    return nums


def selection_sort(nums: List[int]):
    # 1 is subtracted from the len(nums) because by the last element, the array will be sorted. So don't need to
    # process it again.
    for start_index in range(len(nums) - 1):
        low_index = start_index
        # 1 is added to the start_index, because there is no point in comparing the first start_index to itself.
        for i in range(start_index + 1, len(nums)):
            if nums[i] < nums[low_index]:
                low_index = i
        if start_index != low_index:
            nums[start_index], nums[low_index] = nums[low_index], nums[start_index]
    return nums


def insertion_sort(nums: List[int]):
    for index in range(1, len(nums)):
        temp = nums[index]
        check_index = index - 1
        while check_index >= 0 and temp < nums[check_index]:
            nums[check_index + 1] = nums[check_index]
            check_index -= 1
        nums[check_index + 1] = temp
    return nums
