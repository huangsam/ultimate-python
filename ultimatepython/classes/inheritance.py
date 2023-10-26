"""
Inheritance is a way to reuse code and data from a parent class. This
allow us to avoid repeating ourselves and to build upon existing
functionality. This module defines a basic vehicle class, creates a car
class that inherits from vehicle, then creates a truck class that
inherits from car and use it for demonstration purposes.
"""
from inspect import isfunction, ismethod


class Vehicle:
    """Basic definition of a vehicle.

    We begin with a simple mental model of what a vehicle is. It has
    a make, model, year, and miles. That way, we can start exploring
    the core concepts that are associated with a class definition.
    """

    def __init__(self, make, model, year, miles):
        """Construct a vehicle with make, model, year, and miles."""
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles

    def __repr__(self):
        """Return the formal representation of a vehicle."""
        return f"<Vehicle make={self.make} model={self.model} year={self.year}>"

    def __str__(self):
        """Return the informal representation of a vehicle."""
        return f"{self.make} {self.model} ({self.year})"

    def drive(self, rate_in_mph):
        """Drive a vehicle at a certain rate in MPH."""
        return f"{self} is driving at {rate_in_mph} MPH"


class Car(Vehicle):
    """Definition of a car.

    We inherit from the vehicle class to reuse the code and data that
    we have already defined. In addition, we add a new attribute called
    `wheels` to the car class. This is an example of extending the
    functionality of a parent class. In __init__, we call the parent
    constructor with the `super` function. This is a way to invoke the
    parent constructor without having to explicitly name the parent
    class. We also override the method `__repr__` to have a different
    output than the vehicle.
    """

    def __init__(self, make, model, year, miles):
        """Construct a car with make, model, year, miles, and wheels."""
        super().__init__(make, model, year, miles)
        self.wheels = 4

    def __repr__(self):
        """Return the formal representation of a car."""
        return f"<Car make={self.make} model={self.model} year={self.year} wheels={self.wheels}>"


class Truck(Vehicle):
    """Definition of a truck.

    We inherit from vehicle just like we did with the car class. In this case we
    will also override the method `drive` to have a different output than the
    car and the vehicle.
    """

    def __init__(self, make, model, year, miles):
        """Construct a truck with make, model, year, miles, and wheels."""
        super().__init__(make, model, year, miles)
        self.wheels = 6

    def __repr__(self):
        """Return the formal representation of a truck."""
        return f"<Truck make={self.make} model={self.model} year={self.year} wheels={self.wheels}>"

    def drive(self, rate_in_mph):
        """Drive a truck at a certain rate in MPH."""
        return f"{self} is driving a truck at {rate_in_mph} MPH"


def main():
    # Create a vehicle with the provided class constructor
    vehicle = Vehicle("Mistery Machine", "Van", 1969, 100000.0)

    # Formal representation
    assert repr(vehicle) == "<Vehicle make=Mistery Machine model=Van year=1969>"

    # Informal representation
    assert str(vehicle) == "Mistery Machine Van (1969)"

    # Call a method on the class constructor
    assert vehicle.drive(50) == "Mistery Machine Van (1969) is driving at 50 MPH"

    # Check the type of the method drive
    assert ismethod(vehicle.drive) and not isfunction(vehicle.drive)

    # Now we create a car with the provided class constructor
    car = Car("DeLorean", "DMC-12", 1982, 220000.0)

    # The informal representation is similar to the vehicle
    assert str(car) == "DeLorean DMC-12 (1982)"

    # But the formal representation is different because we included
    # the wheels attribute
    assert repr(car) == "<Car make=DeLorean model=DMC-12 year=1982 wheels=4>"

    # And we can check the type of the method drive like we did with
    # the vehicle
    assert ismethod(car.drive) and not isfunction(car.drive)

    # Now we create a truck with the provided class constructor
    truck = Truck("Optimus Prime", "Truck", 1984, 1000000.0)

    # Like car and vehicle, the informal representation is similar
    assert str(truck) == "Optimus Prime Truck (1984)"

    # And the formal representation is different from the vehicle
    # because we included the wheels attribute
    assert repr(truck) == "<Truck make=Optimus Prime model=Truck year=1984 wheels=6>"

    # And we can check the type of the method drive like we did with
    # the vehicle
    assert ismethod(truck.drive) and not isfunction(truck.drive)

    # For the last part, we can see that the method drive is different
    # for the truck
    assert truck.drive(50) == "Optimus Prime Truck (1984) is driving a truck at 50 MPH"


if __name__ == "__main__":
    main()
