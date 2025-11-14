"""
Dictionary union operators allow you to merge dictionaries using
the | (union) and |= (in-place union) operators. These operators
provide a clean and intuitive syntax for combining dictionaries.

This feature was introduced in Python 3.9 through PEP 584. Before
this, you had to use methods like dict.update() or {**dict1, **dict2}
syntax to merge dictionaries.
"""


def main() -> None:
    # Traditional dictionary merging before Python 3.9
    # Method 1: Using dict.update() (modifies the original)
    dict1_old = {"a": 1, "b": 2}
    dict2_old = {"c": 3, "d": 4}
    dict1_old.update(dict2_old)
    assert dict1_old == {"a": 1, "b": 2, "c": 3, "d": 4}

    # Method 2: Using dictionary unpacking (creates a new dict)
    dict3_old = {"a": 1, "b": 2}
    dict4_old = {"c": 3, "d": 4}
    merged_old = {**dict3_old, **dict4_old}
    assert merged_old == {"a": 1, "b": 2, "c": 3, "d": 4}

    # With Python 3.9+, we can use the | operator for union
    # This creates a new dictionary without modifying the originals
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = dict1 | dict2
    assert merged == {"a": 1, "b": 2, "c": 3, "d": 4}

    # The original dictionaries remain unchanged
    assert dict1 == {"a": 1, "b": 2}
    assert dict2 == {"c": 3, "d": 4}

    # When there are overlapping keys, the right operand's values take precedence
    # This is the same behavior as dict.update() and {**d1, **d2}
    dict3 = {"a": 1, "b": 2, "c": 3}
    dict4 = {"b": 20, "c": 30, "d": 4}
    merged2 = dict3 | dict4
    # Keys 'b' and 'c' from dict4 override those from dict3
    assert merged2 == {"a": 1, "b": 20, "c": 30, "d": 4}

    # The order matters! Left operand is the base, right operand overwrites
    merged3 = dict4 | dict3
    # Now keys 'b' and 'c' from dict3 override those from dict4
    assert merged3 == {"b": 2, "c": 3, "d": 4, "a": 1}

    # The |= operator performs in-place union (augmented assignment)
    # This is equivalent to dict.update() but with cleaner syntax
    dict5 = {"a": 1, "b": 2}
    dict6 = {"c": 3, "d": 4}
    dict5 |= dict6
    # dict5 is modified in place
    assert dict5 == {"a": 1, "b": 2, "c": 3, "d": 4}
    # dict6 remains unchanged
    assert dict6 == {"c": 3, "d": 4}

    # The |= operator also handles overlapping keys
    dict7 = {"a": 1, "b": 2, "c": 3}
    dict8 = {"b": 20, "d": 4}
    dict7 |= dict8
    # 'b' from dict8 overwrites 'b' in dict7
    assert dict7 == {"a": 1, "b": 20, "c": 3, "d": 4}

    # You can chain multiple | operations
    dict9 = {"a": 1}
    dict10 = {"b": 2}
    dict11 = {"c": 3}
    dict12 = {"d": 4}
    combined = dict9 | dict10 | dict11 | dict12
    assert combined == {"a": 1, "b": 2, "c": 3, "d": 4}

    # When chaining with overlapping keys, rightmost values win
    dict13 = {"a": 1, "x": 10}
    dict14 = {"b": 2, "x": 20}
    dict15 = {"c": 3, "x": 30}
    combined2 = dict13 | dict14 | dict15
    # 'x' ends up with value 30 from the rightmost dictionary
    assert combined2 == {"a": 1, "b": 2, "c": 3, "x": 30}

    # The union operator works with empty dictionaries
    empty: dict[str, int] = {}
    dict16 = {"a": 1, "b": 2}
    assert empty | dict16 == {"a": 1, "b": 2}
    assert dict16 | empty == {"a": 1, "b": 2}
    assert empty | empty == {}

    # The union operator can be used with dict() constructor results
    dict17 = dict(a=1, b=2)
    dict18 = dict(c=3, d=4)
    merged4 = dict17 | dict18
    assert merged4 == {"a": 1, "b": 2, "c": 3, "d": 4}

    # You can mix different value types in merged dictionaries
    dict19 = {"name": "Alice", "age": 30}
    dict20 = {"city": "NYC", "scores": [85, 90, 95]}
    dict21 = {"active": True}
    person = dict19 | dict20 | dict21
    assert person == {"name": "Alice", "age": 30, "city": "NYC", "scores": [85, 90, 95], "active": True}

    # Practical use case: Configuration merging
    # Start with default configuration
    default_config = {"timeout": 30, "retries": 3, "debug": False, "log_level": "INFO"}

    # User provides custom configuration (partial)
    user_config = {"timeout": 60, "debug": True}

    # Merge configurations, user settings override defaults
    final_config = default_config | user_config
    assert final_config == {
        "timeout": 60,  # Overridden by user
        "retries": 3,  # From default
        "debug": True,  # Overridden by user
        "log_level": "INFO",  # From default
    }

    # Practical use case: Building objects incrementally
    # Start with base attributes
    base = {"id": 1, "type": "user"}

    # Add authentication info
    with_auth = base | {"username": "john", "email": "john@example.com"}

    # Add profile info
    with_profile = with_auth | {"bio": "Developer", "location": "USA"}

    assert with_profile == {"id": 1, "type": "user", "username": "john", "email": "john@example.com", "bio": "Developer", "location": "USA"}

    # Practical use case: Updating records with |=
    user_record = {"id": 100, "name": "Jane", "status": "active", "login_count": 5}

    # Apply update from an external source
    update = {"status": "inactive", "login_count": 6, "last_login": "2024-01-15"}
    user_record |= update

    assert user_record == {"id": 100, "name": "Jane", "status": "inactive", "login_count": 6, "last_login": "2024-01-15"}

    # The union operators only work with dictionaries
    # Attempting to use them with non-dict types raises TypeError
    dict22 = {"a": 1}
    error_raised = False
    try:
        # This will fail because list is not a dict
        dict22 | [("b", 2)]  # type: ignore [operator]
    except TypeError:
        error_raised = True
    assert error_raised is True

    # However, you can use dict() to convert compatible types first
    dict23 = {"a": 1}
    dict24 = dict([("b", 2), ("c", 3)])  # Convert list of tuples to dict
    merged5 = dict23 | dict24
    assert merged5 == {"a": 1, "b": 2, "c": 3}

    # Comparison with the older approaches shows the clarity improvement:

    # OLD: Using update() - modifies original, no expression result
    old1 = {"a": 1}
    old1.update({"b": 2})
    assert old1 == {"a": 1, "b": 2}

    # OLD: Using unpacking - verbose for multiple merges
    old2 = {**{"a": 1}, **{"b": 2}, **{"c": 3}}
    assert old2 == {"a": 1, "b": 2, "c": 3}

    # NEW: Using union operator - clean and chainable
    new1 = {"a": 1} | {"b": 2} | {"c": 3}
    assert new1 == {"a": 1, "b": 2, "c": 3}


if __name__ == "__main__":
    main()
