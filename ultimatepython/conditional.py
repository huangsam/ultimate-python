def main():
    x = 1
    x_add_two = x + 2

    # This condition is obviously true
    if x_add_two == 3:
        print("math wins")  # ran

    # A negated condition can also be true
    if not x_add_two == 1:
        print("math wins here too")  # ran

    # There are else statements as well, which get run
    # if the initial condition fails
    if x_add_two == 1:
        print("math lost here...")
    else:
        print("math wins otherwise")  # ran

    # ...or gets run after multiple conditions fail
    if x_add_two == 1:
        print("nope not this one...")
    elif x_add_two == 2:
        print("nope not this one either...")
    elif x_add_two < 3 or x_add_two > 3:
        print("nope not quite...")
    else:
        print("math wins finally")  # ran


if __name__ == "__main__":
    main()
