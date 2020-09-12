from contextlib import contextmanager
from io import StringIO

# Module-level constants
_FILESYSTEM = {
    "a.txt": "Hello World",
    "b.xml": "<message>Hello World</message>",
    "c.out": "10101010"
}


@contextmanager
def file(filename):
    """File context manager.

    This is the function variant of the context manager. Context managers
    are useful for resources that need to be opened and closed such as
    files, database connections and sockets.
    """
    buffer = StringIO(_FILESYSTEM[filename])
    try:
        # Pass the buffer to the context block
        yield buffer
    finally:
        # Close the buffer unconditionally
        buffer.close()


class FileHandler:
    """File handler context manager.

    This is the class variant of the context manager. Just like the iterator
    lesson, it depends on context and preference that you choose one style
    over the other.
    """

    def __init__(self, filename):
        self.buffer = StringIO(_FILESYSTEM[filename])

    def __enter__(self):
        """Pass the buffer to the context block."""
        return self.buffer

    def __exit__(self, *args):
        """Close the buffer unconditionally."""
        self.buffer.close()


def main():
    # An example of a function-based context manager
    with file("a.txt") as txt_buffer:
        assert txt_buffer.read() == "Hello World"

    # An example of a class-based context manager
    with FileHandler("b.xml") as xml_buffer:
        assert xml_buffer.read() == "<message>Hello World</message>"

    # Examples of context manager failures
    for obj in (file, FileHandler):
        call_failed = False
        try:
            # Whenever any error happens in the context block, the buffer
            # in the context manager gets closed automatically and the
            # error gets raised to the outer block
            with obj("c.out") as _:
                raise RuntimeError("System crash. Abort!")
        except RuntimeError:
            call_failed = True
        assert call_failed is True


if __name__ == "__main__":
    main()
