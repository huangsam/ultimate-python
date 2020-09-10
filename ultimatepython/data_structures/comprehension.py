def main():
    # One interesting fact about data structures is that we can build
    # them with comprehensions. Let's explain how the first one works:
    # we just want to create zeros so our expression is set to `0`
    # since no computing is required; because `0` is a constant value,
    # we can set the item that we compute with to `_`; and we want to
    # create five zeros so we set the iterator as `range(5)`
    assert [0 for _ in range(5)] == [0] * 5 == [0, 0, 0, 0, 0]

    # For the next comprehension operations, let's see what we can do
    # with a list of 3-5 letter words
    words = ["cat", "mice", "horse", "bat"]

    # Tuple comprehension can find the length for each word
    tuple_comp = tuple(len(word) for word in words)
    assert tuple_comp == (3, 4, 5, 3)

    # Set comprehension can find the unique word lengths
    set_comp = {len(word) for word in words}
    assert len(set_comp) < len(words)
    assert set_comp == {3, 4, 5}

    # Dictionary comprehension can map each word to its length
    dict_comp = {word: len(word) for word in words}
    assert len(dict_comp) == len(words)
    assert dict_comp == {"cat": 3,
                         "mice": 4,
                         "horse": 5,
                         "bat": 3}


if __name__ == "__main__":
    main()
