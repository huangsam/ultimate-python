# Contributing

Thanks for taking the time to understand how you can contribute to the
Ultimate Python Study guide!

Please take a look at the [code of conduct](CODE_OF_CONDUCT.md) before
proceeding further.

---

The repository consists of content and code.

## README contributions

The `README.md` is important because it is the most frequently viewed page
in this repository. Any changes here must be of high value. Specifically:

- Python modules must be referenced in the ToC
- Links must point to HTTPS resources that return a `2xx` status
- Links to GitHub repositories should have at least 1k stars
- Links to Python documentation must be valuable to newcomers and professionals

## Standalone modules

Standalone modules act as lessons or notes of how to leverage core Python.

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
