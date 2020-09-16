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

    # We use tuples when the number of items is consistent. An example
    # where this can help is a 2D game with X and Y coordinates. Using a
    # tuple with two numbers can ensure that the number of coordinates
    # doesn't change to one, three, four, etc.
    moved_count = 0
    pos_x, pos_y = (0, 0)
    for i in range(1, 5, 2):
        moved_count += 1
        pos_x, pos_y = (pos_x + 10 * i, pos_y + 15 * i)
    assert moved_count == 2
    assert pos_x == 40 and pos_y == 60


if __name__ == "__main__":
    main()
