class CustomError(Exception):
    """Custom class of errors.

    This is a custom exception for any issues that arise in this module.
    One of the reasons why developers design a class like this is for
    consumption by downstream services and command-line tools.

    If we designed a standalone application with no downstream consumers, then
    it makes little sense to define a custom hierarchy of exceptions. Instead,
    try using the existing hierarchy of builtin exception classes, which are
    listed in the Python docs:

    https://docs.python.org/3/library/exceptions.html
    """


class DivisionError(CustomError):
    """Any division error that results from invalid input.

    This exception can be subclassed with the following exceptions if they
    happen enough across the codebase:

    - ZeroDivisorError
    - NegativeDividendError
    - NegativeDivisorError

    That being said, there's a point of diminishing returns when we design
    too many exceptions. It is better to design few exceptions that many
    developers handle than design many exceptions that few developers handle.
    """


def divide_positive_numbers(dividend, divisor):
    """Divide a positive number by another positive number.

    Writing a program in this style is what is considered defensive
    programming. For more on this programming style, check out the
    Wikipedia link below:

    https://en.wikipedia.org/wiki/Defensive_programming
    """
    if divisor == 0:
        raise DivisionError("Cannot have a zero divisor")
    elif dividend <= 0:
        raise DivisionError("Cannot have a negative dividend")
    elif divisor < 0:
        raise DivisionError("Cannot have a negative divisor")
    return dividend // divisor


def main():
    # Exception classes are no different from concrete classes in that
    # they all have inheritance baked in
    assert issubclass(DivisionError, CustomError)

    # Try a couple of inputs that are known to throw an error based on
    # the exceptions thrown in `divide_positive_numbers`
    for dividend, divisor in [(1, 0), (-1, 1), (1, -1)]:
        try:
            divide_positive_numbers(dividend, divisor)
        except DivisionError as e:
            assert str(e).startswith("Cannot have a")

    # Now let's do it correctly to skip all the exceptions
    result = divide_positive_numbers(1, 1)
    assert result == 1


if __name__ == "__main__":
    main()
