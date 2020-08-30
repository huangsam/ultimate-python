def add(x, y):
    """Add two objects together to produce a new object.

    Two differences between `add` and `main` are that:

    A) It accepts input parameters
    B) It returns a value
    """
    return x + y


def run_until(fn, n):
    """Run a function from 0 until n - 1.

    This expects a function to be provided as its first input and an integer
    as its second input. Unlike `add`, `run_until` does NOT return a value.

    The fact that a function can be passed into `run_until` highlights a core
    concept that was mentioned before: everything in Python is an object, and
    that includes the docstring you are reading right now!
    """
    for i in range(n):
        fn(i)


def main():
    # The `add` function can be used for numbers as expected
    add_result_int = add(1, 2)
    print(f"Add(1, 2) = {add_result_int}")

    # The `add` function can be used for strings as well
    add_result_string = add("hello", " world")
    print(f"Add('hello', ' world') = '{add_result_string}'")

    # Run the input function twice. Notice that we make use of `lambda` to
    # create an anonymous function (i.e. a function without a name) that
    # accepts one input and does something with it. Anonymous functions
    # are powerful because they allow one to write functions inline, unlike
    # `add` and `run_until`
    run_until(lambda i: print(f"hello at {i}"), 2)

    # Did you want to see the `run_until` docstring? Well you can with the
    # `__doc__` magic attribute! Remember this one point - everything in
    # Python is an object
    print(run_until.__doc__)


if __name__ == "__main__":
    main()
