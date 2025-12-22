import math

class Shape:
    """
    Base class for shapes. Defines the interface for calculating area.
    """
    def area(self):
        """
        Calculate the area of the shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the area() method")

class Rectangle(Shape):
    """
    Represents a rectangle with length and width.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle: length × width.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Represents a circle with a given radius.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle: π × radius²
        """
        return math.pi * self.radius ** 2