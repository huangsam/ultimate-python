from functools import wraps

# Module-level constants
_MASKING = "*"


def run_with_stringy(fn):
    """Run a string function with a string or a collection of strings.

    We define a custom decorator that allows us to convert a function whose
    input is a single string into a function whose input can be a string
    or a collection of strings.

    A function decorator consists of the following:

    - An input function to run with
    - A wrapper function that uses the input function

    The `wrapper` does not need to accept the input function as a parameter
    because it can get that from its parent `run_with_any`. Also, the
    parameters that `wrapper` receives do NOT have to be the same as the
    ones that the input function `fn` needs to receive. However, it is highly
    recommended to have the parameter lists for `wrapper` and `fn` line up so
    that developers are less likely to get confused.

    The formal specification for function decorators is here:

    https://www.python.org/dev/peps/pep-0318/

    The formal specification for class decorators is here:

    https://www.python.org/dev/peps/pep-3129/
    """

    @wraps(fn)
    def wrapper(obj):
        """Apply wrapped function to a string or a collection.

        This looks like a policy-based engine which runs a `return` statement
        if a particular set of rules is true. Otherwise it aborts. This is
        an example of the Strategy design pattern.

        https://en.wikipedia.org/wiki/Strategy_pattern

        But instead of writing the logic using classes, we write the logic
        using a single function that encapsulates all possible rules.
        """
        if isinstance(obj, str):
            return fn(obj)
        elif isinstance(obj, dict):
            return {key: wrapper(value) for key, value in obj.items()}
        elif isinstance(obj, (list, set, tuple)):
            sequence_kls = type(obj)
            return sequence_kls(wrapper(value) for value in obj)
        raise ValueError(f"Found an invalid item: {obj}")

    return wrapper


@run_with_stringy
def hide_content(content):
    """Hide half of the string content."""
    start_point = len(content) // 2
    num_of_asterisks = len(content) // 2 + len(content) % 2
    return content[:start_point] + _MASKING * num_of_asterisks


def _is_hidden(obj):
    """Check whether string or collection is hidden."""
    if isinstance(obj, str):
        return _MASKING in obj
    elif isinstance(obj, dict):
        return all(_is_hidden(value) for value in obj.values())
    return all(_is_hidden(value) for value in obj)


def main():
    # There is so much plain-text data out in the open
    insecure_data = [
        {"username": "johndoe", "country": "USA"},  # User information
        ["123-456-7890", "123-456-7891"],  # Social security numbers
        [("johndoe", "janedoe"), ("bobdoe", "marydoe")],  # Couple names
        "secretLaunchCode123",  # Secret launch code
    ]

    # Time to encrypt it all so that it can't be snatched away. This kind
    # of work is the stuff that might be done by a company for GDPR. For more
    # on that policy, check out the following Wikipedia page:
    # https://en.wikipedia.org/wiki/General_Data_Protection_Regulation
    secure_data = hide_content(insecure_data)

    # See what changed between the insecure data and the secure data
    for insecure_item, secure_item in zip(insecure_data, secure_data):
        assert insecure_item != secure_item
        assert not _is_hidden(insecure_item)
        assert _is_hidden(secure_item)

    # Throw an error on a collection with non-string objects
    input_failed = False
    try:
        hide_content([1])
    except ValueError:
        input_failed = True
    assert input_failed is True


if __name__ == "__main__":
    main()
