def main():
    # One interesting fact about data structures is that you can build
    # them with comprehensions. Let's explain how the first one works:
    # we just want to create zeros so our expression is set to `0`
    # since no computing is required; because `0` is a constant value,
    # we can set the item that we compute with to `_`; and we want to
    # create five zeros so we set the iterator as `range(5)`
    list_comp = [0 for _ in range(5)]
    print("List of zeros", list_comp)

    words = ["cat", "mice", "horse", "bat"]

    # Tuple comprehension can find the length for each word
    tuple_comp = tuple(len(word) for word in words)
    assert len(tuple_comp) == len(words)
    print("Tuple of word lengths", tuple_comp)

    # Set comprehension can find the unique word lengths
    set_comp = {len(word) for word in words}
    assert len(set_comp) < len(words)
    print("Set of word lengths", set_comp)

    # Dictionary comprehension can map each word to its length
    dict_comp = {word: len(word) for word in words}
    assert len(dict_comp) == len(words)
    print("Mapping of word to length", dict_comp)


if __name__ == "__main__":
    main()
