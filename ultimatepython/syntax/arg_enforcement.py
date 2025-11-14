"""
Positional-only and keyword-only parameters allow you to enforce how
arguments are passed to a function. This feature helps prevent misuse
of function APIs and makes code more maintainable.

- Positional-only parameters (/) were introduced in Python 3.8 (PEP 570)
- Keyword-only parameters (*) were introduced in Python 3.0 (PEP 3102)

These features give you fine-grained control over your function signatures.
"""


def traditional_function(a, b, c):
    """A traditional function where all parameters can be passed either way.

    This function accepts arguments positionally or by keyword name.
    While flexible, this can lead to API instability if parameter names change.
    """
    return a + b + c


def positional_only(a, b, /):
    """Function with positional-only parameters.

    The / symbol marks that parameters before it MUST be passed positionally.
    This is useful when parameter names are not meaningful or when you want
    to reserve the right to change parameter names without breaking callers.

    Parameters before / cannot be passed as keyword arguments.
    """
    return a + b


def keyword_only(*, x, y):
    """Function with keyword-only parameters.

    The * symbol marks that parameters after it MUST be passed by keyword.
    This is useful for improving readability at call sites and preventing
    accidental argument order mistakes.

    Parameters after * cannot be passed positionally.
    """
    return x * y


def mixed_parameters(pos_only, /, pos_or_kw, *, kw_only):
    """Function that combines all parameter types.

    - pos_only: Must be passed positionally (before /)
    - pos_or_kw: Can be passed either way (between / and *)
    - kw_only: Must be passed by keyword (after *)

    This gives maximum control over the function interface.
    """
    return f"{pos_only}-{pos_or_kw}-{kw_only}"


def positional_with_defaults(a, b=10, /):
    """Positional-only parameters can have default values.

    Default values work the same way as in traditional functions,
    but the parameters still must be passed positionally if provided.
    """
    return a + b


def keyword_with_defaults(*, x=5, y=3):
    """Keyword-only parameters can have default values.

    When providing arguments, you must use the keyword names.
    """
    return x**y


def complex_signature(a, b, /, c, d=10, *, e, f=20):
    """A function demonstrating a complex but valid signature.

    - a, b: positional-only
    - c: positional-or-keyword (no default)
    - d: positional-or-keyword (with default)
    - e: keyword-only (no default)
    - f: keyword-only (with default)
    """
    return a + b + c + d + e + f


def main() -> None:
    # Traditional function: can be called either way
    assert traditional_function(1, 2, 3) == 6
    assert traditional_function(a=1, b=2, c=3) == 6
    assert traditional_function(1, b=2, c=3) == 6

    # Positional-only function: must use positional arguments
    assert positional_only(5, 3) == 8

    # Trying to use keyword arguments with positional-only parameters
    # will raise a TypeError
    positional_error = False
    try:
        # This will fail because 'a' and 'b' are positional-only
        positional_only(a=5, b=3)
    except TypeError:
        positional_error = True
    assert positional_error is True

    # You also can't mix positional and keyword for positional-only params
    positional_error2 = False
    try:
        # This will fail because 'b' is positional-only
        positional_only(5, b=3)
    except TypeError:
        positional_error2 = True
    assert positional_error2 is True

    # Keyword-only function: must use keyword arguments
    assert keyword_only(x=4, y=5) == 20

    # Trying to use positional arguments with keyword-only parameters
    # will raise a TypeError
    keyword_error = False
    try:
        # This will fail because 'x' and 'y' are keyword-only
        keyword_only(4, 5)
    except TypeError:
        keyword_error = True
    assert keyword_error is True

    # Mixed parameters demonstrate all three types
    result = mixed_parameters("first", "second", kw_only="third")
    assert result == "first-second-third"

    # The middle parameter can be passed either way
    result2 = mixed_parameters("first", pos_or_kw="second", kw_only="third")
    assert result2 == "first-second-third"

    # But positional-only must be positional
    mixed_error = False
    try:
        mixed_parameters(pos_only="first", pos_or_kw="second", kw_only="third")
    except TypeError:
        mixed_error = True
    assert mixed_error is True

    # And keyword-only must be keyword
    mixed_error2 = False
    try:
        mixed_parameters("first", "second", "third")
    except TypeError:
        mixed_error2 = True
    assert mixed_error2 is True

    # Positional-only with defaults
    assert positional_with_defaults(5) == 15  # Uses default b=10
    assert positional_with_defaults(5, 20) == 25  # Overrides b with 20

    # Even with defaults, must use positional syntax
    positional_default_error = False
    try:
        positional_with_defaults(a=5, b=20)
    except TypeError:
        positional_default_error = True
    assert positional_default_error is True

    # Keyword-only with defaults
    assert keyword_with_defaults() == 125  # Uses defaults: 5^3
    assert keyword_with_defaults(x=2) == 8  # 2^3
    assert keyword_with_defaults(y=2) == 25  # 5^2
    assert keyword_with_defaults(x=3, y=4) == 81  # 3^4

    # Must still use keyword syntax even when providing defaults
    keyword_default_error = False
    try:
        keyword_with_defaults(2, 3)
    except TypeError:
        keyword_default_error = True
    assert keyword_default_error is True

    # Complex signature: demonstrating all parameter types
    # Minimal call with required params only
    result3 = complex_signature(1, 2, 3, e=4)
    assert result3 == 40  # 1+2+3+10(default)+4+20(default)

    # Providing all parameters
    result4 = complex_signature(1, 2, 3, 4, e=5, f=6)
    assert result4 == 21  # 1+2+3+4+5+6

    # Middle parameter 'c' can be passed by keyword
    result5 = complex_signature(1, 2, c=3, e=4)
    assert result5 == 40

    # Parameter 'd' can also be passed by keyword
    result6 = complex_signature(1, 2, 3, d=15, e=4)
    assert result6 == 45  # 1+2+3+15+4+20

    # But 'a' and 'b' must be positional
    complex_error = False
    try:
        complex_signature(a=1, b=2, c=3, e=4)
    except TypeError:
        complex_error = True
    assert complex_error is True

    # And 'e' must be keyword (even though 'f' has a default)
    complex_error2 = False
    try:
        complex_signature(1, 2, 3, 10, 4)
    except TypeError:
        complex_error2 = True
    assert complex_error2 is True

    # Practical use case: Positional-only is great for functions where
    # parameter names are not meaningful or may change
    def distance(x1, y1, x2, y2, /):
        """Calculate distance between two points.

        The parameter names here are somewhat arbitrary (could be p1_x, etc.)
        so we make them positional-only to give us flexibility to rename them
        without breaking existing code.
        """
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    assert abs(distance(0, 0, 3, 4) - 5.0) < 0.01

    # Practical use case: Keyword-only is great for boolean flags or
    # optional parameters where the intent should be clear at call site
    def create_user(username, *, admin=False, active=True, send_email=False):
        """Create a user with clear intent for optional parameters.

        Making admin, active, and send_email keyword-only ensures that
        callers must specify exactly what they're setting, improving
        readability and preventing accidental mistakes.
        """
        return {"username": username, "admin": admin, "active": active, "send_email": send_email}

    # Clear intent at call site
    user = create_user("john_doe", admin=True, send_email=True)
    assert user["admin"] is True
    assert user["active"] is True  # Used default
    assert user["send_email"] is True


if __name__ == "__main__":
    main()
