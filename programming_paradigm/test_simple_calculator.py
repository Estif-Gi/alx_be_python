# test_simple_calculator.py
# Unit tests for the SimpleCalculator class using Python's unittest framework

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    Test case for the SimpleCalculator class.
    Each test method verifies the behavior of one or more operations.
    """

    def setUp(self):
        """
        This method is called before every individual test method.
        It creates a fresh SimpleCalculator instance for each test
        to ensure tests are independent and don't affect each other.
        """
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(10.5, 4.5), 15.0)  # Test with floats

    def test_subtract(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(0, 8), -8)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)  # Test with floats

    def test_multiply(self):
        """Test the multiply method with various inputs."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(-5, -2), 10)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)  # Test with float

    def test_divide(self):
        """Test the divide method with normal cases and division by zero."""
        # Normal division cases
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)

        # Division by zero should return None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))


# This block allows running the tests directly with: python test_simple_calculator.py
# Or more properly with: python -m unittest test_simple_calculator.py
if __name__ == "__main__":
    unittest.main()