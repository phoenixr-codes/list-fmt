from listfmt import iter_unordered_list, unordered_list

def test_single_item():
    assert list(iter_unordered_list("a", style = "-")) == [("-", "a", 0)]
    assert unordered_list("a", style = "-") == "- a"

def test_multiple_items():
    assert list(iter_unordered_list("abc", style = "-")) == [
        ("-", "a", 0),
        ("-", "b", 0),
        ("-", "c", 0),
    ]
    assert unordered_list("abc", style = "-") == "- a\n- b\n- c"

def test_nested():
    assert list(iter_unordered_list([
        "1",
        "2",
        [
            "A",
            "B",
            [
                "X",
                "Y",
                [[[]]]
            ]
        ],
        "3"
    ], recursive = True)) == [
        ("*", "1", 0),
        ("*", "2", 0),
        ("*", "A", 1),
        ("*", "B", 1),
        ("*", "X", 2),
        ("*", "Y", 2),
        ("*", "3", 0),
    ]

