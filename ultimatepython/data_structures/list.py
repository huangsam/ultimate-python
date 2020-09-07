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

    # We can get a subset of letters with range slices
    assert letters[1:] == ["b", "c", "d", "e"]
    assert letters[:-1] == ["a", "b", "c", "d"]
    assert letters[1:-2] == ["b", "c"]
    assert letters[0:3:2] == ["a", "c"]
    assert letters[::2] == ["a", "c", "e"]
    assert letters[::-2] == ["e", "c", "a"]
    assert letters[::-1] == ["e", "d", "c", "b", "a"]

    # This is a list of integers where
    # 1 is an integer at index 0
    # 5 is an integer at index 4
    numbers = [1, 2, 3, 4, 5]
    print("Numbers", numbers)

    # Note that a list is ordered and mutable. If we want to reverse the order
    # of the `numbers` list, we can start at index 0 and end halfway. At each
    # cycle, we swap values in the front with values in the back
    for ix_front in range(len(numbers) // 2):
        ix_back = len(numbers) - ix_front - 1
        numbers[ix_front], numbers[ix_back] = numbers[ix_back], numbers[ix_front]

    # Suppose that we want to go back to the original order, we can use the
    # builtin `reverse` method in lists
    numbers.reverse()

    # Print letters and numbers side-by-side using the `zip` function. Notice
    # that we pair the letter at index 0 with the number at index 0, and
    # do the same for the remaining indices
    for letter, number in zip(letters, numbers):
        print("Letter and number", letter, number)

    # The `for` loop worked because the lengths of both lists are equal
    assert len(letters) == len(numbers)

    # To see the indices and values of a list at the same time, we can use
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

    # Notice that lists have variable length and can be modified to have
    # more elements. Lists can also be modified to have fewer elements
    lengthy = []
    for i in range(5):  # [0, 1, 2, 3, 4]
        lengthy.append(i)
    lengthy.pop()  # pop out the 4
    print("Lengthy list", lengthy)


if __name__ == "__main__":
    main()
