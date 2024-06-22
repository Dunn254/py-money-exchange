class Currency:
    # Exchange rates relative to USD
    currencies = {'CHF': 0.930023,  # Swiss Franc 
                  'CAD': 1.264553,  # Canadian Dollar
                  'GBP': 0.737414,  # British Pound
                  'JPY': 111.019919,  # Japanese Yen
                  'EUR': 0.862361,  # Euro
                  'USD': 1.0}  # US Dollar

    def __init__(self, value, unit="USD"):
        """
        Initializes the Currency object with a value and unit.
        Default unit is USD if not specified.
        """
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        Transforms the Currency object from its current unit to a new unit.
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __repr__(self):
        """
        Returns a string representation of the Currency object.
        The value is rounded to two decimal places, followed by the unit.
        """
        return f"{self.value:.2f} {self.unit}"

    def __str__(self):
        """
        Returns the same value as __repr__().
        """
        return self.__repr__()

    def __add__(self, other):
        """
        Defines the '+' operator for Currency objects.
        If 'other' is a Currency object, their values are added.
        If 'other' is an int or float, it's treated as a USD value.
        """
        if isinstance(other, Currency):
            # Convert 'other' to the unit of 'self'
            other_value_in_self_unit = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
            return Currency(self.value + other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            # Treat 'other' as USD and convert to the unit of 'self'
            other_value_in_self_unit = other * Currency.currencies[self.unit]
            return Currency(self.value + other_value_in_self_unit, self.unit)
        else:
            return NotImplemented

    def __radd__(self, other):
        """
        Handles the addition where the Currency object is on the right-hand side.
        For example: int/float + Currency
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Defines the '-' operator for Currency objects.
        If 'other' is a Currency object, their values are subtracted.
        If 'other' is an int or float, it's treated as a USD value.
        """
        if isinstance(other, Currency):
            # Convert 'other' to the unit of 'self'
            other_value_in_self_unit = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
            return Currency(self.value - other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            # Treat 'other' as USD and convert to the unit of 'self'
            other_value_in_self_unit = other * Currency.currencies[self.unit]
            return Currency(self.value - other_value_in_self_unit, self.unit)
        else:
            return NotImplemented

    def __rsub__(self, other):
        """
        Handles the subtraction where the Currency object is on the right-hand side.
        For example: int/float - Currency
        """
        if isinstance(other, (int, float)):
            # Treat 'other' as USD and convert to the unit of 'self'
            other_value_in_self_unit = other * Currency.currencies[self.unit]
            return Currency(other_value_in_self_unit - self.value, self.unit)
        else:
            return NotImplemented

# Example usage:
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")

# Adding Currency objects
print(v1 + v2)  # Should print the sum of v1 and v2 in the unit of v1 (EUR)
print(v2 + v1)  # Should print the sum of v2 and v1 in the unit of v2 (USD)

# Adding Currency and a number (treated as USD)
print(v1 + 3)   # Should add 3 USD to v1 (EUR) and print the result
print(3 + v1)   # Should add 3 USD to v1 (EUR) and print the result

# Subtracting a number (treated as USD) from a Currency object
print(v1 - 3)   # Should subtract 3 USD from v1 (EUR) and print the result
print(30 - v2)  # Should subtract v2 (USD) from 30 USD and print the result
