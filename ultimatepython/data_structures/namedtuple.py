"""
This module demonstrates the use of named tuples, which are a data structure
with named fields, similar to a class but lightweight and immutable. Named
tuples are created using the namedtuple function from the collections module.
"""

from collections import namedtuple

def main():
    Point = namedtuple('Point', ['x', 'y'])

    # Create instances of the named tuple
    point1 = Point(x=1, y=2)
    point2 = Point(x=3, y=4)

    # Accessing fields using dot notation
    assert point1.x == 1
    assert point1.y == 2
    assert point2.x == 3
    assert point2.y == 4

    # Named tuples are immutable
    try:
        point1.x = 5  # Attempt to change the 'x' field of point1 (raises an error)
    except AttributeError:
        pass

    # Named tuples support tuple operations
    assert point1[0] + point2[0] == 4  # Access elements like a tuple and perform addition

    # Converting named tuples to dictionaries and vice versa
    point_dict = point1._asdict()  # Convert point1 to a dictionary
    assert point_dict == {'x': 1, 'y': 2}

    point3 = Point._make({'x': 10, 'y': 20})  # Create a new Point from a dictionary
    assert point3.x == 10
    assert point3.y == 20

    # Additional methods and attributes
    assert Point._fields == ('x', 'y')  # Access field names as a tuple
    point4 = point1._replace(x=5)  # Create a new Point with a field value changed
    assert point4.x == 5
    assert point4.y == 2

if __name__ == "__main":
    main()
