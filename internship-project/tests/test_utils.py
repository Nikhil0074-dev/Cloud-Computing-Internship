import unittest
from datetime import datetime

from src.utils import add_numbers, build_greeting, day_of_week


class TestUtils(unittest.TestCase):
    def test_greeting(self):
        self.assertIn("Hello, Asha!", build_greeting("Asha"))

    def test_greeting_strips_spaces(self):
        self.assertIn("Hello, Asha!", build_greeting("  Asha  "))

    def test_greeting_empty_name_fails(self):
        with self.assertRaises(ValueError):
            build_greeting("   ")

    def test_day_of_week(self):
        self.assertEqual(day_of_week(datetime(2026, 11, 12)), "Thursday")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
