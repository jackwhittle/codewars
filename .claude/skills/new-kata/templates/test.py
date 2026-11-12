"""Tests for {{MODULE}}.py.

Run:  python3 -m unittest -v {{MODULE}}_test.py   (from this folder)
"""

import importlib
import unittest

# The module name starts with a digit, so a plain `import` statement can't load it.
{{FUNC}} = importlib.import_module("{{MODULE}}").{{FUNC}}


class Test{{CLASS}}(unittest.TestCase):
    def test_kata_examples(self):
        cases = {{{CASES}}}
        for arg, expected in cases.items():
            with self.subTest(arg=arg):
                self.assertEqual({{FUNC}}(arg), expected)


if __name__ == "__main__":
    unittest.main()
