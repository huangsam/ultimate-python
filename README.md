# Ultimate Python study guide

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

Ultimate Python study guide for newcomers and professionals alike. 🐍 🐍 🐍

```python
print("Ultimate Python study guide")
```

[English](README.md) |
[한국어](README.ko.md) |
[繁体中文](README.zh_tw.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[हिन्दी](README.hi.md) |
[Português - Brasil](README.pt_br.md)

<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" />

## Motivation

I created this GitHub repo to share what I've learned about [core Python](https://www.python.org/)
over the past 5+ years of using it as a college graduate, an employee at
large-scale companies and an open-source contributor of repositories like
[Celery](https://github.com/celery/celery) and
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).
I look forward to seeing more people learn Python and pursue their passions
through it. 🎓

## Goals

Here are the primary goals of creating this guide:

🏆 **Serve as a resource** for Python newcomers who prefer to learn hands-on.
This repository has a collection of standalone modules which can be run in an IDE
like [PyCharm](https://www.jetbrains.com/pycharm/) and in the browser like
[Replit](https://replit.com/languages/python3). Even a plain old terminal will work
with the examples. Most lines have carefully crafted comments which guide a reader
through what the programs are doing step-by-step. Users are encouraged to modify
source code anywhere as long as the `main` routines are not deleted and
[run successfully](runner.py) after each change.

🏆 **Serve as a pure guide** for those who want to revisit core Python concepts.
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

1. Run a single module: `python ultimatepython/fundamentals/variable.py`
2. Run all of the modules: `python runner.py`

## Table of contents

📚 = External resource,
🍰 = Beginner topic,
🤯 = Advanced topic

1. **About Python**
    - Overview: [What is Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )
    - Design philosophy: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )
    - Style guide: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )
    - Data model: [Data model](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )
    - Standard library: [The Python Standard Library](https://docs.python.org/3/library/) ( 📚, 🤯 )
    - Built-in functions: [Built-in Functions](https://docs.python.org/3/library/functions.html) ( 📚 )
2. **Fundamentals**
    - Variable: [Built-in literals](ultimatepython/fundamentals/variable.py) ( 🍰 )
    - Expression: [Numeric operations](ultimatepython/fundamentals/expression.py) ( 🍰 )
    - String: [String operations](ultimatepython/fundamentals/string.py) ( 🍰 )
    - List: [List operations](ultimatepython/fundamentals/list.py) ( 🍰 )
    - Tuple: [Tuple operations](ultimatepython/fundamentals/tuple.py)
    - Set: [Set operations](ultimatepython/fundamentals/set.py)
    - Dict: [Dictionary operations](ultimatepython/fundamentals/dict.py) ( 🍰 )
    - Conditional: [if | if-else | if-elif-else](ultimatepython/fundamentals/conditional.py) ( 🍰 )
    - Loop: [for-loop | while-loop](ultimatepython/fundamentals/loop.py) ( 🍰 )
    - Function: [def | lambda](ultimatepython/fundamentals/function.py) ( 🍰 )
    - Comprehension: [list | tuple | set | dict](ultimatepython/fundamentals/comprehension.py)
3. **Object-Oriented Programming**
    - Basic class: [Basic definition](ultimatepython/oop/basic_class.py) ( 🍰 )
    - Inheritance: [Inheritance](ultimatepython/oop/inheritance.py) ( 🍰 )
    - Encapsulation: [Encapsulation definition](ultimatepython/oop/encapsulation.py)
    - Abstract class: [Abstract definition](ultimatepython/oop/abstract_class.py)
    - Exception class: [Exception definition](ultimatepython/oop/exception_class.py)
    - Iterator class: [Iterator definition | yield](ultimatepython/oop/iterator_class.py) ( 🤯 )
    - Mixin: [Mixin definition](ultimatepython/oop/mixin.py) ( 🤯 )
    - Method resolution order: [mro](ultimatepython/oop/mro.py) ( 🤯 )
4. **Standard Library**
    - File Handling: [File Handling](ultimatepython/stdlib/file_handling.py) ( 🤯 )
    - Regular expression: [search | findall | match | fullmatch](ultimatepython/stdlib/regex.py) ( 🤯 )
    - Data format: [json | xml | csv](ultimatepython/stdlib/data_format.py) ( 🤯 )
    - Datetime: [datetime | timezone](ultimatepython/stdlib/date_time.py) ( 🤯 )
5. **Advanced**
    - Decorator: [Decorator definition | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )
    - Context manager: [Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )
    - Metaclass: [Metaclass definition](ultimatepython/advanced/meta_class.py) ( 🤯 )
    - Weak reference: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )
    - Walrus operator: [Assignment expressions :=](ultimatepython/advanced/walrus_operator.py) ( 🤯 )
    - Argument enforcement: [Positional-only / | Keyword-only *](ultimatepython/advanced/arg_enforcement.py) ( 🤯 )
    - Pattern matching: [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )
    - Template strings: [Template strings (PEP 750)](ultimatepython/advanced/template_strings.py) ( 🤯 )
6. **Concurrency**
    - Thread: [ThreadPoolExecutor](ultimatepython/concurrency/thread.py) ( 🤯 )
    - Asyncio: [async | await](ultimatepython/concurrency/async.py) ( 🤯 )
    - Subinterpreters: [concurrent.interpreters](ultimatepython/concurrency/subinterpreters.py) ( 🤯 )
7. **Engineering**
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/engineering/mocking.py) ( 🤯 )
    - Benchmark: [cProfile | pstats](ultimatepython/engineering/benchmark.py) ( 🤯 )
    - Bitwise: [Bitwise operators](ultimatepython/engineering/bitwise.py) ( 🍰 ), [One's/Two's Complement](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )
    - Deque: [deque](ultimatepython/engineering/deque.py) ( 🤯 )
    - Namedtuple: [namedtuple](ultimatepython/engineering/namedtuple.py) ( 🤯 )
    - Defaultdict: [defaultdict](ultimatepython/engineering/defaultdict.py) ( 🤯 )
    - Itertools: [Iterator tools](ultimatepython/engineering/itertools.py) ( 🤯 )
    - Dict union: [Dictionary merge | and |=](ultimatepython/engineering/dict_union.py) ( 🤯 )
    - Heap: [heap queue](ultimatepython/engineering/heap.py) ( 🤯 )
    - Time complexity: [cPython operations](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )

## Additional resources

👔 = Interview resource,
🧪 = Code samples,
🧠 = Project ideas

### GitHub repositories

Keep learning by reading from other well-regarded resources.

#### Core Python & patterns

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)

#### Data science & machine learning

- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)

#### Curated lists & project ideas

- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )
- [vinta/awesome-python](https://github.com/vinta/awesome-python)
- [lukasmasuch/best-of-python](https://github.com/lukasmasuch/best-of-python)
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )

### Interactive practice

Keep practicing so that your coding skills don't get rusty.

#### Interview preparation

- [leetcode.com](https://leetcode.com/) ( 👔 )
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )

#### Hands-on learning

- [exercism.io](https://exercism.io/)
- [codewars.com](https://www.codewars.com/)
- [labex.io](https://labex.io/exercises/python) ( 🧪 )
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 🧪 )
- [projecteuler.net](https://projecteuler.net/)
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )
