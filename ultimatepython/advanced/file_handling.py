"""File handling is a fundamental concept in Python that involves
opening, reading, writing, and appending to files. This module
demonstrates the basics of file handling in Python.

Python provides various ways to work with files. We can use the
builtin 'open' function to open files in different modes like
reading ('r'), writing ('w'), and appending ('a').In binary mode by adding 'b' to these modes. 

In CSV files, Python offers specialized libraries such as 'csv' for efficient handling. CSV (Comma-Separated Values) files

'a+' (Append and Read), 
'r+' (Read and Write), 
'w+' (Write and Read). These modes provide file manipulation by combining reading and writing capabilities."""

import os
import csv

_TARGET_FILE = "sample.txt"
_CSV_FILE = "data.csv"

def read_file(filename):
    """Read content from an existing file using 'r' mode."""
    with open(filename, "r") as file:
        content = file.read()
        return content

def write_file(filename, content):
    """Write content to a new file using 'w' mode."""
    with open(filename, "w") as file:
        file.write(content)
    return f"Content written to '{filename}'."

def append_file(filename, content):
    """Append content to an existing file using 'a' mode."""
    with open(filename, "a") as file:
        file.write(content)
    return f"Content appended to '{filename}'."

def read_and_write_file(filename, content):
    """Read and write content to an existing file using 'r+' mode."""
    with open(filename, "r+") as file:
        existing_content = file.read()
        file.seek(0)
        file.write(content + existing_content)
    return f"Content read and written to '{filename}' using 'r+' mode."

def write_and_read_file(filename, content):
    """Write and read content to a new file using 'w+' mode."""
    with open(filename, "w+") as file:
        file.write(content)
        file.seek(0)
        new_content = file.read()
    return f"Content written and read from '{filename}' using 'w+' mode."

def append_and_read_file(filename, content):
    """Append and read content from an existing file using 'a+' mode."""
    with open(filename, "a+") as file:
        file.write(content)
        file.seek(0)
        updated_content = file.read()
    return f"Content appended and read from '{filename}' using 'a+' mode."

def read_csv(filename):
    """Read data from an existing CSV file."""
    data = []
    with open(filename, "r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def write_csv(filename, data):
    """Write data to a new CSV file."""
    with open(filename, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
    return f"Data written to '{filename}'."

def main():
    result = write_file(_TARGET_FILE, "This is a test.")
    assert result == f"Content written to '{_TARGET_FILE}'."

    content = read_file(_TARGET_FILE)
    assert content == "This is a test."

    append_result = append_file(_TARGET_FILE, "\nThis is an appended line.")
    assert append_result == f"Content appended to '{_TARGET_FILE}'."

    content = read_file(_TARGET_FILE)
    assert content == "This is a test.\nThis is an appended line."

    read_write_result = read_and_write_file(_TARGET_FILE, "New content added using 'r+' mode.")
    assert read_write_result == f"Content read and written to '{_TARGET_FILE}' using 'r+' mode."

    write_read_result = write_and_read_file("new_file.txt", "Testing 'w+' mode.")
    assert write_read_result == "Content written and read from 'new_file.txt' using 'w+' mode."

    append_read_result = append_and_read_file(_TARGET_FILE, "Updated content using 'a+' mode.")
    assert append_read_result == f"Content appended and read from '{_TARGET_FILE}' using 'a+' mode."

    # Reading data from an existing CSV file
    data = read_csv(_CSV_FILE)
    assert data == [['Name', 'Age'], ['Alice', '30'], ['Bob', '25'], ['Charlie', '35']]

    # Writing data to a new CSV file
    new_data = [["Name", "Age"], ["Eve", "28"]]
    write_result = write_csv("new_data.csv", new_data)
    assert write_result == "Data written to 'new_data.csv'."

if __name__ == "__main__":
    main()
