from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # dict with the required letters and their counts
        t_counts = Counter(t)
        # empty dict that will hold the letters in the sliding window. Values default to zero
        window_counts = defaultdict(int)
        # the left pointer
        left = 0
        # The found variable will keep track of how many required letters we have found. When this number matches the
        # length of t_counts (number of keys) we have found a valid substring.
        found = 0
        # keep track of the minimum substring start and end index range. The start and end indexes will be used at the
        # end to create the substring to return. I'm doing this instead of keeping the actual substring, as I would need
        # to slice "s" each time I find a minimum. The slice operation is an O(K) (where k is the number of elements in
        # the slice). So, it's a bit faster to just store the start and end ranges and do the slice at the end. Infinity
        # is used because we want to find the min value. So, we need an initial value greater than any possible result
        # in order to get the min value.
        min_substring = (float("-inf"), float("inf"))
        for right, char in enumerate(s):
            # just add the char to the sliding window regardless of whether it is a required letter or not. I could
            # check if the letter is not in the t_counts dictionary, but that adds complexity. If this was a real world
            # problem and we found it was taking too much space then we could look at this optimization.
            window_counts[char] += 1
            # we found the number of instances needed for this character, so we can increment the found variable. Note
            # that any additional instances of the required letter do not affect our decision in the found criteria.
            if t_counts[char] == window_counts[char]:
                found += 1
            # We found all the required letters in their appropriate amounts, so we have a valid substring. Now,
            # increment the left pointer to see if we can remove any leading characters to make a smaller substring.
            while left <= right and found == len(t_counts):
                left_char = s[left]
                if right - left < min_substring[1] - min_substring[0]:
                    min_substring = (left, right)
                # remove the character as it will no longer be in the sliding window
                window_counts[left_char] -= 1
                # if the count for this letter falls below the required number, then we are no longer in a valid
                # substring scenario.
                if window_counts[left_char] < t_counts[left_char]:
                    found -= 1
                left += 1
        return "" if min_substring[0] == float("-INF") else s[min_substring[0]:min_substring[1]+ 1 ]

    def minWindow2(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # dict with the required letters and their counts
        t_counts = Counter(t)
        left = 0
        # The number of unique required letters. We are storing this value in this solution, as the t_counts cache will
        # grow as characters are added to it. A possible enhancement would be to NOT store the non-required letters.
        num_needed = len(t_counts)
        found = 0
        # The min_substring works the same as in the above solution
        min_substring = (float("-inf"), float("inf"))
        for right, char in enumerate(s):
            # Non-required letters will have a negative count, they will never be positive. That is good, because we do
            # not want them influencing the found variable.
            t_counts[char] -= 1
            # in this solution, having a count of 0 means we have found the required number of instances of the letter
            # in the sliding window. A negative number means we've found more than required. A positive number means we
            # need to find more instances of it.
            if t_counts[char] == 0:
                found += 1
            while num_needed == found and left <= right:
                left_char = s[left]
                if right - left < min_substring[1] - min_substring[0]:
                    min_substring = (left, right)
                t_counts[left_char] += 1
                # a positive number means we need to find more instances of the letter for the substring. We have an
                # invalid substring, so decrement found.
                if t_counts[left_char] > 0:
                    found -= 1
                left += 1
        return "" if min_substring[0] == float("-inf") else s[min_substring[0]:min_substring[1] + 1]
