"""
Enumerations (`enum` module) provide a way to define sets of symbolic names bound
to unique, constant values.

Using raw strings or magic numbers for status codes, options, or flags introduces
typos, invalid states, and brittle code. The standard `enum` module provides
type-safe, iterable, and comparable constants.

Key enum types demonstrated:
- `Enum`: Base class for standard enumerated constants
- `auto()`: Automatically generates distinct values for enum members
- `IntEnum`: Enum members that are also subclasses of `int` (supports ordering)
- `Flag`: Supports bitwise operations (`|`, `&`) for composite flags / permissions
"""

from enum import Enum, Flag, IntEnum, auto


class Status(Enum):
    """Standard lifecycle status."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"


class Priority(IntEnum):
    """Numeric priority levels that support comparison operators."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Color(Enum):
    """Color palette using auto-generated values."""

    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Permission(Flag):
    """File permissions supporting bitwise combinations."""

    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


def main() -> None:
    # 1. Access by name and value
    status = Status.RUNNING
    assert status.name == "RUNNING"
    assert status.value == "running"

    # 2. Lookups by value and by name
    assert Status("pending") is Status.PENDING
    assert Status["SUCCESS"] is Status.SUCCESS

    # Lookup with an invalid value raises ValueError
    invalid_status_failed = False
    try:
        Status("unknown")
    except ValueError:
        invalid_status_failed = True
    assert invalid_status_failed is True

    # 3. Enum members are singletons: use 'is' or '==' for identity and equality
    assert status is Status.RUNNING
    assert status is not Status.PENDING

    # 4. Iteration yields all members in definition order
    statuses = [s for s in Status]
    assert len(statuses) == 4
    assert statuses[0] is Status.PENDING

    # 5. auto() assigns distinct integer values sequentially
    assert Color.RED.value == 1
    assert Color.GREEN.value == 2
    assert Color.BLUE.value == 3

    # 6. IntEnum supports integer comparisons and sorting
    assert Priority.HIGH > Priority.LOW
    assert Priority.MEDIUM == 2
    priorities = sorted([Priority.HIGH, Priority.LOW, Priority.MEDIUM])
    assert priorities == [Priority.LOW, Priority.MEDIUM, Priority.HIGH]

    # 7. Flag allows bitwise combination and membership checking
    read_write = Permission.READ | Permission.WRITE
    all_perms = read_write | Permission.EXECUTE

    assert Permission.READ in read_write
    assert Permission.WRITE in read_write
    assert Permission.EXECUTE not in read_write
    assert Permission.EXECUTE in all_perms


if __name__ == "__main__":
    main()
