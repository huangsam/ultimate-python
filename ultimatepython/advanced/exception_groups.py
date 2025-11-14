"""
Exception Groups allow you to raise and handle multiple exceptions
simultaneously. This is particularly useful for concurrent code where
multiple operations can fail independently.

Exception Groups were introduced in Python 3.11 through PEP 654. They use
the ExceptionGroup class and the new except* syntax for handling multiple
exception types from a group.
"""


def raising_exception_groups():
    """Demonstrate how to raise exception groups.

    ExceptionGroup is a built-in exception type that contains multiple
    exceptions. You create it with a message and a sequence of exceptions.
    """
    # Create a simple exception group with multiple exceptions
    exceptions = [
        ValueError("Invalid value"),
        TypeError("Wrong type"),
        KeyError("Missing key")
    ]

    try:
        # Raise an ExceptionGroup containing multiple exceptions
        raise ExceptionGroup("Multiple errors occurred", exceptions)
    except ExceptionGroup as eg:
        # We can access the exceptions in the group
        assert len(eg.exceptions) == 3
        assert isinstance(eg.exceptions[0], ValueError)
        assert isinstance(eg.exceptions[1], TypeError)
        assert isinstance(eg.exceptions[2], KeyError)
        return "Caught exception group"



def handling_with_except_star():
    """Demonstrate the except* syntax for handling exception groups.

    The except* syntax allows you to handle specific exception types
    from an ExceptionGroup while leaving others unhandled.
    """
    results = []

    try:
        exceptions = [
            ValueError("Invalid value 1"),
            ValueError("Invalid value 2"),
            TypeError("Wrong type 1")
        ]
        raise ExceptionGroup("Processing errors", exceptions)
    except* ValueError as eg:
        # This catches all ValueError instances from the group
        # Note: eg is still an ExceptionGroup, but only containing ValueErrors
        assert len(eg.exceptions) == 2
        results.append("Caught ValueErrors")
    except* TypeError as eg:
        # This catches all TypeError instances from the group
        assert len(eg.exceptions) == 1
        results.append("Caught TypeError")

    return results


def handling_multiple_types():
    """Handle different exception types from a group separately.

    You can have multiple except* blocks to handle different
    exception types independently.
    """
    results = []

    try:
        exceptions = [
            ValueError("Bad value"),
            TypeError("Bad type"),
            RuntimeError("Runtime issue"),
            ValueError("Another bad value")
        ]
        raise ExceptionGroup("Various errors", exceptions)
    except* ValueError as eg:
        # Handles all ValueErrors (there are 2)
        results.append(f"ValueError count: {len(eg.exceptions)}")
    except* TypeError as eg:
        # Handles all TypeErrors (there is 1)
        results.append(f"TypeError count: {len(eg.exceptions)}")
    except* RuntimeError as eg:
        # Handles all RuntimeErrors (there is 1)
        results.append(f"RuntimeError count: {len(eg.exceptions)}")

    return results


def nested_exception_groups():
    """Exception groups can be nested.

    You can have an ExceptionGroup that contains other ExceptionGroups.
    Note: nested ExceptionGroups are treated as single exceptions themselves
    unless you explicitly unwrap them.
    """
    # Create a flat exception group with mixed exception types
    exceptions = [
        ValueError("Value error 1"),
        ValueError("Value error 2"),
        TypeError("Type error 1"),
        RuntimeError("Runtime error")
    ]

    eg = ExceptionGroup("Multiple errors", exceptions)

    results = []

    try:
        raise eg
    except* ValueError as eg:
        # Catches all ValueErrors from the group
        results.append(f"Caught {len(eg.exceptions)} ValueErrors")
    except* TypeError as eg:
        results.append(f"Caught {len(eg.exceptions)} TypeErrors")
    except* RuntimeError as eg:
        results.append(f"Caught {len(eg.exceptions)} RuntimeErrors")

    return results


def partial_handling():
    """Demonstrate partial handling of exception groups.

    If you don't handle all exceptions in a group, the unhandled ones
    are re-raised as a new ExceptionGroup.
    """
    results = []

    try:
        try:
            exceptions = [
                ValueError("Value error"),
                TypeError("Type error"),
                KeyError("Key error")
            ]
            raise ExceptionGroup("Mixed errors", exceptions)
        except* ValueError as eg:
            # Only handle ValueError, leaving TypeError and KeyError
            results.append("Handled ValueError")
            # The other exceptions are automatically re-raised

    except ExceptionGroup as eg:
        # The re-raised group contains only the unhandled exceptions
        assert len(eg.exceptions) == 2
        assert isinstance(eg.exceptions[0], TypeError)
        assert isinstance(eg.exceptions[1], KeyError)
        results.append("Caught remaining exceptions")

    return results


def filtering_exceptions():
    """Filter and process exceptions from a group.

    The subgroup() method allows you to filter exceptions by type.
    """
    exceptions = [
        ValueError("Value 1"),
        TypeError("Type 1"),
        ValueError("Value 2"),
        RuntimeError("Runtime 1")
    ]

    eg = ExceptionGroup("All errors", exceptions)

    # Get a subgroup containing only ValueErrors
    value_errors = eg.subgroup(ValueError)
    assert value_errors is not None
    assert len(value_errors.exceptions) == 2

    # Get a subgroup containing only TypeErrors
    type_errors = eg.subgroup(TypeError)
    assert type_errors is not None
    assert len(type_errors.exceptions) == 1

    # If no matching exceptions, subgroup returns None
    key_errors = eg.subgroup(KeyError)
    assert key_errors is None

    return "Filtering successful"


