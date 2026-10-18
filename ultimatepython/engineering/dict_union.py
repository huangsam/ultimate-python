"""
Dictionary union operators (`|` and `|=`) provide clean, side-effect-free dictionary
merging, solving a fundamental software engineering challenge in state management.

In production engineering, managing application state and configuration pipelines
often requires combining multiple data sources (such as default settings, environment
variables, and user overrides). Prior to Python 3.9 (PEP 584), merging required
destructive in-place mutations via `dict.update()` or verbose `{**d1, **d2}` unpacking,
which often introduced subtle shared-state bugs across layers.

Key software engineering benefits:
- Immutability & Safety: `|` produces a new dictionary without mutating either operand,
  preventing side-effects across components and concurrent execution paths.
- Deterministic Precedence: Subsequent dictionaries cleanly override earlier ones,
  making layered configuration cascades explicit and predictable.
- Expressive In-Place Updates: `|=` clearly signals intentional local mutation
  without sacrificing readability.
"""

from typing import Any


def cascade_config(base: dict[str, Any], *overrides: dict[str, Any]) -> dict[str, Any]:
    """Cascade configuration layers without mutating input dictionaries.

    Later layers override earlier ones, returning a freshly merged dictionary.
    """
    merged = base.copy()
    for override in overrides:
        merged |= override
    return merged


def apply_patch(record: dict[str, Any], patch: dict[str, Any]) -> None:
    """Apply a partial update in-place to an existing record using |=."""
    record |= patch


def main() -> None:
    # 1. Non-mutating dictionary union (|)
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = dict1 | dict2
    assert merged == {"a": 1, "b": 2, "c": 3, "d": 4}
    # Original dictionaries remain untouched
    assert dict1 == {"a": 1, "b": 2}
    assert dict2 == {"c": 3, "d": 4}

    # 2. Overlapping key precedence: right operand overrides left operand
    dict3 = {"a": 1, "b": 2, "c": 3}
    dict4 = {"b": 20, "c": 30, "d": 4}
    merged2 = dict3 | dict4
    assert merged2 == {"a": 1, "b": 20, "c": 30, "d": 4}

    # Order matters: left is the base, right is the override
    merged3 = dict4 | dict3
    assert merged3 == {"b": 2, "c": 3, "d": 4, "a": 1}

    # 3. In-place dictionary union (|=)
    # Mutates the left operand in place, leaving the right operand unchanged
    dict5 = {"a": 1, "b": 2}
    dict6 = {"b": 20, "c": 3}
    dict5 |= dict6
    assert dict5 == {"a": 1, "b": 20, "c": 3}
    assert dict6 == {"b": 20, "c": 3}

    # 4. Chained unions
    dict_a = {"x": 1}
    dict_b = {"y": 2}
    dict_c = {"z": 3, "x": 10}
    combined = dict_a | dict_b | dict_c
    assert combined == {"x": 10, "y": 2, "z": 3}

    # 5. Empty dictionaries and dict() constructors
    empty: dict[str, int] = {}
    assert empty | {"a": 1} == {"a": 1}
    assert dict(a=1, b=2) | dict(c=3) == {"a": 1, "b": 2, "c": 3}

    # 6. Practical engineering: Cascading configuration layers
    default_config = {"timeout": 30, "retries": 3, "debug": False, "log_level": "INFO"}
    env_config = {"debug": True}
    cli_config = {"timeout": 60, "log_level": "DEBUG"}

    active_config = cascade_config(default_config, env_config, cli_config)
    assert active_config == {
        "timeout": 60,  # Overridden by CLI
        "retries": 3,  # Retained from defaults
        "debug": True,  # Overridden by environment
        "log_level": "DEBUG",  # Overridden by CLI
    }
    # Verified: default_config was never mutated
    assert default_config["timeout"] == 30
    assert default_config["debug"] is False

    # 7. Practical engineering: Applying in-place record patches
    user_record = {"id": 100, "name": "Jane", "status": "active", "login_count": 5}
    patch_data = {"status": "inactive", "login_count": 6}
    apply_patch(user_record, patch_data)
    assert user_record == {"id": 100, "name": "Jane", "status": "inactive", "login_count": 6}

    # 8. Type safety: Unions require both operands to be dict instances
    error_raised = False
    try:
        dict1 | [("c", 3)]  # type: ignore [operator]
    except TypeError:
        error_raised = True
    assert error_raised is True

    # Non-dict compatible mappings must be converted explicitly
    assert dict1 | dict([("c", 3)]) == {"a": 1, "b": 2, "c": 3}

    # 9. Comparison with pre-3.9 approaches
    # Traditional update() mutated in place and returned None (no chaining):
    legacy_dict = {"a": 1}
    legacy_dict.update({"b": 2})
    assert legacy_dict == {"a": 1, "b": 2}

    # Traditional unpacking syntax was verbose:
    legacy_unpacking = {**{"a": 1}, **{"b": 2}}
    assert legacy_unpacking == {"a": 1, "b": 2}


if __name__ == "__main__":
    main()
