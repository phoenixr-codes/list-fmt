from listfmt import join_with

def test_just_three():
    assert join_with("abc") == "a, b, c"
    assert join_with("abc", "+") == "a+b+c"

def test_with_first():
    assert join_with("abc", "+", join_first = "&") == "a&b+c"
    assert join_with("ab", "+", join_first = "&") == "a&b"

def test_with_last():
    assert join_with("abc", "+", join_last = "&") == "a+b&c"
    assert join_with("ab", "+", join_last = "&") == "a&b"

def test_alot():
    assert join_with("abcdefgh", "+") == "a+b+c+d+e+f+g+h"
    assert join_with("abcdefgh", "+", join_first = "&") == "a&b+c+d+e+f+g+h"
    assert join_with("abcdefgh", "+", join_last = "&") == "a+b+c+d+e+f+g&h"
    assert join_with("abcdefgh", "+", join_first = "&", join_last = "/") == "a&b+c+d+e+f+g/h"
