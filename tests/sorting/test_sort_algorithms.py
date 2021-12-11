from algorithms.sorting.sort_algorithms import bubble_sort, selection_sort, insertion_sort


class TestSortAlgorithms:
    def test_bubble_sort(self):
        assert bubble_sort([65, 55, 45, 35, 25, 15, 10]) == [10, 15, 25, 35, 45, 55, 65]
        assert bubble_sort([37]) == [37]
        assert bubble_sort([37, 35]) == [35, 37]
        assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
        assert bubble_sort([4, 2, 7, 1, 3]) == [1, 2, 3, 4, 7]

    def test_selection_sort(self):
        assert selection_sort([65, 55, 45, 35, 25, 15, 10]) == [10, 15, 25, 35, 45, 55, 65]
        assert selection_sort([37]) == [37]
        assert selection_sort([37, 35]) == [35, 37]
        assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
        assert selection_sort([4, 2, 7, 1, 3]) == [1, 2, 3, 4, 7]

    def test_insertion_sort(self):
        assert insertion_sort([65, 55, 45, 35, 25, 15, 10]) == [10, 15, 25, 35, 45, 55, 65]
        assert insertion_sort([37]) == [37]
        assert insertion_sort([37, 35]) == [35, 37]
        assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
        assert insertion_sort([4, 2, 7, 1, 3]) == [1, 2, 3, 4, 7]
