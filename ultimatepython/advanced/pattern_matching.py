"""
Structural pattern matching allows you to match complex data structures
against patterns and extract values in a clean, readable way. This feature
is similar to switch-case statements in other languages but much more powerful.

Pattern matching was introduced in Python 3.10 through PEP 634, PEP 635,
and PEP 636. It uses the 'match' and 'case' keywords.
"""


def classify_number(value):
    """Classify a number using pattern matching with literals.

    This demonstrates matching against specific literal values.
    """
    match value:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case _:
            # The underscore _ is a wildcard that matches anything
            return "other"


def classify_http_status(status):
    """Classify HTTP status codes using pattern matching.

    This shows how pattern matching can make code more readable
    than a series of if-elif-else statements.
    """
    match status:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"


def process_point(point):
    """Process a point tuple using pattern matching with sequences.

    This demonstrates pattern matching against tuple structures
    and extracting values from them.
    """
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            # Match any point on the y-axis, capture y coordinate
            return f"Y-axis at y={y}"
        case (x, 0):
            # Match any point on the x-axis, capture x coordinate
            return f"X-axis at x={x}"
        case (x, y):
            # Match any other point, capture both coordinates
            return f"Point at ({x}, {y})"
        case _:
            return "Not a valid 2D point"


def analyze_sequence(data):
    """Analyze sequences using pattern matching.

    This shows how to match lists with specific structures
    and extract elements.
    """
    match data:
        case []:
            return "Empty list"
        case [x]:
            # Match a list with exactly one element
            return f"Single element: {x}"
        case [x, y]:
            # Match a list with exactly two elements
            return f"Pair: {x}, {y}"
        case [first, *rest]:
            # Match a list with at least one element
            # The *rest captures remaining elements
            return f"First: {first}, Rest: {rest}"
        case _:
            return "Not a list"  # pragma: no cover


def process_command(command):
    """Process commands using pattern matching with guards.

    Guards are if conditions that provide additional filtering
    after a pattern match.
    """
    match command:
        case ["quit"]:
            return "Quitting"
        case ["go", direction] if direction in ["north", "south", "east", "west"]:
            # Guard clause: only match if direction is valid
            return f"Going {direction}"
        case ["go", direction]:
            # This matches any direction that failed the guard above
            return f"Invalid direction: {direction}"
        case ["take", item]:
            return f"Taking {item}"
        case ["take", item, quantity] if quantity > 0:
            return f"Taking {quantity} {item}"
        case ["take", item, quantity]:
            return f"Invalid quantity: {quantity}"
        case _:
            return "Unknown command"


