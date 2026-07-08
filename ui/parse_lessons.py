import ast
import json
import os

CATEGORY_MAP = {"syntax": "Syntax", "data_structures": "Data Structures", "classes": "Classes", "advanced": "Advanced"}

CATEGORY_ORDER = ["syntax", "data_structures", "classes", "advanced"]


def humanize_name(name: str) -> str:
    # Convert variable_name to Variable Name
    return " ".join(word.capitalize() for word in name.split("_"))


LESSON_ANNOTATIONS = {
    # Syntax
    "template_strings": {"version": "Python 3.6", "feature": "f-strings"},
    "walrus_operator": {"version": "Python 3.8", "feature": "Assignment expressions (:=)"},
    "arg_enforcement": {"version": "Python 3.8", "feature": "Positional-only parameters (/)"},
    # Data structures
    "dict_union": {"version": "Python 3.9", "feature": "Dictionary union operators (|)"},
    # Advanced
    "context_manager": {"version": "Python 2.5", "feature": "with statement"},
    "meta_class": {"version": "Python 3.0", "feature": "metaclass keyword"},
    "subinterpreters": {"version": "Python 3.12", "feature": "Per-interpreter GIL (PEP 684)"},
    "async": {"version": "Python 3.5", "feature": "async/await syntax"},
    "mocking": {"version": "Python 3.3", "feature": "unittest.mock module"},
    "pattern_matching": {"version": "Python 3.10", "feature": "Structural Pattern Matching (match/case)"},
}


def parse_file(filepath: str, relative_path: str) -> dict:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    try:
        tree = ast.parse(content)
        docstring = ast.get_docstring(tree) or ""
    except Exception:
        docstring = ""

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
    "syntax": [
        "variable",
        "template_strings",
        "expression",
        "bitwise",
        "conditional",
        "loop",
        "function",
        "walrus_operator",
        "arg_enforcement",
    ],
    "data_structures": [
        "list",
        "tuple",
        "set",
        "dict",
        "dict_union",
        "comprehension",
        "string",
        "deque",
        "namedtuple",
        "defaultdict",
        "heap",
        "itertools",
    ],
    "classes": [
        "basic_class",
        "inheritance",
        "abstract_class",
        "exception_class",
        "iterator_class",
        "encapsulation",
    ],
    "advanced": [
        "decorator",
        "file_handling",
        "context_manager",
        "mro",
        "mixin",
        "meta_class",
        "thread",
        "subinterpreters",
        "async",
        "weak_ref",
        "benchmark",
        "mocking",
        "regex",
        "data_format",
        "date_time",
        "pattern_matching",
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

    print(f"Successfully parsed {len(lessons)} lessons and saved to {output_file}")


if __name__ == "__main__":
    main()
