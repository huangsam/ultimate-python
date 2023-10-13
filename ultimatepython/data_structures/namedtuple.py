"""
This module demonstrates the use of named tuples, which are a data structure
with named fields, similar to a class but lightweight and immutable. Named
tuples are created using the namedtuple function from the collections module.
"""

from collections import namedtuple

def main():
    # Named Tuple Attributes:
    # - namedtuple: A function from the collections module used to define a named tuple type.
    # - Point: A named tuple type with fields 'x' and 'y.
    Point = namedtuple('Point', ['x', 'y'])

    # Named Tuple Fields:
    # - x and y: Fields of the named tuple Point representing coordinates.
    # - point1 and point2: Instances of the Point named tuple.
    point1 = Point(x=1, y=2)
    point2 = Point(x=3, y=4)

    # Named Tuple Operations:
    # - Accessing fields using dot notation.
    # - Named tuples are immutable.
    # - Named tuples support tuple operations.
    # - Converting named tuples to dictionaries and vice versa.
    # - Additional methods and attributes.
    assert point1.x == 1
    assert point1.y == 2
    assert point2.x == 3
    assert point2.y == 4
    try:
        point1.x = 5  # Attempt to change the 'x' field of point1 (raises an error)
    except AttributeError:
        pass
    assert point1[0] + point2[0] == 4
    point_dict = point1._asdict()
    assert point_dict == {'x': 1, 'y': 2}
    point3 = Point._make({'x': 10, 'y': 20})
    assert point3.x == 10
    assert point3.y == 20
    assert Point._fields == ('x', 'y')
    point4 = point1._replace(x=5)
    assert point4.x == 5
    assert point4.y == 2

if __name__ == "__main":
    main()
