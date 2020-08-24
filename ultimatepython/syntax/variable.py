def main():
    # Here are the main literal types to be aware of
    a = 1
    b = 2.0
    c = True
    d = "hello"

    # Notice that each type is a `class`. Each of the variables above refers
    # to an `instance` of the class it belongs to. For instance, `a` is of type
    # `int` which is a `class`
    a_type = type(a)  # <class 'int'>
    b_type = type(b)  # <class 'float'>
    c_type = type(c)  # <class 'bool'>
    d_type = type(d)  # <class 'str'>

    # This leads to an important point: everything is an object in Python.
    # Notice that all instances and classes are objects. Also, say hello
    # to the `assert` keyword! This is a debugging aid that we use to validate
    # the code as we progress through the `main` functions. These statements
    # are used to validate the correctness of the data and to reduce
    # the amount of standard output that is sent when running `main`
    assert isinstance(a, object) and isinstance(a_type, object)
    assert isinstance(b, object) and isinstance(b_type, object)
    assert isinstance(c, object) and isinstance(c_type, object)
    assert isinstance(d, object) and isinstance(d_type, object)

    # Here is a summary via the `print` function. Notice that we print more
    # than one variable at a time
    print(a, a_type)
    print(b, b_type)
    print(c, c_type)
    print(d, d_type)


if __name__ == "__main__":
    main()
