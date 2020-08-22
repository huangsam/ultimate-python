from ultimatepython.classes.abstract_class import Employee, Engineer, Manager


class EmployeeIterator:
    """Employee iterator."""

    def __init__(self, employee):
        self.employees_to_visit = [employee]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.employees_to_visit:
            raise StopIteration
        employee = self.employees_to_visit.pop()
        if isinstance(employee, Engineer):
            return employee
        if isinstance(employee, Manager):
            for report in employee.direct_reports:
                self.employees_to_visit.append(report)
            return employee
        raise StopIteration


def main():
    manager = Manager("Max Doe", "Engineering Manager", [
        Engineer("John Doe", "Software Engineer", "Android"),
        Engineer("Jane Doe", "Software Engineer", "iOS")
    ])
    employees = [emp for emp in EmployeeIterator(manager)]
    assert len(employees) == 3
    assert all(isinstance(emp, Employee) for emp in employees)
    assert any(isinstance(emp, Engineer) for emp in employees)
    assert any(isinstance(emp, Manager) for emp in employees)
    print(employees)


if __name__ == '__main__':
    main()
