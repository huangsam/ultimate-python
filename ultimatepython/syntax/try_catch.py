"""
This module demonstrates the use of try-catch blocks (exception handling) in Python.
"""

def main():
    x = 1
    x_add_two = x + 2

    # Handling a division by zero error using a try-catch block
    ran_1 = False
    try:
        result = x_add_two / 0  # This will trigger an error
    except ZeroDivisionError:
        ran_1 = True  # This block runs if a 'ZeroDivisionError' occurs
    assert ran_1 is True  # This checks if 'ran_1' is True

    # Handling a value conversion error (converting text to an integer)
    ran_2 = False
    try:
        result = int("text")  # This will trigger a 'ValueError'
    except ValueError:
        ran_2 = True  # This block runs if a 'ValueError' occurs
    assert ran_2 is True  # This checks if 'ran_2' is True

    # Handling an error, but no exception is raised
    try:
        result = 10 / 2  # This division doesn't raise an error
    except ZeroDivisionError:
        ran_3 = False  # This block is skipped
    else:
        ran_3 = True  # This block runs if no exception occurs
    assert ran_3 is True  # This checks if 'ran_3' is True

    # Handling different types of errors with multiple except blocks
    try:
        result = x_add_two / 0  # This will trigger a 'ZeroDivisionError'
    except ValueError:
        ran_4 = False  # This block is skipped
    except ZeroDivisionError:
        ran_4 = True  # This block runs if a 'ZeroDivisionError' occurs
    assert ran_4 is True  # This checks if 'ran_4' is True

    # Handling an error and extracting its error message
    ran_5 = False
    try:
        result = int("text")  # This will trigger a 'ValueError'
    except ValueError as e:
        ran_5 = True
        error_message = str(e)  # Get the error message
    assert ran_5 is True  # This checks if 'ran_5' is True

if __name__ == "__main__":
    main()
