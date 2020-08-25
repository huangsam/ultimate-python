def main():
    # This is a list of strings where
    # "a" is a string at index 0 and
    # "e" is a string at index 4
    letters = ["a", "b", "c", "d", "e"]
    print("Letters", letters)

    for letter in letters:
        # Each of the strings is one character
        assert len(letter) == 1

        # Each of the strings is a letter
        assert letter.isalpha()

    # You can get a subset of letters with the range selector
    assert letters[1:] == ["b", "c", "d", "e"]
    assert letters[:-1] == ["a", "b", "c", "d"]
    assert letters[1:-2] == ["b", "c"]
    assert letters[::2] == ["a", "c", "e"]
    assert letters[::-1] == ["e", "d", "c", "b", "a"]

    # This is a list of integers where
    # 1 is an integer at index 0
    # 5 is an integer at index 4
    numbers = [1, 2, 3, 4, 5]
    print("Numbers", numbers)

    # Print letters and numbers side-by-side using the `zip` function. Notice
    # that we pair the letter at index 0 with the number at index 0, and
    # do the same for the remaining indices
    for letter, number in zip(letters, numbers):
        print("Letter and number", letter, number)

    # The for loop worked because the lengths of both lists are equal
    assert len(letters) == len(numbers)

    # To see the indices and values of a list at the same time, you can use
    # `enumerate` to transform the list of values into an iterator of
    # index-number pairs
    for index, number in enumerate(numbers):
        print(f"At numbers[{index}]", number)

    # Lists can be nested at arbitrary levels
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matrix of lists", matrix)

    # This matrix just so happens to be a square so the the length of each
    # row is the same as the number of rows in the matrix
    for row in matrix:
        assert len(matrix) == len(row)

    # Something to know about lists is that they are mutable
    mutable = []
    for _ in range(5):  # [0, 0, 0, 0, 0]
        mutable.append(0)
    mutable.pop()  # pop out the fifth zero
    mutable[0] = 100  # first item
    mutable[1] = 30  # second item
    mutable[-1] = 50  # last item
    mutable[-2] = 20  # second to last item
    print("Mutable list", mutable)


if __name__ == "__main__":
    main()
