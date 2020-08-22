import sys
from contextlib import contextmanager
from importlib import import_module
from inspect import isfunction, signature
from os import devnull
from pkgutil import walk_packages

import ultimatepython as root


@contextmanager
def no_stdout():
    save_stdout = sys.stdout
    with open(devnull, "w") as dev_null:
        sys.stdout = dev_null
        yield
    sys.stdout = save_stdout


def main():
    print(f">>> Start {root.__name__} runner \U0001F447")

    for item in walk_packages(root.__path__, root.__name__ + "."):
        mod = import_module(item.name)

        if not hasattr(mod, "main"):
            continue

        # By this point, there is a main object in the module
        main_func = getattr(mod, "main")

        # The main object is a function
        assert isfunction(main_func)

        # The main function has zero parameters
        assert len(signature(main_func).parameters) == 0

        # The main function should not throw any errors
        print(f"Run {mod.__name__}:{main_func.__name__}")
        with no_stdout():
            main_func()

    print(f">>> End {root.__name__} runner \U0001F44C")


if __name__ == "__main__":
    main()
