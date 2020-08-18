def main():
    # Here are the main literal types to be aware of
    a = 1
    b = 2.0
    c = True
    d = "hello"

    # Notice that each type is a 'class'. Each variable
    # refers to an 'instance' of the class it belongs to
    a_type = type(a)  # <class 'int'>
    b_type = type(b)  # <class 'float'>
    c_type = type(c)  # <class 'bool'>
    d_type = type(d)  # <class 'str'>

    # This leads to an important point: everything
    # is an object in Python
    print(isinstance(a, object) and issubclass(a_type, object))
    print(isinstance(b, object) and issubclass(b_type, object))
    print(isinstance(c, object) and issubclass(c_type, object))
    print(isinstance(d, object) and issubclass(d_type, object))


if __name__ == "__main__":
    main()
