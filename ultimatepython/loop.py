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
    # the loop
    i = 0
    while i < 5:
        print(f"While {i} < 5")
        i += 2

    # This is a while loop that is terminated with break
    # and its counter is multiplied in the loop, showing
    # that you can do anything to the counter
    i = 2
    while True:
        print(f"Do While {i} < 5")

        # Putting this code block after the print statement
        # makes the loop look like a do-while block in other
        # programming languages
        if i >= 5:
            print(f"Break out! {i} is no longer < 5")
            break

        i *= 2


if __name__ == "__main__":
    main()
