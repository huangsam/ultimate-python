def main():
    x = 1
    x_add_two = x + 2

    # Test that the obvious is true
    if x_add_two == 3:
        print("math wins")  # ran

    # Test that a double-negative is true. This
    # could also be written as the following:
    # ... if x_add_two != 1
    if not x_add_two == 1:
        print("math wins here too")  # ran

    # There are else statements as well, which get run
    # if the initial condition fails
    if x_add_two == 1:
        print("math lost here...")  # skipped
    else:
        print("math wins otherwise")  # ran

    # ...or gets run after multiple conditions fail
    if x_add_two == 1:
        print("nope not this one...")  # skipped
    elif x_add_two == 2:
        print("nope not this one either...")  # skipped
    elif x_add_two < 3:
        print("nope not quite...")  # skipped
    else:
        print("math wins finally")  # ran


if __name__ == "__main__":
    main()
