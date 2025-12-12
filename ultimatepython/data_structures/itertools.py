"""
Itertools provides a collection of tools for handling iterators. This
module demonstrates how to use itertools functions to efficiently work
with sequences, combine iterables, and create infinite iterators.
"""

import itertools


def main() -> None:
    # chain() combines multiple iterables into a single iterator
    letters = ["a", "b", "c"]
    numbers = [1, 2, 3]
    combined = list(itertools.chain(letters, numbers))
    assert combined == ["a", "b", "c", 1, 2, 3]

    # cycle() creates an infinite iterator that cycles through the elements
    # We'll use islice to take only the first few elements
    cycled = list(itertools.islice(itertools.cycle(["A", "B"]), 6))
    assert cycled == ["A", "B", "A", "B", "A", "B"]

    # repeat() creates an iterator that repeats a value infinitely
    repeated = list(itertools.islice(itertools.repeat("hello"), 4))
    assert repeated == ["hello", "hello", "hello", "hello"]

    # count() creates an infinite iterator that counts up from a start value
    counted = list(itertools.islice(itertools.count(10), 5))
    assert counted == [10, 11, 12, 13, 14]

    # islice() allows slicing of iterators (similar to list slicing)
    data = itertools.count()  # infinite count from 0
    sliced = list(itertools.islice(data, 2, 8, 2))  # start=2, stop=8, step=2
    assert sliced == [2, 4, 6]

    # tee() creates multiple independent iterators from one
    original = iter([1, 2, 3, 4, 5])
    iter1, iter2 = itertools.tee(original, 2)
    list1 = list(iter1)
    list2 = list(iter2)
    assert list1 == [1, 2, 3, 4, 5]
    assert list2 == [1, 2, 3, 4, 5]

    # groupby() groups consecutive equal elements
    group_data = [1, 1, 2, 2, 2, 3, 1, 1]
    groups = [(key, list(group)) for key, group in itertools.groupby(group_data)]
    assert groups == [(1, [1, 1]), (2, [2, 2, 2]), (3, [3]), (1, [1, 1])]

    # product() creates cartesian product of input iterables
    colors = ["red", "blue"]
    sizes = ["S", "M"]
    combinations = list(itertools.product(colors, sizes))
    assert combinations == [("red", "S"), ("red", "M"), ("blue", "S"), ("blue", "M")]

    # permutations() generates all possible orderings
    perms = list(itertools.permutations([1, 2, 3], 2))  # length 2 permutations
    assert len(perms) == 6  # 3! / (3-2)! = 6
    assert (1, 2) in perms
    assert (2, 1) in perms

    # combinations() generates combinations (order doesn't matter)
    combos = list(itertools.combinations([1, 2, 3, 4], 2))
    assert len(combos) == 6  # C(4,2) = 6
    assert (1, 2) in combos
    assert (2, 1) not in combos  # order doesn't matter


if __name__ == "__main__":
    main()
