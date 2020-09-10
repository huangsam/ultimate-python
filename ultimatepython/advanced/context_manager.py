from contextlib import contextmanager

# Module-level constants
_FILESYSTEM = {
    "a.txt": "Hello World",
    "b.xml": "<message>Hello World</message>",
    "c.out": "10101010"
}


class ContentBuffer:
    """Content buffer."""

    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

    def close(self):
        self.content = None


@contextmanager
def file(filename):
    """File context manager."""
    buffer = ContentBuffer(_FILESYSTEM[filename])
    try:
        yield buffer
    finally:
        # Close the buffer unconditionally
        buffer.close()


class FileHandler:
    """File handler context manager."""

    def __init__(self, filename):
        self.buffer = ContentBuffer(_FILESYSTEM[filename])

    def __enter__(self):
        return self.buffer

    def __exit__(self, *args):
        # Close the buffer unconditionally
        self.buffer.close()


def main():
    # An example of a function-based context manager
    with file("a.txt") as txt_buffer:
        assert txt_buffer.read() == "Hello World"

    # An example of a class-based context manager
    with FileHandler("b.xml") as xml_buffer:
        assert xml_buffer.read() == "<message>Hello World</message>"

    # Examples of how a context manager might fail
    for obj in (file, FileHandler):
        call_fails = False
        try:
            with obj("c.out") as _:
                raise RuntimeError("System crash. Abort!")
        except RuntimeError:
            call_fails = True
        assert call_fails is True


if __name__ == '__main__':
    main()
