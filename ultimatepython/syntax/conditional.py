def main():
    x = 1
    x_add_two = x + 2

    # This condition is obviously true
    ran_1 = False
    if x_add_two == 3:  # skip: else
        ran_1 = True  # run
    assert ran_1 is True

    # A negated condition can also be true
    ran_2 = False
    if not x_add_two == 1:  # skip: else
        ran_2 = True  # run
    assert ran_2 is True

    # There are `else` statements as well, which run if the initial condition
    # fails. Notice that one line gets skipped, and that this conditional
    # does not help one make a conclusion on the variable's true value
    if x_add_two == 1:
        ran_3 = False  # skip: if
    else:
        ran_3 = True  # run
    assert ran_3 is True

    # The `else` statement also runs once all other `if` and `elif` conditions
    # fail. Notice that multiple lines get skipped, and that all of the
    # conditions could have been compressed to `x_add_two != 3` for
    # simplicity. In this case, less logic results in more clarity
    if x_add_two == 1:
        ran_4 = False  # skip: if
    elif x_add_two == 2:
        ran_4 = False  # skip: if
    elif x_add_two < 3 or x_add_two > 3:
        ran_4 = False  # skip: if
    else:
        ran_4 = True  # run
    assert ran_4 is True


if __name__ == "__main__":
    main()
