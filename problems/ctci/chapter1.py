#question 1.7
def rotate_matrix(matrix):
    size = len(matrix)
    for layer in range(size//2):
        first = layer
        last = size - 1 - layer
        for j in range(first, last):
            offset = j - first
            top_value = matrix[first][j]
            right_side = matrix[j][last]
            bottom = matrix[last][last - offset]
            left = matrix[last-offset][first]

            matrix[j][last] = top_value
            matrix[last][last-offset] = right_side
            matrix[last-offset][first] = bottom
            matrix[first][j] = left


def is_string_rotation(s1: str, s2: str) -> bool:
    """
    question 1.9
    I messed this one up and didn't see the pattern of stringing s1 together twice to check for the substring.
    I guess I should have read all the hints. My original attempt (which didn't work for lily when rotated on the y
    is commented out below
    """
    def is_substring(s1: str, s2: str) -> bool:
        return False if s1.find(s2) == -1 else True

    if len(s1) != len(s2) or len(s1) == 0 or len(s2) == 0:
        return False

    double_string = s1 + s1
    return is_substring(double_string, s2)

    # first_letter = s1[0]
    # rotation_point = None
    # for i in range(len(s2) - 1, -1, -1):
    #     if first_letter == s2[i]:
    #         rotation_point = i
    #         break
    # # check tail matches
    # print(rotation_point)
    # if rotation_point is not None:
    #     length_of_tail = len(s2) - rotation_point
    #     print(length_of_tail)
    #     if s1[0:length_of_tail] == s2[rotation_point:]:
    #         substring = s2[0:rotation_point]
    #         print(substring)
    #         return is_substring(s1, substring)
    #     else:
    #         return False
    # return False
