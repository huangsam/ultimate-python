def main():
    # Here are the main literal types to be aware of
    a = 1
    b = 2.0
    c = True
    d = "hello"

    # Notice that each type is a `class`. Each of the variables above refers
    # to an `instance` of the class it belongs to
    a_type = type(a)  # <class 'int'>
    b_type = type(b)  # <class 'float'>
    c_type = type(c)  # <class 'bool'>
    d_type = type(d)  # <class 'str'>

    # This leads to an important point: everything is an object in Python
    a_is_obj = isinstance(a, object) and issubclass(a_type, object)
    b_is_obj = isinstance(b, object) and issubclass(b_type, object)
    c_is_obj = isinstance(c, object) and issubclass(c_type, object)
    d_is_obj = isinstance(d, object) and issubclass(d_type, object)

    # Here is a summary via the `print` function. Notice that we print more
    # than one variable at a time
    print(a, a_type, a_is_obj)
    print(b, b_type, b_is_obj)
    print(c, c_type, c_is_obj)
    print(d, d_type, d_is_obj)


if __name__ == "__main__":
    main()
