# Contributing

Thanks for taking the time to understand how you can contribute to the
Ultimate Python Study guide!

Please take a look at the [code of conduct](CODE_OF_CONDUCT.md) before
proceeding further.

---

The repository consists of documentation and modules.

## README documentation

The `README.md` is important because it is the most frequently viewed page
in this repository. As such, any changes that are made to this page must be
legitimate and meaningful. Specifically:

- Python modules must be referenced in the ToC
- Links must point to HTTPS resources that return a `2xx` status
- Links to GitHub repositories should have at least 1k stars
- Links to Python documentation must be valuable to newcomers and professionals

## Python modules

Standalone modules are lessons which act as building blocks that help
newcomers and professionals develop an intuition for core Python. The
modules tend to avoid physical I/O operations as they may be run in a
constrained / restricted resource such as a browser.

### Standard block

Every standalone Python module consists of the following:

```python
# Main function
def main():
    # Assertion comments
    assert 1 + 1 == 2
    assert True is not False


# Main function conditional
if __name__ == '__main__':
    main()
```

### Code coverage

Each module should aim for 80-100% code coverage with the test runner, which
is [runner.py](runner.py). The reason for this high standard is that the
repository code is relatively simple to test since all of the learning should
happen in the `main` function. Furthermore, having high code coverage means
that the code proactively lets developers know when they made a mistake. This
is valuable feedback, and helps the developer to improve quickly.

To validate code coverage, run the following commands:

```bash
$ coverage run -m runner
$ coverage html
$ open htmlcov/index.html
```
