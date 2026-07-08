#!/usr/bin/env python3
"""Script to systematically verify consistency of translated READMEs.

It checks that all translation READMEs:
1. Have the same heading hierarchy structure.
2. Link to all the same content targets (ignoring language/README links).
3. Order the python lesson links in the exact same sequence.
"""

import glob
import os
import re
import sys


def extract_headings(filepath: str) -> list[int]:
    """Extract heading levels (number of # characters) from file."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    # Find lines starting with #
    headings = re.findall(r"^(#+)\s+(.+)$", content, re.MULTILINE)
    return [len(h[0]) for h in headings]


def extract_links(filepath: str) -> list[tuple[str, str]]:
    """Extract markdown link targets (excluding README/translation links)."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    raw_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    # Ignore any links that refer to README files (which vary by translation)
    normalized = []
    for text, target in raw_links:
        if "README" in target:
            continue
        normalized.append((text, target))
    return normalized


def get_lesson_links(links: list[tuple[str, str]]) -> list[str]:
    """Filter links to only those pointing to python files in ultimatepython/."""
    return [target for _, target in links if "ultimatepython/" in target]


def main() -> int:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    main_readme = os.path.join(root_dir, "README.md")

    if not os.path.exists(main_readme):
        print(f"Error: Main README not found at {main_readme}")
        return 1

    main_headings = extract_headings(main_readme)
    main_links = extract_links(main_readme)
    main_targets = {target for _, target in main_links}
    main_lessons = get_lesson_links(main_links)

    other_readmes = sorted(glob.glob(os.path.join(root_dir, "README.*.md")))
    failed = False

    print(f"Checking {len(other_readmes)} translation files against README.md...")

    for readme in other_readmes:
        name = os.path.basename(readme)
        headings = extract_headings(readme)
        links = extract_links(readme)
        targets = {target for _, target in links}
        lessons = get_lesson_links(links)

        # 1. Heading structure check
        if headings != main_headings:
            print(f"FAIL: {name} heading hierarchy does not match README.md")
            print(f"  Expected heading levels: {main_headings}")
            print(f"  Found heading levels:    {headings}")
            failed = True

        # 2. Content link targets check
        missing_targets = main_targets - targets
        if missing_targets:
            print(f"FAIL: {name} is missing the following links:")
            for target in sorted(missing_targets):
                print(f"  - {target}")
            failed = True

        # 3. Lesson ordering check
        if lessons != main_lessons:
            print(f"FAIL: {name} lesson links are out of order or mismatched.")
            # Simple diff view for lessons
            print("  Expected sequence:")
            for i, lesson in enumerate(main_lessons):
                found = lessons[i] if i < len(lessons) else "<MISSING>"
                if found != lesson:
                    print(f"    Index {i}: Expected '{lesson}', got '{found}'")
            failed = True

        if not failed:
            print(f"PASS: {name} is consistent.")

    if failed:
        print("\nVerification failed: translated READMEs are inconsistent.")
        return 1

    print("\nAll translation READMEs are consistent!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
