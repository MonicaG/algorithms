from collections import defaultdict

"""
424. Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

What I learned: For leetcode questions use the test runner to verify my understanding of the problem. Have the solution
return a dummy value. Put in my test cases and get the results to verify my understanding.  

I read the question wrong, and made it harder than it needed to be.  I thought you could only pick one
character to replace with another character. For example, could only replace B's with A's. But this is not the case.
You could replace multiple letters with the chosen letter. Example:
s = "ABCA" k = 2
Answer 4 because B and C could be replaced with A's.
solution "AAAA" answer 4 


Solution:
A sliding window is used to keep track of the longest substring. As the right pointer increments, we need to check if
k has been exceeded. k is the number of characters we can change (although we could change less than k). By keeping
track of the letter frequency in the sliding window we can determine if the left pointer needs to increment (and 
hence decrement the frequency for the letter that is leaving the window). 
 
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        # sliding window pointers
        left, right = 0, 0
        # answer
        max_substring = 0
        # could also be a for loop
        while right < len(s):
            char_freq[s[right]] += 1
            # add 1 because a single letter would have a substring length of 1
            width = right - left + 1
            # The highest frequency letter will not be changed, as it will form the longest substring. So, its frequency
            # is subtracted from the width of the sliding window. k is the number of letters to change.  If the width
            # minus the max frequency is greater than k, then the left side of the window needs to increment (and we
            # need to decrement the letter that is leaving the sliding window).
            if width - max(char_freq.values()) > k:
                # if we're over k then we need to move the left side of the window along. But first decrement the
                # character frequency as that instance of the letter is no longer part of the sliding window
                char_freq[s[left]] -= 1
                left += 1
            else:
                max_substring = max(max_substring, width)
            right += 1

        return max_substring
