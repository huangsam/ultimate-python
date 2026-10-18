"""
The walrus operator, also known as the assignment expression operator,
allows you to assign values to variables as part of an expression. This
feature was introduced in Python 3.8 through PEP 572.

The walrus operator uses the := syntax and is particularly useful in
reducing redundancy when you need to compute a value and then use it
in a condition or comprehension.
"""


class InputBuffer:
    """Simulate an interactive input buffer for while-loop demonstrations."""

    def __init__(self, inputs: list[str]) -> None:
        self._inputs = inputs
        self._index = 0

    def read_next(self) -> int:
        """Return next integer from inputs or 0 when exhausted."""
        if self._index < len(self._inputs):
            result = int(self._inputs[self._index])
            self._index += 1
            return result
        return 0


def collect_until_zero(buffer: InputBuffer) -> list[int]:
    """Collect non-zero integers using walrus assignment in a while condition."""
    numbers = []
    while (num := buffer.read_next()) != 0:
        numbers.append(num)
    return numbers


def filter_by_length_range(words: list[str], min_len: int, max_len: int) -> list[str]:
    """Filter words with length strictly between min_len and max_len using walrus operator.

    Assigning (word_len := len(word)) calculates length once and reuses it in
    the second comparison, avoiding redundant len() calls per element.
    """
    return [word for word in words if min_len < (word_len := len(word)) and word_len < max_len]


def filter_squares_below(numbers: list[int], limit: int) -> list[int]:
    """Filter squared numbers strictly below limit without redundant calculations.

    Assigning (square := n * n) in the filter condition allows reusing the
    result directly in the comprehension output expression.
    """
    return [square for n in numbers if (square := n * n) < limit]


def map_long_word_lengths(words: list[str], min_len: int) -> dict[str, int]:
    """Build a mapping of words to lengths exceeding min_len using walrus.

    Assigning (word_len := len(word)) in the filter allows using the calculated
    length directly as the dictionary value.
    """
    return {word: word_len for word in words if (word_len := len(word)) > min_len}


def main() -> None:
    # 1. Condition expressions: traditional vs walrus operator
    text = "Hello, Python!"
    length = len(text)
    if length > 5:
        assert length == 14

    # With the walrus operator, assign and check in one expression
    text2 = "Ultimate"
    if (length2 := len(text2)) > 5:
        assert length2 == 8

    # 2. While loop: traditional approach requires duplicating input reading logic
    # Simulating a user providing 5 then 0
    numbers_old = []
    n = int("5")
    while n != 0:
        numbers_old.append(n)
        n = int("0")
    assert numbers_old == [5]

    # With the walrus operator in while condition via InputBuffer
    buffer = InputBuffer(["3", "7", "0"])
    assert collect_until_zero(buffer) == [3, 7]
    assert buffer.read_next() == 0

    # 3. List comprehension: avoid computing len() twice per item
    data = ["apple", "banana", "cherry", "date"]
    long_words_old = [word for word in data if len(word) > 5 and len(word) < 7]
    assert long_words_old == ["banana", "cherry"]
    assert filter_by_length_range(data, 5, 7) == ["banana", "cherry"]

    # Filtering and transforming simultaneously without recomputing squares
    numbers = [3, 5, 7, 9, 11]
    squares_old = [n * n for n in numbers if n * n < 50]
    assert squares_old == [9, 25, 49]
    assert filter_squares_below(numbers, 50) == [9, 25, 49]

    # 4. Set comprehension with walrus operator
    words = ["hi", "hello", "world", "python", "code"]
    long_lengths = {word_len for word in words if (word_len := len(word)) > 4}
    assert long_lengths == {5, 6}

    # 5. Dictionary comprehension with walrus operator
    assert map_long_word_lengths(words, 4) == {"hello": 5, "world": 5, "python": 6}

    # 6. Enclosing scope: variables assigned with := in comprehensions leak to enclosing scope
    [result for x in [1, 2, 3] if (result := x * 2) > 2]
    assert result == 6

    # 7. Nested walrus expressions
    values = [1, 2, 3, 4, 5]
    if (total := sum(doubled := [x * 2 for x in values])) > 15:
        assert doubled == [2, 4, 6, 8, 10]
        assert total == 30


if __name__ == "__main__":
    main()
