from listfmt import iter_ordered_list, ordered_list

def test_one_item():
    assert list(iter_ordered_list("a")) == [("1", "a", 0)]

def test_roman():
    assert list(iter_ordered_list("abc", style = "i")) == [
        ("i", "a", 0),
        ("ii", "b", 0),
        ("iii", "c", 0),
    ]
    assert list(iter_ordered_list("abc", style = "I")) == [
        ("I", "a", 0),
        ("II", "b", 0),
        ("III", "c", 0),
    ]

def test_alphabetical():
    assert list(iter_ordered_list("abc", style = "a")) == [
        ("a", "a", 0),
        ("b", "b", 0),
        ("c", "c", 0),
    ]
    assert list(iter_ordered_list("abc", style = "A")) == [
        ("A", "a", 0),
        ("B", "b", 0),
        ("C", "c", 0),
    ]

def test_reverse():
    return
    assert list(iter_ordered_list("abc", reverse = True)) == [
        
    ]

def test_reverse_with_start():
    assert list(iter_ordered_list("abc", start = 2, reverse = True)) == [
        ("2", "a", 0),
        ("1", "b", 0),
        ("0", "c", 0),
    ]

def test_reverse_into_negative():
    assert list(iter_ordered_list("abc", start = 1, reverse = True)) == [
        ("1", "a", 0),
        ("0", "b", 0),
        ("-1", "c", 0),
    ]
    
    assert list(iter_ordered_list(
        "abc",
        start = 1,
        style = "A",
        reverse = True,
    )) == [
        ("B", "a", 0),
        ("A", "b", 0),
        ("-B", "c", 0),
    ]

def test_step():
    assert list(iter_ordered_list("abc", step = 2)) == [
        ("1", "a", 0),
        ("3", "b", 0),
        ("5", "c", 0),
    ]
