import pytest
import unittest
from problems.leetcode.q347_top_k_frequent_elements import Solution


@pytest.fixture()
def mixed_input_list():
    return [1, 1, 1, 2, 2, 3]


@pytest.fixture()
def two_nums_with_same_freq():
    return [1, 5, 1, 5, 3, 4]


@pytest.fixture()
def all_nums_same_list():
    return [2, 2, 2, 2, 2]


@pytest.fixture()
def only_one_number():
    return [1]


def test_sort(mixed_input_list, all_nums_same_list, only_one_number, two_nums_with_same_freq):
    sol = Solution()
    assert sol.topKFrequent_sort(mixed_input_list, 1) == [1]
    assert sol.topKFrequent_sort(mixed_input_list, 2) == [1, 2]
    assert sol.topKFrequent_sort(mixed_input_list, 3) == [1, 2, 3]

    assert sol.topKFrequent_sort(all_nums_same_list, 1) == [2]

    assert sol.topKFrequent_sort(only_one_number, 1) == [1]

    assert sol.topKFrequent_sort(two_nums_with_same_freq, 2) == [1, 5]


def test_heap(mixed_input_list, all_nums_same_list, only_one_number, two_nums_with_same_freq):
    sol = Solution()
    assert sol.topKFrequent_heap(mixed_input_list, 1) == [1]
    assert sol.topKFrequent_heap(mixed_input_list, 2) == [1, 2]
    assert sol.topKFrequent_heap(mixed_input_list, 3) == [1, 2, 3]

    assert sol.topKFrequent_heap(all_nums_same_list, 1) == [2]

    assert sol.topKFrequent_heap(only_one_number, 1) == [1]

    assert sol.topKFrequent_heap(two_nums_with_same_freq, 2) == [1, 5]


def test_bucket_sort(mixed_input_list, all_nums_same_list, only_one_number, two_nums_with_same_freq):
    sol = Solution()
    assert sol.topKFrequent_bucket_sort(mixed_input_list, 1) == [1]
    assert sol.topKFrequent_bucket_sort(mixed_input_list, 2) == [1, 2]
    assert sol.topKFrequent_bucket_sort(mixed_input_list, 3) == [1, 2, 3]

    assert sol.topKFrequent_bucket_sort(all_nums_same_list, 1) == [2]

    assert sol.topKFrequent_bucket_sort(only_one_number, 1) == [1]

    assert sol.topKFrequent_bucket_sort(two_nums_with_same_freq, 2) == [1, 5]


def test_quick_select(mixed_input_list, all_nums_same_list, only_one_number, two_nums_with_same_freq):
    sol = Solution()
    ut = unittest.TestCase()
    ut.assertCountEqual(sol.topKFrequent_quick_select(mixed_input_list, 1), [1])
    ut.assertCountEqual(sol.topKFrequent_quick_select(mixed_input_list, 2), [1, 2])
    ut.assertCountEqual(sol.topKFrequent_quick_select(mixed_input_list, 3), [1, 2, 3])

    ut.assertCountEqual(sol.topKFrequent_quick_select(all_nums_same_list, 1), [2])

    ut.assertCountEqual(sol.topKFrequent_quick_select(only_one_number, 1), [1])
                            
    ut.assertCountEqual(sol.topKFrequent_quick_select(two_nums_with_same_freq, 2), [1, 5])