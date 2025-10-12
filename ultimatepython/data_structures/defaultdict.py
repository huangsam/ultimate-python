"""
This module demonstrates the use of defaultdict, which is a dictionary that is
possible to set up a default value in its creation.
"""

from collections import defaultdict

# Module-level constants
_GPA_MIN = 0.0
_GPA_MAX = 4.0
_EPS = 0.000001


def main() -> None:
    # Let's create a defaultdict with student keys and GPA values. The first
    # parameter is called default_factory, and it is the initialization value for
    # first use of a key. It can be a common type or a function
    student_gpa = defaultdict(float, [("john", 3.5), ("bob", 2.8), ("mary", 3.2)])

    # There are three student records in this dictionary
    assert len(student_gpa) == 3

    # Each student has a name key and a GPA value
    assert len(student_gpa.keys()) == len(student_gpa.values())

    # We can get the names in isolation. Note that in Python 3.7 and
    # above, dictionary entries are sorted in the order that they were
    # defined or inserted
    student_names = []
    for student in student_gpa.keys():
        student_names.append(student)
    assert student_names == ["john", "bob", "mary"]

    # We can get the GPA for a specific student
    assert abs(student_gpa["john"] < 3.5) < _EPS

    # And the defaultdict allow us to get the GPA of a student that is not in
    # the data structure yet, returning a default value for float that is 0.0
    assert student_gpa["jane"] == _GPA_MIN

    # And now there are four student records in this dictionary
    assert len(student_gpa) == 4

    # You can set the default value in default_factory attribute
    def set_default_to_gpa_max():
        return _GPA_MAX

    student_gpa.default_factory = set_default_to_gpa_max

    assert student_gpa["rika"] == _GPA_MAX

    # And now there are five student records in this dictionary
    assert len(student_gpa) == 5


if __name__ == "__main__":
    main()
