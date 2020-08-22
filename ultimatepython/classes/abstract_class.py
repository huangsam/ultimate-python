from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract representation of an employee."""

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
    """Concrete representation of an engineer."""

    def __init__(self, name, title, skill):
        super().__init__(name, title)
        self.skill = skill

    def __repr__(self):
        return f"<Engineer name={self.name}>"

    def do_work(self):
        print(f"{self} is doing {self.skill} work")

    def join_meeting(self):
        print(f"{self} is joining a meeting on {self.skill}")

    def relax(self):
        print(f"{self} is relaxing by watching YouTube")


class Manager(Employee):
    """Concrete representation of a manager."""

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


def main():
    engineer_john = Engineer("John Doe", "Software Engineer", "Android")
    engineer_jane = Engineer("Jane Doe", "Software Engineer", "iOS")

    engineers = [engineer_john, engineer_jane]
    for engineer in engineers:
        engineer.do_work()
        engineer.join_meeting()
        engineer.relax()

    manager_max = Manager("Max Doe", "Engineering Manager", engineers)
    manager_max.do_work()
    manager_max.join_meeting()
    manager_max.relax()


if __name__ == '__main__':
    main()
