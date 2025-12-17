# test_simple_calculator.py
# Unit tests for the SimpleCalculator class

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    Test case class for SimpleCalculator.
    Inherits from unittest.TestCase to use assertion methods.
    """

    def setUp(self):
        """
        This method runs before each individual test.
        It creates a new SimpleCalculator instance for every test
        to ensure tests are isolated.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the addition method with various cases.
        Note: The method name must start with 'test_' and takes 'self' as parameter.
        Example structure: test_addition(self)
        """
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(10.5, 4.5), 15.0)

    def test_subtraction(self):
        """Test the subtract method (a - b)."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(0, 8), -8)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(-5, -2), 10)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division(self):
        """Test the divide method, including division by zero."""
        # Normal cases
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)

        # Division by zero should return None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))


if __name__ == "__main__":
    unittest.main()