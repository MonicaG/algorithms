from algorithms.strings.expand_around_the_center import is_string_a_palindrome


def test():
    assert is_string_a_palindrome("")
    assert is_string_a_palindrome("a")
    assert is_string_a_palindrome("aa")
    assert is_string_a_palindrome("ab") is False
    assert is_string_a_palindrome("aba")
    assert is_string_a_palindrome("abc") is False
    assert is_string_a_palindrome("abba")
    assert is_string_a_palindrome("abbc") is False
    assert is_string_a_palindrome("abca") is False
    assert is_string_a_palindrome("abbba")
    assert is_string_a_palindrome("abbbc") is False
    assert is_string_a_palindrome("abbbba")
    assert is_string_a_palindrome("abbbbc") is False
