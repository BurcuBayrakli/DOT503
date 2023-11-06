import unittest
from main import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_successful_addition(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)  # pass

    def test_failed_addition(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 6)  # fail

    def test_successful_subtraction(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 2)  # pass

    def test_failed_subtraction(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)  #  fail

    def test_successful_addition(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)  # pass

    def test_another_successful_addition(self):
        result = add_numbers(7, 8)
        self.assertEqual(result, 15)  # This test should also pass


if __name__ == '__main__':
    unittest.main()