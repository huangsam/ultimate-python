def main():
    # This is a tuple of integers
    immutable = (1, 2, 3, 4)

    # It can be indexed like a list
    assert immutable[0] == 1
    assert immutable[-1] == 4

    # It can be sliced like a list
    assert immutable[1:3] == (2, 3)
    assert immutable[3:4] == (4,)
    assert immutable[1::2] == (2, 4)
    assert immutable[::-1] == (4, 3, 2, 1)

    # It can be iterated over like a list
    for ix, number in enumerate(immutable):
        assert immutable[ix] == number

    # But its contents cannot be changed. As an alternative, we can
    # create new tuples from existing tuples
    bigger_immutable = immutable + (5, 6)
    assert bigger_immutable == (1, 2, 3, 4, 5, 6)
    smaller_immutable = immutable[0:2]
    assert smaller_immutable == (1, 2)


if __name__ == "__main__":
    main()
