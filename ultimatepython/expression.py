def main():
    # This is a simple integer
    x = 1

    # Its value can used as part of expressions
    print(x + 1)

    # An expression can be chained indefinitely
    print(x * 2 * 2 * 2)

    # Division is a bit tricky in Python because it returns a result
    # of type 'float' by default
    print(x / 2)

    # If an integer division is desired, then an extra slash
    # must be added to the expression
    print(x // 2)


if __name__ == "__main__":
    main()
