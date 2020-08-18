def main():
    # This is a list of one-letter strings where
    # 'a' is a string at index 0 and
    # 'e' is a string at index 4
    letters = ["a", "b", "c", "d", "e"]

    # This is a list of integers where
    # 1 is an integer at index 0
    # 5 is an integer at index 4
    numbers = [1, 2, 3, 4, 5]

    # Print letters and numbers side-by-side. Notice
    # that we pair the letter at index 0 with the
    # number at index 0, and do the same for the rest
    # of the indices
    for letter, number in zip(letters, numbers):
        print(letter, number)


if __name__ == "__main__":
    main()
