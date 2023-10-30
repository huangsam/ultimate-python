"""
This module shows how to use if blocks, if-else blocks and if-elif-else
blocks to decide which lines of code to run (and skip).
"""


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
    # fails. Notice that one line gets skipped and this conditional does not
    # help us make a conclusion on the variable's true value
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

    # Conditionals can also be written in one line using `if` and `else`
    # with the following form: A if condition else B. This can be used
    # for assignments as shown below
    ran_5 = False
    ran_5 = True if x_add_two == 3 else False
    assert ran_5 is True

    # Python is one of the few programming languages that allows chained
    # comparisons. This is useful for checking if a variable is within
    # a range of values
    ran_6 = False
    if 2 < x_add_two < 4:  # run
        ran_6 = True
    assert ran_6 is True


if __name__ == "__main__":
    main()
