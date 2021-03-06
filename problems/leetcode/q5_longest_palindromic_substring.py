"""
Question: https://leetcode.com/problems/longest-palindromic-substring/

I didn't know how to do this one. I tried brute force to start, whereby I was comparing the first letter with the
last and then moving the pointers. This didn't work and I ended up with multiple loops.

I had to google and found the Expand around the center technique for determining palindromes.
One way to find palindromes is to compare the first letter to the last letter, the second letter to the 2nd to last
letter and so on.
Another way is to look at the palindrome as a mirror image of itself based on a center point. For example: the string
"aba" has a center point "b" and the letters are mirrored around that center point. So, we could set a left and right
pointer to the letter b. Then we would increment the right pointer, decrement the left pointer compare the letters and
so on.
If there is an even number of letters in the palindrome, then the center point is the two center letters. Example:
"abba" the center would be bb. In this case the left pointer would be the first b and the right pointer would be the
second b. Other than that the logic is the same.

To find an anagram within a string, then we need to loop over the string providing the index for the left and right
pointers. We need to peform the expand twice, once for the odd size case and once for the even sized case.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        # I stored the palindrome itself. Leetcode had an alternate solution where they store the position and
        # max length of the anagram. At the end they return the substring based on that position and length.
        # That approach is faster than my approach below as I'm getting the substring from each call to the
        # expand_around_center function. And then I'm checking lengths on the substring. Just checking the maths
        # is faster. This still works though.
        longest_palindrome = s[0]
        for i in range(len(s)):
            # find for odd sized, where the center is one character: "aba"
            palindrome_odd = self.expand_around_center(s, i, i)
            # find for even sized, where center is two characters: "abba"
            palindrome_even = self.expand_around_center(s, i, i + 1)
            temp_palindrome = palindrome_odd if len(palindrome_odd) > len(palindrome_even) else palindrome_even
            longest_palindrome = longest_palindrome if len(longest_palindrome) >= len(temp_palindrome) \
                else temp_palindrome
        return longest_palindrome

    def expand_around_center(self, s: str, left: int, right: int) -> str:
        """
        I returned a substring here. An alternative approach is to return the length of the substring
        :param s: the string to search
        :param left: index for left pointer to start at
        :param right: index for right pointer to start at
        :return: The substring
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]