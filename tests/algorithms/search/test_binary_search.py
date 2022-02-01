from algorithms.search.binary_search import binary_search, binary_search_recursive


def test():
    assert binary_search([], 3) is None
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) is None
    assert binary_search([1, 2], 1) == 0
    assert binary_search([1, 2], 2) == 1
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 1) == 0
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 2) == 1
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 3) == 2
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 5) == 4
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 6) == 5
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 7) == 6
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 10) is None
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 0) is None
    assert binary_search([-7, -3, 0, 2, 7, 13], -7) == 0
    assert binary_search([-7, -3, 0, 2, 7, 13], -3) == 1
    assert binary_search([-7, -3, 0, 2, 7, 13], 0) == 2
    assert binary_search([-7, -3, 0, 2, 7, 13], 2) == 3
    assert binary_search([-7, -3, 0, 2, 7, 13], 7) == 4
    assert binary_search([-7, -3, 0, 2, 7, 13], 13) == 5
    assert binary_search([-7, -3, 0, 2, 7, 13], 20) is None
    assert binary_search([-7, -3, 0, 2, 7, 13], -9) is None


def test_recursive():
    assert binary_search_recursive([], 3) is None
    assert binary_search_recursive([1], 1) == 0
    assert binary_search_recursive([1], 2) is None
    assert binary_search_recursive([1, 2], 1) == 0
    assert binary_search_recursive([1, 2], 2) == 1
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 1) == 0
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 2) == 1
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 3) == 2
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 4) == 3
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 5) == 4
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 6) == 5
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 7) == 6
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 10) is None
    assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 0) is None
    assert binary_search_recursive([-7, -3, 0, 2, 7, 13], -7) == 0
    assert binary_search_recursive([-7, -3, 0, 2, 7, 13], -3) == 1
    assert binary_search_recursive([-7, -3, 0, 2, 7, 13], 0) == 2
    assert binary_search_recursive([-7, -3, 0, 2, 7, 13], 2) == 3
    assert binary_search_recursive([-7, -3, 0, 2, 7, 13], 7) == 4
    assert binary_search_recursive([-7, -3, 0, 2, 7, 13], 13) == 5
    assert binary_search_recursive([-7, -3, 0, 2, 7, 13], 20) is None
    assert binary_search_recursive([-7, -3, 0, 2, 7, 13], -9) is None