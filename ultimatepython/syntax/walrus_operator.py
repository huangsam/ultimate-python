"""
The walrus operator, also known as the assignment expression operator,
allows you to assign values to variables as part of an expression. This
feature was introduced in Python 3.8 through PEP 572.

The walrus operator uses the := syntax and is particularly useful in
reducing redundancy when you need to compute a value and then use it
in a condition or comprehension.
"""


def main() -> None:
    # Traditional approach: compute a value and check it separately
    # Let's say we want to check if a string has more than 5 characters
    text = "Hello, Python!"
    length = len(text)
    if length > 5:
        assert length == 14

    # With the walrus operator, we can assign and check in one expression.
    # This is cleaner and avoids repeating the computation or storing
    # intermediate variables unnecessarily
    text2 = "Ultimate"
    if (length2 := len(text2)) > 5:
        # The walrus operator assigned len(text2) to length2 AND returned it
        # for the comparison, all in the same line
        assert length2 == 8

    # The walrus operator is especially powerful in while loops. Here's a
    # traditional approach that requires reading input twice
    numbers_old = []
    n = int("5")  # Simulating user input
    while n != 0:
        numbers_old.append(n)
        n = int("0")  # Simulating next input
    assert numbers_old == [5]

    # With the walrus operator, we can assign and check in the loop condition.
    # This is more concise and avoids the duplication of the input reading logic
    numbers_new = []
    inputs = ["3", "7", "0"]  # Simulating a sequence of inputs
    index = 0

    # Note: In a real scenario, you'd read from input() instead of a list
    def get_next_input():
        nonlocal index
        if index < len(inputs):
            result = int(inputs[index])
            index += 1
            return result
        return 0

    while (num := get_next_input()) != 0:
        # The walrus operator assigns get_next_input() to num and checks if it's not 0
        numbers_new.append(num)
    assert numbers_new == [3, 7]

    # The walrus operator shines in list comprehensions when you need to
    # compute a value once and reuse it. Without walrus, you'd either:
    # 1. Compute the value multiple times (inefficient)
    # 2. Use a for loop instead of comprehension (less elegant)
    data = ["apple", "banana", "cherry", "date"]

    # Traditional approach: computing len() twice per item is wasteful
    long_words_old = [word for word in data if len(word) > 5 and len(word) < 7]
    assert long_words_old == ["banana", "cherry"]

    # With walrus operator: compute len() once and reuse the result
    # The walrus operator assigns len(word) to word_len, which we can
    # then use multiple times in the same comprehension
    long_words_new = [word for word in data if 5 < (word_len := len(word)) < 7]
    assert long_words_new == ["banana", "cherry"]

    # The walrus operator can be used in comprehensions to filter and transform
    # data simultaneously. Here we square numbers but only keep those where
    # the square is less than 50
    numbers = [3, 5, 7, 9, 11]

    # Without walrus: we'd need to compute the square twice or use a for loop
    squares_old = [n * n for n in numbers if n * n < 50]
    assert squares_old == [9, 25, 49]

    # With walrus: compute the square once, store it, and use it
    # This is both more efficient and clearer about the intent
    squares_new = [square for n in numbers if (square := n * n) < 50]
    assert squares_new == [9, 25, 49]

    # The walrus operator works in set comprehensions too
    # Let's find unique word lengths greater than 4
    words = ["hi", "hello", "world", "python", "code"]

    # With walrus operator in a set comprehension
    long_lengths = {word_len for word in words if (word_len := len(word)) > 4}
    assert long_lengths == {5, 6}

    # And in dictionary comprehensions as well
    # Create a dict of words to their lengths, but only for words > 4 chars
    word_length_map = {word: word_len for word in words if (word_len := len(word)) > 4}
    assert word_length_map == {"hello": 5, "world": 5, "python": 6}

    # Important note: The walrus operator creates variables in the enclosing scope.
    # This means variables assigned with := inside a comprehension are accessible
    # outside of it (unlike traditional loop variables in comprehensions)
    [result for x in [1, 2, 3] if (result := x * 2) > 2]
    # The variable 'result' is now accessible here, with its last assigned value
    assert result == 6

    # The walrus operator can be nested, though this can reduce readability
    # Use nesting sparingly and only when it genuinely improves the code
    values = [1, 2, 3, 4, 5]
    if (total := sum(doubled := [x * 2 for x in values])) > 15:
        # Here 'doubled' is assigned inside the expression for 'total'
        assert doubled == [2, 4, 6, 8, 10]
        assert total == 30


if __name__ == "__main__":
    main()
