"""
Properties provide a Pythonic mechanism for managed attributes.

In many object-oriented languages, developers write getter and setter methods
(e.g., `get_balance()` and `set_balance()`) to protect private variables.
In Python, this is considered unidiomatic because public attributes are preferred
until validation or dynamic computation is needed.

The `@property` decorator allows a method to be accessed like a standard
attribute. Pair it with `@<attribute>.setter` to validate incoming values
and `@<attribute>.deleter` to control attribute deletion without altering
the public API of your class.
"""

# Module-level constants
_ABSOLUTE_ZERO_CELSIUS = -273.15
_DEFAULT_CELSIUS = 0.0


class Temperature:
    """Temperature representation supporting Celsius and Fahrenheit scales."""

    def __init__(self, celsius: float = _DEFAULT_CELSIUS) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        """Get the current temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Set the temperature in Celsius with physical lower-bound validation."""
        if value < _ABSOLUTE_ZERO_CELSIUS:
            raise ValueError(f"Temperature cannot be below {_ABSOLUTE_ZERO_CELSIUS}°C")
        self._celsius = float(value)

    @celsius.deleter
    def celsius(self) -> None:
        """Reset temperature to default value when deleted."""
        self._celsius = _DEFAULT_CELSIUS

    @property
    def fahrenheit(self) -> float:
        """Compute temperature in Fahrenheit on demand."""
        return round((self._celsius * 9.0 / 5.0) + 32.0, 2)

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Set temperature using Fahrenheit, updating Celsius internally."""
        self.celsius = round((value - 32.0) * 5.0 / 9.0, 2)

    @property
    def is_freezing(self) -> bool:
        """Read-only property checking whether the temperature is at or below freezing."""
        return self._celsius <= 0.0


def main() -> None:
    # 1. Basic property access behaves like a regular attribute
    temp = Temperature(25.0)
    assert temp.celsius == 25.0

    # 2. Computed property is derived on-the-fly
    assert temp.fahrenheit == 77.0
    assert not temp.is_freezing

    # 3. Setter handles dynamic conversion across units
    temp.fahrenheit = 32.0
    assert temp.celsius == 0.0
    assert temp.is_freezing

    # 4. Setter enforces validation rules
    temp.celsius = -100.0
    assert temp.is_freezing
    invalid_celsius_failed = False
    try:
        temp.celsius = -300.0
    except ValueError as e:
        invalid_celsius_failed = True
        assert str(e) == f"Temperature cannot be below {_ABSOLUTE_ZERO_CELSIUS}°C"
    assert invalid_celsius_failed is True

    # 5. Read-only properties cannot be overwritten directly
    readonly_overwrite_failed = False
    try:
        temp.is_freezing = True  # type: ignore[misc]
    except AttributeError:
        readonly_overwrite_failed = True
    assert readonly_overwrite_failed is True

    # 6. Deleter hooks into attribute deletion syntax
    del temp.celsius
    assert temp.celsius == _DEFAULT_CELSIUS


if __name__ == "__main__":
    main()
