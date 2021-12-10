import unittest
from algorithms.sorting.sort_algorithms import bubble_sort, selection_sort, insertion_sort


class SortAlgorithmsTestCase(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual([10, 15, 25, 35, 45, 55, 65], bubble_sort([65, 55, 45, 35, 25, 15, 10]))
        self.assertEqual([37], bubble_sort([37]))
        self.assertEqual([35, 37], bubble_sort([37, 35]))
        self.assertEqual([1, 2, 3, 4], bubble_sort([1, 2, 3, 4]))
        self.assertEqual([1, 2, 3, 4, 7], bubble_sort([4, 2, 7, 1, 3]))

    def test_selection_sort(self):
        self.assertEqual([10, 15, 25, 35, 45, 55, 65], selection_sort([65, 55, 45, 35, 25, 15, 10]))
        self.assertEqual([37], selection_sort([37]))
        self.assertEqual([35, 37], selection_sort([37, 35]))
        self.assertEqual([1, 2, 3, 4], selection_sort([1, 2, 3, 4]))
        self.assertEqual([1, 2, 3, 4, 7], selection_sort([4, 2, 7, 1, 3]))

    def test_insertion_sort(self):
        self.assertEqual([10, 15, 25, 35, 45, 55, 65], insertion_sort([65, 55, 45, 35, 25, 15, 10]))
        self.assertEqual([37], insertion_sort([37]))
        self.assertEqual([35, 37], insertion_sort([37, 35]))
        self.assertEqual([1, 2, 3, 4], insertion_sort([1, 2, 3, 4]))
        self.assertEqual([1, 2, 3, 4, 7], insertion_sort([4, 2, 7, 1, 3]))


if __name__ == '__main__':
    unittest.main()
