from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = "".join(sorted(list(word)))
            anagrams[key].append(word)

        return list(anagrams.values())
