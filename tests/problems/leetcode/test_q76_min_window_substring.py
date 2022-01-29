from problems.leetcode.q76_min_window_substring import Solution


def test():
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    assert sol.minWindow("abcdef", "bd") == "bcd"
    assert sol.minWindow("abccdefbxd", "bd") == "bxd"
    assert sol.minWindow("aaboced", "abc") == "aboc"
    assert sol.minWindow("bdab", "ab") == "ab"
    assert sol.minWindow("cabwefgewcwaefgcf", "cae") == "cwae"
    assert sol.minWindow("fadbgcabeafcz", "baac") == "cabea"
    assert sol.minWindow("abcdefg", "z") == ""
    assert sol.minWindow("acbbaca", "aba") == "baca"
    assert sol.minWindow("acbbac", "aba") == "acbba"
    assert sol.minWindow("bbbbbbbaac", "aba") == "baa"
    assert sol.minWindow("aab", "ab") == "ab"


def test2():
    sol = Solution()
    assert sol.minWindow2("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow2("a", "a") == "a"
    assert sol.minWindow2("a", "aa") == ""
    assert sol.minWindow2("abcdef", "bd") == "bcd"
    assert sol.minWindow2("abccdefbxd", "bd") == "bxd"
    assert sol.minWindow2("aaboced", "abc") == "aboc"
    assert sol.minWindow2("bdab", "ab") == "ab"
    assert sol.minWindow2("cabwefgewcwaefgcf", "cae") == "cwae"
    assert sol.minWindow2("fadbgcabeafcz", "baac") == "cabea"
    assert sol.minWindow2("abcdefg", "z") == ""
    assert sol.minWindow2("acbbaca", "aba") == "baca"
    assert sol.minWindow2("acbbac", "aba") == "acbba"
    assert sol.minWindow2("bbbbbbbaac", "aba") == "baa"
    assert sol.minWindow2("aab", "ab") == "ab"
