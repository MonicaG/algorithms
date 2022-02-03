# See: https://monica-granbois.gitbook.io/cs-theory-and-problems/algorithms/sliding-window#expand-around-the-center
def is_string_a_palindrome(s: str) -> bool:
    mid = len(s) // 2
    right = mid
    if len(s) % 2 == 0:
        left = mid - 1
    else:
        left = mid
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            return False
        left -= 1
        right += 1
    return True
