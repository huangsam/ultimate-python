def main():
    student_gpa = {"john": 3.5,
                   "jane": 4.0,
                   "bob": 2.8,
                   "mary": 3.2}

    # You can access the value of a particular key
    assert student_gpa["john"] == 3.5

    # You can access the dictionary keys in isolation
    for student in student_gpa.keys():
        assert len(student) > 2

    # You can access the dictionary values in isolation
    for gpa in student_gpa.values():
        assert gpa > 2.0

    # You can access the dictionary keys and values simultaneously
    for student, gpa in student_gpa.items():
        print(f"Student {student} has a {gpa} GPA")


if __name__ == '__main__':
    main()
