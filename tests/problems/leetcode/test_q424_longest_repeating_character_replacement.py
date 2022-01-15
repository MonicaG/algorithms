from problems.leetcode.q424_longest_repeating_character_replacement import Solution


def test_q424():
    sol = Solution()
    assert sol.characterReplacement("ABCA", 2) == 4
    assert sol.characterReplacement("ABCA", 1) == 2
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    assert sol.characterReplacement("ABACDEFAB", 3) == 5
    assert sol.characterReplacement("AABAB", 0) == 2
    assert sol.characterReplacement("A", 1) == 1
    assert sol.characterReplacement("AAAAA", 2) == 5
    assert sol.characterReplacement("ABCDEFG", 1) == 2
    assert sol.characterReplacement("ABCDEFG", 2) == 3
