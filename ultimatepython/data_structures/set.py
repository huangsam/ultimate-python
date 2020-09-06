def main():
    # Define two `set` collections
    multiples_two = set()
    multiples_four = set()

    # Fill sensible values into the set using `add`
    for i in range(10):
        multiples_two.add(i * 2)
        multiples_four.add(i * 4)

    print("Multiples of two", multiples_two)
    print("Multiples of three", multiples_four)

    # We cannot decide in which order the numbers come out - so let's
    # look for fundamental truths instead, such as divisibility against
    # 2 and 4. We do this by checking whether the modulus of 2 and 4
    # yields 0 (i.e. no remainder from performing a division)
    multiples_common = multiples_two.intersection(multiples_four)
    for number in multiples_common:
        assert number % 2 == 0 and number % 4 == 0

    print("Multiples in common", multiples_common)

    # We can compute exclusive multiples
    multiples_two_exclusive = multiples_two.difference(multiples_four)
    multiples_four_exclusive = multiples_four.difference(multiples_two)
    assert len(multiples_two_exclusive) > 0
    assert len(multiples_four_exclusive) > 0

    # Numbers in this bracket are greater than 2 * 9 and less than 4 * 10
    for number in multiples_four_exclusive:
        assert 18 < number < 40

    print("Exclusive multiples of two", multiples_two_exclusive)
    print("Exclusive multiples of four", multiples_four_exclusive)

    # By computing a set union against the two sets, we have all integers
    # in this program
    multiples_all = multiples_two.union(multiples_four)
    print("All multiples", multiples_all)

    # Check if set A is a subset of set B
    assert multiples_four_exclusive.issubset(multiples_four)
    assert multiples_four.issubset(multiples_all)

    # Check that set A is a subset and superset of itself
    assert multiples_all.issubset(multiples_all)
    assert multiples_all.issuperset(multiples_all)

    # Check if set A is a superset of set B
    assert multiples_all.issuperset(multiples_two)
    assert multiples_two.issuperset(multiples_two_exclusive)


if __name__ == "__main__":
    main()
