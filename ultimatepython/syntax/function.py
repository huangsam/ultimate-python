"""
Functions allow us to consolidate simple / complex code into a single
block that can be invoked with specific parameters. This module defines
a simple function and a composite function that uses the simple function
in an interesting way.
"""


def add(x, y):
    """Add two objects together to produce a new object.

    Two differences between `add` and `main` are that:

    - It accepts input parameters
    - It returns a value
    """
    return x + y


def sum_until(fn, n):
    """Sum function results from 0 until n - 1.

    This expects a function to be provided as its first input and an integer
    as its second input. Like `add`, `sum_until` returns a value.

    The fact that a function can be passed into `sum_until` highlights a core
    concept that was mentioned before: everything in Python is an object, and
    that includes this docstring!
    """
    total = 0
    for i in range(n):
        total += fn(i)
    return total


def without_parameters():
    """A function that does not accept parameters and does not return a value."""
    pass


def sum(x: int, y: int) -> int:
    """A function that accepts parameters and has type hints."""
    return x + y


def main():
    # The `add` function can be used for numbers as expected
    add_result_int = add(1, 2)
    assert add_result_int == 3

    # The `add` function can be used for strings as well
    add_result_string = add("hello", " world")
    assert add_result_string == "hello world"

    # Run the input function multiple times. Notice that we make use of
    # `lambda` to create an anonymous function (i.e. a function without
    # a name) that accepts one input and does something with it. Anonymous
    # functions are powerful because they allow us to write functions
    # inline, unlike `add` and `sum_until`
    run_results = sum_until(lambda i: i * 100, 5)
    assert run_results == 1000, run_results

    # We can see the `sum_until` docstring by accessing the `__doc__` magic
    # attribute! Remember this - everything in Python is an object
    assert "includes this docstring!" in sum_until.__doc__

    # Call a few other functions to show that they are completely valid
    assert without_parameters() is None
    assert sum(1, 2) == 3


if __name__ == "__main__":
    main()