class Point:
    """A simple 2D point class for pattern matching examples."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    """A circle with center and radius for pattern matching examples."""

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def describe_shape(shape):
    """Describe shapes using pattern matching with class patterns.

    This demonstrates matching against class instances and
    extracting their attributes.
    """
    match shape:
        case Point(x=0, y=0):
            # Match a Point at the origin
            return "Point at origin"
        case Point(x=0, y=y):
            # Match a Point on the y-axis
            return f"Point on Y-axis at {y}"
        case Point(x=x, y=0):
            # Match a Point on the x-axis
            return f"Point on X-axis at {x}"
        case Point(x=x, y=y) if x == y:
            # Match a Point on the diagonal line y=x
            return f"Point on diagonal at ({x}, {y})"
        case Point(x=x, y=y):
            # Match any other Point
            return f"Point at ({x}, {y})"
        case Circle(center=Point(x=0, y=0), radius=r):
            # Match a Circle centered at origin
            return f"Circle at origin with radius {r}"
        case Circle(center=Point(x=x, y=y), radius=r):
            # Match any other Circle
            return f"Circle at ({x}, {y}) with radius {r}"
        case _:
            return "Unknown shape"


def process_json_data(data):
    """Process JSON-like dictionary data with pattern matching.

    This shows how to match against dictionary structures.
    """
    match data:
        case {"type": "user", "name": name, "age": age}:
            return f"User {name} is {age} years old"
        case {"type": "user", "name": name}:
            # Match user without age
            return f"User {name} with unknown age"
        case {"type": "product", "name": name, "price": price} if price > 0:
            return f"Product {name} costs ${price}"
        case {"type": "product", "name": name, "price": price}:
            return f"Product {name} has invalid price: {price}"
        case {"type": type_name}:
            # Match any dict with a type key
            return f"Unknown type: {type_name}"
        case _:
            return "Invalid data"


def main() -> None:
    # Test literal pattern matching
    assert classify_number(0) == "zero"
    assert classify_number(1) == "one"
    assert classify_number(2) == "two"
    assert classify_number(5) == "other"
    assert classify_number(100) == "other"

    # Test HTTP status classification
    assert classify_http_status(200) == "OK"
    assert classify_http_status(404) == "Not Found"
    assert classify_http_status(999) == "Unknown Status"
    assert classify_http_status(201) == "Created"
    assert classify_http_status(400) == "Bad Request"
    assert classify_http_status(401) == "Unauthorized"
    assert classify_http_status(500) == "Internal Server Error"

    # Test sequence pattern matching with tuples
    assert process_point((0, 0)) == "Origin"
    assert process_point((0, 5)) == "Y-axis at y=5"
    assert process_point((3, 0)) == "X-axis at x=3"
    assert process_point((4, 7)) == "Point at (4, 7)"

    # Test sequence pattern matching with lists
    assert analyze_sequence([]) == "Empty list"
    assert analyze_sequence([42]) == "Single element: 42"
    assert analyze_sequence([1, 2]) == "Pair: 1, 2"
    assert analyze_sequence([1, 2, 3, 4]) == "First: 1, Rest: [2, 3, 4]"
    assert analyze_sequence("not a list") == "Not a list"

    # Test pattern matching with guards
    assert process_command(["quit"]) == "Quitting"
    assert process_command(["go", "north"]) == "Going north"
    assert process_command(["go", "west"]) == "Going west"
    assert process_command(["go", "up"]) == "Invalid direction: up"
    assert process_command(["take", "key"]) == "Taking key"
    assert process_command(["take", "coin", 5]) == "Taking 5 coin"
    assert process_command(["take", "coin", 0]) == "Invalid quantity: 0"
    assert process_command(["take", "coin", -1]) == "Invalid quantity: -1"
    assert process_command(["jump"]) == "Unknown command"

    # Test class pattern matching
    p1 = Point(0, 0)
    assert describe_shape(p1) == "Point at origin"

    p2 = Point(0, 5)
    assert describe_shape(p2) == "Point on Y-axis at 5"

    p3 = Point(3, 0)
    assert describe_shape(p3) == "Point on X-axis at 3"

    p4 = Point(5, 5)
    assert describe_shape(p4) == "Point on diagonal at (5, 5)"

    p5 = Point(3, 7)
    assert describe_shape(p5) == "Point at (3, 7)"

    c1 = Circle(Point(0, 0), 10)
    assert describe_shape(c1) == "Circle at origin with radius 10"

    c2 = Circle(Point(5, 5), 3)
    assert describe_shape(c2) == "Circle at (5, 5) with radius 3"

    # Test unknown shape
    assert describe_shape("unknown") == "Unknown shape"

    # Test dictionary pattern matching
    user1 = {"type": "user", "name": "Alice", "age": 30}
    assert process_json_data(user1) == "User Alice is 30 years old"

    user2 = {"type": "user", "name": "Bob"}
    assert process_json_data(user2) == "User Bob with unknown age"

    product1 = {"type": "product", "name": "Laptop", "price": 999}
    assert process_json_data(product1) == "Product Laptop costs $999"

    product2 = {"type": "product", "name": "Free Sample", "price": 0}
    assert process_json_data(product2) == "Product Free Sample has invalid price: 0"

    unknown = {"type": "order"}
    assert process_json_data(unknown) == "Unknown type: order"

    invalid = {"data": "something"}
    assert process_json_data(invalid) == "Invalid data"

    # Pattern matching with OR patterns
    def check_value(val):
        match val:
            case 0 | 1 | 2:
                # Match any of these values
                return "small"
            case 3 | 4 | 5:
                return "medium"
            case _:
                return "large"

    assert check_value(0) == "small"
    assert check_value(2) == "small"
    assert check_value(3) == "medium"
    assert check_value(10) == "large"

    # Pattern matching with AS patterns (walrus-like capture)
    def process_range(data):
        match data:
            case [x, y] as pair if x < y:
                # Capture the entire matched value with 'as'
                return f"Valid range: {pair}"
            case [x, y]:
                return f"Invalid range: [{x}, {y}]"
            case _:
                return "Not a pair"

    assert process_range([1, 5]) == "Valid range: [1, 5]"
    assert process_range([5, 1]) == "Invalid range: [5, 1]"
    assert process_range("not a pair") == "Not a pair"

    # Nested pattern matching
    def analyze_nested(data):
        match data:
            case [["pair", x, y], ["pair", a, b]]:
                # Match nested structure
                return f"Two pairs: ({x},{y}) and ({a},{b})"
            case [["single", val]]:
                return f"Single value: {val}"
            case _:
                return "Unknown structure"

    assert analyze_nested([["pair", 1, 2], ["pair", 3, 4]]) == "Two pairs: (1,2) and (3,4)"
    assert analyze_nested([["single", 42]]) == "Single value: 42"
    assert analyze_nested("invalid") == "Unknown structure"

    # Pattern matching is particularly useful for parsing and handling
    # structured data like API responses, configuration files, or
    # abstract syntax trees in compilers/interpreters


if __name__ == "__main__":
    main()
