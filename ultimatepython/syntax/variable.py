def main():
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

    # Integer literals in Python can be represented in 4 bases: decimal,
    # hexadecimal, octal, and binary. Decimal literals does not require any
    # prefix, but hexadecimal, octal, and binary requires a base prefix, i.e.
    # `0x` for hexadecimal, `0o` for octal, and `0b` for binary.
    # see (https://docs.python.org/3/library/functions.html#int)
    assert 100 == 0x64 == 0o144 == 0b1100100

    # Integer literals in Python can have underscores (literal `_`) as digit
    # group separators, but integer literals cannot start or end with
    # underscores.
    # see (https://www.python.org/dev/peps/pep-0515/)
    assert 10_000 == 10000
    assert 0x01_0f_2c == 69_420
    assert 3.456_290e-1 == 0.3_456_290


if __name__ == "__main__":
    main()
