# Ultimate Python study guide

[![CircleCI](https://img.shields.io/circleci/build/github/huangsam/ultimate-python)](https://circleci.com/gh/huangsam/ultimate-python)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/master/LICENSE)
[![r/Python](https://img.shields.io/reddit/subreddit-subscribers/Python)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

Ultimate Python study guide for newcomers and professionals alike. :snake: :snake: :snake:

```python
print("Ultimate Python study guide")
```

[English](README.md) |
[한국어](README.ko.md) |
[繁体中文](README.zh_tw.md) |
[Español](README.es.md) |
[Deutsch](README.de.md)

## Motivation

I created this GitHub repo to share what I've learned about [core Python](https://www.python.org/)
over the past 5+ years of using it as a college graduate, an employee at
large-scale companies and an open-source contributor of repositories like
[Celery](https://github.com/celery/celery) and
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).
I look forward to seeing more people learn Python and pursue their passions
through it. :mortar_board:

## Goals

Here are the primary goals of creating this guide:

:trophy: **Serve as a resource** for Python newcomers who prefer to learn hands-on.
This repository has a collection of standalone modules which can be run in an IDE
like [PyCharm](https://www.jetbrains.com/pycharm/) and in the browser like
[Replit](https://replit.com/languages/python3). Even a plain old terminal will work
with the examples. Most lines have carefully crafted comments which guide a reader
through what the programs are doing step-by-step. Users are encouraged to modify
source code anywhere as long as the `main` routines are not deleted and
[run successfully](runner.py) after each change.

:trophy: **Serve as a pure guide** for those who want to revisit core Python concepts.
Only [builtin libraries](https://docs.python.org/3/library/) are leveraged so that
these concepts can be conveyed without the overhead of domain-specific concepts. As
such, popular open-source libraries and frameworks (i.e. `sqlalchemy`, `requests`,
`pandas`) are not installed. However, reading the source code in these frameworks is
inspiring and highly encouraged if your goal is to become a true
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).

## Getting started

[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)

Click the badge above to spin up a working environment in the browser without
needing Git and Python installed on your local machine. If these requirements
are already met, feel free to clone the repository directly.

Once the repository is accessible, you are ready to learn from the standalone
modules. To get the most out of each module, read the module code and run it.
There are two ways of running the modules:

1. Run a single module: `python ultimatepython/syntax/variable.py`
2. Run all of the modules: `python runner.py`

## Table of contents

:books: = External resource,
:cake: = Beginner topic,
:exploding_head: = Advanced topic

1. **About Python**
    - Overview: [What is Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) (:books:, :cake:)
    - Design philosophy: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) (:books:)
    - Style guide: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) (:books:, :exploding_head:)
    - Data model: [Data model](https://docs.python.org/3/reference/datamodel.html) (:books:, :exploding_head:)
    - Standard library: [The Python Standard Library](https://docs.python.org/3/library/) (:books:, :exploding_head:)
    - Built-in functions: [Built-in Functions](https://docs.python.org/3/library/functions.html) (:books:)
2. **Syntax**
    - Variable: [Built-in literals](ultimatepython/syntax/variable.py) (:cake:)
    - Expression: [Numeric operations](ultimatepython/syntax/expression.py) (:cake:)
    - Conditional: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) (:cake:)
    - Loop: [for-loop | while-loop](ultimatepython/syntax/loop.py) (:cake:)
    - Function: [def | lambda](ultimatepython/syntax/function.py) (:cake:)
3. **Data Structures**
    - List: [List operations](ultimatepython/data_structures/list.py) (:cake:)
    - Tuple: [Tuple operations](ultimatepython/data_structures/tuple.py)
    - Set: [Set operations](ultimatepython/data_structures/set.py)
    - Dict: [Dictionary operations](ultimatepython/data_structures/dict.py) (:cake:)
    - Comprehension: [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)
    - String: [String operations](ultimatepython/data_structures/string.py) (:cake:)
    - Deque: [deque](ultimatepython/data_structures/deque.py) (:exploding_head:)
    - Time complexity: [cPython operations](https://wiki.python.org/moin/TimeComplexity) (:books:, :exploding_head:)
4. **Classes**
    - Basic class: [Basic definition](ultimatepython/classes/basic_class.py) (:cake:)
    - Abstract class: [Abstract definition](ultimatepython/classes/abstract_class.py)
    - Exception class: [Exception definition](ultimatepython/classes/exception_class.py)
    - Iterator class: [Iterator definition | yield](ultimatepython/classes/iterator_class.py) (:exploding_head:)
5. **Advanced**
    - Decorator: [Decorator definition | wraps](ultimatepython/advanced/decorator.py) (:exploding_head:)
    - Context manager: [Context managers](ultimatepython/advanced/context_manager.py) (:exploding_head:)
    - Method resolution order: [mro](ultimatepython/advanced/mro.py) (:exploding_head:)
    - Mixin: [Mixin definition](ultimatepython/advanced/mixin.py) (:exploding_head:)
    - Metaclass: [Metaclass definition](ultimatepython/advanced/meta_class.py) (:exploding_head:)
    - Thread: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) (:exploding_head:)
    - Asyncio: [async | await](ultimatepython/advanced/async.py) (:exploding_head:)
    - Weak reference: [weakref](ultimatepython/advanced/weak_ref.py) (:exploding_head:)
    - Benchmark: [cProfile | pstats](ultimatepython/advanced/benchmark.py) (:exploding_head:)
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) (:exploding_head:)
    - Regular expression: [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) (:exploding_head:)
    - Data format: [json | xml | csv](ultimatepython/advanced/data_format.py) (:exploding_head:)
    - Datetime: [datetime | timezone](ultimatepython/advanced/date_time.py) (:exploding_head:)

## Additional resources

:necktie: = Interview resource,
:test_tube: = Code samples,
:brain: = Project ideas

### GitHub repositories

Keep learning by reading from other well-regarded resources.

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) (:necktie:, :test_tube:)
- [faif/python-patterns](https://github.com/faif/python-patterns) (:necktie:, :test_tube:)
- [geekcomputers/Python](https://github.com/geekcomputers/Python) (:test_tube:)
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) (:test_tube:)
- [karan/Projects](https://github.com/karan/Projects) (:brain:)
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) (:brain:)
- [vinta/awesome-python](https://github.com/vinta/awesome-python)
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) (:test_tube:)
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)

### Interactive practice

Keep practicing so that your coding skills don't get rusty.

- [leetcode.com](https://leetcode.com/) (:necktie:)
- [hackerrank.com](https://www.hackerrank.com/) (:necktie:)
- [kaggle.com](https://www.kaggle.com/) (:brain:)
- [exercism.io](https://exercism.io/)
- [projecteuler.net](https://projecteuler.net/)
- [DevProjects](https://www.codementor.io/projects/python)
- [codewars.com](https://www.codewars.com/)