def practical_concurrent_example():
    """A practical example simulating concurrent operations.

    This demonstrates a common use case: running multiple tasks
    where each can fail independently.
    """
    def process_user(user_id):
        """Simulate processing a user."""
        if user_id == 1:
            raise ValueError(f"Invalid user ID: {user_id}")
        elif user_id == 3:
            raise ConnectionError(f"Cannot connect for user: {user_id}")
        return f"Processed user {user_id}"

    user_ids = [1, 2, 3, 4]
    errors = []
    successes = []

    # Simulate processing multiple users
    for user_id in user_ids:
        try:
            result = process_user(user_id)
            successes.append(result)
        except Exception as e:
            errors.append(e)

    # If there were errors, raise them all together
    results = {"successes": len(successes), "errors": 0}

    if errors:
        try:
            raise ExceptionGroup("User processing errors", errors)
        except* ValueError as eg:
            results["errors"] += len(eg.exceptions)
        except* ConnectionError as eg:
            results["errors"] += len(eg.exceptions)

    return results


def exception_group_with_notes():
    """Exception groups work with exception notes (also new in Python 3.11).

    You can add contextual information to exceptions using add_note().
    """
    results = []

    try:
        exc1 = ValueError("Invalid input")
        exc1.add_note("Occurred in data validation")
        exc1.add_note("User input was: 'abc123'")

        exc2 = TypeError("Wrong type provided")
        exc2.add_note("Expected int, got str")

        raise ExceptionGroup("Processing failed", [exc1, exc2])

    except* ValueError as eg:
        # The notes are preserved in the exception
        exception = eg.exceptions[0]
        assert hasattr(exception, "__notes__")
        results.append("ValueError with notes caught")

    except* TypeError as eg:
        exception = eg.exceptions[0]
        assert hasattr(exception, "__notes__")
        results.append("TypeError with notes caught")

    return results


def main() -> None:
    # Test basic exception group raising and catching
    result1 = raising_exception_groups()
    assert result1 == "Caught exception group"

    # Test except* syntax
    result2 = handling_with_except_star()
    assert result2 == ["Caught ValueErrors", "Caught TypeError"]

    # Test handling multiple exception types
    result3 = handling_multiple_types()
    assert "ValueError count: 2" in result3
    assert "TypeError count: 1" in result3
    assert "RuntimeError count: 1" in result3

    # Test nested exception groups
    result4 = nested_exception_groups()
    assert len(result4) == 3
    assert "Caught 2 ValueErrors" in result4
    assert "Caught 1 TypeErrors" in result4
    assert "Caught 1 RuntimeErrors" in result4

    # Test partial handling
    result5 = partial_handling()
    assert result5 == ["Handled ValueError", "Caught remaining exceptions"]

    # Test filtering exceptions
    result6 = filtering_exceptions()
    assert result6 == "Filtering successful"

    # Test practical concurrent example
    result7 = practical_concurrent_example()
    assert result7["successes"] == 2  # Users 2 and 4 processed successfully
    assert result7["errors"] == 2  # Users 1 and 3 had errors

    # Test exception groups with notes
    result8 = exception_group_with_notes()
    assert len(result8) == 2

    # You can also split exception groups programmatically
    def split_by_type(eg):
        """Split an exception group into separate groups by type."""
        value_errors = eg.subgroup(ValueError)
        type_errors = eg.subgroup(TypeError)
        return value_errors, type_errors

    exceptions = [
        ValueError("Value 1"),
        TypeError("Type 1"),
        ValueError("Value 2")
    ]
    eg = ExceptionGroup("Mixed", exceptions)
    values, types = split_by_type(eg)

    assert values is not None and len(values.exceptions) == 2
    assert types is not None and len(types.exceptions) == 1

    # The derive() method creates a new ExceptionGroup with the same message
    new_eg = eg.derive([RuntimeError("New error")])
    assert new_eg.message == eg.message
    assert len(new_eg.exceptions) == 1
    assert isinstance(new_eg.exceptions[0], RuntimeError)

    # Exception groups are particularly valuable in async code
    # where multiple coroutines can fail simultaneously
    def simulate_async_failures():
        """Simulate collecting errors from multiple async operations."""
        # In real async code, you might use asyncio.gather with return_exceptions=True
        task_errors = [
            TimeoutError("Task 1 timed out"),
            ValueError("Task 2 invalid input"),
            ConnectionError("Task 3 connection failed")
        ]

        results = {"timeout": 0, "value": 0, "connection": 0}

        try:
            raise ExceptionGroup("Async task failures", task_errors)
        except* TimeoutError:
            results["timeout"] += 1
        except* ValueError:
            results["value"] += 1
        except* ConnectionError:
            results["connection"] += 1

        return results

    async_results = simulate_async_failures()
    assert async_results["timeout"] == 1
    assert async_results["value"] == 1
    assert async_results["connection"] == 1

    # Traditional exception handling vs exception groups:
    # Traditional: You can only catch one exception at a time
    # Exception groups: You can catch and handle multiple exceptions simultaneously
    # This is crucial for modern concurrent and parallel programming patterns


if __name__ == "__main__":
    main()
