import unittest
from algorithms.strings_arrays import longestString


class MyTestCase(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        sol = longestString.Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(2, sol.lengthOfLongestSubstring("au"))
        self.assertEqual(3, sol.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(0, sol.lengthOfLongestSubstring(""))
        self.assertEqual(1, sol.lengthOfLongestSubstring("a"))
        self.assertEqual(1, sol.lengthOfLongestSubstring("aaaaaa"))


if __name__ == '__main__':
    unittest.main()
