def main():
    # Here are the main literal types to be aware of
    a = 1
    b = 2.0
    c = True
    d = "hello"

    # Notice that each type is a 'class'. Each variable
    # refers to an 'instance' of the class they belong
    # to. This leads to an important point: everything
    # is an object in Python
    print(a, type(a))  # <class 'int'>
    print(b, type(b))  # <class 'float'>
    print(c, type(c))  # <class 'bool'>
    print(d, type(d))  # <class 'str'>


if __name__ == "__main__":
    main()
