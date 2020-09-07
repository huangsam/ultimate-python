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


if __name__ == "__main__":
    main()
