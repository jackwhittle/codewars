#!/usr/bin/env bash
# Create <kyu>kyu-<slug>/ at the repo root with a solution and test file
# copied from the templates.
# Usage: new_kata.sh <kyu> <slug>    e.g. new_kata.sh 8 keep-hydrated
set -euo pipefail

if [ $# -ne 2 ]; then
  echo "Usage: $0 <kyu> <slug>" >&2
  exit 1
fi

kyu=$1
slug=$2

if ! [[ $kyu =~ ^[1-8]$ ]]; then
  echo "kyu must be a number from 1 to 8, got: $kyu" >&2
  exit 1
fi
if ! [[ $slug =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "slug must be lowercase words separated by hyphens, got: $slug" >&2
  exit 1
fi

name="${kyu}kyu-${slug}"
skill_dir="$(cd "$(dirname "$0")/.." && pwd)"
repo_root="$(git -C "$skill_dir" rev-parse --show-toplevel)"
dest="$repo_root/$name"

if [ -e "$dest" ]; then
  echo "Already exists: $dest" >&2
  exit 1
fi

mkdir "$dest"
sed -e "s/{{MODULE}}/$name/g" -e "s/{{KYU}}/$kyu/g" \
  "$skill_dir/templates/solution.py" > "$dest/$name.py"
sed -e "s/{{MODULE}}/$name/g" -e "s/{{KYU}}/$kyu/g" \
  "$skill_dir/templates/test.py" > "$dest/${name}_test.py"

echo "Created $dest/"
echo "  $name.py"
echo "  ${name}_test.py"
