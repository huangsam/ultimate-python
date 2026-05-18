import sys
from importlib import import_module
from inspect import isfunction, signature
from pkgutil import walk_packages

from ultimatepython import __name__ as root_name
from ultimatepython import __path__ as root_path

# Module-level constants
_STYLE_SUCCESS = "\033[92m"
_STYLE_FAILURE = "\033[91m"
_STYLE_BOLD = "\033[1m"
_STYLE_END = "\033[0m"
_RUNNER_PROGRESS = "->"
_RUNNER_MAIN = "main"


def style_text(text: str, color: str = "") -> str:
    """Get styled text."""
    return f"{color}{_STYLE_BOLD}{text}{_STYLE_END}"


def main() -> None:
    # Get filter from command line arguments
    filter_str = sys.argv[1] if len(sys.argv) > 1 else None

    print(style_text(f"Start {root_name} runner"))

    stats = {"passed": 0, "failed": 0, "skipped": 0}

    for item in walk_packages(root_path, f"{root_name}."):
        # Skip packages (folders), only run modules (files)
        if item.ispkg:
            continue

        # Filter modules based on command line argument
        if filter_str and filter_str not in item.name:
            continue

        try:
            mod = import_module(item.name)
        except (ImportError, SyntaxError) as e:
            print(f"{_RUNNER_PROGRESS} Skip {item.name}: {e}")
            stats["skipped"] += 1
            continue

        # Skip modules without a valid main object
        mod_main = getattr(mod, _RUNNER_MAIN, None)
        if not isfunction(mod_main) or len(signature(mod_main).parameters) != 0:
            print(f"{_RUNNER_PROGRESS} Skip {item.name}: No valid {_RUNNER_MAIN}() function")
            stats["skipped"] += 1
            continue

        # Execution phase
        print(f"{_RUNNER_PROGRESS} Run {mod.__name__}:{_RUNNER_MAIN}", end="")
        try:
            mod_main()
            print(style_text(" [PASS]", _STYLE_SUCCESS))
            stats["passed"] += 1
        except Exception as e:
            print(style_text(" [FAIL]", _STYLE_FAILURE))
            print(f"    Error in {item.name}: {e}")
            stats["failed"] += 1

    # Summary report
    print("\n" + "=" * 30)
    print(style_text(f"Finish {root_name} runner", _STYLE_SUCCESS))
    print(f"Passed: {stats['passed']} | Failed: {stats['failed']} | Skipped: {stats['skipped']}")
    print("=" * 30)


if __name__ == "__main__":
    main()
