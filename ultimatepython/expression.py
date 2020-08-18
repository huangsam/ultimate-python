def main():
    # This is a simple integer
    x = 1

    # Its value can used as part of expressions
    print(x + 1)

    # An expression can be chained indefinitely. This concept
    # of chaining expressions is powerful because it allows
    # you to compose simple pieces of code into larger pieces
    # of code over time
    print(x * 2 * 2 * 2)

    # Division is a bit tricky in Python because it returns a result
    # of type 'float' by default
    print(x / 2)

    # If an integer division is desired, then an extra slash
    # must be added to the expression
    print(x // 2)

    # Powers of an integer can be leveraged too. If you want
    # more math functionality, then you may have to leverage
    # the builtin `math` library, a third-party library or
    # your own library
    print(x * 2 ** 3)


if __name__ == "__main__":
    main()
