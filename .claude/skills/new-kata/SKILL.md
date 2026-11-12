---
name: new-kata
description: Set up a new Codewars kata in this repo - fetch the kata, create its <kyu>kyu-<name> folder with a solution and unittest file, and run the tests. Use when the user asks to get, set up, add or solve a Codewars kata or challenge.
---

# New kata

Each kata lives in its own folder at the repo root, named `<kyu>kyu-<kata-name>`,
containing a solution file and a test file with the same name. Read
`conventions.md` for the naming rules and the import workaround before writing code.

## Steps

1. **Find the kata.** If the user gave a URL, name or id, use it. If they asked for
   a random one (e.g. "get an 8 kyu python challenge"), pick one that isn't already
   a folder in the repo. Fetch its details from the Codewars API:
   `https://www.codewars.com/api/v1/code-challenges/<slug-or-id>`
   (returns `name`, `slug`, `rank`, `description`, `url`). Check it supports Python.

2. **Create the files** with the scaffold script, run from anywhere in the repo:

   ```bash
   .claude/skills/new-kata/scripts/new_kata.sh <kyu> <slug>
   ```

   e.g. `new_kata.sh 8 keep-hydrated` creates `8kyu-keep-hydrated/` containing
   `8kyu-keep-hydrated.py` and `8kyu-keep-hydrated_test.py`, copied from
   `templates/`. It refuses to overwrite an existing folder.

3. **Fill in the solution file.** Replace every `{{...}}` placeholder: the title,
   URL, a short plain-English summary of the task, the function (using the exact
   name and signature Codewars expects), and the kata's examples in the
   `__main__` block. Keep the solution short and idiomatic.

4. **Fill in the test file.** Replace the placeholders, then write tests covering
   the categories listed in `conventions.md` (kata examples, edge cases, return
   type, and a brute-force or reference comparison where one exists).

5. **Run the tests:**

   ```bash
   .claude/skills/new-kata/scripts/run_tests.sh <kata-folder>
   ```

   With no arguments it runs every kata in the repo. Fix failures before
   reporting back.

6. **Report** the kata name, link and a one-line explanation of the solution,
   then offer to commit. Only commit when the user agrees, with the message
   `Add <kyu>kyu-<kata-name>`.
