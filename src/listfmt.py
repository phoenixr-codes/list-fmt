# TODO: add docs
# TODO: UnorderedListStyle necessary?
# TODO: add more tests

from __future__ import annotations

from collections.abc import Collection, Generator, Iterable
from enum import auto, IntEnum
from itertools import chain, repeat, zip_longest
import operator
from typing import Any, Literal, Optional, Union

import b26
import roman


class OrderedListStyle(IntEnum):
    NUMBER = auto()
    LOWERCASE_ASCII = auto()
    UPPERCASE_ASCII = auto()
    LOWERCASE_ROMAN = auto()
    UPPERCASE_ROMAN = auto()

    @classmethod
    def from_char(cls, char: str) -> OrderedListStyle:
        """
        Parameters
        ----------
        char
            * ``'A'`` returns UPPERCASE_ASCII,
            * ``'a'`` returns LOWERCASE_ASCII,
            * ``'I'`` returns UPPERCASE_ROMAN,
            * ``'i'`` returns LOWERCASE_ROMAN,
            * ``'1'`` returns NUMBER.
        """
        return {
            "a": cls.LOWERCASE_ASCII,
            "A": cls.UPPERCASE_ASCII,
            "i": cls.LOWERCASE_ROMAN,
            "I": cls.UPPERCASE_ROMAN,
            "1": cls.NUMBER,
        }[char]


class UnorderedListStyle(IntEnum):
    BULLET = auto()
    HYPHEN = auto()


def strjoin(string: str, items: Iterable[Any], /) -> str:
    """
    Shorthand for ``str.join(map(str, iterable))``.

    Parameters
    ----------
    string
        String that joins each item.

    items
        Items to join the string with.
    """
    return string.join(map(str, items))


def reprjoin(string: str, items: Iterable[Any], /) -> str:
    """
    Shorthand for ``str.join(map(repr, iterable))``.

    Parameters
    ----------
    string
        String that joins each item.

    items
        Items to join the string with.
    """
    return string.join(map(repr, items))


def join_with(
    items: Collection[str],
    /,
    join: str = ", ",
    *,
    join_first: Optional[str] = None,
    join_last: Optional[str] = None,
) -> str:
    """
    ``str.join`` but with more control.

    Parameters
    ----------
    items
        A sized iterable of strings.

    join
        String that is inserted between all
        elements in the list.

    join_first
        String that is inserted between the
        first and second element in the list.

    join_last
        String that is inserted beteeen the
        last its predecessor element in the
        list.

        This has precedence over ``join_first``
        if there are exactly two elements.
    """
    # this is like `str.join` but as a list
    parts = list(
        chain.from_iterable(
            zip_longest(
                items,
                repeat(join, max(0, len(items) - 1)),
            )
        )
    )
    while None in parts:
        parts.remove(None)

    # modify first and last sep
    if len(parts) >= 2:
        if join_first is not None:
            parts[1] = join_first
        if join_last is not None:
            parts[-2] = join_last

    return "".join(parts)


def iter_ordered_list(
    items: Collection[str],
    /,
    *,
    reverse: bool = False,
    step: int = 1,
    start: Optional[int] = None,
    style: Union[
        OrderedListStyle,
        Literal["a"],
        Literal["A"],
        Literal["i"],
        Literal["I"],
        Literal["1"],
    ] = OrderedListStyle.NUMBER,
    recursive: bool = False,
    _level: int = 0,
) -> Generator[tuple[str, str, int], None, None]:
    """
    Parameters
    ----------
    items
        A sized iterable of strings.

    reverse
        Starts counting from behind.

    step
        Amount of steps when increasing.

    start
        Integer indicating from where to start counting.
        Defaults to ``1``.

    style
        Either an item of :class:`OrderedListStyle` or
        ``'a'`` for lowercase letters,
        ``'A'`` for uppercase letters,
        ``'i'`` for lowercase roman numerals,
        ``'I'`` for uppercase roman numerals or
        ``'1'`` for integers.

    recursive
        Turns nested iterables into ordered lists too.

    Yields
    ------
    Each item as a tuple containing the prefix, the content and the level.
    """
    if reverse:
        incr = operator.sub
    else:
        incr = operator.add

    if isinstance(style, str):
        style = OrderedListStyle.from_char(style)

    level = _level

    if start is not None:
        i = start
    elif reverse:
        i = len(items)
    elif style in [OrderedListStyle.LOWERCASE_ASCII, OrderedListStyle.UPPERCASE_ASCII]:
        i = 0
    else:
        i = 1

    for item in items:
        if recursive and not isinstance(item, str):
            yield from iter_ordered_list(
                item,
                reverse=reverse,
                step=step,
                start=start,
                style=style,
                recursive=True,
                _level=level + 1,
            )
            continue

        if style == OrderedListStyle.NUMBER:
            prefix = str(abs(i))
        elif style == OrderedListStyle.LOWERCASE_ASCII:
            prefix = b26.encode(abs(i)).lower()
        elif style == OrderedListStyle.UPPERCASE_ASCII:
            prefix = b26.encode(abs(i)).upper()
        elif style == OrderedListStyle.LOWERCASE_ROMAN:
            prefix = roman.toRoman(abs(i)).lower()
        elif style == OrderedListStyle.UPPERCASE_ROMAN:
            prefix = roman.toRoman(abs(i)).upper()

        if i < 0:
            prefix = "-" + prefix

        yield (prefix, item, level)
        i = incr(i, step)


def ordered_list(
    *args: Any,
    join: str = ". ",
    **kwargs: Any,
) -> str:
    """
    Parameters
    ----------
    items
        A sized iterable of strings.

    join
        String that joins between the prefix
        and the item.

    reverse
        Starts counting from behind.

    step
        Amount of steps when increasing.

    start
        Integer indicating from where to start counting.
        Defaults to ``1``.

    style
        Either an item of :class:`OrderedListStyle` or
        ``'a'`` for lowercase letters,
        ``'A'`` for uppercase letters,
        ``'i'`` for lowercase roman numerals,
        ``'I'`` for uppercase roman numerals or
        ``'1'`` for integers.

    recursive
        Turns nested iterables into ordered lists too.

    """
    return "\n".join(join.join(x[:2]) for x in iter_ordered_list(*args, **kwargs))


def iter_unordered_list(
    items: Iterable[str],
    /,
    *,
    style: str = "*",
    recursive: bool = False,
    _level: int = 0,
) -> Generator[tuple[str, str, int], None, None]:
    """
    Parameters
    ----------
    items
        A sized iterable of strings.

    style
        A character to prefix the list items with.

    recursive
        Turns nested iterables into unordered lists too.

    Yields
    ------
    Each item as a tuple containing the prefix, the content and the level.
    """
    level = _level
    for item in items:
        if recursive and not isinstance(item, str):
            yield from iter_unordered_list(
                item,
                style=style,
                recursive=True,
                _level=level + 1,
            )
            continue

        yield (style, item, level)


def unordered_list(
    *args: Any,
    join: str = " ",
    indent: int = 2,
    **kwargs: Any,
) -> str:
    """
    Parameters
    ----------
    items
        A sized iterable of strings.

    join
        String that joins between the prefix
        and the item.

    style
        A character to prefix the list items with.

    recursive
        Turns nested iterables into unordered lists too.
    """
    return "\n".join(
        f"{' ' * indent * level}{prefix}{join}{item}"
        for prefix, item, level in iter_unordered_list(*args, **kwargs)
    )
