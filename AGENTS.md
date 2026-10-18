# Quick orientation for AI coding agents

## Architecture & Conventions

- **Standard library only**: Lessons in `ultimatepython/` strictly use the Python standard library. No external runtime dependencies, external services, or network calls.
- **Lesson structure**: Docstring, helper definitions, parameterless idempotent `main()` with assertions for verification, and `if __name__ == "__main__": main()`.
- **Runner discovery**: `runner.py` dynamically discovers modules under `ultimatepython/` and executes `main()`.
- **Web UI (`ui/`)**: An Astro + TypeScript application for browsing lessons. Lessons are parsed by `ui/parse_lessons.py`.

## Verification & Commands

Run `./pre-commit.sh` to run the full Python verification suite:
- **Lint & Format**: `ruff check` and `ruff format`
- **Type Checking**: `mypy ultimatepython check_readmes.py runner.py`
- **README Sync**: `python check_readmes.py` (verifies header hierarchy and lesson links)
- **Tests & Coverage**: `coverage run runner.py` and `coverage report` (target >= 80%)
- **Single Lesson**: `python ultimatepython/<category>/<module>.py`
- **UI Checks**: `npm run lint` (`astro check`) and `npm run build` in `ui/`
