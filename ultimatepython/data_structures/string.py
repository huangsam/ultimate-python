# Module-level constants
_DELIMITER = " | "
_PADDING = 10


def label(name, padding=_PADDING):
    """Get name as title with right-side padding."""
    return f"{name.title()}:".ljust(padding)


def main():
    # Strings are some of the most robust data structures around
    content = "Ultimate Python study guide"

    # We can compute a string's length just like all other data structures
    assert len(content) > 0

    # We can use range slices to get substrings from the content
    assert content[:8] == "Ultimate"
    assert content[9:15] == "Python"
    assert content[::-1] == "ediug yduts nohtyP etamitlU"

    # And unsurprisingly, we can print its contents as well
    print(label("original"), content)

    # Like tuples, we cannot change the data in a string. However, we can
    # create a new string from existing strings
    new_content = f"{content.upper()}{_DELIMITER}{content.lower()}"
    print(label("new"), new_content)

    # We can split one string into a list of strings
    split_content = new_content.split(_DELIMITER)
    assert isinstance(split_content, list)
    assert len(split_content) == 2
    assert all(isinstance(item, str) for item in split_content)

    # A two-element list can be decomposed as two variables
    upper_content, lower_content = split_content
    assert upper_content.isupper() and lower_content.islower()

    # Notice that the data in `upper_content` and `lower_content` exists
    # in the `new_content` variable as expected
    assert upper_content in new_content
    assert new_content.startswith(upper_content)
    assert lower_content in new_content
    assert new_content.endswith(lower_content)

    # Let's print the split variables for visual proof
    print(label("upper"), upper_content)
    print(label("lower"), lower_content)

    # Notice that `upper_content` and `lower_content` are smaller
    # than `new_content` and have the same length as the original
    # `content` they were derived from
    assert len(upper_content) < len(new_content)
    assert len(lower_content) < len(new_content)
    assert len(upper_content) == len(lower_content) == len(content)

    # We can also join `upper_content` and `lower_content` back into one
    # string with the same contents as `new_content`. The `join` method is
    # useful for joining an arbitrary amount of text items together.
    joined_content = _DELIMITER.join(split_content)
    assert isinstance(joined_content, str)
    assert new_content == joined_content
    print(label("joined"), joined_content)


if __name__ == '__main__':
    main()
