from ultimatepython.classes.abstract_class import Employee, Engineer, Manager
from ultimatepython.classes.exception_class import IterationError


class EmployeeIterator:
    """Employee iterator.

    An iterator class is composed of three methods:

    - A constructor which defines data structures
    - An iterator returns the instance itself
    - A retriever which gets the next element
    """

    def __init__(self, employee):
        """Constructor logic."""
        self.employees_to_visit = [employee]
        self.employees_visited = set()

    def __iter__(self):
        """Iterator is self by convention."""
        return self

    def __next__(self):
        """Return the next employee available."""
        if not self.employees_to_visit:
            raise StopIteration
        employee = self.employees_to_visit.pop()
        if employee.name in self.employees_visited:
            raise IterationError("Cyclic loop detected")
        self.employees_visited.add(employee.name)
        if isinstance(employee, Engineer):
            return employee
        if isinstance(employee, Manager):
            for report in employee.direct_reports:
                self.employees_to_visit.append(report)
            return employee
        raise StopIteration


def employee_generator(top_employee):
    """Employee generator.

    It is essentially the same logic as above except constructed as a
    generator function. Notice that the generator code is in a single
    place, whereas the iterator code is in multiple places. Also notice
    that we are using the `yield` keyword in the generator code.

    It is a matter of preference and context that we choose one approach
    over the other. If we want something simple, go with the generator.
    Otherwise, go with the iterator to fulfill more demanding requirements.
    In this case, examples of such requirements are tasks like encrypting
    the employee's username, running statistics on iterated employees or
    excluding the reports under a particular set of managers.
    """
    to_visit = [top_employee]
    visited = set()
    while len(to_visit) > 0:
        employee = to_visit.pop()
        if employee.name in visited:
            raise IterationError("Cyclic loop detected")
        visited.add(employee.name)
        if isinstance(employee, Engineer):
            yield employee
        elif isinstance(employee, Manager):
            for report in employee.direct_reports:
                to_visit.append(report)
            yield employee
        else:
            raise StopIteration


def main():
    # Manager with two direct reports
    manager = Manager("Max Doe", "Engineering Manager", [
        Engineer("John Doe", "Software Engineer", "Android"),
        Engineer("Jane Doe", "Software Engineer", "iOS")
    ])

    # We should provide the same three employees in the same order regardless
    # of whether we use the iterator class or the generator function
    employees = [emp for emp in EmployeeIterator(manager)]
    assert employees == [emp for emp in employee_generator(manager)]
    assert len(employees) == 3

    # Make sure that the employees are who we expect them to be
    assert all(isinstance(emp, Employee) for emp in employees)
    assert isinstance(employees[0], Manager)
    assert all(isinstance(emp, Engineer) for emp in employees[1:])
    print(employees)


if __name__ == "__main__":
    main()
