# Contributing

Thanks for taking the time to understand how you can contribute to the
Ultimate Python Study guide!

Please take a look at the [code of conduct](CODE_OF_CONDUCT.md) before
proceeding further.

---

The repository consists of documentation and Python modules. Before you
contribute to the repository with a pull request, review all of the standards
listed in upcoming sections. That way, you can maintain the craftsmanship of
this project and still make an impact on the developers using this project
for learning purposes.

## README documentation

The [README](README.md) is important because it is the most frequently viewed
page in this repository. As such, any changes that are made to this page must
follow these guidelines:

- Translations are referenced at the top
- Python modules are referenced in the ToC
- External links point to HTTPS resources that return a `2xx` status
- Python documentation is useful for newcomers and professionals
- GitHub repositories have at least 1k stars
- Practice resources have Python exercises

## Python modules

Every Python module is a standalone lesson which helps developers build
their own intuition for core Python. Each module has a name that corresponds
to a topic and explores concepts with `assert` statements. This approach
encourages test-driven development and makes it simple for developers to
discern what the expected output from the code is.

Certain Python concepts are skipped in this study guide because the modules
do not reference each other and make small use of I/O operations. But this
limitation also allows the lessons to be pasted freely to any computing
environment such as an IDE, a browser window or a standalone application.

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
- Module constants follow an `_UNDER_SCORE_FIRST` convention
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
