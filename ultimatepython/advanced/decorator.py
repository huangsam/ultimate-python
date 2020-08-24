from contextlib import contextmanager
from functools import wraps

_HEADER = "---"


@contextmanager
def header_section():
    """Print header line first before running anything.

    Notice a context manager is used so that we enter a block where a header
    is printed out before proceeding with the function call at the point
    of yielding.

    Also notice that `header_section` is a generator that is wrapped by
    `contextmanager`. The `contextmanager` handles entering and exiting a section
    of code without defining a full-blown class to handle `__enter__` and
    `__exit__` use cases.

    There are many more use cases for context managers, like writing / reading
    data from a file. Another one is protecting database integrity while sending
    CREATE / UPDATE / DELETE statements over the network. For more on how context
    managers work, please consult the Python docs for more information.

    https://docs.python.org/3/library/contextlib.html
    """
    print(_HEADER)
    yield


def run_with_any(fn):
    """Run with a string or a collection with strings exclusively.

    We define a custom decorator that allows one to convert a function whose
    input is a single string into a function whose input can be many things.

    A function decorator consists of the following:

    - An input function to run with
    - A wrapper function that uses the input function

    The `wrapper` does not need to accept the input function as a parameter
    because it can get that from its parent `run_with_any`. Furthermore, the
    data that wrapper receives does NOT have to be the same as the data that
    the input function needs to accept.

    The formal specification for function decorators is here:

    https://www.python.org/dev/peps/pep-0318/

    The formal specification for class decorators is here:

    https://www.python.org/dev/peps/pep-3129/
    """

    @wraps(fn)
    def wrapper(stringy):
        """Apply wrapped function to a string or a collection."""
        if isinstance(stringy, str):
            return fn(stringy)
        elif isinstance(stringy, dict):
            if all(isinstance(item, str) for item in stringy.values()):
                return {key: fn(value) for key, value in stringy.items()}
            # Nested call on unknown data entries
            return {key: wrapper(value) for key, value in stringy.items()}
        elif isinstance(stringy, (list, set, tuple)):
            sequence_kls = type(stringy)
            if all(isinstance(item, str) for item in stringy):
                return sequence_kls(fn(value) for value in stringy)
            # Nested call on unknown data entries
            return sequence_kls(wrapper(value) for value in stringy)
        raise ValueError("Found item that is not a collection or a string.")

    return wrapper


@run_with_any
def hide_content(content):
    """Hide half of the stringy content."""
    start_point = len(content) // 2
    num_of_asterisks = len(content) // 2 + len(content) % 2
    return content[:start_point] + "*" * num_of_asterisks


def main():
    # There are so many plain-text secrets out in the open
    insecure_stringy = [
        {"username": "johndoe", "password": "s3cret123"},  # User credentials
        ["123-456=7890", "123-456-7891"],  # Social security numbers
        [("johndoe", "janedoe"), ("bobdoe", "marydoe")],  # Couple names
        "secretLaunchCode123",  # Secret launch code
    ]

    # Time to encrypt them all so that they can't be snatched away
    secure_stringy = hide_content(insecure_stringy)

    # See what changed between the old stringy and the new stringy
    for insecure_item, secure_item in zip(insecure_stringy, secure_stringy):
        with header_section():
            print("Insecure item", insecure_item)
            print("Secure item", secure_item)


if __name__ == '__main__':
    main()
