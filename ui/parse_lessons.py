import ast
import json
import os

CATEGORY_MAP = {"syntax": "Syntax", "data_structures": "Data Structures", "classes": "Classes", "advanced": "Advanced"}

CATEGORY_ORDER = ["syntax", "data_structures", "classes", "advanced"]


def humanize_name(name):
    # Convert variable_name to Variable Name
    return " ".join(word.capitalize() for word in name.split("_"))


def parse_file(filepath, relative_path):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    try:
        tree = ast.parse(content)
        docstring = ast.get_docstring(tree) or ""
    except Exception:
        docstring = ""

    # Strip leading docstring from code display
    code_clean = content
    stripped = content.strip()
    if docstring:
        if stripped.startswith('"""'):
            end_idx = stripped.find('"""', 3)
            if end_idx != -1:
                code_clean = stripped[end_idx + 3 :].strip()
        elif stripped.startswith("'''"):
            end_idx = stripped.find("'''", 3)
            if end_idx != -1:
                code_clean = stripped[end_idx + 3 :].strip()

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
        "code": code_clean,
        "raw_code": content,
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
