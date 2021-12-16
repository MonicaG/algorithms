from problems.leetcode.q5_longest_palindromic_substring import Solution

def test_longest_palindroic_substring():
    sol = Solution()
    assert sol.longestPalindrome("banana") == "anana"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("baab") == "baab"
    assert sol.longestPalindrome("BAab") == "B"
    assert sol.longestPalindrome("BanaNa") == "ana"
