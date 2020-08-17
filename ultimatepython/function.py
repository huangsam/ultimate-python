def add(x, y):
    """Add two objects together to produce a new object.

    This add function is a function, just like main is. Two
    differences between add and main are that:

    A) It accepts input parameters
    B) It returns a value
    """
    return x + y


def main():
    # The add function can be used for numbers as expected
    add_result_int = add(1, 2)
    print(f"Add(1, 2) = {add_result_int}")

    # The add function can be used for strings as well
    add_result_string = add('hello', ' world')
    print(f"Add('hello', ' world') = '{add_result_string}'")


if __name__ == '__main__':
    main()
