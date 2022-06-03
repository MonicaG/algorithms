from algorithms.sorting import quick_select


def test_kth_smallest():
    arr = [5, 6, 1, 9, 3, 8, 4, 0, 2]
    assert quick_select.kth_smallest(1, arr) == 0
    assert quick_select.kth_smallest(2, arr) == 1
    assert quick_select.kth_smallest(3, arr) == 2
    assert quick_select.kth_smallest(4, arr) == 3
    assert quick_select.kth_smallest(5, arr) == 4
    assert quick_select.kth_smallest(6, arr) == 5
    assert quick_select.kth_smallest(7, arr) == 6
    assert quick_select.kth_smallest(8, arr) == 8
    assert quick_select.kth_smallest(9, arr) == 9
    assert quick_select.kth_smallest(10, arr) is None
    assert quick_select.kth_smallest(0, arr) is None

