import ast
import json
import os

CATEGORY_MAP = {
    "fundamentals": "Fundamentals",
    "oop": "OOP",
    "stdlib": "Standard Library",
    "advanced": "Advanced",
    "concurrency": "Concurrency",
    "engineering": "Engineering",
}

CATEGORY_ORDER = ["fundamentals", "oop", "stdlib", "advanced", "concurrency", "engineering"]


def humanize_name(name: str) -> str:
    # Convert variable_name to Variable Name
    return " ".join(word.capitalize() for word in name.split("_"))


LESSON_ANNOTATIONS = {
    # Python 3.14
    "template_strings": {
        "version": "Python 3.14",
        "pep": "PEP 750",
        "pep_url": "https://peps.python.org/pep-0750/",
        "feature": "Template Strings",
        "syntax": 't"..."',
        "summary": "Safe, composable string templating with custom tag functions to prevent injection attacks and construct DSLs.",
    },
    "subinterpreters": {
        "version": "Python 3.14",
        "pep": "PEP 734",
        "pep_url": "https://peps.python.org/pep-0734/",
        "feature": "Multiple Interpreters in the Stdlib",
        "syntax": "concurrent.interpreters",
        "summary": "True parallel multi-core execution in pure Python via independent per-interpreter GILs.",
    },
    # Python 3.11
    "async": {
        "version": "Python 3.11",
        "pep": "PEP 654",
        "pep_url": "https://peps.python.org/pep-0654/",
        "feature": "Exception Groups & Task Groups",
        "syntax": "asyncio.TaskGroup",
        "summary": "Robust structured concurrency where child tasks cancel cleanly if any sibling task fails.",
    },
    # Python 3.10
    "pattern_matching": {
        "version": "Python 3.10",
        "pep": "PEP 634",
        "pep_url": "https://peps.python.org/pep-0634/",
        "feature": "Structural Pattern Matching",
        "syntax": "match / case",
        "summary": "Expressive destructuring and pattern matching for complex data structures and objects.",
    },
    # Python 3.9
    "dict_union": {
        "version": "Python 3.9",
        "pep": "PEP 584",
        "pep_url": "https://peps.python.org/pep-0584/",
        "feature": "Dictionary Union Operators",
        "syntax": "| and |=",
        "summary": "Clean, functional dictionary merging without in-place mutation or verbose copy operations.",
    },
    # Python 3.8
    "walrus_operator": {
        "version": "Python 3.8",
        "pep": "PEP 572",
        "pep_url": "https://peps.python.org/pep-0572/",
        "feature": "Assignment Expressions",
        "syntax": ":=",
        "summary": "Assign values to variables inside expressions to eliminate redundant computation.",
    },
    "arg_enforcement": {
        "version": "Python 3.8",
        "pep": "PEP 570",
        "pep_url": "https://peps.python.org/pep-0570/",
        "feature": "Positional-Only Parameters",
        "syntax": "/",
        "summary": "Enforce clean API boundaries and prevent callers from coupling to internal parameter names.",
    },
}


def extract_docstring_fallback(content: str) -> str:
    content = content.strip()
    if content.startswith(('"""', "'''")):
        quote = content[:3]
        end_idx = content.find(quote, 3)
        if end_idx != -1:
            return content[3:end_idx].strip()
    return ""


def parse_file(filepath: str, relative_path: str) -> dict:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    try:
        tree = ast.parse(content)
        docstring = ast.get_docstring(tree) or ""
    except Exception:
        docstring = extract_docstring_fallback(content)

    category = relative_path.split(os.sep)[0]
    filename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(filename)[0]

    return {
        "name": humanize_name(name_without_ext),
        "id": name_without_ext,
        "path": f"{category}/{name_without_ext}",
        "filename": filename,
        "category": category,
        "category_name": CATEGORY_MAP.get(category, category.capitalize()),
        "docstring": docstring.strip(),
        "code": content,
        "annotation": LESSON_ANNOTATIONS.get(name_without_ext),
    }


LESSON_ORDER = {
    "fundamentals": [
        "variable",
        "expression",
        "string",
        "list",
        "tuple",
        "set",
        "dict",
        "conditional",
        "loop",
        "function",
        "comprehension",
    ],
    "oop": [
        "basic_class",
        "inheritance",
        "encapsulation",
        "abstract_class",
        "exception_class",
        "iterator_class",
        "mixin",
        "mro",
    ],
    "stdlib": [
        "file_handling",
        "regex",
        "data_format",
        "date_time",
    ],
    "advanced": [
        "decorator",
        "context_manager",
        "meta_class",
        "weak_ref",
        "walrus_operator",
        "arg_enforcement",
        "pattern_matching",
        "template_strings",
    ],
    "concurrency": [
        "thread",
        "async",
        "subinterpreters",
    ],
    "engineering": [
        "mocking",
        "benchmark",
        "bitwise",
        "deque",
        "namedtuple",
        "ordereddict",
        "defaultdict",
        "itertools",
        "dict_union",
        "heap",
    ],
}


def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(root_dir, "ultimatepython")

    lessons = []

    for category in CATEGORY_ORDER:
        cat_dir = os.path.join(target_dir, category)
        if not os.path.exists(cat_dir):
            continue

        # Sort files according to prescribed LESSON_ORDER or alphabetically as fallback
        order_list = LESSON_ORDER.get(category, [])

        def get_sort_key(filename, order_list=order_list):
            name = os.path.splitext(filename)[0]
            try:
                return (0, order_list.index(name))
            except ValueError:
                return (1, name)

        files = sorted(os.listdir(cat_dir), key=get_sort_key)
        for filename in files:
            if filename.endswith(".py") and filename != "__init__.py":
                filepath = os.path.join(cat_dir, filename)
                rel_path = os.path.join(category, filename)
                lesson = parse_file(filepath, rel_path)
                lessons.append(lesson)

    output_dir = os.path.join(root_dir, "ui", "src", "data")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "lessons.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    categories_file = os.path.join(output_dir, "categories.json")
    with open(categories_file, "w", encoding="utf-8") as f:
        json.dump(CATEGORY_ORDER, f, indent=2, ensure_ascii=False)

    print(f"Successfully parsed {len(lessons)} lessons and saved to {output_file}")


if __name__ == "__main__":
    main()
