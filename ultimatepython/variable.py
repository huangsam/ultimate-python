def main():
    # Here are the main literal types to be aware of
    a = 1
    b = 2.0
    c = True
    d = "hello"

    # Notice that each type is a 'class'. This leads
    # to an important point: in Python, everything
    # is an object
    print(a, type(a))  # <class 'int'>
    print(b, type(b))  # <class 'float'>
    print(c, type(c))  # <class 'bool'>
    print(d, type(d))  # <class 'str'>


if __name__ == "__main__":
    main()
