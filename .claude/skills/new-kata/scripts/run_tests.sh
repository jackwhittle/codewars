#!/usr/bin/env bash
# Run the tests for every kata in the repo, or just the folders given.
# Exits non-zero if any kata fails.
# Usage: run_tests.sh [kata-folder ...]
set -o pipefail

repo_root="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)" || exit 1
cd "$repo_root" || exit 1

if [ $# -gt 0 ]; then
  folders=("$@")
else
  folders=(*kyu-*/)
fi

failed=""
for dir in "${folders[@]}"; do
  dir=$(basename "$dir")
  test_file="${dir}_test.py"
  if [ ! -f "$dir/$test_file" ]; then
    echo "SKIP  $dir (no $test_file)"
    continue
  fi
  # -B stops Python writing __pycache__ folders.
  if output=$(cd "$dir" && python3 -B -m unittest "$test_file" 2>&1); then
    echo "PASS  $dir"
  else
    echo "FAIL  $dir"
    echo "$output"
    failed="$failed $dir"
  fi
done

if [ -n "$failed" ]; then
  echo "Failed:$failed"
  exit 1
fi
echo "All kata passed."
