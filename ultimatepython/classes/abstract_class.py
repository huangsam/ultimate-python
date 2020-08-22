from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract definition of an employee."""

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        return f"{self.name} ({self.title})"

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
    """Concrete definition of an engineer."""

    def __init__(self, name, title, skill):
        super().__init__(name, title)
        self.skill = skill

    def __repr__(self):
        return f"<Engineer name={self.name}>"

    def do_work(self):
        print(f"{self} is coding in {self.skill}")

    def join_meeting(self):
        print(f"{self} is joining a meeting on {self.skill}")

    def relax(self):
        print(f"{self} is relaxing by watching YouTube")

    def do_refactor(self):
        """Do the hard work of refactoring code, unlike managers."""
        print(f"{self} is refactoring work in {self.skill}")


class Manager(Employee):
    """Concrete definition of a manager."""

    def __init__(self, name, title, direct_reports):
        super().__init__(name, title)
        self.direct_reports = direct_reports

    def __repr__(self):
        return f"<Manager name={self.name}>"

    def do_work(self):
        print(f"{self} is meeting up with {self.direct_reports}")

    def join_meeting(self):
        print(f"{self} is starting a meeting with {self.direct_reports}")

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
        engineer.do_work()
        engineer.join_meeting()
        engineer.relax()
        engineer.do_refactor()

    # Declare manager with engineers as direct reports
    manager_max = Manager("Max Doe", "Engineering Manager", engineers)

    assert isinstance(manager_max, (Manager, Employee))
    assert not isinstance(manager_max, Engineer)
    manager_max.do_work()
    manager_max.join_meeting()
    manager_max.relax()
    manager_max.do_hire()


if __name__ == '__main__':
    main()
