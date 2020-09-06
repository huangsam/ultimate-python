def main():
    # Let's create a mapping of student name to GPA
    student_gpa = {"john": 3.5,
                   "jane": 4.0,
                   "bob": 2.8,
                   "mary": 3.2}

    # There are four students
    assert len(student_gpa) == 4

    # Each student has a name key and a GPA value
    assert len(student_gpa.keys()) == len(student_gpa.values())

    # You can get the names in isolation
    for student in student_gpa.keys():
        assert len(student) > 2

    # You can get the GPAs in isolation
    for gpa in student_gpa.values():
        assert gpa > 2.0

    # You can get the GPA for a specific student
    assert student_gpa["john"] == 3.5

    # You can access the student and GPA simultaneously
    for student, gpa in student_gpa.items():
        print(f"Student {student} has a {gpa} GPA")


if __name__ == "__main__":
    main()
