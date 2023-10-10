# Step 1: Import the namedtuple class from the collections module
from collections import namedtuple

# Step 2: Define a named tuple type
# The first argument is the typename, and the second argument is a space-separated list of field names as strings.
# In this example, we create a Point named tuple with fields x and y.
Point = namedtuple('Point', ['x', 'y'])

# Step 3: Create instances of the named tuple
# You can create instances of the named tuple like you would with a regular class.
# Here, we create two Point objects.
point1 = Point(x=1, y=2)
point2 = Point(x=3, y=4)

# Step 4: Accessing fields using dot notation
# You can access the fields of a named tuple using dot notation.
print("Point 1: x =", point1.x, ", y =", point1.y)
print("Point 2: x =", point2.x, ", y =", point2.y)

# Step 5: Named tuples are immutable
# Named tuples, like regular tuples, are immutable, meaning you can't change their values once set.
# point1.x = 5  # This will result in an error

# Step 6: Named tuples support tuple operations
# Named tuples support all the standard tuple operations, including indexing and iteration.
# You can use them in the same way as regular tuples.
print("Sum of x coordinates:", point1[0] + point2[0])

# Step 7: Converting named tuples to dictionaries and vice versa
# You can convert a named tuple to a dictionary using _asdict() method.
point_dict = point1._asdict()
print("Point 1 as a dictionary:", point_dict)

# You can also create a named tuple from a dictionary using the _make() method.
point3 = Point._make({'x': 10, 'y': 20})
print("Point 3: x =", point3.x, ", y =", point3.y)

# Step 8: Additional methods and attributes
# Named tuples provide some additional methods and attributes:
# - _fields: Returns a tuple of field names.
# - _replace(**kwargs): Creates a new named tuple with some fields replaced.
print("Field names:", Point._fields)
point4 = point1._replace(x=5)
print("Updated Point 1: x =", point4.x, ", y =", point4.y)

# OUTPUT:
# Point 1: x = 1 , y = 2
# Point 2: x = 3 , y = 4
# Sum of x coordinates: 4
# Point 1 as a dictionary: {'x': 1, 'y': 2}
# Point 3: x = 10 , y = 20
# Field names: ('x', 'y')
# Updated Point 1: x = 5 , y = 2
