def main():
    # Let's create a dictionary with student keys and GPA values
    student_gpa = {"john": 3.5,
                   "jane": 4.0,
                   "bob": 2.8,
                   "mary": 3.2}

    # There are four student records in this dictionary
    assert len(student_gpa) == 4

    # Each student has a name key and a GPA value
    assert len(student_gpa.keys()) == len(student_gpa.values())

    # We can get the names in isolation
    for student in student_gpa.keys():
        assert len(student) > 2

    # We can get the GPAs in isolation
    for gpa in student_gpa.values():
        assert gpa > 2.0

    # We can get the GPA for a specific student
    assert student_gpa["john"] == 3.5

    # We can access the student and GPA simultaneously
    for student, gpa in student_gpa.items():
        assert student_gpa[student] == gpa


if __name__ == "__main__":
    main()
