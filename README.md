list-fmt
========

Format iterables into human readable text.


Installation
------------

```bash
pip install list-fmt
```

Basic Usage
-----------

```python
>>> from listfmt import join_with
>>> L = ["one", "two", "three"]
>>> join_with(L, join_last = " and ")
'one, two and three'
>>> 
>>> from listfmt import strjoin
>>> strjoin(", ", [1, 2, 3])
'1, 2, 3'
>>> 
>>> from list import ordered_list
>>> print(ordered_list(["one", "two", "three"], style = "A"))
A. one
B. two
C. three
>>> 
>>> from listfmt import unordered_list
>>> print(unordered_list(["one", "two", ["a", "b"], "three"], recursive = True))
* one
* two
  * a
  * b
* three
>>> 
```

Links
-----

* [Repository](https://github.com/phoenixr-codes/list-fmt/)
* [Documentation](https://phoenixr-codes.github.io/list-fmt/)
* [PyPI](https://pypi.org/project/list-fmt)
