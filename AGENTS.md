# Quick orientation for AI coding agents

## Key facts an agent must know (short):

- The runner: `runner.py` dynamically imports every module under `ultimatepython` and runs any callable named `main` with zero parameters. Keep `main()` functions parameterless, idempotent, and side-effect safe for CI.
- Single-file runs are supported: modules are runnable with `python ultimatepython/<category>/<module>.py`. Most modules already include `if __name__ == "__main__": main()`.
- Examples use plain Python stdlib only. Avoid adding new third-party dependencies without updating `requirements.txt` and `pyproject.toml`.
- Assertions are used as the primary verification mechanism inside examples (not pytest tests). Preserve their intent and messages when editing.

## Patterns and conventions to follow

- main() contract: must be a function, accept zero parameters, and not raise exceptions when run. The runner asserts the function is callable and has zero parameters. Example: `ultimatepython/syntax/function.py` and `ultimatepython/classes/basic_class.py`.
- Module structure: brief module docstring, helper functions/classes, then `main()` demonstrating usage via asserts, and final `if __name__ == "__main__": main()`.
- Avoid long-running or destructive operations in examples. If a module interacts with the filesystem (e.g., `advanced/file_handling.py`), keep operations local to ephemeral files (module uses `_TARGET_FILE = "sample.txt"`), and clean up after running.
- Typing: some modules include simple type hints; prefer to keep existing style and minimal typing additions only.
- Formatting & linting: the repo uses `ruff` and `isort` settings in `pyproject.toml`. Try to keep line-length <= 160 and maintain import ordering consistent with isort defaults.

## When creating or modifying modules

- Preserve the didactic nature: keep explanatory comments and short, clear examples.
- If you add new modules, include them under the appropriate folder and follow the same pattern (module docstring, helpers, `main()`, `if __name__...`). The runner will pick them up automatically.
- If a change requires a new dependency, add it to `requirements.txt` and update `pyproject.toml` before proposing a PR.

## Top-level README files

- The top-level `README.md` is the primary project landing page: it explains the repo goals, running instructions, and links to example modules (it also shows badges for CI and coverage). When changing top-level documentation, keep the runner guidance intact (it points to `runner.py`) and preserve any badges and links.
- Translated files like `README.ko.md`, `README.zh_tw.md`, `README.es.md`, `README.de.md`, `README.fr.md`, and `README.hi.md` are language variants of the same content. If you update the English `README.md`, consider updating translations or add a brief note in the PR explaining why translations were not updated.

## Developer workflows and useful commands

- Run all examples locally (fast smoke):

```bash
python runner.py
```

- Run a single example (recommended when editing):

```bash
python ultimatepython/syntax/function.py
```

- Check formatting/linting (ruff/isort configured in `pyproject.toml`): run your local ruff/isort commands or CI.
- Coverage config exists in `pyproject.toml` (coverage fail_under=80). The examples use assertions; running `runner.py` is a good quick coverage smoke.

## Integration points & CI notes

- CI expects that running `runner.py` and executing each `main()` will succeed. Avoid adding code that requires network access, long sleeps, or interactive input.
- Do not introduce external services or config files; this repo intentionally uses only the Python standard library.

## Files and locations of interest (examples to inspect)

- `runner.py` — how modules are discovered and executed (pkgutil.walk_packages + `main` lookups).
- `ultimatepython/syntax/*.py` — simple, illustrative examples of the `main()` pattern.
- `ultimatepython/advanced/*` — more involved examples; watch for filesystem or concurrency code (e.g., `advanced/file_handling.py`, `advanced/async.py`).
- `pyproject.toml` — linting/format settings and coverage rules.

If anything in these instructions is unclear or you want additional examples (CI commands, recommended local dev Docker container, or a tiny unit-test harness), tell me which areas to expand and I'll iterate.
