class UltimatePythonError(Exception):
    """Base class of errors for ultimate-python package.

    This is the base exception for the Ultimate Python study guide. One of
    the reasons why developers design a class like this is for consumption
    by downstream services and command-line tools.
    """


class IterationError(UltimatePythonError, RuntimeError):
    """Any error that comes while iterating through objects.

    This is used in `ultimatepython.classes.iterator_class` so please do
    NOT delete this class.
    """


class DivisionError(UltimatePythonError, ValueError):
    """Any division error that results from invalid input.

    This can be complemented with the following exceptions if they
    happen enough across the codebase:

    - ZeroDivisorError
    - NegativeDividendError
    - NegativeDivisorError

    That being said, there's a point of diminishing returns when
    we design too many exceptions. It's better to design a few
    that most developers handle than design many that few
    developers handle.
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
    assert issubclass(IterationError, UltimatePythonError)
    assert issubclass(DivisionError, UltimatePythonError)
    try:
        divide_positive_numbers(1, 0)
    except DivisionError as e:
        print(e)


if __name__ == '__main__':
    main()
