# Contributing

Thanks for taking the time to understand how you can contribute to the
Ultimate Python Study guide!

Please take a look at the [code of conduct](CODE_OF_CONDUCT.md) before
proceeding further.

---

The repository consists of documentation and Python modules. Before you
contribute to the repository with a pull request, review all the standards
listed in upcoming sections. That way, you can uphold the craftsmanship of
this project and still make an impact on the developers using this project
for learning purposes.

## README documentation

The [README](README.md) is important because it is the most frequently viewed
page in this repository. As such, any changes that are made to this page
must be legitimate and meaningful. Specifically:

- All Python modules are referenced in the ToC
- All links point to HTTPS resources that return a `2xx` status
- External Python documentation are useful for newcomers and professionals
- External GitHub repositories have at least 1k stars
- External practice resources have Python exercises

## Python modules

Every Python module is a standalone lesson which helps developers build their
own intuition for core Python. The primary way to teach these concepts is
through `assert` statements and not `print` statements.

Certain Python concepts are skipped in this study guide in pursuit of the
statement above. However, it does open the doors for Python to run on any
computing environment - whether it be a IDE, browser, terminal or
standalone application.

When creating or updating Python modules, please respect the guidelines in
the sub-sections below.

### Standard structure

Every standalone Python module consists of the following:

```python
# Main function
def main():
    # Assertion comments
    assert 1 + 1 == 2
    assert True is not False


# Main function conditional
if __name__ == "__main__":
    main()
```

If the module involves additional functions and classes, they are placed
above the `main` function.

### Style conventions

The project follows conventions from these PEP proposals:

- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

The project has additional conventions:

- Module imports are arranged by [isort](https://github.com/timothycrosley/isort)
- Module constants follow a `_UNDER_SCORE_FIRST` convention
- Strings have "double-quotes" unless a `"` exists in the string
- Dynamic strings make use of [f-strings](https://www.python.org/dev/peps/pep-0498/)

### Code coverage

Each module should have 80-100% code coverage with the [test runner](runner.py).
The reason for this high standard is that the repository code is relatively
simple. All interactive learning tends to revolve around the `main` function
since that is where the assertions are. That way, developers immediately know
when they make a mistake in the module. This is valuable feedback because it
helps them improve quickly.

To validate code coverage, run the following commands:

```bash
$ coverage run -m runner
$ coverage html
$ open htmlcov/index.html
```
