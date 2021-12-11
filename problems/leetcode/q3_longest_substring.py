from collections import defaultdict
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# solution uses a sliding window.


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        answer = 0
        seen_letters = defaultdict(int)
        left_window_edge = 0
        for right_window_edge, right_letter in enumerate(s):
            seen_letters[right_letter] += 1
            while seen_letters.get(right_letter) > 1:
                left_char = s[left_window_edge]
                seen_letters[left_char] -= 1
                left_window_edge += 1

            answer = max(answer, right_window_edge - left_window_edge + 1)

        return answer

    # Optimized sliding window, where the position of the character is stored as the hash value
    # if len(s) <= 1:
    #     return len(s)
    # answer = 0
    # seen_letters = defaultdict(int)
    # char_position = 0
    # for right_window_edge, right_letter in enumerate(s):
    #     if seen_letters[right_letter]:
    #         char_position = max(seen_letters[right_letter], char_position)
    #     answer = max(answer, right_window_edge - char_position + 1)
    #     seen_letters[right_letter] = right_window_edge + 1
    # return answer