def add(x, y):
    """Add two objects together to produce a new object.

    Two differences between `add` and `main` are that:

    A) It accepts input parameters
    B) It returns a value
    """
    return x + y


def sum_until(fn, n):
    """Sum a function output from 0 until n - 1.

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
    # functions are powerful because they allow one to write functions
    # inline, unlike `add` and `sum_until`
    run_results = sum_until(lambda i: i * 100, 5)
    assert run_results == 1000, run_results

    # We can see the `sum_until` docstring by accessing the `__doc__` magic
    # attribute! Remember this - everything in Python is an object
    assert "includes this docstring!" in sum_until.__doc__


if __name__ == "__main__":
    main()
