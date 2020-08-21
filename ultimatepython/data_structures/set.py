def main():
    # Define two `set` collections
    multiples_two = set()
    multiples_three = set()

    # Fill sensible values into the set using `add`
    for i in range(10):
        multiples_two.add(i * 2)
        multiples_three.add(i * 3)

    print("twos", multiples_two)
    print("threes", multiples_three)

    # Numbers in common are multiples of 6
    multiples_common = multiples_two.intersection(multiples_three)
    for number in multiples_common:
        assert number % 6 == 0

    print("common", multiples_common)

    # You can compute exclusive multiples
    multiples_two_exclusive = multiples_two.difference(multiples_three)
    multiples_three_exclusive = multiples_three.difference(multiples_two)
    assert len(multiples_two_exclusive) and len(multiples_three_exclusive)

    print("twos_exclusive", multiples_two_exclusive)
    print("threes_exclusive", multiples_three_exclusive)


if __name__ == "__main__":
    main()
