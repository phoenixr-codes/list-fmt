**********
Quickstart
**********

Installation
************

.. code-block:: bash
    
    pip install list-fmt

Basic Usage
***********

.. repl::
    from listfmt import join_with
    L = ["one", "two", "three"]
    join_with(L, join_last = " and ")

.. repl::
    from listfmt import strjoin
    strjoin(", ", [1, 2, 3])

.. repl::
    from listfmt import ordered_list
    print(ordered_list(["one", "two", "three"], style = "A"))

.. repl::
    from listfmt import unordered_list
    print(unordered_list(["one", "two", ["a", "b"], "three"], recursive = True))

