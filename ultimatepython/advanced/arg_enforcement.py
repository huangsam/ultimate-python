"""
Positional-only and keyword-only parameters allow you to enforce how
arguments are passed to a function. This feature helps prevent misuse
of function APIs and makes code more maintainable.

- Positional-only parameters (/) were introduced in Python 3.8 (PEP 570)
- Keyword-only parameters (*) were introduced in Python 3.0 (PEP 3102)

These features give you fine-grained control over your function signatures.
"""

from collections.abc import Callable
from typing import Any


def traditional_function(a: int, b: int, c: int) -> int:
    """A traditional function where all parameters can be passed either way.

    This function accepts arguments positionally or by keyword name.
    While flexible, this can lead to API instability if parameter names change.
    """
    return a + b + c


def positional_only(a: int, b: int, /) -> int:
    """Function with positional-only parameters.

    The / symbol marks that parameters before it MUST be passed positionally.
    This is useful when parameter names are not meaningful or when you want
    to reserve the right to change parameter names without breaking callers.

    Parameters before / cannot be passed as keyword arguments.
    """
    return a + b


def keyword_only(*, x: int, y: int) -> int:
    """Function with keyword-only parameters.

    The * symbol marks that parameters after it MUST be passed by keyword.
    This is useful for improving readability at call sites and preventing
    accidental argument order mistakes.

    Parameters after * cannot be passed positionally.
    """
    return x * y


def mixed_parameters(pos_only: str, /, pos_or_kw: str, *, kw_only: str) -> str:
    """Function that combines all parameter types.

    - pos_only: Must be passed positionally (before /)
    - pos_or_kw: Can be passed either way (between / and *)
    - kw_only: Must be passed by keyword (after *)

    This gives maximum control over the function interface.
    """
    return f"{pos_only}-{pos_or_kw}-{kw_only}"


def positional_with_defaults(a: int, b: int = 10, /) -> int:
    """Positional-only parameters can have default values.

    Default values work the same way as in traditional functions,
    but the parameters still must be passed positionally if provided.
    """
    return a + b


def keyword_with_defaults(*, x: int = 5, y: int = 3) -> int:
    """Keyword-only parameters can have default values.

    When providing arguments, you must use the keyword names.
    """
    return x**y


def complex_signature(a: int, b: int, /, c: int, d: int = 10, *, e: int, f: int = 20) -> int:
    """A function demonstrating a complex but valid signature.

    - a, b: positional-only
    - c: positional-or-keyword (no default)
    - d: positional-or-keyword (with default)
    - e: keyword-only (no default)
    - f: keyword-only (with default)
    """
    return a + b + c + d + e + f


def distance(x1: float, y1: float, x2: float, y2: float, /) -> float:
    """Calculate distance between two points.

    The parameter names here are somewhat arbitrary (could be p1_x, etc.)
    so we make them positional-only to give us flexibility to rename them
    without breaking existing code.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def create_user(username: str, *, admin: bool = False, active: bool = True, send_email: bool = False) -> dict[str, object]:
    """Create a user with clear intent for optional parameters.

    Making admin, active, and send_email keyword-only ensures that
    callers must specify exactly what they're setting, improving
    readability and preventing accidental mistakes.
    """
    return {"username": username, "admin": admin, "active": active, "send_email": send_email}


def assert_raises_type_error(fn: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
    """Verify that calling fn with given arguments raises a TypeError."""
    raised = False
    try:
        fn(*args, **kwargs)
    except TypeError:
        raised = True
    assert raised is True


def main() -> None:
    # Traditional function: can be called either way
    assert traditional_function(1, 2, 3) == 6
    assert traditional_function(a=1, b=2, c=3) == 6
    assert traditional_function(1, b=2, c=3) == 6

    # Positional-only function: must use positional arguments
    assert positional_only(5, 3) == 8
    # Arguments before / cannot be passed by keyword name
    assert_raises_type_error(positional_only, a=5, b=3)
    assert_raises_type_error(positional_only, 5, b=3)

    # Keyword-only function: must use keyword arguments
    assert keyword_only(x=4, y=5) == 20
    # Arguments after * cannot be passed positionally
    assert_raises_type_error(keyword_only, 4, 5)

    # Mixed parameters demonstrate all three types
    assert mixed_parameters("first", "second", kw_only="third") == "first-second-third"
    assert mixed_parameters("first", pos_or_kw="second", kw_only="third") == "first-second-third"
    # Positional-only must be positional, keyword-only must be keyword
    assert_raises_type_error(mixed_parameters, pos_only="first", pos_or_kw="second", kw_only="third")
    assert_raises_type_error(mixed_parameters, "first", "second", "third")

    # Positional-only with defaults still requires positional passing
    assert positional_with_defaults(5) == 15
    assert positional_with_defaults(5, 20) == 25
    assert_raises_type_error(positional_with_defaults, a=5, b=20)

    # Keyword-only with defaults still requires keyword passing
    assert keyword_with_defaults() == 125
    assert keyword_with_defaults(x=2) == 8
    assert keyword_with_defaults(y=2) == 25
    assert keyword_with_defaults(x=3, y=4) == 81
    assert_raises_type_error(keyword_with_defaults, 2, 3)

    # Complex signature: demonstrating all parameter types
    assert complex_signature(1, 2, 3, e=4) == 40
    assert complex_signature(1, 2, 3, 4, e=5, f=6) == 21
    assert complex_signature(1, 2, c=3, e=4) == 40
    assert complex_signature(1, 2, 3, d=15, e=4) == 45
    assert_raises_type_error(complex_signature, a=1, b=2, c=3, e=4)
    assert_raises_type_error(complex_signature, 1, 2, 3, 10, 4)

    # Practical use case 1: Positional-only parameter renaming flexibility
    assert abs(distance(0, 0, 3, 4) - 5.0) < 0.01

    # Practical use case 2: Keyword-only clarity for optional flags
    user = create_user("john_doe", admin=True, send_email=True)
    assert user["admin"] is True
    assert user["active"] is True
    assert user["send_email"] is True


if __name__ == "__main__":
    main()
