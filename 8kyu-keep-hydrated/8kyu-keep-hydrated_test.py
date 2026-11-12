"""Tests for 8kyu-keep-hydrated.py.

Run:  python3 -m unittest -v 8kyu-keep-hydrated_test.py   (from this folder)
"""

import importlib
import math
import unittest

# The module name starts with a digit, so a plain `import` statement can't load it.
litres = importlib.import_module("8kyu-keep-hydrated").litres


class TestLitres(unittest.TestCase):
    def test_kata_examples(self):
        cases = {3: 1, 6.7: 3, 11.8: 5}
        for time, expected in cases.items():
            with self.subTest(time=time):
                self.assertEqual(litres(time), expected)

    def test_zero_and_under_two_hours_is_zero(self):
        for time in (0, 0.5, 1, 1.99):
            with self.subTest(time=time):
                self.assertEqual(litres(time), 0)

    def test_even_hours_give_exact_litres(self):
        for hours in range(0, 101, 2):
            with self.subTest(time=hours):
                self.assertEqual(litres(hours), hours // 2)

    def test_rounds_down_not_to_nearest(self):
        self.assertEqual(litres(3.9), 1)   # 1.95 -> 1, not 2
        self.assertEqual(litres(1345.99), 672)

    def test_returns_int(self):
        self.assertIsInstance(litres(6.7), int)
        self.assertIsInstance(litres(4), int)

    def test_matches_floor_definition(self):
        for tenths in range(0, 2001):
            time = tenths / 10
            with self.subTest(time=time):
                self.assertEqual(litres(time), math.floor(time * 0.5))


if __name__ == "__main__":
    unittest.main()
