def main():
    # This is a `for` loop that iterates on values 0..4 and adds each
    # value to `total`. It leverages the `range` iterator. Providing
    # a single integer implies that the start point is 0, the end point
    # is 5 and the increment step is 1 (going forward one step)
    total = 0
    for i in range(5):
        total += i

    # The answer is...10!
    assert total == 10

    # This is a `for` loop that iterates on values 5..1 and multiplies each
    # value to `fib`. The `range` iterator is used here more explicitly by
    # setting the start point at 5, the end point at 0 and the increment
    # step at -1 (going backward one step)
    fib = 1
    for i in range(5, 0, -1):
        fib *= i

    # The answer is...120!
    assert fib == 120

    # This is a simple `while` loop, similar to a `for` loop except that the
    # counter is declared outside of the loop and its state is explicitly
    # managed inside of the loop. The loop will continue until the counter
    # exceeds 8
    i = 0
    while i < 8:
        i += 2

    # The `while` loop terminated at this value
    assert i == 8

    # This is a `while` loop that is stopped with `break` and its counter is
    # multiplied in the loop, showing that we can do anything to the
    # counter. Like the previous `while` loop, this one continues until
    # the counter exceeds 8
    i = 1
    break_hit = False
    continue_hit = False
    other_hit = False
    while True:
        i *= 2

        if i >= 8:
            # The `break` statement stops the current `while` loop.
            # If this `while` loop was nested in another loop,
            # this statement would not stop the parent loop
            break_hit = True
            break

        if i == 2:
            # The `continue` statement returns to the start of the
            # current `while` loop
            continue_hit = True
            continue

        # This statement runs when the counter equals 4
        other_hit = True

    # The `while` loop terminated at this value
    assert i == 8

    # The `while` loop hit the `break` and `continue` blocks
    assert break_hit is True
    assert continue_hit is True
    assert other_hit is True


if __name__ == "__main__":
    main()
