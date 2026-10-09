"""
An `OrderedDict` (`collections.OrderedDict`) remembers the order in which
entries were added, like a regular `dict`. Its distinguishing feature is that
it also provides methods for changing and removing entries by their position.

Regular dictionaries preserve insertion order starting with Python 3.7, but
they do not have `move_to_end()` or allow `popitem(last=False)` to remove the
first entry.
"""

from collections import OrderedDict


def main() -> None:
    # Both dict and OrderedDict preserve insertion order.
    regular: dict[str, int] = {"first": 1, "second": 2, "third": 3}
    ordered: OrderedDict[str, int] = OrderedDict(regular)
    assert list(regular) == ["first", "second", "third"]
    assert list(ordered) == ["first", "second", "third"]

    # Updating a value does not change the key's position in either mapping.
    regular["first"] = 10
    ordered["first"] = 10
    assert list(regular) == ["first", "second", "third"]
    assert list(ordered) == ["first", "second", "third"]

    # With dict, deleting and reinserting a key moves it to the end.
    del regular["first"]
    regular["first"] = 10
    assert list(regular) == ["second", "third", "first"]

    # OrderedDict can move an existing key directly to the end or beginning.
    ordered.move_to_end("first")
    assert list(ordered) == ["second", "third", "first"]
    ordered.move_to_end("first", last=False)
    assert list(ordered) == ["first", "second", "third"]

    # popitem() removes the newest entry by default; last=False removes the
    # oldest entry.
    assert ordered.popitem() == ("third", 3)
    assert ordered.popitem(last=False) == ("first", 10)
    assert list(ordered) == ["second"]


if __name__ == "__main__":
    main()
