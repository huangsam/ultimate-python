"""
Using regular expressions is a robust way to search for text. Implementing
them is difficult but Python provides a package for us to use them easily.
This module shows a few examples of how to use the `re` package to search
predefined text snippets stored in module-level constants.
"""

import re

# Module-level constants
_TEXT_HELLO = "World Hello Hello"
_TEXT_NAMES = "John, Jane"
_TEXT_ABC123 = "abc123"
_TEXT_BYE = "Bye for now"
_TEXT_EMAILS = "My work email is kayode@dodo.ng while nerdthejohn@yahoo.com is personal"


def main() -> None:
    # Running `search` with "Hello" has a match for first Hello
    match_first = re.search(r"Hello", _TEXT_HELLO)
    assert match_first is not None
    assert match_first.start() == 6

    # Running `search` with "Hello$" has a match for last Hello
    match_last = re.search(r"Hello$", _TEXT_HELLO)
    assert match_last is not None
    assert match_last.start() == 12

    # Running `search` with "(Hello) (Hello)" has matches for Hello
    match_groups = re.search(r"(Hello) (Hello)", _TEXT_HELLO)
    assert match_groups is not None
    assert match_groups.groups() == ("Hello", "Hello")

    # Running `findall` with "Hi \w+" has a list of strings
    assert re.findall(r"\w+", _TEXT_NAMES) == ["John", "Jane"]

    # Running `findall` with "[a-z]+@[a-z]+\.[a-z]+" has a list of email strings
    assert re.findall(r"[a-z]+@[a-z]+\.[a-z]+", _TEXT_EMAILS) == ["kayode@dodo.ng", "nerdthejohn@yahoo.com"]

    # Running `match` with "[123]+" has nothing
    assert re.match(r"[123]+", _TEXT_ABC123) is None

    # Running `match` with "[abc]+" has a match for abc
    match_abc = re.match(r"[abc]+", _TEXT_ABC123)
    assert match_abc is not None
    assert match_abc.group(0) == "abc"

    # Running `fullmatch` with "[\w]+" has nothing
    assert re.fullmatch(r"[\w]+", _TEXT_BYE) is None

    # Running `fullmatch` with "[\w ]+" has a full match
    match_bye = re.fullmatch(r"[\w ]+", _TEXT_BYE)
    assert match_bye is not None
    assert match_bye.group(0) == _TEXT_BYE

    # To learn more about regular expressions:
    # https://en.wikipedia.org/wiki/Regular_expression
    # https://github.com/ziishaned/learn-regex

    # To play around with regular expressions in the browser:
    # https://regex101.com


if __name__ == "__main__":
    main()
