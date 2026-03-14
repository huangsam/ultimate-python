# Quick orientation for AI coding agents

## Key facts an agent must know (short):

- The runner: `runner.py` dynamically imports every module under `ultimatepython` and runs any callable named `main` with zero parameters. Keep `main()` functions parameterless, idempotent, and side-effect safe for CI.
- Single-file runs are supported: modules are runnable with `python ultimatepython/<category>/<module>.py`. Most modules already include `if __name__ == "__main__": main()`.
- Examples use plain Python stdlib only. Avoid adding new third-party dependencies without updating `requirements.txt` and `pyproject.toml`.
- Assertions are used as the primary verification mechanism inside examples (not pytest tests). Preserve their intent and messages when editing.

## Patterns and conventions

- `main()` must be parameterless and not raise exceptions when run. Examples: `ultimatepython/syntax/function.py`, `ultimatepython/classes/basic_class.py`.
- Module structure: docstring, helpers, `main()` demonstrating usage via asserts, `if __name__ == "__main__": main()`.
- Avoid long-running or destructive operations. For filesystem interactions, keep them local to ephemeral files and clean up after running.
- Use `ruff` and `isort` (configured in `pyproject.toml`) for consistency with existing modules.

## Before committing

- New modules go under the appropriate folder—the runner discovers them automatically.
- If a change requires a new dependency, update `requirements.txt` and `pyproject.toml`.
- When updating `README.md`, consider updating translations or note why they were skipped.

## Quick reference

- Run all examples: `python runner.py`
- Run single example: `python ultimatepython/<category>/<module>.py`
- Coverage target: 80% (in `pyproject.toml`)

## Integration points & CI notes

- CI expects that running `runner.py` and executing each `main()` will succeed. Avoid adding code that requires network access, long sleeps, or interactive input.
- Do not introduce external services or config files; this repo intentionally uses only the Python standard library.

## Key files

- `runner.py` — discovery and execution (pkgutil.walk_packages + `main` lookups)
- `pyproject.toml` — formatting, linting, coverage rules
