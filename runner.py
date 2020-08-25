import io
import sys
from contextlib import contextmanager
from importlib import import_module
from inspect import isfunction, signature
from os import devnull
from pkgutil import walk_packages

import ultimatepython as root

# Module-level constants
_STYLE_SUCCESS = "\033[92m"
_STYLE_BOLD = "\033[1m"
_STYLE_END = "\033[0m"
_RUNNER_PROGRESS = "->"
_MODULE_MAIN = "main"


@contextmanager
def no_stdout():
    """Silence standard output with /dev/null."""
    save_stdout = sys.stdout
    with io.open(devnull, "w") as dev_null:
        sys.stdout = dev_null
        yield
    sys.stdout = save_stdout


def success_text(text):
    """Get success text."""
    return f"{_STYLE_SUCCESS}{bold_text(text)}{_STYLE_END}"


def bold_text(text):
    """Get bold text."""
    return f"{_STYLE_BOLD}{text}{_STYLE_END}"


def main():
    print(bold_text(f"Start {root.__name__} runner"))

    for item in walk_packages(root.__path__, root.__name__ + "."):
        mod = import_module(item.name)

        # Skip modules without a main object
        if not hasattr(mod, _MODULE_MAIN):
            continue

        # By this point, there is a main object in the module
        main_func = getattr(mod, _MODULE_MAIN)

        # The main object is a function
        assert isfunction(main_func)

        # The main function has zero parameters
        assert len(signature(main_func).parameters) == 0

        # The main function should not throw any errors
        print(f"{_RUNNER_PROGRESS} Run {mod.__name__}:{_MODULE_MAIN}", end="")
        with no_stdout():
            main_func()
        print(" [PASS]")

    print(success_text(f"Finish {root.__name__} runner"))


if __name__ == "__main__":
    main()
