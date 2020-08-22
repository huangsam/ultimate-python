class Car:
    """Simple representation of a car.

    A car is a simple example to get started with defining a class because
    it has state and capabilities associated with it. We start with a
    simple mental model of what a car is, so that we can start with basic
    concepts associated with a class definition.
    """

    def __init__(self, make, model, year, miles):
        """Constructor logic."""
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles

    def __repr__(self):
        """Formal representation for developers."""
        return f"<Car make={self.make} model={self.model} year={self.year}>"

    def __str__(self):
        """Informal representation for users."""
        return f"{self.make} {self.model} ({self.year})"

    def drive(self, rate_in_mph):
        """Drive car at a certain rate."""
        print(f"{self} is driving at {rate_in_mph} MPH")


def main():
    # Create a car with the provided class constructor
    car = Car("Bumble", "Bee", 2000, 200000.0)

    # Formal and informal representations are not the same
    assert repr(car) != str(car)

    # Call a method on the class constructor
    car.drive(75)


if __name__ == "__main__":
    main()
