# Codewars repo conventions

## Naming

- Folder: `<kyu>kyu-<kata-slug>` at the repo root, e.g. `8kyu-century-from-year`.
  Use the slug from the Codewars URL/API (lowercase, hyphen-separated).
- Solution: `<folder>/<folder>.py`
- Tests: `<folder>/<folder>_test.py`

Existing examples: `8kyu-century-from-year/`, `8kyu-keep-hydrated/`.

## Importing the solution in tests

The module names start with a digit and contain hyphens, so
`import 8kyu-keep-hydrated` is a syntax error. Tests load the module with
`importlib` instead:

```python
import importlib

# The module name starts with a digit, so a plain `import` statement can't load it.
litres = importlib.import_module("8kyu-keep-hydrated").litres
```

This works because tests are run from inside the kata folder.

## Running tests

- One kata, from inside its folder: `python3 -m unittest -v <folder>_test.py`
  (the `.py` is required, because the name isn't a valid module name).
- Every kata: `.claude/skills/new-kata/scripts/run_tests.sh`
- `python3 -m unittest discover` does **not** work here: it skips files whose
  names aren't valid identifiers, so it finds 0 tests.

## Solution file layout

1. Docstring: `Codewars <kyu> kyu: <Kata Name>`, the kata URL, and a short
   summary of the task in your own words.
2. The function, with the exact name and arguments Codewars expects.
3. An `if __name__ == "__main__":` block that prints the kata's examples as
   `input -> output`.

## What the tests should cover

One `unittest.TestCase` class, `Test<FunctionName>`, with:

- **Kata examples**: every example from the description, using `subTest`.
- **Edge cases**: boundaries, zero, empty input, smallest/largest values.
- **Return type**: e.g. `assertIsInstance(result, int)` when the kata expects one.
- **Reference comparison**: where a simple, obviously correct definition exists
  (e.g. `math.ceil`, `math.floor`, a brute-force loop), compare against it over
  a range of inputs.

## Git

- `.gitignore` already excludes `.DS_Store` and `__pycache__/`.
- One commit per kata: `Add <kyu>kyu-<kata-name>`.
