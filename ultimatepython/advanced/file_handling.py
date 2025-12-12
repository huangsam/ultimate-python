"""
File handling is a fundamental concept in Python that involves
opening, reading, writing, and appending to files. This module
demonstrates both traditional and modern approaches using pathlib.

Traditional approach: The builtin 'open' function works with string
paths and different modes like reading ('r'), writing ('w'), and
appending ('a').

Modern approach: pathlib.Path provides an object-oriented interface
for working with filesystem paths, offering cleaner syntax and
cross-platform support. pathlib is preferred for new code as it
replaces older os.path operations with an intuitive API.
"""

import os
from pathlib import Path

_TARGET_FILE = "sample.txt"
_TARGET_PATH = Path(_TARGET_FILE)


def read_file(filename: str) -> str:
    """Read content from existing file."""
    with open(filename, "r") as file:
        content = file.read()
        return content


def write_file(filename: str, content: str) -> str:
    """Write content to new file."""
    with open(filename, "w") as file:
        file.write(content)
    return f"Content written to '{filename}'."


def append_file(filename: str, content: str) -> str:
    """Append content to existing file."""
    with open(filename, "a") as file:
        file.write(content)
    return f"Content appended to '{filename}'."


def delete_file(filename: str) -> str:
    """Delete content of existing file."""
    os.remove(filename)
    return f"'{filename}' has been deleted."


def write_file_pathlib(filename: str, content: str) -> str:
    """Write content using pathlib.Path."""
    path = Path(filename)
    path.write_text(content)
    return f"Content written to '{filename}' using pathlib."


def read_file_pathlib(filename: str) -> str:
    """Read content using pathlib.Path."""
    path = Path(filename)
    return path.read_text()


def append_file_pathlib(filename: str, content: str) -> str:
    """Append content using pathlib.Path."""
    path = Path(filename)
    current = path.read_text()
    path.write_text(current + content)
    return f"Content appended to '{filename}' using pathlib."


def delete_file_pathlib(filename: str) -> str:
    """Delete file using pathlib.Path."""
    path = Path(filename)
    path.unlink()
    return f"'{filename}' has been deleted using pathlib."


def main() -> None:
    # Test traditional file operations
    result = write_file(_TARGET_FILE, "This is a test.")
    assert result == f"Content written to '{_TARGET_FILE}'."

    content = read_file(_TARGET_FILE)
    assert content == "This is a test."

    append_result = append_file(_TARGET_FILE, "\nThis is an appended line.")
    assert append_result == f"Content appended to '{_TARGET_FILE}'."

    content = read_file(_TARGET_FILE)
    assert content == "This is a test.\nThis is an appended line."

    delete_result = delete_file(_TARGET_FILE)
    assert delete_result == f"'{_TARGET_FILE}' has been deleted."

    # Test pathlib operations
    pathlib_file = "pathlib_sample.txt"
    result = write_file_pathlib(pathlib_file, "Pathlib is modern.")
    assert result == f"Content written to '{pathlib_file}' using pathlib."

    content = read_file_pathlib(pathlib_file)
    assert content == "Pathlib is modern."

    append_result = append_file_pathlib(pathlib_file, "\nIt's object-oriented.")
    assert append_result == f"Content appended to '{pathlib_file}' using pathlib."

    content = read_file_pathlib(pathlib_file)
    assert content == "Pathlib is modern.\nIt's object-oriented."

    # Test path operations with pathlib
    path = Path(pathlib_file)
    assert path.exists()
    assert path.is_file()
    assert path.suffix == ".txt"
    assert path.stem == "pathlib_sample"

    delete_result = delete_file_pathlib(pathlib_file)
    assert delete_result == f"'{pathlib_file}' has been deleted using pathlib."
    assert not path.exists()


if __name__ == "__main__":
    main()
