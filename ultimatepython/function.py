def add(x, y):
    """Add two objects together to produce a new object.

    This add function is a function, just like main is. Two
    differences between add and main are that:

    A) It accepts input parameters
    B) It returns a value
    """
    return x + y


def do_until(fn, n):
    """Run a function for n times in a row.

    A function is provided as input. This shows how it is
    a plain old Python object, just like any other thing
    is an object. In fact, everything is an object in
    Python.

    We treat the passed-in function like a
    piece of data that can be called with an integer.
    Therefore, the input function must accept one number
    as its argument.
    """
    for i in range(n):
        fn(i)


def main():
    # The add function can be used for numbers as expected
    add_result_int = add(1, 2)
    print(f"Add(1, 2) = {add_result_int}")

    # The add function can be used for strings as well
    add_result_string = add("hello", " world")
    print(f"Add('hello', ' world') = '{add_result_string}'")

    # Run the same function twice in a row. Notice that
    # we make use of lambda definitions to create a
    # function that accepts one input and prints
    # something to the screen
    do_until(lambda n: print(f"hello at {n}"), 2)


if __name__ == '__main__':
    main()
