from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract definition of an employee.

    The Employee class is abstract because it inherits the `ABC` class
    and has at least one `abstractmethod`. That means we cannot create
    an instance directly from its constructor.

    For more about abstract classes, click the link below:

    https://www.python.org/dev/peps/pep-3119/
    """

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        return f"{self.name} ({self.title})"

    def __repr__(self):
        return f"<{type(self).__name__} name={self.name}>"

    @abstractmethod
    def do_work(self):
        raise NotImplementedError

    @abstractmethod
    def join_meeting(self):
        raise NotImplementedError

    @abstractmethod
    def relax(self):
        raise NotImplementedError


class Engineer(Employee):
    """Concrete definition of an engineer.

    The Engineer class is concrete because it implements every
    `abstractmethod` that was not implemented above.

    Notice that we leverage the parent's constructor when creating
    this object. We also define `do_refactor` for an engineer, which
    is something that a manager prefers not to do.
    """

    def __init__(self, name, title, skill):
        super().__init__(name, title)
        self.skill = skill

    def do_work(self):
        print(f"{self} is coding in {self.skill}")

    def join_meeting(self):
        print(f"{self} is joining a meeting on {self.skill}")

    def relax(self):
        print(f"{self} is relaxing by watching YouTube")

    def do_refactor(self):
        """Do the hard work of refactoring code, unlike managers."""
        print(f"{self} is refactoring code")


class Manager(Employee):
    """Concrete definition of a manager.

    The Manager class is concrete for the same reasons as the Engineer
    class is concrete. Notice that a manager has direct reports and
    has the responsibility of hiring people on the team, unlike an
    engineer.
    """

    def __init__(self, name, title, direct_reports):
        super().__init__(name, title)
        self.direct_reports = direct_reports

    def do_work(self):
        print(f"{self} is meeting up with {self.direct_reports}")

    def join_meeting(self):
        print(f"{self} is joining a meeting with {self.direct_reports}")

    def relax(self):
        print(f"{self} is taking a trip to the Bahamas")

    def do_hire(self):
        """Do the hard work of hiring employees, unlike engineers."""
        print(f"{self} is hiring employees")


def main():
    # Declare two engineers
    engineer_john = Engineer("John Doe", "Software Engineer", "Android")
    engineer_jane = Engineer("Jane Doe", "Software Engineer", "iOS")

    engineers = [engineer_john, engineer_jane]
    for engineer in engineers:
        assert isinstance(engineer, (Engineer, Employee))
        assert not isinstance(engineer, Manager)
        print("Created", repr(engineer))

        engineer.do_work()
        engineer.join_meeting()
        engineer.relax()
        engineer.do_refactor()

    # Declare manager with engineers as direct reports
    manager_max = Manager("Max Doe", "Engineering Manager", engineers)

    assert isinstance(manager_max, (Manager, Employee))
    assert not isinstance(manager_max, Engineer)
    print("Created", repr(manager_max))

    manager_max.do_work()
    manager_max.join_meeting()
    manager_max.relax()
    manager_max.do_hire()


if __name__ == '__main__':
    main()
