def main():
    # This is a for loop that iterates on values 0..4
    # and adds each value to total
    total = 0
    for i in range(5):
        total += i

    # The answer is...10!
    print(f"Sum(0..4) = {total}")

    # This is a for loop that iterates on values 5..1
    # and multiplies each value to fib
    fib = 1
    for i in range(5, 0, -1):
        fib *= i

    # The answer is...120!
    print(f"Fibonacci(5..1) = {fib}")

    # This is a simple while loop, similar to a for loop
    # except that the counter is declared outside of the
    # loop and its state is explicitly managed inside of
    # the loop. The loop will continue until the counter
    # exceeds 5
    i = 0
    while i < 5:
        print(f"While {i} < 5")
        i += 2

    # This is a while loop that is terminated with break
    # and its counter is multiplied in the loop, showing
    # that you can do anything to the counter. Like the
    # previous while loop, this one also terminates when
    # the counter exceeds 5
    i = 1
    while True:
        print(f"Do While {i} < 5")
        i *= 2

        # Putting this conditional after the print statement
        # makes the loop look like the do-while loop from other
        # programming languages
        if i >= 5:
            print(f"Break out! {i} is no longer < 5")
            break


if __name__ == "__main__":
    main()
