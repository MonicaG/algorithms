from problems.ctci.chapter1 import rotate_matrix, is_string_rotation


def test_rotate_matrix():
    """
    1   2  3  4
    5   6  7  8
    9  10 11 12
    13 14 15 16

    Becomes

    13  9 5 1
    14 10 6 2
    15 11 7 3
    16 12 8 4

    """
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    expected = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    rotate_matrix(matrix)
    assert matrix == expected


def test_is_string_rotation():
    assert is_string_rotation("waterbottle", "erbottlewat")
    assert is_string_rotation("waterbottle", "bottlewater")
    assert is_string_rotation("title", "tleti")
    assert is_string_rotation("aaaa", "aaaa")
    assert is_string_rotation("look", "look")
    assert is_string_rotation("lily", "ylil")
    assert not is_string_rotation("abc", "defghij")
    assert not is_string_rotation("waterbottle", "elttobrewat")
    assert not is_string_rotation("", "") 

