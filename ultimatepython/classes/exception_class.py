class UltimatePythonError(Exception):
    """Base class of errors for ultimate-python package.

    This is the base exception for the Ultimate Python study guide. One of
    the reasons why developers design a class like this is for consumption
    by downstream services and command-line tools.
    """


class IterationError(UltimatePythonError, RuntimeError):
    """Any error that comes while iterating through objects."""


class DivisionError(UltimatePythonError, ValueError):
    """Any division error that results from invalid input."""


def divide_positive_numbers(dividend, divisor):
    """Divide a positive number by another positive number"""
    if divisor == 0:
        raise DivisionError("Cannot have a zero divisor")
    elif dividend < 0:
        raise DivisionError("Cannot have a negative dividend")
    elif divisor < 0:
        raise DivisionError("Cannot have a negative divisor")
    return dividend // divisor


def main():
    # Exception classes are no different from concrete classes in that
    # they all have inheritance baked in
    assert issubclass(IterationError, UltimatePythonError)
    assert issubclass(DivisionError, UltimatePythonError)
    try:
        divide_positive_numbers(1, 0)
    except DivisionError as e:
        print(e)


if __name__ == '__main__':
    main()
