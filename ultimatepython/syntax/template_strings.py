"""
Template strings (t-strings) introduced in Python 3.14 (PEP 750).

T-strings look like f-strings but prefixed with 't' or 'T'. Instead of
immediately evaluating to a string, they evaluate to a Template object from
the string.templatelib module. This allows for deferred evaluation and
custom processing of the template parts and interpolations.
"""

import string.templatelib


def process_template(template):
    """Simple processor to demonstrate how Template objects work."""
    # A Template object has 'strings' (tuple of static parts)
    # and 'interpolations' (tuple of evaluated expression results)
    # The number of strings is always len(interpolations) + 1
    result = []
    for i, s in enumerate(template.strings):
        result.append(s)
        if i < len(template.interpolations):
            # Each item in interpolations is an object with a 'value' attribute
            result.append(str(template.interpolations[i].value))
    return "".join(result)


def main():
    name = "World"
    year = 2026

    # 1. Basic t-string creation
    # It evaluates to a string.templatelib.Template object
    tpl = t"Hello {name}, welcome to {year}!"

    assert isinstance(tpl, string.templatelib.Template)

    # 2. Inspecting the template parts
    # Static parts of the string
    assert tpl.strings == ("Hello ", ", welcome to ", "!")

    # Values of the expressions
    assert tpl.interpolations[0].value == "World"
    assert tpl.interpolations[1].value == 2026

    # 3. Processing the template
    # We can join them together manually or with a processor
    processed = process_template(tpl)
    assert processed == "Hello World, welcome to 2026!"

    # 4. T-strings are great for safe processing (e.g. SQL, HTML)
    # because they keep the structure separate from the data
    user_input = "'; DROP TABLE users; --"
    query_template = t"SELECT * FROM users WHERE name = {user_input}"

    # In a real scenario, a processor would escape the values in query_template.interpolations
    assert query_template.strings == ("SELECT * FROM users WHERE name = ", "")
    assert query_template.interpolations[0].value == user_input


if __name__ == "__main__":
    main()
