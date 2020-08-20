def main():
    # This is a tuple of integers
    immutable = (1, 2, 3, 4)
    print(immutable)

    # It can be indexed like a list
    assert immutable[0] == 1

    # It can be iterated over like a list
    for number in immutable:
        print("immutable", number)

    # But its contents cannot be changed. As an alternative, you can
    # create new tuples from existing tuples
    bigger_immutable = immutable + (5, 6)
    print(bigger_immutable)
    smaller_immutable = immutable[0:2]
    print(smaller_immutable)


if __name__ == '__main__':
    main()
