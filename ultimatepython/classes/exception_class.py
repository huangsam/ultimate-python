class UltimatePythonError(Exception):
    """Base class of errors for ultimate-python package."""


class BadInputError(UltimatePythonError, ValueError):
    """Bad input provided by developer."""

    def __init__(self, bad_input, bad_reason):
        self.bad_input = bad_input
        self.bad_reason = bad_reason

    def __repr__(self):
        return f"<BadInputError {self.bad_input} ({type(self.bad_input)})>"

    def __str__(self):
        return f"Input {self.bad_input} is bad. {self.bad_reason}"


def divide(num_x, num_y):
    if num_y == 0:
        raise BadInputError(num_y, "Cannot have a zero for the divisor")
    return num_x // num_y


def main():
    try:
        divide(1, 0)
    except BadInputError as e:
        assert isinstance(e, UltimatePythonError)
        print(e)


if __name__ == '__main__':
    main()
