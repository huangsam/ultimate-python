from inspect import isfunction, ismethod, signature


class Car:
    """Basic definition of a car.

    A car is a good entity to define a class with because it has state
    and methods associated with it. We begin with a simple mental model
    of what a car is. That way, we can start talking about core concepts
    that are associated with a class definition.
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
        """Drive car at a certain rate in MPH."""
        return f"{self} is driving at {rate_in_mph} MPH"


def main():
    # Create a car with the provided class constructor
    car = Car("Bumble", "Bee", 2000, 200000.0)

    # Formal representation is good for debugging issues
    assert repr(car) == "<Car make=Bumble model=Bee year=2000>"

    # Informal representation is good for user output
    assert str(car) == "Bumble Bee (2000)"

    # Call a method on the class constructor
    assert car.drive(75) == "Bumble Bee (2000) is driving at 75 MPH"

    # As a reminder: everything in Python is an object! And that applies
    # to classes in the most interesting way - because they're not only
    # subclasses of object - they are also instances of object. This
    # means that we can modify the `Car` class at runtime, just like any
    # other piece of data we define in Python
    assert issubclass(Car, object) and isinstance(Car, object)

    # To emphasize the idea that everything is an object, let's look at
    # the `drive` method in more detail
    driving = getattr(car, "drive")

    # The variable method is the same as the instance method
    assert driving == car.drive

    # The variable method is bound to the instance
    assert driving.__self__ == car

    # That is why `driving` is considered a method and not a function
    assert ismethod(driving) and not isfunction(driving)

    # And there is only one parameter for `driving` because `__self__`
    # binding is implicit
    driving_params = signature(driving).parameters
    assert len(driving_params) == 1
    assert "rate_in_mph" in driving_params


if __name__ == "__main__":
    main()
