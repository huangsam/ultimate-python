# Module-level constants
_DELIMITER = " | "
_PADDING = 10


def main():
    # String is one of the most robust data structures around
    content = "Ultimate Python study guide"

    # We can compute its length just like all other data structures
    assert len(content) > 0

    # Notice that we pad the right of the label with spaces
    print("Original:".ljust(_PADDING), content)

    # Like tuples, we cannot change the data in a string. However, we can
    # create a new string from an existing string
    new_content = f"{content.upper()}{_DELIMITER}{content.lower()}"
    print("New:".ljust(_PADDING), new_content)

    # We can split one string into a list of strings
    split_content = new_content.split(_DELIMITER)
    assert isinstance(split_content, list)
    assert len(split_content) == 2
    assert all(isinstance(item, str) for item in split_content)

    # A two-element list can be decomposed as two variables
    upper_content, lower_content = split_content
    assert upper_content.isupper() and lower_content.islower()

    # Keep in mind that the two content variables reference substrings
    # in the original string they were split from
    assert upper_content in new_content
    assert new_content.startswith(upper_content)
    assert lower_content in new_content
    assert new_content.endswith(lower_content)

    # We can also join multiple strings into one string
    joined_content = _DELIMITER.join(split_content)
    assert isinstance(joined_content, str)
    assert new_content == joined_content
    print("Joined:".ljust(_PADDING), joined_content)


if __name__ == '__main__':
    main()
