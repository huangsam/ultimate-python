def add(x, y):
    """Add two objects together to produce a new object.

    This add function is a function, just like main is. Two
    differences between add and main are that:

    A) It accepts input parameters
    B) It returns a value
    """
    return x + y


def run_until(fn, n):
    """Run a function from 0 until n - 1.

    A function is provided as its first input and an integer
    as its second input. This demonstrates that anything can
    be passed into the function parameters.

    This leads to an important point that was brought up in
    the variable lesson: everything in Python is an object,
    and that includes this docstring from run_until.
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

    # Run the input function twice. Notice that we make
    # use of lambda to create an anonymous function (i.e.
    # a function without a name) that accepts one input
    # and does something with it. Anonymous functions
    # are powerful because they allow one to write
    # functions inline and not have to declare
    # them explicitly, unlike add and run_until
    run_until(lambda i: print(f"hello at {i}"), 2)


if __name__ == '__main__':
    main()
