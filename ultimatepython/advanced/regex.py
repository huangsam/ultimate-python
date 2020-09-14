import re

# Module-level constants
_TEXT_HELLO = "World Hello Hello"
_TEXT_NAMES = "John, Jane"
_TEXT_ABC123 = "abc123"
_TEXT_BYE = "Bye for now"


def main():
    # Running `search` with "Hello" returns a `Match` object for first Hello
    assert re.search(r"Hello", _TEXT_HELLO).start() == 6

    # Running `search` with "Hello$" returns a `Match` object for last Hello
    assert re.search(r"Hello$", _TEXT_HELLO).start() == 12

    # Running `findall` with "Hi \w+" returns a list of strings
    assert re.findall(r"\w+", _TEXT_NAMES) == ["John", "Jane"]

    # Running `match` with "[123]+" returns a `None`
    assert re.match(r"[123]+", _TEXT_ABC123) is None

    # Running `match` with "[abc]+" returns a `Match` object
    assert re.match(r"[abc]+", _TEXT_ABC123).group(0) == "abc"

    # Running `fullmatch` with "[\w]+" returns a `None`
    assert re.fullmatch(r"[\w]+", _TEXT_BYE) is None

    # Running `fullmatch` with "[\w ]+" returns a `Match` object
    assert re.fullmatch(r"[\w ]+", _TEXT_BYE).group(0) == _TEXT_BYE

    # There are many more ways to leverage regular expressions than what
    # is shown here. To learn more about this topic, please consult the
    # following resources:
    # https://en.wikipedia.org/wiki/Regular_expression
    # https://github.com/ziishaned/learn-regex
    # https://github.com/learnbyexample/py_regular_expressions


if __name__ == "__main__":
    main()
