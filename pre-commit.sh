#!/bin/bash
# pre-commit.sh: Run the same checks as CI (see .github/workflows/ci.yml)
# Usage:
#   ./pre-commit.sh         # Run checks
#   ./pre-commit.sh install # Install as .git/hooks/pre-commit

set -euo pipefail

if [[ "${1:-}" == "install" ]]; then
	hook_path=".git/hooks/pre-commit"
	cp -- "$0" "$hook_path"
	chmod +x "$hook_path"
	echo "Installed pre-commit hook to $hook_path"
	exit 0
fi

# 1. Find the project root
PROJECT_ROOT="$(git rev-parse --show-toplevel)"

# 2. Define standard virtual environment names
VENV_NAMES=(".venv" "venv")

# 3. Locate the virtual environment directory
VENV_DIR=""
for name in "${VENV_NAMES[@]}"; do
    CANDIDATE="$PROJECT_ROOT/$name"
    if [ -d "$CANDIDATE" ]; then
        VENV_DIR="$CANDIDATE"
        break
    fi
done

# 4. Check if a virtual environment was found
if [ -z "$VENV_DIR" ]; then
    echo "Error: Virtual environment not found. Please create one (e.g., 'python3 -m venv .venv') and run the hook again."
    exit 1
fi

# 5. Define the full path to the Python interpreter within the found VENV
PYTHON_EXEC="$VENV_DIR/bin/python"

# 6. Check if the interpreter exists
if [ ! -x "$PYTHON_EXEC" ]; then
    echo "Error: Python executable not found at $PYTHON_EXEC"
    exit 1
fi

# --- Use the specific Python executable for all commands ---

# Run all examples
"$PYTHON_EXEC" runner.py

# Lint and format checks (ruff and isort are installed in the venv)
"$PYTHON_EXEC" -m ruff check
"$PYTHON_EXEC" -m isort --check --diff .

# Coverage
"$PYTHON_EXEC" -m coverage run runner.py
"$PYTHON_EXEC" -m coverage report --fail-under=80
