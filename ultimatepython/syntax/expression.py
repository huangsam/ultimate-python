def main():
    # This is a simple integer
    x = 1

    # Its value can be used as part of expressions
    assert x + 1 == 2

    # An expression can be chained indefinitely. This concept of chaining
    # expressions is powerful because it allows us to compose simple pieces
    # of code into larger pieces of code over time
    assert x * 2 * 2 * 2 == 8

    # Division is tricky because Python 3.x returns 0.5 of type `float`
    # whereas Python 2.x returns 0 of type `int`. If this line fails, it
    # is a sign that the wrong version of Python was used
    assert x / 2 == 0.5

    # If an integer division is desired, then an extra slash must be
    # added to the expression. In Python 2.x and Python 3.x, the behavior
    # is exactly the same
    assert x // 2 == 0

    # Powers of an integer can be leveraged too. If more features are
    # needed, then leverage the builtin `math` library or a third-party
    # library. Otherwise, we have to build our own math library
    assert x * 2 ** 3 == 8


if __name__ == "__main__":
    main()
