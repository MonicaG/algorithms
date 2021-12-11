import unittest
from problems.leetcode import q3_longest_substring


class Question3TestCase(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        sol = q3_longest_substring.Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(2, sol.lengthOfLongestSubstring("au"))
        self.assertEqual(3, sol.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(0, sol.lengthOfLongestSubstring(""))
        self.assertEqual(1, sol.lengthOfLongestSubstring("a"))
        self.assertEqual(1, sol.lengthOfLongestSubstring("aaaaaa"))


if __name__ == '__main__':
    unittest.main()
