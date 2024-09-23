# Summary of Differences:

# Feature            | Instance Method        | Class Method       | Static Method
# -----------------------------------------------------------------------------
# First Parameter     | self (instance)        | cls (class)        | No first parameter
# Bound to            | Instance               | Class              | Neither
# Can access          | Instance & class data  | Class data         | Neither
# Decorator           | None                   | @classmethod       | @staticmethod
# Use Case            | Modify instance data   | Modify class data  | Utility functions


class Circle:
    pi = 3.14159  # Class variable

    def __init__(self, radius):
        self.radius = radius

    # Instance method
    def area(self):
        return Circle.pi * (self.radius ** 2)

    # Class method
    @classmethod
    def unit_circle(cls):
        return cls(1)  # Returns an instance with radius = 1

    # Static method
    @staticmethod
    def is_valid_radius(radius):
        return radius > 0

# Usage:
circle1 = Circle(5)  # Instance method usage
print(circle1.area())  # Output: 78.53975

unit_circle = Circle.unit_circle()  # Class method usage
print(unit_circle.area())  # Output: 3.14159 (area of a circle with radius 1)

print(Circle.is_valid_radius(5))  # Static method usage, Output: True
