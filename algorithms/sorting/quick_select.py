from typing import List


def lomuto_partition(arr: List[int], left: int, right: int) -> int:
    # There are various schemes to choose a pivot point. This code is using the midpoint. Some other options use
    # the right most element, a random index, median of 3 (median of first, middle and last element of the partition),
    # and median of medians
    pivot_index = (left + right) // 2
    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
    mark = left
    for i in range(left, right):
        if arr[i] < arr[right]:
            arr[i], arr[mark] = arr[mark], arr[i]
            mark += 1
    arr[mark], arr[right] = arr[right], arr[mark]
    return mark


def quick_select(k: int, arr: List[int], left, right) -> int:
    position = lomuto_partition(arr, left, right)
    if position < k:
        return quick_select(k, arr, position + 1, right)
    elif position > k:
        return quick_select(k, arr, left, position - 1)
    else:
        return position


def kth_smallest(k: int, arr: List[int]) -> int | None:
    if k <= 0 or k > len(arr):
        return None
    # k - 1 because arrays are zero based. So, if we want to find the first smallest item, it will be at index 0
    # If we want to find the 4th smallest item, it will be at index 3.
    kth_position = quick_select(k - 1, arr, 0, len(arr) - 1)
    return arr[kth_position]
