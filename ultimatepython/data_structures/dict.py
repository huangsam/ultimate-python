"""
Dictionaries are a mapping of keys to values. This module shows how to
access, modify, remove and extend key-value pairs with this data
structure.
"""

# Module-level constants
_GPA_MIN = 0.0
_GPA_MAX = 4.0


def main():
    # Let's create a dictionary with student keys and GPA values
    student_gpa = {"john": 3.5,
                   "jane": _GPA_MAX,
                   "bob": 2.8,
                   "mary": 3.2}

    # There are four student records in this dictionary
    assert len(student_gpa) == 4

    # Each student has a name key and a GPA value
    assert len(student_gpa.keys()) == len(student_gpa.values())

    # We can get the names in isolation. Note that in Python 3.7 and
    # above, dictionary entries are sorted in the order that they were
    # defined or inserted
    student_names = []
    for student in student_gpa.keys():
        student_names.append(student)
    assert student_names == ["john", "jane", "bob", "mary"]

    # We can check that `student_gpa` has the names that were stored
    # in `student_names` from the loop above
    for student in student_names:
        assert student in student_gpa

    # We can get the GPAs in isolation
    gpa_values = []
    for gpa in student_gpa.values():
        gpa_values.append(gpa)
    assert gpa_values == [3.5, _GPA_MAX, 2.8, 3.2]

    # We can get the GPA for a specific student
    assert student_gpa["john"] == 3.5

    # In cases where the key may not exists inside the dict, it is possible to
    # check using `in`
    is_bob_in_dict = "bob" in student_gpa
    assert is_bob_in_dict is True

    is_alice_in_dict = "alice" in student_gpa
    assert is_alice_in_dict is False

    # Or if you are trying to retrieve a value that may not exsits inside the
    # dict, you can use `get` that allows you to return a default value in case
    # the checked key is not in the dict
    gpa_jane = student_gpa.get("jane", 0)
    assert gpa_jane == _GPA_MAX

    gpa_alice = student_gpa.get("alice", 0)
    assert gpa_alice == 0

    # We can update the GPA for a specific student
    student_gpa["john"] = _GPA_MAX

    # Or update the GPA for multiple students
    student_gpa.update(bob=_GPA_MIN, mary=_GPA_MIN)

    # We can access the student and GPA simultaneously
    gpa_binary = []
    for student, gpa in student_gpa.items():
        assert student_gpa[student] == gpa
        gpa_binary.append(gpa)
    assert gpa_binary == [_GPA_MAX, _GPA_MAX, _GPA_MIN, _GPA_MIN]

    # Let's remove all the students
    for student in student_names:
        student_gpa.pop(student)
    assert len(student_gpa) == 0

    # Let's add all the students back in
    for student, gpa in zip(student_names, gpa_binary):
        student_gpa[student] = gpa
    assert len(student_gpa) == len(student_names)


if __name__ == "__main__":
    main()
