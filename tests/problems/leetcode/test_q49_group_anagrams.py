from problems.leetcode.q49_group_anagrams import Solution


def test():
    sol = Solution()
    assert sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]
