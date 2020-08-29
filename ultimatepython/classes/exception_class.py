class CustomError(Exception):
    """Custom class of errors.

    This is a custom base exception for any issues that arise in this module.
    One of the reasons why developers design a class like this is for
    consumption by downstream services and command-line tools.

    If you are designing a standalone application with few downstream
    consumers, then it makes little sense to make a base class of exceptions.
    Try using the existing hierarchy of builtin exception classes, which are
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

    That being said, there's a point of diminishing returns when
    we design too many exceptions. It's better to design a few exceptions
    that most developers handle than design many exceptions that
    few developers handle.
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
    for dividend, divisor in [(1, 0), (-1, 1), (1, -1)]:
        try:
            divide_positive_numbers(dividend, divisor)
        except DivisionError as e:
            print(e)
    result = divide_positive_numbers(1, 1)
    print(f"Divide(1, 1) = {result}")


if __name__ == '__main__':
    main()
