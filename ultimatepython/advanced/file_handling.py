"""
File handling in Python allows you to work with files, such as creating, reading, writing, and appending to them.
This module demonstrates the basic file handling operations.
"""


def file_handling_basics():
    # Creating and Writing to a File
    # You can create and write to a new file using the 'open' function with the 'w' mode.
    with open("example.txt", "w") as file:
        file.write("Hello, this is a text file.\n")
        file.write("We can write multiple lines to it.\n")
        file.write("And then close it when we are done.\n")

    # Reading from a File
    # You can open an existing file for reading using the 'open' function with the 'r' mode.
    with open("example.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)

    # Appending to a File
    # You can open an existing file and append to it using the 'a' mode.
    with open("example.txt", "a") as file:
        file.write("Now we are appending more text to the file.\n")

    # Reading Specific Lines
    # You can also read specific lines from a file using a for loop.
    with open("example.txt", "r") as file:
        print("Specific Lines:")
        for i, line in enumerate(file, 1):
            if i in [2, 4]:
                print(line.strip())

    # Closing a File
    # It's important to close the file explicitly when you're done with it.
    # However, using a 'with' block as shown above will automatically close the file for you when the block exits.

    # Assertions
    # Now, let's use assert statements to check the results of our file handling operations.
    with open("example.txt", "r") as file:
        content = file.read()

    # Assert that the content of the file contains the expected text.
    assert "Hello, this is a text file." in content
    assert "Now we are appending more text to the file." in content


if __name__ == "__main__":
    file_handling_basics()
