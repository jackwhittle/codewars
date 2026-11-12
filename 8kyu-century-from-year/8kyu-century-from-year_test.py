"""Tests for 8kyu-century-from-year.py.

Run:  python3 -m unittest -v 8kyu-century-from-year_test.py   (from this folder)
"""

import importlib
import math
import unittest

# The module name starts with a digit, so a plain `import` statement can't load it.
century = importlib.import_module("8kyu-century-from-year").century


class TestCentury(unittest.TestCase):
    def test_kata_examples(self):
        cases = {1705: 18, 1900: 19, 1601: 17, 2000: 20, 2742: 28}
        for year, expected in cases.items():
            with self.subTest(year=year):
                self.assertEqual(century(year), expected)

    def test_first_century_boundaries(self):
        self.assertEqual(century(1), 1)
        self.assertEqual(century(100), 1)
        self.assertEqual(century(101), 2)

    def test_years_ending_in_00_close_their_century(self):
        for c in range(1, 30):
            with self.subTest(year=c * 100):
                self.assertEqual(century(c * 100), c)
                self.assertEqual(century(c * 100 + 1), c + 1)

    def test_returns_int(self):
        self.assertIsInstance(century(1999), int)

    def test_matches_ceiling_definition(self):
        for year in range(1, 5001):
            with self.subTest(year=year):
                self.assertEqual(century(year), math.ceil(year / 100))


if __name__ == "__main__":
    unittest.main()
