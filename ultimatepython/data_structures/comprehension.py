def main():
    # One interesting fact about lists is that you can build them with
    # list comprehensions. Let's break this down in simple terms:
    # we just want to create zeros so our expression is set to `0`
    # since no computing is required; because `0` is a constant value,
    # we can set the item that we compute with to `_`; and we want to
    # create five zeros so we set the iterator as `range(5)`. This
    # looks like an embedded for-loop and you are right! So you can
    # build a list out of anything. You can imagine using this same
    # pattern to convert a collection of words into a list of word
    # lengths. You can also use it to convert a series of numbers into
    # a list of number strings
    print("List of zeros", [0 for _ in range(5)])


if __name__ == '__main__':
    main()
