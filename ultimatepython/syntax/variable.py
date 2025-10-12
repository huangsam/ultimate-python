"""
Variables allow us to store values in named records that can be used in
a program. This module shows how to define variables and make assertions
about the state of each defined variable.
"""

import math


def main() -> None:
    # Here are the main literal types to be aware of
    a = 1
    b = 2.0
    c = True
    d = "hello"

    # Notice that each type is a class. Each of the variables above refers
    # to an instance of the class it belongs to
    a_type = type(a)
    b_type = type(b)
    c_type = type(c)
    d_type = type(d)

    # Also, say hello to the `assert` keyword! This is a debugging aid that
    # we will use to validate the code as we progress through each `main`
    # function. These statements are used to validate the correctness of
    # the data and to reduce the amount of output sent to the screen
    assert a_type is int
    assert b_type is float
    assert c_type is bool
    assert d_type is str

    # Everything is an object in Python. That means instances are objects
    # and classes are objects as well
    assert isinstance(a, object) and isinstance(a_type, object)
    assert isinstance(b, object) and isinstance(b_type, object)
    assert isinstance(c, object) and isinstance(c_type, object)
    assert isinstance(d, object) and isinstance(d_type, object)

    # We can represent integer literals in Python using 4 bases: decimal,
    # hexadecimal, octal, and binary. Decimal literals do not require any
    # prefix while other bases require prefixes:
    # - `0x` for hexadecimal
    # - `0o` for octal
    # - `0b` for binary
    assert 100 == 0x64 == 0o144 == 0b1100100

    # We can use underscores (literal `_`) to separate digit groups in
    # integer literals
    assert 10_000 == 10000
    assert 0x01_0F_2C == 69_420
    assert math.isclose(3.456_290e-1, 0.3_456_290)

    # There is also a special literal called None. This literal is used to
    # point that a particular variable or object is not created
    e = None
    e_type = type(e)
    assert e_type is type(None)
    assert isinstance(e, object) and isinstance(e_type, object)


if __name__ == "__main__":
    main()
