from problems.leetcode import q3_longest_substring


def test_length_of_longest_substring():
    sol = q3_longest_substring.Solution()
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("au") == 2
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("a") == 1
    assert sol.lengthOfLongestSubstring("aaaaaa") == 1
