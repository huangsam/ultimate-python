from importlib import import_module
from inspect import isfunction, signature
from pkgutil import walk_packages

from ultimatepython import __name__ as root_name
from ultimatepython import __path__ as root_path

# Module-level constants
_STYLE_SUCCESS = "\033[92m"
_STYLE_BOLD = "\033[1m"
_STYLE_END = "\033[0m"
_RUNNER_PROGRESS = "->"
_MODULE_MAIN = "main"


def success_text(text):
    """Get success text."""
    return f"{_STYLE_SUCCESS}{bold_text(text)}{_STYLE_END}"


def bold_text(text):
    """Get bold text."""
    return f"{_STYLE_BOLD}{text}{_STYLE_END}"


def main():
    print(bold_text(f"Start {root_name} runner"))

    for item in walk_packages(root_path, f"{root_name}."):
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
        main_func()
        print(" [PASS]")

    print(success_text(f"Finish {root_name} runner"))


if __name__ == "__main__":
    main()
