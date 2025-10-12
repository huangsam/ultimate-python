"""
Context managers are used to open and close resources as Python enters
and exits a code block respectively. Some examples of the resources it
can manage are files, database connections and sockets. In this module,
we simulate how a context manager can handle open and close operations of
a file-like object called StringIO.
"""

from contextlib import contextmanager
from io import StringIO
from typing import Generator

# Simple directory with file contents
_FILESYSTEM = {
    "a.txt": "Hello World",
    "b.xml": "<message>Hello World</message>",
    "c.out": "10101010",
}


@contextmanager
def file(filename: str) -> Generator[StringIO, None, None]:
    """File context manager.

    This is the function variant of the context manager. Context managers
    are useful for resources that need to be opened and closed such as
    files, database connections and sockets.
    """
    io_buffer = StringIO(_FILESYSTEM[filename])
    try:
        # Pass the buffer to the context block
        yield io_buffer
    finally:
        # Close the buffer unconditionally
        io_buffer.close()


class FileHandler:
    """File handler context manager.

    This is the class variant of the context manager. Just like with
    iterators, it depends on context and preference that we design a
    class or simply write a function.
    """

    def __init__(self, filename: str) -> None:
        self.io_buffer = StringIO(_FILESYSTEM[filename])

    def __enter__(self) -> StringIO:
        """Pass the buffer to the context block."""
        return self.io_buffer

    def __exit__(self, *args) -> None:
        """Close the buffer unconditionally."""
        self.io_buffer.close()


def main() -> None:
    # An example of a function-based context manager
    with file("a.txt") as txt_buffer:
        assert txt_buffer.read() == "Hello World"

    # An example of a class-based context manager
    with FileHandler("b.xml") as xml_buffer:
        assert xml_buffer.read() == "<message>Hello World</message>"

    # Examples of context manager failures
    for context_obj in (file, FileHandler):
        call_failed = False
        try:
            # Whenever any error happens in the context block, the buffer
            # in the context manager gets closed automatically and the
            # error gets raised to the outer block
            with context_obj("c.out"):
                raise RuntimeError("System crash. Abort!")
        except RuntimeError:
            call_failed = True
        assert call_failed is True


if __name__ == "__main__":
    main()
