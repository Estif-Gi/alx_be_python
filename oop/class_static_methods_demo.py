class Calculator:
    """
    A class that demonstrates the use of static methods and class methods in Python.
    """
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not require access to the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Accesses the class attribute via cls and prints it.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b