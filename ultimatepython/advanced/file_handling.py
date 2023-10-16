"""
File handling is a fundamental concept in Python that involves opening, reading, writing, and appending to files.
This code example demonstrates the basics of file handling in Python.
Python provides various ways to work with files.
We can use the built-in 'open' function to open files in different modes like reading ('r'), writing ('w'), and appending ('a').
"""


# Open a file for reading
def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content


# Open a file for writing
def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    return f"Content written to '{filename}'."


# Open a file for appending
def append_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
    return f"Content appended to '{filename}'."


def main():
    # Example of writing to a file
    result = write_file("sample.txt", "This is a test.")
    assert result == "Content written to 'sample.txt'."

    # Example of reading a file
    content = read_file("sample.txt")
    assert content == "This is a test."

    # Example of appending to a file
    append_result = append_file("sample.txt", "\nThis is an appended line.")
    assert append_result == "Content appended to 'sample.txt'."

    # Verify the content after appending
    content = read_file("sample.txt")
    assert content == "This is a test.\nThis is an appended line."


if __name__ == "__main__":
    main()
