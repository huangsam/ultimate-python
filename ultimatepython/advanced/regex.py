import re

# Module-level constants
_TEXT_HELLO = "World Hello Hello"
_TEXT_NAMES = "John, Jane"
_TEXT_ABC123 = "abc123"
_TEXT_BYE = "Bye for now"


def main():
    # Running `search` with "Hello" has a match for first Hello
    assert re.search(r"Hello", _TEXT_HELLO).start() == 6

    # Running `search` with "Hello$" has a match for last Hello
    assert re.search(r"Hello$", _TEXT_HELLO).start() == 12

    # Running `search` with "(Hello) (Hello)" has matches for Hello
    assert re.search(r"(Hello) (Hello)", _TEXT_HELLO).groups() == ("Hello", "Hello")

    # Running `findall` with "Hi \w+" has a list of strings
    assert re.findall(r"\w+", _TEXT_NAMES) == ["John", "Jane"]

    # Running `match` with "[123]+" has nothing
    assert re.match(r"[123]+", _TEXT_ABC123) is None

    # Running `match` with "[abc]+" has a match for abc
    assert re.match(r"[abc]+", _TEXT_ABC123).group(0) == "abc"

    # Running `fullmatch` with "[\w]+" has nothing
    assert re.fullmatch(r"[\w]+", _TEXT_BYE) is None

    # Running `fullmatch` with "[\w ]+" has a full match
    assert re.fullmatch(r"[\w ]+", _TEXT_BYE).group(0) == _TEXT_BYE

    # To learn more about regular expressions:
    # https://en.wikipedia.org/wiki/Regular_expression
    # https://github.com/ziishaned/learn-regex

    # To play around with regular expressions in the browser:
    # https://regex101.com


if __name__ == "__main__":
    main()
