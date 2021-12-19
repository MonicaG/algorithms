"""
From: https://leetcode.com/discuss/interview-question/1488281/Amazon-OA and
https://www.reddit.com/r/leetcode/comments/rjf21f/just_did_the_amazon_oa_and_encountered_this/

Take away from this problem: Could approach this as a DP, backtracking problem. But this could be solved by inspecting
the data for the math solution below. Not sure how applicable this is to solving other problems, or if this is just
a one off. It is an example of looking at the data set and not jumping into immediately trying to solve it with a
solution I think will fit problem.

"""


def number_of_ways(pages: str) -> int:
    """
    Problem: Find the number of ways to select 3 pages in ascending index order such that no two adjacent selected pages
    are of the same type.

    Approach: This can be solved by math rather than by trying to traverse or store the possible combinations.
    If we assume a page is the middle page in the 3 page-combination, then find the number of opposite numbers to the
    left and right. Example: pages = "0010101001" . Suppose we are at index 6 (which is a 1). A valid combination of
    pages would be "010". So we need to find the number of zeros to the left and right of index 6. In this case there
    are four 0 to the left of index 6 and two 0 to the right of it. The number of combinations that can be made at
    index 6 is num_left_zeros * num_right_zeros (4 * 2).

    To calculate for the entire string we keep the running sum as we iterate over each character in the string. We also
    need to increment/decrement the left and right counters at each iteration. This is to keep the count of 1s and 0s
    correct for the left and right side. We also start iteration at index 1 and stop iterating at n-1.

    Example: pages = "01001"

    At the first 1, there is one 0 to the left and two 0 to the right. So there are two possible
    combinations at this point (1 * 2) ( 0,1,0 using indexes 0,1,2 and 0,1,0 using indexes 0,1,3). At the second
     0 there is one 1 to the left and one 1 to the right. So there is only one possible combination at this point
     (1 * 1) (1,0,1 using indexes 1,2,4). At the third 0, it is the same scenario as the second 0, only one possible
    combination (1 * 1) with 1,0,1 using index 1,3,4. Summing up the results gives the total number of possibilities
    2 + 1 + 1 = 4


    :param pages: a binary string where '0' is an ordinary page and '1' is a book marked page
    :return: the total number of ways to select 3 pages that meet the criterion
    """
    result = 0
    num_zeros_right_side = pages.count("0")
    num_zeros_left_side = 0
    num_ones_right_side = pages.count("1")
    num_ones_left_side = 0

    # adjust the left/right counts based on the first page
    if pages[0] == '0':
        num_zeros_right_side -= 1
        num_zeros_left_side = 1
    else:
        num_ones_right_side -= 1
        num_ones_left_side = 1

    for index in range(1, len(pages) - 1):
        current_page = pages[index]
        if current_page == '0':
            if num_ones_left_side > 0 and num_ones_right_side > 0:
                result += num_ones_left_side * num_ones_right_side
            num_zeros_left_side += 1
            num_zeros_right_side -= 1
        else:
            if num_zeros_left_side > 0 and num_zeros_right_side > 0:
                result += num_zeros_left_side * num_zeros_right_side
            num_ones_left_side += 1
            num_ones_right_side -= 1

    return result
