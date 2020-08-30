def main():
    x = 1
    x_add_two = x + 2

    # This condition is obviously true
    if x_add_two == 3:  # skip: else
        print("Math wins")  # run

    # A negated condition can also be true
    if not x_add_two == 1:  # skip: else
        print("Math wins here too")  # run

    # There are `else` statements as well, which run if the initial condition
    # fails. Notice that one line gets skipped, and that this conditional
    # does not help one make a conclusion on the variable's true value
    if x_add_two == 1:
        print("Math lost here...")  # skip: if
    else:
        print("Math wins otherwise")  # run

    # The `else` statement also run once all other `if` and `elif` conditions
    # fail. Notice that multiple lines get skipped, and that all of the
    # conditions could have been compressed to `x_add_two != 3` for
    # simplicity. In this case, less logic results in more clarity
    if x_add_two == 1:
        print("Nope not this one...")  # skip: if
    elif x_add_two == 2:
        print("Nope not this one either...")  # skip: if
    elif x_add_two < 3 or x_add_two > 3:
        print("Nope not quite...")  # skip: if
    else:
        print("Math wins finally")  # run


if __name__ == "__main__":
    main()
