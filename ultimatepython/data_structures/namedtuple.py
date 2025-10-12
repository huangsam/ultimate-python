"""
This module demonstrates the use of named tuples, which are a data structure
with named fields, similar to a class but lightweight and immutable. Named
tuples are created using the namedtuple function from the collections module.
"""

from collections import namedtuple


def main():
    # Named Tuple Attributes:
    # - namedtuple: Callable from collections to define a named tuple
    # - Point: A named tuple type with fields "x" and "y"
    Point = namedtuple("Point", ["x", "y"])

    # Named Tuple Fields:
    # - x and y: Fields of the named tuple Point representing coordinates
    # - point1 and point2: Instances of the Point named tuple
    point1 = Point(x=1, y=2)
    point2 = Point(x=3, y=4)
    assert isinstance(point1, Point) is True
    assert isinstance(point2, Point) is True

    # Named Tuple Operations:
    # - Accessing fields using dot notation
    # - Named tuples are immutable
    # - Named tuples support tuple operations
    # - Converting named tuples to dictionaries and vice versa
    # - Additional methods and attributes
    assert point1.x == 1
    assert point1.y == 2
    assert point2.x == 3
    assert point2.y == 4

    # Attempt to change the "x" field of point1 (raises an error)
    access_immutable_error = False
    try:
        point1.x = 5
    except AttributeError:
        access_immutable_error = True
    assert access_immutable_error is True

    # One can access Point data by indexes
    assert point1[0] + point2[0] == 4
    assert point1[0] + point2[1] == 5
    assert point1[1] + point2[0] == 5
    assert point1[1] + point2[1] == 6

    point_dict = point1._asdict()
    assert point_dict == {"x": 1, "y": 2}

    # It is possible to initialize a Point without explicit parameters
    point3 = Point(10, 20)
    assert point3.x == 10
    assert point3.y == 20
    assert Point._fields == ("x", "y")

    # It is also possible to create a new point out of an existing one
    point4 = point1._replace(x=5)
    assert point4.x == 5
    assert point4.y == 2

    # Note that point4 is not the same as point1
    assert id(point4) != id(point1)


if __name__ == "__main__":
    main()
