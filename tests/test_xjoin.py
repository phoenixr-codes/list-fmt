from listfmt import strjoin, reprjoin

def test_strjoin():
    assert strjoin("+", [1, 2, 3]) == "1+2+3"

def test_reprjoin():
    assert reprjoin("+", ["1", "2", "3"]) == "'1'+'2'+'3'"

