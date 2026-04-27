<!--@nrg.languages=en,de,es,fr,hi,ko,pt_br,zh_tw-->
<!--@nrg.defaultLanguage=en-->
# Ultimate Python study guide<!--en-->
<!--en-->
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)<!--en-->
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)<!--en-->
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)<!--en-->
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)<!--en-->
<!--en-->
Ultimate Python study guide for newcomers and professionals alike. 🐍 🐍 🐍<!--en-->
<!--en-->
```python<!--en-->
print("Ultimate Python study guide")<!--en-->
```<!--en-->
<!--en-->
[English](README.md) |<!--en-->
[한국어](README.ko.md) |<!--en-->
[繁体中文](README.zh_tw.md) |<!--en-->
[Español](README.es.md) |<!--en-->
[Deutsch](README.de.md) |<!--en-->
[Français](README.fr.md) |<!--en-->
[हिन्दी](README.hi.md) |<!--en-->
[Português - Brasil](README.pt_br.md)<!--en-->
<!--en-->
<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" /><!--en-->
<!--en-->
## Motivation<!--en-->
<!--en-->
I created this GitHub repo to share what I've learned about [core Python](https://www.python.org/)<!--en-->
over the past 5+ years of using it as a college graduate, an employee at<!--en-->
large-scale companies and an open-source contributor of repositories like<!--en-->
[Celery](https://github.com/celery/celery) and<!--en-->
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).<!--en-->
I look forward to seeing more people learn Python and pursue their passions<!--en-->
through it. 🎓<!--en-->
<!--en-->
## Goals<!--en-->
<!--en-->
Here are the primary goals of creating this guide:<!--en-->
<!--en-->
🏆 **Serve as a resource** for Python newcomers who prefer to learn hands-on.<!--en-->
This repository has a collection of standalone modules which can be run in an IDE<!--en-->
like [PyCharm](https://www.jetbrains.com/pycharm/) and in the browser like<!--en-->
[Replit](https://replit.com/languages/python3). Even a plain old terminal will work<!--en-->
with the examples. Most lines have carefully crafted comments which guide a reader<!--en-->
through what the programs are doing step-by-step. Users are encouraged to modify<!--en-->
source code anywhere as long as the `main` routines are not deleted and<!--en-->
[run successfully](runner.py) after each change.<!--en-->
<!--en-->
🏆 **Serve as a pure guide** for those who want to revisit core Python concepts.<!--en-->
Only [builtin libraries](https://docs.python.org/3/library/) are leveraged so that<!--en-->
these concepts can be conveyed without the overhead of domain-specific concepts. As<!--en-->
such, popular open-source libraries and frameworks (i.e. `sqlalchemy`, `requests`,<!--en-->
`pandas`) are not installed. However, reading the source code in these frameworks is<!--en-->
inspiring and highly encouraged if your goal is to become a true<!--en-->
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).<!--en-->
<!--en-->
## Getting started<!--en-->
<!--en-->
[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)<!--en-->
<!--en-->
Click the badge above to spin up a working environment in the browser without<!--en-->
needing Git and Python installed on your local machine. If these requirements<!--en-->
are already met, feel free to clone the repository directly.<!--en-->
<!--en-->
Once the repository is accessible, you are ready to learn from the standalone<!--en-->
modules. To get the most out of each module, read the module code and run it.<!--en-->
There are two ways of running the modules:<!--en-->
<!--en-->
1. Run a single module: `python ultimatepython/syntax/variable.py`<!--en-->
2. Run all of the modules: `python runner.py`<!--en-->
<!--en-->
## Table of contents<!--en-->
<!--en-->
📚 = External resource,<!--en-->
🍰 = Beginner topic,<!--en-->
🤯 = Advanced topic<!--en-->
<!--en-->
1. **About Python**<!--en-->
    - Overview: [What is Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )<!--en-->
    - Design philosophy: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )<!--en-->
    - Style guide: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )<!--en-->
    - Data model: [Data model](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )<!--en-->
    - Standard library: [The Python Standard Library](https://docs.python.org/3/library/) ( 📚, 🤯 )<!--en-->
    - Built-in functions: [Built-in Functions](https://docs.python.org/3/library/functions.html) ( 📚 )<!--en-->
2. **Syntax**<!--en-->
    - Variable: [Built-in literals](ultimatepython/syntax/variable.py) ( 🍰 )<!--en-->
    - Expression: [Numeric operations](ultimatepython/syntax/expression.py) ( 🍰 )<!--en-->
    - Bitwise: [Bitwise operators](ultimatepython/syntax/bitwise.py) ( 🍰 ), [One's/Two's Complement](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )<!--en-->
    - Conditional: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )<!--en-->
    - Loop: [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )<!--en-->
    - Function: [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )<!--en-->
    - Walrus operator: [Assignment expressions :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )<!--en-->
    - Argument enforcement: [Positional-only / | Keyword-only *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )<!--en-->
3. **Data Structures**<!--en-->
    - List: [List operations](ultimatepython/data_structures/list.py) ( 🍰 )<!--en-->
    - Tuple: [Tuple operations](ultimatepython/data_structures/tuple.py)<!--en-->
    - Set: [Set operations](ultimatepython/data_structures/set.py)<!--en-->
    - Dict: [Dictionary operations](ultimatepython/data_structures/dict.py) ( 🍰 )<!--en-->
    - Dict union: [Dictionary merge | and |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )<!--en-->
    - Comprehension: [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)<!--en-->
    - String: [String operations](ultimatepython/data_structures/string.py) ( 🍰 )<!--en-->
    - Deque: [deque](ultimatepython/data_structures/deque.py) ( 🤯 )<!--en-->
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )<!--en-->
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )<!--en-->
    - Itertools: [Iterator tools](ultimatepython/data_structures/itertools.py) ( 🤯 )<!--en-->
    - Time complexity: [cPython operations](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )<!--en-->
4. **Classes**<!--en-->
    - Basic class: [Basic definition](ultimatepython/classes/basic_class.py) ( 🍰 )<!--en-->
    - Inheritance: [Inheritance](ultimatepython/classes/inheritance.py) ( 🍰 )<!--en-->
    - Abstract class: [Abstract definition](ultimatepython/classes/abstract_class.py)<!--en-->
    - Exception class: [Exception definition](ultimatepython/classes/exception_class.py)<!--en-->
    - Iterator class: [Iterator definition | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )<!--en-->
    - Encapsulation: [Encapsulation definition](ultimatepython/classes/encapsulation.py)<!--en-->
5. **Advanced**<!--en-->
    - Decorator: [Decorator definition | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )<!--en-->
    - File Handling: [File Handling](ultimatepython/advanced/file_handling.py) ( 🤯 )<!--en-->
    - Context manager: [Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )<!--en-->
    - Method resolution order: [mro](ultimatepython/advanced/mro.py) ( 🤯 )<!--en-->
    - Mixin: [Mixin definition](ultimatepython/advanced/mixin.py) ( 🤯 )<!--en-->
    - Metaclass: [Metaclass definition](ultimatepython/advanced/meta_class.py) ( 🤯 )<!--en-->
    - Thread: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )<!--en-->
    - Asyncio: [async | await](ultimatepython/advanced/async.py) ( 🤯 )<!--en-->
    - Weak reference: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )<!--en-->
    - Benchmark: [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )<!--en-->
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )<!--en-->
    - Regular expression: [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )<!--en-->
    - Data format: [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )<!--en-->
    - Datetime: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )<!--en-->
    - Pattern matching: [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )<!--en-->
<!--en-->
## Additional resources<!--en-->
<!--en-->
👔 = Interview resource,<!--en-->
🧪 = Code samples,<!--en-->
🧠 = Project ideas<!--en-->
<!--en-->
### GitHub repositories<!--en-->
<!--en-->
Keep learning by reading from other well-regarded resources.<!--en-->
<!--en-->
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )<!--en-->
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )<!--en-->
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )<!--en-->
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )<!--en-->
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )<!--en-->
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )<!--en-->
- [vinta/awesome-python](https://github.com/vinta/awesome-python)<!--en-->
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)<!--en-->
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)<!--en-->
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)<!--en-->
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )<!--en-->
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)<!--en-->
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)<!--en-->
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )<!--en-->
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )<!--en-->
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )<!--en-->
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) ( 🧪 )<!--en-->
<!--en-->
### Author projects<!--en-->
<!--en-->
Projects I've built with Python that showcase what you can create after learning these concepts:<!--en-->
<!--en-->
- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )<!--en-->
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )<!--en-->
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )<!--en-->
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )<!--en-->
<!--en-->
### Interactive practice<!--en-->
<!--en-->
Keep practicing so that your coding skills don't get rusty.<!--en-->
<!--en-->
- [codechef.com](https://www.codechef.com/) ( 👔 )<!--en-->
- [codeforces.com](https://codeforces.com/)<!--en-->
- [codementor.io](https://www.codementor.io) ( 🧠 )<!--en-->
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )<!--en-->
- [codewars.com](https://www.codewars.com/)<!--en-->
- [exercism.io](https://exercism.io/)<!--en-->
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )<!--en-->
- [hackerearth.com](https://www.hackerearth.com/)<!--en-->
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )<!--en-->
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )<!--en-->
- [labex.io](https://labex.io/exercises/python)( 🧪 )<!--en-->
- [leetcode.com](https://leetcode.com/) ( 👔 )<!--en-->
- [projecteuler.net](https://projecteuler.net/)<!--en-->
- [replit.com](https://replit.com/)<!--en-->
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )<!--en-->
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )<!--en-->
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )<!--en-->
<!--en-->
## Stargazers over time<!--en-->
<!--en-->
[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)<!--en-->
# Ultimativer Python-Lernführer<!--de-->
<!--de-->
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)<!--de-->
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)<!--de-->
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)<!--de-->
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)<!--de-->
<!--de-->
Der ultimative Python-Lernführer für Einsteiger und Profis gleichermaßen. 🐍 🐍 🐍<!--de-->
<!--de-->
```python<!--de-->
print("Ultimativer Python-Lernführer")<!--de-->
```<!--de-->
<!--de-->
[English](README.md) |<!--de-->
[한국어](README.ko.md) |<!--de-->
[繁体中文](README.zh_tw.md) |<!--de-->
[Español](README.es.md) |<!--de-->
[Deutsch](README.de.md) |<!--de-->
[Français](README.fr.md) |<!--de-->
[हिन्दी](README.hi.md) |<!--de-->
[Português - Brasil](README.pt_br.md)<!--de-->
<!--de-->
<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" /><!--de-->
<!--de-->
## Motivation<!--de-->
<!--de-->
Ich habe dieses GitHub-Repository erstellt, um meine Erkenntnisse über [core Python](https://www.python.org/)<!--de-->
in den letzten 5 Jahren als Hochschulabsolvent, Angestellter in<!--de-->
großen Unternehmen und als Open-Source-Mitarbeiter von Repositories wie<!--de-->
[Celery](https://github.com/celery/celery) und<!--de-->
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com) weiterzugeben.<!--de-->
Ich freue mich darauf, dass noch mehr Menschen Python lernen und damit ihren Leidenschaften nachgehen. 🎓<!--de-->
<!--de-->
## Ziele<!--de-->
<!--de-->
Dies sind die Hauptziele bei der Erstellung dieses Leitfadens:<!--de-->
<!--de-->
🏆 **Als Ressource fungieren** für Python-Neulinge, die es vorziehen, praktisch zu lernen.<!--de-->
Dieses Repository enthält eine Sammlung von eigenständigen Modulen, die in einer IDE<!--de-->
 wie [PyCharm](https://www.jetbrains.com/pycharm/) oder im Browser via<!--de-->
 [Replit](https://replit.com/languages/python3) ausgeführt werden können. Ein Terminal funktioniert<!--de-->
 ebenfalls gut für die Beispiele. Die meisten Zeilen enthalten sorgfälltig formulierte Kommentare, die den Leser<!--de-->
 Schritt für Schritt durch die Abläufe führen. Benutzer werden ermutigt, den Quellcode zu ändern,<!--de-->
 sofern die `main`-Routinen nicht entfernt werden und die Programme nach Änderungen weiterhin erfolgreich<!--de-->
 ausgeführt werden (siehe `runner.py`).<!--de-->
<!--de-->
🏆 **Als reiner Leitfaden dienen** für diejenigen, die die wichtigsten Python-Konzepte wiederholen möchten.<!--de-->
Wo nur [builtin libraries](https://docs.python.org/3/library/) genutzt werden, so dass<!--de-->
diese Konzepte ohne den Overhead der bereichsspezifischen Konzepte vermittelt werden können. Als<!--de-->
beliebte Open-Source-Bibliotheken und -Frameworks (d.h. `sqlalchemy`, `requests`,<!--de-->
`pandas`) nicht installiert sind. Das Lesen des Quellcodes dieser Frameworks ist jedoch<!--de-->
inspirierend und wird dringend empfohlen, wenn Sie ein echter Profi werden wollen.<!--de-->
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).<!--de-->
<!--de-->
## Erste Schritte<!--de-->
<!--de-->
[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)<!--de-->
<!--de-->
Klicken Sie auf das obige Abzeichen, um eine Arbeitsumgebung im Browser zu starten, ohne<!--de-->
ohne dass Sie Git und Python auf Ihrem lokalen Rechner installiert haben müssen. Wenn diese Voraussetzungen<!--de-->
bereits erfüllt sind, können Sie das Repository direkt klonen.<!--de-->
<!--de-->
Sobald das Repository zugänglich ist, können Sie mit den eigenständigen<!--de-->
Modulen lernen. Um den größtmöglichen Nutzen aus jedem Modul zu ziehen, lesen Sie den Modulcode und führen Sie ihn aus.<!--de-->
Es gibt zwei Möglichkeiten, die Module auszuführen:<!--de-->
<!--de-->
1. Führen Sie ein einzelnes Modul aus: `python ultimatepython/syntax/variable.py`<!--de-->
2. Führen Sie alle Module aus: `python runner.py`<!--de-->
<!--de-->
## Inhaltsübersicht<!--de-->
<!--de-->
📚 = Externe Ressource,<!--de-->
🍰 = Thema für Anfänger,<!--de-->
🤯 = Fortgeschrittenes Thema<!--de-->
<!--de-->
1. **Über Python**<!--de-->
    - Overview: [What is Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )<!--de-->
    - Design philosophy: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )<!--de-->
    - Style guide: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )<!--de-->
    - Data model: [Data model](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )<!--de-->
    - Standard library: [The Python Standard Library](https://docs.python.org/3/library/) ( 📚, 🤯 )<!--de-->
    - Built-in functions: [Built-in Functions](https://docs.python.org/3/library/functions.html) ( 📚 )<!--de-->
2. **Syntax**<!--de-->
    - Variable: [Built-in literals](ultimatepython/syntax/variable.py) ( 🍰 )<!--de-->
    - Expression: [Numeric operations](ultimatepython/syntax/expression.py) ( 🍰 )<!--de-->
    - Bitwise: [Bitwise operators](ultimatepython/syntax/bitwise.py) ( 🍰 ), [One's/Two's Complement](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )<!--de-->
    - Conditional: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )<!--de-->
    - Loop: [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )<!--de-->
    - Function: [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )<!--de-->
    - Walrus operator: [Assignment expressions :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )<!--de-->
    - Argument enforcement: [Positional-only / | Keyword-only *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )<!--de-->
3. **Daten-Strukturen**<!--de-->
    - List: [List operations](ultimatepython/data_structures/list.py) ( 🍰 )<!--de-->
    - Tuple: [Tuple operations](ultimatepython/data_structures/tuple.py)<!--de-->
    - Set: [Set operations](ultimatepython/data_structures/set.py)<!--de-->
    - Dict: [Dictionary operations](ultimatepython/data_structures/dict.py) ( 🍰 )<!--de-->
    - Dict union: [Dictionary merge | and |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )<!--de-->
    - Comprehension: [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)<!--de-->
    - String: [String operations](ultimatepython/data_structures/string.py) ( 🍰 )<!--de-->
    - Deque: [deque](ultimatepython/data_structures/deque.py) ( 🤯 )<!--de-->
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )<!--de-->
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )<!--de-->
    - Iterator-Tools: [Iterator-Tools](ultimatepython/data_structures/itertools.py) ( 🤯 )<!--de-->
    - Time complexity: [cPython operations](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )<!--de-->
4. **Klassen**<!--de-->
    - Basic class: [Basic definition](ultimatepython/classes/basic_class.py) ( 🍰 )<!--de-->
    - Inheritance: [Inheritance](ultimatepython/classes/inheritance.py) ( 🍰 )<!--de-->
    - Abstract class: [Abstract definition](ultimatepython/classes/abstract_class.py)<!--de-->
    - Exception class: [Exception definition](ultimatepython/classes/exception_class.py)<!--de-->
    - Iterator class: [Iterator definition | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )<!--de-->
    - Encapsulation: [Encapsulation definition](ultimatepython/classes/encapsulation.py)<!--de-->
5. **Fortgeschrittene**<!--de-->
    - Decorator: [Decorator definition | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )<!--de-->
    - File Handling: [File Handling](ultimatepython/advanced/file_handling.py) ( 🤯 )<!--de-->
    - Context manager: [Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )<!--de-->
    - Method resolution order: [mro](ultimatepython/advanced/mro.py) ( 🤯 )<!--de-->
    - Mixin: [Mixin definition](ultimatepython/advanced/mixin.py) ( 🤯 )<!--de-->
    - Metaclass: [Metaclass definition](ultimatepython/advanced/meta_class.py) ( 🤯 )<!--de-->
    - Thread: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )<!--de-->
    - Asyncio: [async | await](ultimatepython/advanced/async.py) ( 🤯 )<!--de-->
    - Weak reference: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )<!--de-->
    - Benchmark: [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )<!--de-->
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )<!--de-->
    - Regular expression: [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )<!--de-->
    - Data format: [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )<!--de-->
    - Datetime: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )<!--de-->
    - Pattern Matching: [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )<!--de-->
<!--de-->
## Zusätzliche Ressourcen<!--de-->
<!--de-->
👔 = Interview-Ressource,<!--de-->
🧪 = Code-Beispiele,<!--de-->
🧠 = Projektideen<!--de-->
<!--de-->
### GitHub repositories<!--de-->
<!--de-->
Lernen Sie weiter, indem Sie von anderen Quellen lesen.<!--de-->
<!--de-->
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )<!--de-->
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )<!--de-->
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )<!--de-->
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )<!--de-->
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )<!--de-->
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )<!--de-->
- [vinta/awesome-python](https://github.com/vinta/awesome-python)<!--de-->
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)<!--de-->
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)<!--de-->
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)<!--de-->
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )<!--de-->
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)<!--de-->
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)<!--de-->
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )<!--de-->
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )<!--de-->
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )<!--de-->
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) ( 🧪 )<!--de-->
<!--de-->
### Projekte des Autors<!--de-->
<!--de-->
Projekte, die ich mit Python erstellt habe und die zeigen, was man nach dem Erlernen dieser Konzepte erstellen kann:<!--de-->
<!--de-->
- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )<!--de-->
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )<!--de-->
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )<!--de-->
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )<!--de-->
<!--de-->
### Interaktive Übungen<!--de-->
<!--de-->
Üben Sie weiter, damit Ihre Programmierkenntnisse nicht einrosten.<!--de-->
<!--de-->
- [codechef.com](https://www.codechef.com/) ( 👔 )<!--de-->
- [codeforces.com](https://codeforces.com/)<!--de-->
- [codementor.io](https://www.codementor.io) ( 🧠 )<!--de-->
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )<!--de-->
- [codewars.com](https://www.codewars.com/)<!--de-->
- [exercism.io](https://exercism.io/)<!--de-->
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )<!--de-->
- [hackerearth.com](https://www.hackerearth.com/)<!--de-->
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )<!--de-->
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )<!--de-->
- [labex.io](https://labex.io/exercises/python)( 🧪 )<!--de-->
- [leetcode.com](https://leetcode.com/) ( 👔 )<!--de-->
- [projecteuler.net](https://projecteuler.net/)<!--de-->
- [replit.com](https://replit.com/)<!--de-->
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )<!--de-->
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )<!--de-->
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )<!--de-->
<!--de-->
## Sternengucker der Zeit<!--de-->
<!--de-->
[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)<!--de-->
# Guía de estudio "Python Definitivo"<!--es-->
<!--es-->
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)<!--es-->
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)<!--es-->
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)<!--es-->
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)<!--es-->
<!--es-->
Guía de estudio "Python Definitivo" para principiantes y profesionales. 🐍 🐍 🐍<!--es-->
<!--es-->
```python<!--es-->
print("Guía de estudio 'Python Definitivo'")<!--es-->
```<!--es-->
<!--es-->
[English](README.md) |<!--es-->
[한국어](README.ko.md) |<!--es-->
[繁体中文](README.zh_tw.md) |<!--es-->
[Español](README.es.md) |<!--es-->
[Deutsch](README.de.md) |<!--es-->
[Français](README.fr.md) |<!--es-->
[हिन्दी](README.hi.md) |<!--es-->
[Português - Brasil](README.pt_br.md)<!--es-->
<!--es-->
<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" /><!--es-->
<!--es-->
## Motivación<!--es-->
<!--es-->
Creé este repositorio de GitHub para compartir lo que he aprendido sobre [Python](https://www.python.org/)<!--es-->
durante más de 5 años usándolo como graduado de universidad, empleado en grandes empresas y como contribuidor<!--es-->
de código abierto en repositorios como [Celery](https://github.com/celery/celery) y<!--es-->
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).<!--es-->
Espero ver a más personas aprendiendo Python y persiguiendo su pasión a través de él. 🎓<!--es-->
<!--es-->
## Objetivos<!--es-->
<!--es-->
Estos son los objetivos principales de esta guía:<!--es-->
<!--es-->
🏆 **Servir como un recurso** para principiantes de Python que prefieren aprender de forma práctica.<!--es-->
Este repositorio contiene una colección de módulos independientes que pueden ejecutarse en<!--es-->
un IDE como [PyCharm](https://www.jetbrains.com/pycharm/) y en el navegador, como<!--es-->
[Replit](https://replit.com/languages/python3). Incluso una terminal sencilla funcionará con los ejemplos.<!--es-->
La mayoría de las líneas de código tienen comentarios útiles que guían al lector paso a paso.<!--es-->
Se anima a los usuarios a modificar el código fuente en cualquier parte siempre y cuando las rutinas<!--es-->
principales (`main`) no se eliminen y los programas se ejecuten con éxito tras cada cambio (ver `runner.py`).<!--es-->
<!--es-->
🏆 **Servir como una guía pura** para aquellos que quieren reforzar los conceptos base de<!--es-->
Python. Se utilizan sólo las [librerías integradas](https://docs.python.org/3/library/) para que<!--es-->
estos conceptos puedan adquirirse sin el esfuerzo de aprender conocimientos de dominios específicos.<!--es-->
Por ello no se han instalado librerías y entornos de código abierto populares (como `sqlalchemy`,<!--es-->
`requests`, `pandas`). No obstante, leer el código fuente de estos frameworks es inspirador y altamente<!--es-->
recomendado si tu objetivo es convertirte en un verdadero<!--es-->
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).<!--es-->
<!--es-->
## Empezando<!--es-->
<!--es-->
[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)<!--es-->
<!--es-->
Haz clic en la imagen de arriba para crear un ambiente de trabajo en el navegador sin necesidad<!--es-->
de tener Git y Python instalados en tu ordenador local. Si estos requisitos ya se cumplen,<!--es-->
puedes clonar el repositorio directamente.<!--es-->
<!--es-->
Una vez que el repositorio sea accesible, estás listo para aprender de los módulos independientes.<!--es-->
Para aprender el máximo de cada módulo, lee el código del módulo y ejecútalo.<!--es-->
Hay dos maneras de ejecutar los módulos:<!--es-->
<!--es-->
1. Ejecuta un solo módulo: `python ultimatepython/syntax/variable.py`<!--es-->
2. Ejecuta todos los módulos: `python runner.py`<!--es-->
<!--es-->
## Contenido<!--es-->
<!--es-->
📚 = Recurso externo,<!--es-->
🍰 = Tema principiante,<!--es-->
🤯 = Tema avanzado<!--es-->
<!--es-->
1. **Sobre Python**<!--es-->
    - Resumen: [¿Qué es Python?](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )<!--es-->
    - Filosofía de diseño: [El Zen de Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )<!--es-->
    - Guía de estilos: [Guía de estilos para código de Python](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )<!--es-->
    - Modelo de datos: [Modelo de datos](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )<!--es-->
    - Librería estándar: [La librería estándar de Python](https://docs.python.org/3/library/) ( 📚, 🤯 )<!--es-->
    - Funciones integradas: [Funciones integradas](https://docs.python.org/3/library/functions.html) ( 📚 )<!--es-->
2. **Sintaxis**<!--es-->
    - Variables: [Literales integrados](ultimatepython/syntax/variable.py) ( 🍰 )<!--es-->
    - Expresiones: [Operaciones numéricas](ultimatepython/syntax/expression.py) ( 🍰 )<!--es-->
    - Bit a bit: [Operadores bit a bit](ultimatepython/syntax/bitwise.py) ( 🍰 ), [Complemento a uno/dos](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )<!--es-->
    - Condicionales: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )<!--es-->
    - Iteraciones: [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )<!--es-->
    - Funciones: [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )<!--es-->
    - Operador morsa: [Expresiones de asignación :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )<!--es-->
    - Aplicación de argumentos: [Solo posicional / | Solo palabra clave *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )<!--es-->
3. **Estructura de datos**<!--es-->
    - Lista: [Operaciones con listas](ultimatepython/data_structures/list.py) ( 🍰 )<!--es-->
    - Tupla: [Operaciones con tuplas](ultimatepython/data_structures/tuple.py)<!--es-->
    - Set: [Operaciones con sets](ultimatepython/data_structures/set.py)<!--es-->
    - Diccionario: [Operaciones con dicts](ultimatepython/data_structures/dict.py) ( 🍰 )<!--es-->
    - Unión de diccionarios: [Fusión de diccionarios | y |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )<!--es-->
    - Comprensión: [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)<!--es-->
    - Cadena: [Operaciones con strings](ultimatepython/data_structures/string.py) ( 🍰 )<!--es-->
    - Deque: [deque](ultimatepython/data_structures/deque.py) ( 🤯 )<!--es-->
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )<!--es-->
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )<!--es-->
    - Herramientas de iteradores: [Herramientas de iteradores](ultimatepython/data_structures/itertools.py) ( 🤯 )<!--es-->
    - Complejidad de tiempo: [Operaciones de cPython](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )<!--es-->
4. **Clases**<!--es-->
    - Clase básica: [Definición de básica](ultimatepython/classes/basic_class.py) ( 🍰 )<!--es-->
    - Herencia: [Herencia](ultimatepython/classes/inheritance.py) ( 🍰 )<!--es-->
    - Clase abstracta: [Definición de abstracta](ultimatepython/classes/abstract_class.py)<!--es-->
    - Clase de excepción: [Definición de excepción](ultimatepython/classes/exception_class.py)<!--es-->
    - Clase iteradora: [Definición de iteradora | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )<!--es-->
    - Encapsulación: [Definición de encapsulación](ultimatepython/classes/encapsulation.py)<!--es-->
5. **Avanzado**<!--es-->
    - Decorador: [Definición de decorador | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )<!--es-->
    - Manejo de archivos: [Manejo de archivos](ultimatepython/advanced/file_handling.py) ( 🤯 )<!--es-->
    - Gestor de contexto: [Gestores de contexto](ultimatepython/advanced/context_manager.py) ( 🤯 )<!--es-->
    - Orden de resolución de método (MRO por sus siglas en inglés): [mro](ultimatepython/advanced/mro.py) ( 🤯 )<!--es-->
    - Mixin: [Definición de Mixin](ultimatepython/advanced/mixin.py) ( 🤯 )<!--es-->
    - Metaclase: [Definición de metaclase](ultimatepython/advanced/meta_class.py) ( 🤯 )<!--es-->
    - Hilos: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )<!--es-->
    - Asyncio: [async | await](ultimatepython/advanced/async.py) ( 🤯 )<!--es-->
    - Referencias débiles: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )<!--es-->
    - Referencia: [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )<!--es-->
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )<!--es-->
    - Expresiones regulares: [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )<!--es-->
    - Formatos de datos: [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )<!--es-->
    - Fecha y hora: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )<!--es-->
    - Coincidencia de patrones: [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )<!--es-->
<!--es-->
## Recursos adicionales<!--es-->
<!--es-->
👔 = Recurso de entrevista,<!--es-->
🧪 = Ejemplos de código,<!--es-->
🧠 = Ideas para proyecto<!--es-->
<!--es-->
### Repositorios de GitHub<!--es-->
<!--es-->
Sigue aprendiendo leyendo otros buenos recursos.<!--es-->
<!--es-->
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )<!--es-->
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )<!--es-->
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )<!--es-->
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )<!--es-->
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )<!--es-->
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )<!--es-->
- [vinta/awesome-python](https://github.com/vinta/awesome-python)<!--es-->
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)<!--es-->
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)<!--es-->
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)<!--es-->
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )<!--es-->
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)<!--es-->
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)<!--es-->
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )<!--es-->
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )<!--es-->
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )<!--es-->
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) ( 🧪 )<!--es-->
<!--es-->
### Proyectos del autor<!--es-->
<!--es-->
Proyectos que he creado con Python que muestran lo que puedes crear después de aprender estos conceptos:<!--es-->
<!--es-->
- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )<!--es-->
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )<!--es-->
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )<!--es-->
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )<!--es-->
<!--es-->
### Práctica interactiva<!--es-->
<!--es-->
Continua practicando para que no se oxiden tus habilidades de programación.<!--es-->
<!--es-->
- [codechef.com](https://www.codechef.com/) ( 👔 )<!--es-->
- [codeforces.com](https://codeforces.com/)<!--es-->
- [codementor.io](https://www.codementor.io) ( 🧠 )<!--es-->
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )<!--es-->
- [codewars.com](https://www.codewars.com/)<!--es-->
- [exercism.io](https://exercism.io/)<!--es-->
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )<!--es-->
- [hackerearth.com](https://www.hackerearth.com/)<!--es-->
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )<!--es-->
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )<!--es-->
- [labex.io](https://labex.io/exercises/python)( 🧪 )<!--es-->
- [leetcode.com](https://leetcode.com/) ( 👔 )<!--es-->
- [projecteuler.net](https://projecteuler.net/)<!--es-->
- [replit.com](https://replit.com/)<!--es-->
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )<!--es-->
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )<!--es-->
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )<!--es-->
<!--es-->
## Astrónomos en el tiempo<!--es-->
<!--es-->
[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)<!--es-->
# Guide d’étude Python ultime<!--fr-->
<!--fr-->
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)<!--fr-->
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)<!--fr-->
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)<!--fr-->
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)<!--fr-->
<!--fr-->
Guide d’étude Python ultime pour les débutants comme pour les professionnels. 🐍 🐍 🐍<!--fr-->
<!--fr-->
```python<!--fr-->
print("Guide d’étude Python ultime")<!--fr-->
```<!--fr-->
<!--fr-->
[English](README.md) |<!--fr-->
[한국어](README.ko.md) |<!--fr-->
[繁体中文](README.zh_tw.md) |<!--fr-->
[Español](README.es.md) |<!--fr-->
[Deutsch](README.de.md) |<!--fr-->
[Français](README.fr.md) |<!--fr-->
[हिन्दी](README.hi.md) |<!--fr-->
[Português - Brasil](README.pt_br.md)<!--fr-->
<!--fr-->
<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" /><!--fr-->
<!--fr-->
## Motivation<!--fr-->
<!--fr-->
J’ai créé ce dépôt GitHub pour partager ce que j’ai appris sur le [cœur de Python](https://www.python.org/)<!--fr-->
au cours de plus de 5 années d’utilisation: en tant que diplômé universitaire, employé<!--fr-->
dans de grandes entreprises et contributeur open-source à des dépôts tels que<!--fr-->
[Celery](https://github.com/celery/celery) et<!--fr-->
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).<!--fr-->
J’espère voir de plus en plus de personnes apprendre Python et poursuivre leurs passions<!--fr-->
grâce à ce langage. 🎓<!--fr-->
<!--fr-->
## Objectifs<!--fr-->
<!--fr-->
Voici les principaux objectifs de ce guide :<!--fr-->
<!--fr-->
🏆 **Servir de ressource** pour les débutants en Python qui préfèrent apprendre de manière pratique.<!--fr-->
Ce dépôt contient une collection de modules indépendants pouvant être exécutés dans un IDE<!--fr-->
comme [PyCharm](https://www.jetbrains.com/pycharm/) ou dans le navigateur via<!--fr-->
[Replit](https://replit.com/languages/python3). Même un simple terminal suffit<!--fr-->
pour exécuter les exemples. La plupart des lignes contiennent des commentaires détaillés<!--fr-->
qui guident le lecteur pas à pas.<!--fr-->
Les utilisateurs sont encouragés à modifier le code source à leur guise tant que les<!--fr-->
routines `main` ne sont pas supprimées et que les programmes<!--fr-->
[s’exécutent correctement](runner.py) après chaque modification.<!--fr-->
<!--fr-->
🏆 **Servir de guide pur** pour ceux qui souhaitent revoir les concepts fondamentaux de Python.<!--fr-->
Seules les [bibliothèques intégrées](https://docs.python.org/3/library/) sont utilisées afin de<!--fr-->
présenter les concepts sans dépendre de notions spécifiques à un domaine. Ainsi, les<!--fr-->
bibliothèques open-source populaires comme `sqlalchemy`, `requests` ou `pandas`<!--fr-->
ne sont pas installées.<!--fr-->
Cependant, lire le code source de ces frameworks est fortement recommandé<!--fr-->
si ton objectif est de devenir un véritable<!--fr-->
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).<!--fr-->
<!--fr-->
## Pour commencer<!--fr-->
<!--fr-->
[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)<!--fr-->
<!--fr-->
Clique sur le badge ci-dessus pour lancer un environnement fonctionnel dans ton navigateur<!--fr-->
sans avoir besoin d’installer Git ou Python localement.<!--fr-->
Si ces outils sont déjà installés, tu peux cloner directement le dépôt.<!--fr-->
<!--fr-->
Une fois le dépôt accessible, tu es prêt à apprendre à partir des modules indépendants.<!--fr-->
Pour tirer le meilleur parti de chaque module, lis le code et exécute-le.<!--fr-->
<!--fr-->
Deux méthodes sont possibles :<!--fr-->
<!--fr-->
1. Exécuter un seul module :<!--fr-->
  `python ultimatepython/syntax/variable.py`<!--fr-->
2. Exécuter tous les modules :<!--fr-->
  `python runner.py`<!--fr-->
<!--fr-->
## Table des matières<!--fr-->
<!--fr-->
📚 = Ressource externe<!--fr-->
🍰 = Sujet débutant<!--fr-->
🤯 = Sujet avancé<!--fr-->
<!--fr-->
1. **À propos de Python**<!--fr-->
    - Vue d’ensemble : [Qu’est-ce que Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )<!--fr-->
    - Philosophie : [Le Zen de Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )<!--fr-->
    - Guide de style : [Guide de style du code Python](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )<!--fr-->
    - Modèle de données : [Modèle de données](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )<!--fr-->
    - Bibliothèque standard : [Bibliothèque standard Python](https://docs.python.org/3/library/) ( 📚, 🤯 )<!--fr-->
    - Fonctions intégrées : [Fonctions intégrées](https://docs.python.org/3/library/functions.html) ( 📚 )<!--fr-->
<!--fr-->
2. **Syntaxe**<!--fr-->
    - Variable : [Littéraux intégrés](ultimatepython/syntax/variable.py) ( 🍰 )<!--fr-->
    - Expression : [Opérations numériques](ultimatepython/syntax/expression.py) ( 🍰 )<!--fr-->
    - Opérateurs binaires : [Opérateurs binaires](ultimatepython/syntax/bitwise.py) ( 🍰 ), [Complément à un et à deux](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )<!--fr-->
    - Conditionnelle : [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )<!--fr-->
    - Boucle : [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )<!--fr-->
    - Fonction : [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )<!--fr-->
    - Opérateur morse : [Expressions d'affectation :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )<!--fr-->
    - Application d'arguments : [Positionnels uniquement / | Mots-clés uniquement *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )<!--fr-->
<!--fr-->
3. **Structures de données**<!--fr-->
    - Liste : [Opérations sur les listes](ultimatepython/data_structures/list.py) ( 🍰 )<!--fr-->
    - Tuple : [Opérations sur les tuples](ultimatepython/data_structures/tuple.py)<!--fr-->
    - Ensemble : [Opérations sur les ensembles](ultimatepython/data_structures/set.py)<!--fr-->
    - Dictionnaire : [Opérations sur les dictionnaires](ultimatepython/data_structures/dict.py) ( 🍰 )<!--fr-->
    - Union de dictionnaires : [Fusion de dictionnaires | et |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )<!--fr-->
    - Compréhension : [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)<!--fr-->
    - Chaîne : [Opérations sur les chaînes](ultimatepython/data_structures/string.py) ( 🍰 )<!--fr-->
    - Deque : [deque](ultimatepython/data_structures/deque.py) ( 🤯 )<!--fr-->
    - Namedtuple : [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )<!--fr-->
    - Defaultdict : [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )<!--fr-->
    - Outils d'itérateurs : [Outils d'itérateurs](ultimatepython/data_structures/itertools.py) ( 🤯 )<!--fr-->
    - Complexité temporelle : [Opérations CPython](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )<!--fr-->
<!--fr-->
4. **Classes**<!--fr-->
    - Classe basique : [Définition basique](ultimatepython/classes/basic_class.py) ( 🍰 )<!--fr-->
    - Héritage : [Héritage](ultimatepython/classes/inheritance.py) ( 🍰 )<!--fr-->
    - Classe abstraite : [Définition abstraite](ultimatepython/classes/abstract_class.py)<!--fr-->
    - Classe d’exception : [Définition d’exception](ultimatepython/classes/exception_class.py)<!--fr-->
    - Itérateur : [Définition d’itérateur | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )<!--fr-->
    - Encapsulation : [Définition de l’encapsulation](ultimatepython/classes/encapsulation.py)<!--fr-->
<!--fr-->
5. **Avancé**<!--fr-->
    - Décorateur : [Définition de décorateur | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )<!--fr-->
    - Gestion de fichiers : [File Handling](ultimatepython/advanced/file_handling.py) ( 🤯 )<!--fr-->
    - Gestionnaire de contexte : [Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )<!--fr-->
    - Ordre de résolution des méthodes : [mro](ultimatepython/advanced/mro.py) ( 🤯 )<!--fr-->
    - Mixin : [Définition de Mixin](ultimatepython/advanced/mixin.py) ( 🤯 )<!--fr-->
    - Métaclasse : [Définition de métaclasse](ultimatepython/advanced/meta_class.py) ( 🤯 )<!--fr-->
    - Thread : [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )<!--fr-->
    - Asyncio : [async | await](ultimatepython/advanced/async.py) ( 🤯 )<!--fr-->
    - Référence faible : [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )<!--fr-->
    - Benchmark : [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )<!--fr-->
    - Mocking : [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )<!--fr-->
    - Expressions régulières : [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )<!--fr-->
    - Format de données : [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )<!--fr-->
    - Date et heure : [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )<!--fr-->
    - Correspondance de motifs : [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )<!--fr-->
<!--fr-->
## Ressources supplémentaires<!--fr-->
<!--fr-->
👔 = Ressource d’entretien<!--fr-->
🧪 = Exemples de code<!--fr-->
🧠 = Idées de projets<!--fr-->
<!--fr-->
### Dépôts GitHub<!--fr-->
<!--fr-->
Continue d’apprendre grâce à ces ressources bien établies :<!--fr-->
<!--fr-->
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )<!--fr-->
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )<!--fr-->
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )<!--fr-->
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )<!--fr-->
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )<!--fr-->
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )<!--fr-->
- [vinta/awesome-python](https://github.com/vinta/awesome-python)<!--fr-->
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)<!--fr-->
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)<!--fr-->
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)<!--fr-->
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )<!--fr-->
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)<!--fr-->
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)<!--fr-->
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )<!--fr-->
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )<!--fr-->
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )<!--fr-->
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) ( 🧪 )<!--fr-->
<!--fr-->
### Projets de l'auteur<!--fr-->
<!--fr-->
Projets que j'ai créés avec Python qui montrent ce que vous pouvez créer après avoir appris ces concepts :<!--fr-->
<!--fr-->
- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )<!--fr-->
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )<!--fr-->
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )<!--fr-->
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )<!--fr-->
<!--fr-->
### Pratique interactive<!--fr-->
<!--fr-->
Continue à t’exercer pour ne pas perdre la main :<!--fr-->
<!--fr-->
- [codechef.com](https://www.codechef.com/) ( 👔 )<!--fr-->
- [codeforces.com](https://codeforces.com/)<!--fr-->
- [codementor.io](https://www.codementor.io) ( 🧠 )<!--fr-->
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )<!--fr-->
- [codewars.com](https://www.codewars.com/)<!--fr-->
- [exercism.io](https://exercism.io/)<!--fr-->
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )<!--fr-->
- [hackerearth.com](https://www.hackerearth.com/)<!--fr-->
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )<!--fr-->
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )<!--fr-->
- [labex.io](https://labex.io/exercises/python)( 🧪 )<!--fr-->
- [leetcode.com](https://leetcode.com/) ( 👔 )<!--fr-->
- [projecteuler.net](https://projecteuler.net/)<!--fr-->
- [replit.com](https://replit.com/)<!--fr-->
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )<!--fr-->
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )<!--fr-->
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )<!--fr-->
<!--fr-->
## Observateurs d'étoiles dans le temps<!--fr-->
<!--fr-->
[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)<!--fr-->
# अल्टीमेट Python अध्ययन गाइड<!--hi-->
<!--hi-->
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)<!--hi-->
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)<!--hi-->
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)<!--hi-->
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)<!--hi-->
<!--hi-->
नए और पेशेवर लोगों के लिए अल्टीमेट पायथन अध्ययन गाइड। 🐍 🐍 🐍<!--hi-->
<!--hi-->
```python<!--hi-->
print("Ultimate Python स्टडी गाइड")<!--hi-->
```<!--hi-->
<!--hi-->
[English](README.md) |<!--hi-->
[한국어](README.ko.md) |<!--hi-->
[繁体中文](README.zh_tw.md) |<!--hi-->
[Español](README.es.md) |<!--hi-->
[Deutsch](README.de.md) |<!--hi-->
[Français](README.fr.md) |<!--hi-->
[हिन्दी](README.hi.md) |<!--hi-->
[Português - Brasil](README.pt_br.md)<!--hi-->
<!--hi-->
<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" /><!--hi-->
<!--hi-->
## प्रेरणा<!--hi-->
<!--hi-->
मैंने यह गिटहब रिपोजिटरी [core Python](https://www.python.org/) के बारे में जो कुछ मैंने पिछले 5+ वर्षों में सीखा है, उसे साझा करने के लिए बनाई है। मैंने इसे एक कॉलेज ग्रेजुएट, बड़ी कंपनियों के कर्मचारी, और [Celery](https://github.com/celery/celery) और [Full Stack Python](https://github.com/mattmakai/fullstackpython.com) जैसी रिपोजिटरी के ओपन-सोर्स कंट्रीब्यूटर के रूप में उपयोग किया है। मैं यह देखने के लिए उत्सुक हूँ कि और लोग पायथन सीखें और इसके माध्यम से अपने जुनून को आगे बढ़ाएं। 🎓<!--hi-->
<!--hi-->
<!--hi-->
## लक्ष्य<!--hi-->
<!--hi-->
इस गाइड को बनाने के मुख्य लक्ष्य निम्नलिखित हैं:<!--hi-->
<!--hi-->
🏆 **संसाधन के रूप में सेवा देना** उन नए पायथन उपयोगकर्ताओं के लिए जो प्रैक्टिकल तरीके से सीखना पसंद करते हैं। इस रिपोजिटरी में स्वतंत्र मॉड्यूलों का एक संग्रह है, जिन्हें IDE जैसे [PyCharm](https://www.jetbrains.com/pycharm/) में या [Replit](https://replit.com/languages/python3) जैसे ब्राउज़र में चलाया जा सकता है। पुराने साधारण टर्मिनल में भी इन उदाहरणों को चलाया जा सकता है। अधिकतर लाइनों में बहुत ही अच्छे से लिखे गए comments होते हैं, जो पाठक को प्रोग्राम्स के प्रत्येक चरण के माध्यम से मार्गदर्शन करते हैं। उपयोगकर्ताओं को कोड में बदलाव करने के लिए प्रोत्साहित किया जाता है, बशर्ते कि `main` रूटीन को हटाया न जाए और हर परिवर्तन के बाद [सफलतापूर्वक चलाया जाए](runner.py)।<!--hi-->
<!--hi-->
🏆 **शुद्ध गाइड के रूप में सेवा देना** उन लोगों के लिए जो मुख्य पायथन अवधारणाओं को फिर से समझना चाहते हैं। केवल [बिल्ट-इन लाइब्रेरीज़](https://docs.python.org/3/library/) का उपयोग किया गया है ताकि इन अवधारणाओं को बिना किसी विशेष डोमेन की अवधारणाओं के सरलता से समझाया जा सके। इसी कारण से लोकप्रिय ओपन-सोर्स लाइब्रेरीज़ और फ्रेमवर्क (जैसे `sqlalchemy`, `requests`, `pandas`) को इंस्टॉल नहीं किया गया है। हालांकि, इन फ्रेमवर्क्स के स्रोत कोड को पढ़ना प्रेरणादायक है और यदि आपका लक्ष्य एक सच्चे [Pythonista](https://www.urbandictionary.com/define.php?term=pythonista) बनने का है तो इसे ज़रूर पढ़ना चाहिए।<!--hi-->
<!--hi-->
<!--hi-->
## शुरूआत<!--hi-->
<!--hi-->
[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)<!--hi-->
<!--hi-->
ऊपर दिए गए बैज पर क्लिक करें ताकि आप ब्राउज़र में एक कार्यशील वातावरण शुरू कर सकें, इसके लिए आपके स्थानीय मशीन पर Git और पायथन की आवश्यकता नहीं होगी। यदि ये आवश्यकताएँ पहले से ही पूरी हो चुकी हैं, तो आप सीधे रिपोजिटरी को क्लोन कर सकते हैं।<!--hi-->
<!--hi-->
एक बार जब रिपोजिटरी उपलब्ध हो जाती है, तो आप स्वतंत्र मॉड्यूल से सीखने के लिए तैयार हैं। प्रत्येक मॉड्यूल का अधिकतम लाभ उठाने के लिए, मॉड्यूल का कोड पढ़ें और इसे चलाएं। मॉड्यूल चलाने के दो तरीके हैं:<!--hi-->
<!--hi-->
1. एकल मॉड्यूल चलाएं: `python ultimatepython/syntax/variable.py`<!--hi-->
2. सभी मॉड्यूल चलाएं: `python runner.py`<!--hi-->
<!--hi-->
## विषय सूची<!--hi-->
<!--hi-->
📚 = बाहरी स्रोत,<!--hi-->
🍰 = शुरुआती विषय,<!--hi-->
🤯 = उन्नत विषय<!--hi-->
<!--hi-->
<!--hi-->
1. **पायथन के बारे में**<!--hi-->
    - अवलोकन: [पायथन क्या है](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )<!--hi-->
    - डिज़ाइन दर्शन: [पायथन का ज़ेन](https://www.python.org/dev/peps/pep-0020/) ( 📚 )<!--hi-->
    - शैली मार्गदर्शिका: [पायथन कोड के लिए शैली मार्गदर्शिका](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )<!--hi-->
    - डेटा मॉडल: [डेटा मॉडल](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )<!--hi-->
    - मानक पुस्तकालय: [पायथन मानक पुस्तकालय](https://docs.python.org/3/library/) ( 📚, 🤯 )<!--hi-->
    - अंतर्निहित कार्य: [अंतर्निहित कार्य](https://docs.python.org/3/library/functions.html) ( 📚 )<!--hi-->
2. **सिंटेक्स**<!--hi-->
    - वेरिएबल: [अंतर्निहित लिटरल](ultimatepython/syntax/variable.py) ( 🍰 )<!--hi-->
    - अभिव्यक्ति: [संख्यात्मक ऑपरेशन्स](ultimatepython/syntax/expression.py) ( 🍰 )<!--hi-->
    - बाइनरी: [बाइनरी ऑपरेटर](ultimatepython/syntax/bitwise.py) ( 🍰 ), [एक्स/टू का पूरक](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )<!--hi-->
    - कंडीशनल: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )<!--hi-->
    - लूप: [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )<!--hi-->
    - फ़ंक्शन: [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )<!--hi-->
    - वॉलरस ऑपरेटर: [असाइनमेंट एक्सप्रेशन :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )<!--hi-->
    - तर्क प्रवर्तन: [केवल स्थितीय / | केवल कीवर्ड *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )<!--hi-->
3. **डेटा संरचनाएँ**<!--hi-->
    - लिसट: [लिसट ऑपरेशन्स](ultimatepython/data_structures/list.py) ( 🍰 )<!--hi-->
    - ट्यूपल: [ट्यूपल ऑपरेशन्स](ultimatepython/data_structures/tuple.py)<!--hi-->
    - सेट: [सेट ऑपरेशन्स](ultimatepython/data_structures/set.py)<!--hi-->
    - डिक्ट: [डिक्शनरी ऑपरेशन्स](ultimatepython/data_structures/dict.py) ( 🍰 )<!--hi-->
    - डिक्शनरी यूनियन: [डिक्शनरी मर्ज | और |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )<!--hi-->
    - संकलन: [लिसट | ट्यूपल | सेट | डिक्ट](ultimatepython/data_structures/comprehension.py)<!--hi-->
    - स्ट्रिंग: [स्ट्रिंग ऑपरेशन्स](ultimatepython/data_structures/string.py) ( 🍰 )<!--hi-->
    - डेक: [डेक](ultimatepython/data_structures/deque.py) ( 🤯 )<!--hi-->
    - नामित ट्यूपल: [नामित ट्यूपल](ultimatepython/data_structures/namedtuple.py) ( 🤯 )<!--hi-->
    - डिफ़ॉल्ट डिक्ट: [डिफ़ॉल्ट डिक्ट](ultimatepython/data_structures/defaultdict.py) ( 🤯 )<!--hi-->
    - इटरेटर टूल्स: [इटरेटर टूल्स](ultimatepython/data_structures/itertools.py) ( 🤯 )<!--hi-->
    - समय कोम्पलेक्सिटी: [cPython ऑपरेशन्स](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )<!--hi-->
4. **क्लासेज़**<!--hi-->
    - बेसिक क्लास: [बेसिक परिभाषा](ultimatepython/classes/basic_class.py) ( 🍰 )<!--hi-->
    - इन्हरिटैंस: [इन्हरिटैंस](ultimatepython/classes/inheritance.py) ( 🍰 )<!--hi-->
    - एैबस्टराक्ट क्लास: [एैबस्टराक्ट परिभाषा](ultimatepython/classes/abstract_class.py)<!--hi-->
    - एक्सेपशन क्लास: [एक्सेपशन परिभाषा](ultimatepython/classes/exception_class.py)<!--hi-->
    - इटरेटर क्लास: [इटरेटर परिभाषा | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )<!--hi-->
    - ऐनकैपसुलेषन: [ऐनकैपसुलेषन परिभाषा](ultimatepython/classes/encapsulation.py)<!--hi-->
5. **उन्नत**<!--hi-->
    - डेकोरेटर: [डेकोरेटर परिभाषा | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )<!--hi-->
    - फ़ाइल प्रबंधन: [फ़ाइल प्रबंधन](ultimatepython/advanced/file_handling.py) ( 🤯 )<!--hi-->
    - संदर्भ प्रबंधक: [संदर्भ प्रबंधक](ultimatepython/advanced/context_manager.py) ( 🤯 )<!--hi-->
    - मेथड रिज़ॉल्यूशन क्रम: [mro](ultimatepython/advanced/mro.py) ( 🤯 )<!--hi-->
    - मिक्सिन: [मिक्सिन परिभाषा](ultimatepython/advanced/mixin.py) ( 🤯 )<!--hi-->
    - मेटाक्लास: [मेटाक्लास परिभाषा](ultimatepython/advanced/meta_class.py) ( 🤯 )<!--hi-->
    - थ्रेड: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )<!--hi-->
    - एसिंको: [async | await](ultimatepython/advanced/async.py) ( 🤯 )<!--hi-->
    - वीक रेफरेंस: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )<!--hi-->
    - बेंचमार्क: [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )<!--hi-->
    - मॉकिंग: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )<!--hi-->
    - नियमित अभिव्यक्ति: [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )<!--hi-->
    - डेटा फ़ॉर्मेट: [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )<!--hi-->
    - दिनांक और समय: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )<!--hi-->
    - पैटर्न मिलान: [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )<!--hi-->
<!--hi-->
<!--hi-->
## अतिरिक्त संसाधन<!--hi-->
<!--hi-->
👔 = इंटरव्यू संसाधन,<!--hi-->
🧪 = कोड नमूने,<!--hi-->
🧠 = प्रोजेक्ट विचार<!--hi-->
<!--hi-->
<!--hi-->
### गिटहब रिपॉजिटरी<!--hi-->
<!--hi-->
अन्य उच्च मानक संसाधनों से पढ़कर सीखना जारी रखें।<!--hi-->
<!--hi-->
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )<!--hi-->
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )<!--hi-->
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )<!--hi-->
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )<!--hi-->
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )<!--hi-->
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )<!--hi-->
- [vinta/awesome-python](https://github.com/vinta/awesome-python)<!--hi-->
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)<!--hi-->
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)<!--hi-->
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)<!--hi-->
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )<!--hi-->
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)<!--hi-->
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)<!--hi-->
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )<!--hi-->
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )<!--hi-->
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )<!--hi-->
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) ( 🧪 )<!--hi-->
<!--hi-->
### लेखक की परियोजनाएँ<!--hi-->
<!--hi-->
Python से बनाई गई परियोजनाएं जो दिखाती हैं कि इन अवधारणाओं को सीखने के बाद आप क्या बना सकते हैं:<!--hi-->
<!--hi-->
- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )<!--hi-->
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )<!--hi-->
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )<!--hi-->
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )<!--hi-->
<!--hi-->
### इंटरैक्टिव प्रैक्टिस<!--hi-->
<!--hi-->
अभ्यास करते रहें ताकि आपकी कोडिंग कौशल खराब न हों।<!--hi-->
<!--hi-->
- [codechef.com](https://www.codechef.com/) ( 👔 )<!--hi-->
- [codeforces.com](https://codeforces.com/)<!--hi-->
- [codementor.io](https://www.codementor.io) ( 🧠 )<!--hi-->
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )<!--hi-->
- [codewars.com](https://www.codewars.com/)<!--hi-->
- [exercism.io](https://exercism.io/)<!--hi-->
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )<!--hi-->
- [hackerearth.com](https://www.hackerearth.com/)<!--hi-->
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )<!--hi-->
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )<!--hi-->
- [labex.io](https://labex.io/exercises/python)( 🧪 )<!--hi-->
- [leetcode.com](https://leetcode.com/) ( 👔 )<!--hi-->
- [projecteuler.net](https://projecteuler.net/)<!--hi-->
- [replit.com](https://replit.com/)<!--hi-->
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )<!--hi-->
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )<!--hi-->
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )<!--hi-->
<!--hi-->
## समय के खगोलशास्त्री<!--hi-->
<!--hi-->
[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)<!--hi-->
# Ultimate Python 학습 가이드<!--ko-->
<!--ko-->
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)<!--ko-->
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)<!--ko-->
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)<!--ko-->
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)<!--ko-->
<!--ko-->
초보자와 전문가 모두를 위한 최고의 Python 학습 가이드입니다. 🐍 🐍 🐍<!--ko-->
<!--ko-->
```python<!--ko-->
print("Ultimate Python 학습 가이드")<!--ko-->
```<!--ko-->
<!--ko-->
[English](README.md) |<!--ko-->
[한국어](README.ko.md) |<!--ko-->
[繁体中文](README.zh_tw.md) |<!--ko-->
[Español](README.es.md) |<!--ko-->
[Deutsch](README.de.md) |<!--ko-->
[Français](README.fr.md) |<!--ko-->
[हिन्दी](README.hi.md) |<!--ko-->
[Português - Brasil](README.pt_br.md)<!--ko-->
<!--ko-->
<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" /><!--ko-->
<!--ko-->
## 동기<!--ko-->
<!--ko-->
이 GitHub 저장소는 대학 졸업 후, 대규모 회사에서 근무하면서<!--ko-->
그리고 [Celery](https://github.com/celery/celery)와 [Full Stack Python](https://github.com/mattmakai/fullstackpython.com) 같은 오픈소스 프로젝트에 기여하면서<!--ko-->
지난 5년 이상 동안 배운 [core Python](https://www.python.org/)에 대한 지식을 공유하기 위해 만들었습니다.<!--ko-->
저는 더 많은 사람들이 Python을 배우고 자신의 열정을 추구하길 기대합니다. 🎓<!--ko-->
<!--ko-->
## 목표<!--ko-->
<!--ko-->
이 가이드를 만드는 주요 목표는 다음과 같습니다:<!--ko-->
<!--ko-->
🏆 실습 학습을 선호하는 Python 초보자를 위한 **학습 자료를 제공합니다.**<!--ko-->
이 저장소에는 [PyCharm](https://www.jetbrains.com/pycharm/)과 같은 IDE 및 [Replit](https://replit.com/languages/python3)와 같은 브라우저에서 실행할 수 있는 독립형 모듈 모음이 있습니다. 기본 터미널에서도 예제를 실행할 수 있습니다.<!--ko-->
대부분의 코드 라인에 프로그램이 단계별로 어떤 작업을 하는지 안내하는 신중하게 작성된 주석이 있습니다.<!--ko-->
사용자는 `main` 루틴을 삭제하지 않고, 각 변경 후에 [성공적으로 실행](runner.py)되는 한 소스 코드를 얼마든지 수정할 수 있습니다.<!--ko-->
<!--ko-->
🏆 core Python 개념을 다시 복습하고 싶은 사람들을 위한 **순수 가이드를 제공합니다.**<!--ko-->
여기서는 오직 [내장 라이브러리](https://docs.python.org/3/library/)만을 사용하여 이러한 개념을 도메인 특화된 개념의 오버헤드 없이 전달합니다.<!--ko-->
따라서 유명한 오픈소스 라이브러리와 프레임워크(`sqlalchemy`, `requests`, `pandas` 등)는 설치되어 있지 않습니다.<!--ko-->
그러나, 당신의 목표가 진정한 진정한 [Pythonista](https://www.urbandictionary.com/define.php?term=pythonista)이 되는 것 이라면 이러한 프레임워크의 소스 코드를 읽는 것은 매우 고무적이고 권장이 됩니다.<!--ko-->
<!--ko-->
## 시작하기<!--ko-->
<!--ko-->
[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)<!--ko-->
<!--ko-->
로컬 컴퓨터에 Git 및 Python을 설치하지 않고도 브라우저에서 작업 환경을 시작하려면 위의 배지를 클릭하세요. 이러한<!--ko-->
요구 사항이 이미 충족된 경우, 저장소를 바로 clone해도 됩니다.<!--ko-->
<!--ko-->
저장소에 접근할 수 있게 되면 단독 모듈에서 배울 준비가 된 것입니다. 각 모듈을 최대한 활용하려면 모듈 코드를<!--ko-->
읽고 실행하십시오. 모듈을 실행하는 두 가지 방법이 있습니다:<!--ko-->
<!--ko-->
1. 단일 모듈 실행 : `python ultimatepython/syntax/variable.py`<!--ko-->
2. 전체 모듈 실행 : `python runner.py`<!--ko-->
<!--ko-->
## 목차<!--ko-->
<!--ko-->
📚 = 외부 리소스,<!--ko-->
🍰 = 초급 주제,<!--ko-->
🤯 = 고급 주제<!--ko-->
<!--ko-->
1. **Python 정보**<!--ko-->
    - 개요 : [Python이란 무엇인가](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )<!--ko-->
    - 디자인 철학 : [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )<!--ko-->
    - 스타일 가이드 : [Python 코드 스타일 가이드](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )<!--ko-->
    - 데이터 모델 : [데이터 모델](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )<!--ko-->
    - 표준 라이브러리 : [Python 표준 라이브러리](https://docs.python.org/3/library/) ( 📚, 🤯 )<!--ko-->
    - 내장 함수 : [내장 함수](https://docs.python.org/3/library/functions.html) ( 📚 )<!--ko-->
2. **통사론**<!--ko-->
    - 변수 : [내장 리터럴](ultimatepython/syntax/variable.py) ( 🍰 )<!--ko-->
    - 표현식 : [숫자 연산](ultimatepython/syntax/expression.py) ( 🍰 )<!--ko-->
    - 비트 연산 : [비트 연산자](ultimatepython/syntax/bitwise.py) ( 🍰 ), [1의 보수/2의 보수](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )<!--ko-->
    - 조건문 : [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )<!--ko-->
    - 반복문 : [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )<!--ko-->
    - 함수 : [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )<!--ko-->
    - 바다코끼리 연산자 : [할당 표현식 :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )<!--ko-->
    - 인수 강제 : [위치 전용 / | 키워드 전용 *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )<!--ko-->
3. **데이터 구조**<!--ko-->
    - 리스트 : [리스트 연산](ultimatepython/data_structures/list.py) ( 🍰 )<!--ko-->
    - 튜플 : [튜플 연산](ultimatepython/data_structures/tuple.py)<!--ko-->
    - 세트 : [세트 연산](ultimatepython/data_structures/set.py)<!--ko-->
    - 딕셔너리 : [딕셔너리 연산](ultimatepython/data_structures/dict.py) ( 🍰 )<!--ko-->
    - 딕셔너리 합병 : [딕셔너리 병합 | 및 |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )<!--ko-->
    - 컴프리헨션 : [리스트 | 튜플 | 세트 | 딕셔너리](ultimatepython/data_structures/comprehension.py)<!--ko-->
    - 문자열 : [문자열 연산](ultimatepython/data_structures/string.py) ( 🍰 )<!--ko-->
    - 덱: [deque](ultimatepython/data_structures/deque.py) ( 🤯 )<!--ko-->
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )<!--ko-->
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )<!--ko-->
    - 이터레이터 도구: [이터레이터 도구](ultimatepython/data_structures/itertools.py) ( 🤯 )<!--ko-->
    - 시간 복잡도 : [cPython 연산](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )<!--ko-->
4. **클래스**<!--ko-->
    - 기본 클래스 : [기본 정의](ultimatepython/classes/basic_class.py) ( 🍰 )<!--ko-->
    - 계승: [계승](ultimatepython/classes/inheritance.py) ( 🍰 )<!--ko-->
    - 추상 클래스 : [추상 정의](ultimatepython/classes/abstract_class.py)<!--ko-->
    - 예외 클래스 : [예외 정의](ultimatepython/classes/exception_class.py)<!--ko-->
    - 이터레이터 클래스 : [이터레이터 정의 | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )<!--ko-->
    - 캡슐화: [캡슐화 정의](ultimatepython/classes/encapsulation.py)<!--ko-->
5. **고급**<!--ko-->
    - 데코레이터 : [데코레이터 정의 | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )<!--ko-->
    - 파일 처리: [파일 처리](ultimatepython/advanced/file_handling.py) ( 🤯 )<!--ko-->
    - 컨텍스트 매니저 : [컨텍스트 매니저](ultimatepython/advanced/context_manager.py) ( 🤯 )<!--ko-->
    - 메서드 결정 순서 : [mro](ultimatepython/advanced/mro.py) ( 🤯 )<!--ko-->
    - 믹스인 : [믹스인 정의](ultimatepython/advanced/mixin.py) ( 🤯 )<!--ko-->
    - 메타클래스 : [메타클래스 정의](ultimatepython/advanced/meta_class.py) ( 🤯 )<!--ko-->
    - 스레드 : [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )<!--ko-->
    - Asyncio : [async | await](ultimatepython/advanced/async.py) ( 🤯 )<!--ko-->
    - 약한 참조 : [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )<!--ko-->
    - 벤치마크 : [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )<!--ko-->
    - 모킹 : [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )<!--ko-->
    - 정규식 : [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )<!--ko-->
    - 데이터 포맷 : [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )<!--ko-->
    - 날짜와 시간 : [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )<!--ko-->
    - 패턴 매칭: [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )<!--ko-->
<!--ko-->
## 추가 자료<!--ko-->
<!--ko-->
👔 = 인터뷰 자료,<!--ko-->
🧪 = 코드 샘플,<!--ko-->
🧠 = 프로젝트 아이디어<!--ko-->
<!--ko-->
### GitHub 저장소<!--ko-->
<!--ko-->
잘 알려진 다른 자료를 읽으면서 계속 배우세요.<!--ko-->
<!--ko-->
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )<!--ko-->
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )<!--ko-->
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )<!--ko-->
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )<!--ko-->
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )<!--ko-->
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )<!--ko-->
- [vinta/awesome-python](https://github.com/vinta/awesome-python)<!--ko-->
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)<!--ko-->
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)<!--ko-->
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)<!--ko-->
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )<!--ko-->
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)<!--ko-->
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)<!--ko-->
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )<!--ko-->
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )<!--ko-->
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )<!--ko-->
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) ( 🧪 )<!--ko-->
<!--ko-->
### 저자의 프로젝트<!--ko-->
<!--ko-->
이러한 개념을 익힌 후 무엇을 만들 수 있는지 보여주는 Python으로 제작한 프로젝트들입니다:<!--ko-->
<!--ko-->
- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )<!--ko-->
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )<!--ko-->
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )<!--ko-->
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )<!--ko-->
<!--ko-->
### 대화형 연습<!--ko-->
<!--ko-->
코딩 실력이 녹슬지 않기 위해 계속 연습하세요.<!--ko-->
<!--ko-->
- [codechef.com](https://www.codechef.com/) ( 👔 )<!--ko-->
- [codeforces.com](https://codeforces.com/)<!--ko-->
- [codementor.io](https://www.codementor.io) ( 🧠 )<!--ko-->
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )<!--ko-->
- [codewars.com](https://www.codewars.com/)<!--ko-->
- [exercism.io](https://exercism.io/)<!--ko-->
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )<!--ko-->
- [hackerearth.com](https://www.hackerearth.com/)<!--ko-->
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )<!--ko-->
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )<!--ko-->
- [labex.io](https://labex.io/exercises/python)( 🧪 )<!--ko-->
- [leetcode.com](https://leetcode.com/) ( 👔 )<!--ko-->
- [projecteuler.net](https://projecteuler.net/)<!--ko-->
- [replit.com](https://replit.com/)<!--ko-->
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )<!--ko-->
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )<!--ko-->
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )<!--ko-->
<!--ko-->
## 시대의 별 관측자<!--ko-->
<!--ko-->
[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)<!--ko-->
# Ultimate Python - O seu guia de estudos de Python definitivo<!--pt_br-->
<!--pt_br-->
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)<!--pt_br-->
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)<!--pt_br-->
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)<!--pt_br-->
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)<!--pt_br-->
<!--pt_br-->
Guia de estudo definitivo de Python para iniciantes e profissionais. 🐍 🐍 🐍<!--pt_br-->
<!--pt_br-->
```python<!--pt_br-->
print("Ultimate Python - O seu guia de estudos de Python definitivo")<!--pt_br-->
```<!--pt_br-->
<!--pt_br-->
[English](README.md) |<!--pt_br-->
[한국어](README.ko.md) |<!--pt_br-->
[繁体中文](README.zh_tw.md) |<!--pt_br-->
[Español](README.es.md) |<!--pt_br-->
[Deutsch](README.de.md) |<!--pt_br-->
[Français](README.fr.md) |<!--pt_br-->
[हिन्दी](README.hi.md) |<!--pt_br-->
[Português - Brasil](README.pt_br.md)<!--pt_br-->
<!--pt_br-->
<img src="images/ultimatepython.webp" alt="Ultimate Python - O seu guia de estudos de Python definitivo" width="250px" /><!--pt_br-->
<!--pt_br-->
## Motivação<!--pt_br-->
<!--pt_br-->
Eu criei este repositório a fim de compartilhar o que eu aprendi sobre o [básico de Python](https://www.python.org/) nos último 5+ anos de uso como graduado universitário, um empregado em uma empresa de grande porte e um contribuidor de repositórios open-source como [Celery](https://github.com/celery/celery) e<!--pt_br-->
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).<!--pt_br-->
Eu estou ansiono para ver mais pessoas aprendendo Python e buscando suas paixões através disso. 🎓<!--pt_br-->
<!--pt_br-->
## Objetivos<!--pt_br-->
<!--pt_br-->
Aqui estão os principais objetivos da criação deste guia:<!--pt_br-->
<!--pt_br-->
🏆 **Servir como um recurso** para iniciantes em Python que preferem aprender na prática.<!--pt_br-->
Este repositório possui uma coleção de módulos autônomos que podem ser executados em um IDE como [PyCharm](https://www.jetbrains.com/pycharm/) e no navegador como [Replit](https://replit.com/languages/python3). Até mesmo um terminal simples funcionará com os exemplos.<!--pt_br-->
A maioria das linhas possui comentários cuidadosamente elaborados que guiam o leitor passo a passo sobre o que os programas estão fazendo. Usuários são incentivados a modificar o código fonte em qualquer lugar, desde que as rotinas `main` não sejam excluídas e [sejam executadas com sucesso](runner.py) após cada alteração.<!--pt_br-->
<!--pt_br-->
🏆 **Servir como um guia prático** para aqueles que queiram revisitar os conceitos básicos de Python.<!--pt_br-->
Apenas [blibliotecas internas](https://docs.python.org/3/library/) são utilizadas para que esses conceitos possam ser transmitidos sem a sobrecarga de conceitos específicos de domínio.<!--pt_br-->
Dessa forma, bibliotecas e frameworks populares de código aberto (como por exemplo `sqlalchemy`, `requests`,<!--pt_br-->
`pandas`) não são instalados. No entanto, ler o código fonte desses estruturas é inspirador e altamente recomendado se o seu objetivo é se tornar um verdadeiro [Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).<!--pt_br-->
<!--pt_br-->
## Começando<!--pt_br-->
<!--pt_br-->
[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)<!--pt_br-->
<!--pt_br-->
Click no emblema acima para criar um ambiente de trabalho no navegador sem a necessidade de instalar Git e Python na sua máquina local. Se esses requisitos já forem atendidos (se você já tem isso instalado), sinta-se à vontade para clonar o repositório diretamente.<!--pt_br-->
<!--pt_br-->
Uma vez que o repositório esteja acessível você está pronto para aprender com os módulos independentes. Para aproveitar ao máximo cada módulo, leia o código  do módulo e execute-o.<!--pt_br-->
<!--pt_br-->
Existem duas maneiras de rodar os módulos:<!--pt_br-->
<!--pt_br-->
1. Execute um módulo único: `python ultimatepython/syntax/variable.py`<!--pt_br-->
2. Execute todos os módulos: `python runner.py`<!--pt_br-->
<!--pt_br-->
## Índice<!--pt_br-->
<!--pt_br-->
📚 = Recurso externo,<!--pt_br-->
🍰 = Tópico para iniciantes,<!--pt_br-->
🤯 = Tópico avançado<!--pt_br-->
<!--pt_br-->
1. **Sobre Python**<!--pt_br-->
    - Visão geral: [O que é Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )<!--pt_br-->
    - Filosofia de design: [O zen do Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )<!--pt_br-->
    - Guia de estilo: [Guia de estilo para código Python](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )<!--pt_br-->
    - Modelo de dados: [Modelo de dados](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )<!--pt_br-->
    - Biblioteca padrão: [A Biblioteca padrão do Python](https://docs.python.org/3/library/) ( 📚, 🤯 )<!--pt_br-->
    - Funções integradas: [Funções integradas](https://docs.python.org/3/library/functions.html) ( 📚 )<!--pt_br-->
2. **Sintaxe**<!--pt_br-->
    - Variável: [Literais integrados](ultimatepython/syntax/variable.py) ( 🍰 )<!--pt_br-->
    - Expressão: [Operações numéricas](ultimatepython/syntax/expression.py) ( 🍰 )<!--pt_br-->
    - Bitwise: [Operadores bitwise](ultimatepython/syntax/bitwise.py) ( 🍰 ), [Complemento de Um/Dois](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )<!--pt_br-->
    - Condicional: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )<!--pt_br-->
    - Loop/Laço: [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )<!--pt_br-->
    - Função: [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )<!--pt_br-->
    - Operador morsa: [Expressões de atribuição :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )<!--pt_br-->
    - Aplicação de argumentos: [Somente posicional / | Somente palavra-chave *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )<!--pt_br-->
3. **Estrutura de dados**<!--pt_br-->
    - Lista: [Operações de lista](ultimatepython/data_structures/list.py) ( 🍰 )<!--pt_br-->
    - Tupla: [Operações de tuplas](ultimatepython/data_structures/tuple.py)<!--pt_br-->
    - Conjunto: [Operações de conjuntos](ultimatepython/data_structures/set.py)<!--pt_br-->
    - Dicionário: [Operações de dicionários](ultimatepython/data_structures/dict.py) ( 🍰 )<!--pt_br-->
    - União de dicionários: [Fusão de dicionários | e |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )<!--pt_br-->
    - Comprehension: [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)<!--pt_br-->
    - String: [Operações de String](ultimatepython/data_structures/string.py) ( 🍰 )<!--pt_br-->
    - Deque: [deque](ultimatepython/data_structures/deque.py) ( 🤯 )<!--pt_br-->
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )<!--pt_br-->
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )<!--pt_br-->
    - Ferramentas de iteradores: [Ferramentas de iteradores](ultimatepython/data_structures/itertools.py) ( 🤯 )<!--pt_br-->
    - Time complexity: [Operações de cPython](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )<!--pt_br-->
4. **Classes**<!--pt_br-->
    - O básico de classes: [Definição de classe](ultimatepython/classes/basic_class.py) ( 🍰 )<!--pt_br-->
    - Herança: [Herança](ultimatepython/classes/inheritance.py) ( 🍰 )<!--pt_br-->
    - Classe abstrata: [Definição de classe abstrata](ultimatepython/classes/abstract_class.py)<!--pt_br-->
    - Classe de exceção: [Definição de Classe de exceção](ultimatepython/classes/exception_class.py)<!--pt_br-->
    - Classe Iterator: [Definição de classe Iterator | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )<!--pt_br-->
    - Encapsulamento: [Definição de encapsulamento](ultimatepython/classes/encapsulation.py)<!--pt_br-->
5. **Avançado**<!--pt_br-->
    - Decorator: [Definição de decorator | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )<!--pt_br-->
    - Manuseio de arquivos: [Manuseio de arquivos](ultimatepython/advanced/file_handling.py) ( 🤯 )<!--pt_br-->
    - Gerenciador de contexto: [Gerenciador de contexto](ultimatepython/advanced/context_manager.py) ( 🤯 )<!--pt_br-->
    - Ordem de resolução do método: [mro](ultimatepython/advanced/mro.py) ( 🤯 )<!--pt_br-->
    - Mixin: [Definição de  mixin](ultimatepython/advanced/mixin.py) ( 🤯 )<!--pt_br-->
    - Metaclass: [Definição de metaclass](ultimatepython/advanced/meta_class.py) ( 🤯 )<!--pt_br-->
    - Thread: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )<!--pt_br-->
    - Asyncio: [async | await](ultimatepython/advanced/async.py) ( 🤯 )<!--pt_br-->
    - Referência fraca: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )<!--pt_br-->
    - Benchmark: [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )<!--pt_br-->
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )<!--pt_br-->
    - Expressões regulares (regexp): [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )<!--pt_br-->
    - Formato de dados: [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )<!--pt_br-->
    - Datetime: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )<!--pt_br-->
    - Correspondência de padrões: [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )<!--pt_br-->
<!--pt_br-->
## Recursos adicionais<!--pt_br-->
<!--pt_br-->
👔 = Recurso para entrevista,<!--pt_br-->
🧪 = Exemplos de código,<!--pt_br-->
🧠 = Ideias para projetos<!--pt_br-->
<!--pt_br-->
### Repositórios GitHub<!--pt_br-->
<!--pt_br-->
Continue aprendendo lendo outros recursos bem conceituados.<!--pt_br-->
<!--pt_br-->
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )<!--pt_br-->
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )<!--pt_br-->
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )<!--pt_br-->
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )<!--pt_br-->
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )<!--pt_br-->
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )<!--pt_br-->
- [vinta/awesome-python](https://github.com/vinta/awesome-python)<!--pt_br-->
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)<!--pt_br-->
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)<!--pt_br-->
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)<!--pt_br-->
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )<!--pt_br-->
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)<!--pt_br-->
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)<!--pt_br-->
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )<!--pt_br-->
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )<!--pt_br-->
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )<!--pt_br-->
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) ( 🧪 )<!--pt_br-->
<!--pt_br-->
### Projetos do autor<!--pt_br-->
<!--pt_br-->
Projetos que construí com Python que mostram o que você pode criar após aprender esses conceitos:<!--pt_br-->
<!--pt_br-->
- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )<!--pt_br-->
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )<!--pt_br-->
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )<!--pt_br-->
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )<!--pt_br-->
<!--pt_br-->
### Prática interativa<!--pt_br-->
<!--pt_br-->
Continue praticando para que suas habilidades de codificação não enferrujem.<!--pt_br-->
<!--pt_br-->
- [codechef.com](https://www.codechef.com/) ( 👔 )<!--pt_br-->
- [codeforces.com](https://codeforces.com/)<!--pt_br-->
- [codementor.io](https://www.codementor.io) ( 🧠 )<!--pt_br-->
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )<!--pt_br-->
- [codewars.com](https://www.codewars.com/)<!--pt_br-->
- [exercism.io](https://exercism.io/)<!--pt_br-->
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )<!--pt_br-->
- [hackerearth.com](https://www.hackerearth.com/)<!--pt_br-->
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )<!--pt_br-->
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )<!--pt_br-->
- [labex.io](https://labex.io/exercises/python)( 🧪 )<!--pt_br-->
- [leetcode.com](https://leetcode.com/) ( 👔 )<!--pt_br-->
- [projecteuler.net](https://projecteuler.net/)<!--pt_br-->
- [replit.com](https://replit.com/)<!--pt_br-->
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )<!--pt_br-->
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )<!--pt_br-->
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )<!--pt_br-->
<!--pt_br-->
## Astrônomos no tempo<!--pt_br-->
<!--pt_br-->
[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)<!--pt_br-->
# Ultimate Python 學習大綱<!--zh_tw-->
<!--zh_tw-->
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)<!--zh_tw-->
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)<!--zh_tw-->
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)<!--zh_tw-->
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)<!--zh_tw-->
<!--zh_tw-->
Ultimate Python 學習大綱 - 適用於新手和專業人士。🐍 🐍 🐍<!--zh_tw-->
<!--zh_tw-->
```python<!--zh_tw-->
print("Ultimate Python 學習大綱")<!--zh_tw-->
```<!--zh_tw-->
<!--zh_tw-->
[English](README.md) |<!--zh_tw-->
[한국어](README.ko.md) |<!--zh_tw-->
[繁体中文](README.zh_tw.md) |<!--zh_tw-->
[Español](README.es.md) |<!--zh_tw-->
[Deutsch](README.de.md) |<!--zh_tw-->
[Français](README.fr.md) |<!--zh_tw-->
[हिन्दी](README.hi.md) |<!--zh_tw-->
[Português - Brasil](README.pt_br.md)<!--zh_tw-->
<!--zh_tw-->
<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" /><!--zh_tw-->
<!--zh_tw-->
## 動力<!--zh_tw-->
<!--zh_tw-->
我為了分享過去五年作為一個學生，大公司員工，以及開源（例如 Celery 和 Full Stack Python）貢獻者所習得的知識而創<!--zh_tw-->
建了這個代碼倉庫。我期待更多人能抱持熱忱並開始一段與Python的美好旅程。🎓<!--zh_tw-->
<!--zh_tw-->
## 目標<!--zh_tw-->
<!--zh_tw-->
這是創建本指南的主要目標：<!--zh_tw-->
<!--zh_tw-->
🏆 **為喜歡動手學習的Python新手提供資源。** 本存儲庫集合了不同題目的獨立模組範例，而每個模組可以獨立在普通<!--zh_tw-->
終端機（Terminal），IDE（如PyCharm）或者瀏覽器（如Repl.it）中運行。範例中的註解都經過精心編寫，引導讀者逐步了解程<!--zh_tw-->
式流程。在不刪除主例程（main)並在修改後成功運行大前題下，我鼓勵讀者修改源代碼作練習。<!--zh_tw-->
<!--zh_tw-->
🏆 **為想重溫Python核心概念的程式員提供指南。** 本存儲庫主要借助內置庫（builtin libraries）作重溫工具，<!--zh_tw-->
故不需額外安裝開源庫（如`sqlalchemy`，`requests`，`pandas`）。但是，如果您的目標是成為一個真正的Python<!--zh_tw-->
達人（Pythonista)，那麼我會鼓勵您閱讀這些源代碼，而激發靈感。<!--zh_tw-->
<!--zh_tw-->
## 學習之旅<!--zh_tw-->
<!--zh_tw-->
[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)<!--zh_tw-->
<!--zh_tw-->
單擊上面的徽章就可在瀏覽器中啟動工作環境，而無需在電腦上額外安裝Git和Python。當你完成啟動，請複製這存儲庫。<!--zh_tw-->
當你可以開啟你所複製存儲庫後，您就準備好Python學習之旅!善用每個模組，請細讀註解並嘗試運行模組代碼。<!--zh_tw-->
<!--zh_tw-->
有兩種運行模組的方式：<!--zh_tw-->
<!--zh_tw-->
1. 運行單一模組：`python ultimatepython/syntax/variable.py`<!--zh_tw-->
2. 運行所有模組：`python runner.py`<!--zh_tw-->
<!--zh_tw-->
## 目錄<!--zh_tw-->
<!--zh_tw-->
📚 = 外部資源，<!--zh_tw-->
🍰 = 入門題目，<!--zh_tw-->
🤯 = 進階題目<!--zh_tw-->
<!--zh_tw-->
1. **關於 Python**<!--zh_tw-->
    - 概述：[什麼是 Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )<!--zh_tw-->
    - 設計理念：[Python之格言](https://www.python.org/dev/peps/pep-0020/) ( 📚 )<!--zh_tw-->
    - 樣式指南：[Python代碼樣式指南](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )<!--zh_tw-->
    - 數據模型：[數據模型](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )<!--zh_tw-->
    - 標準庫：[Python標準庫](https://docs.python.org/3/library/) ( 📚, 🤯 )<!--zh_tw-->
    - 內置函式：[內置函式](https://docs.python.org/3/library/functions.html) ( 📚 )<!--zh_tw-->
2. **語法**<!--zh_tw-->
    - 變數：[內置值](ultimatepython/syntax/variable.py) ( 🍰 )<!--zh_tw-->
    - 運算式：[數值運算](ultimatepython/syntax/expression.py) ( 🍰 )<!--zh_tw-->
    - 按位: [中的位元運算符](ultimatepython/syntax/bitwise.py) ( 🍰 ), [一個的補語/補碼](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )<!--zh_tw-->
    - 條件運算式：[if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )<!--zh_tw-->
    - 迴圈：[for迴圈 | while迴圈](ultimatepython/syntax/loop.py) ( 🍰 )<!--zh_tw-->
    - 定義函式：[def | lambda](ultimatepython/syntax/function.py) ( 🍰 )<!--zh_tw-->
    - 海象運算子：[賦值表達式 :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )<!--zh_tw-->
    - 參數強制：[僅位置 / | 僅關鍵字 *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )<!--zh_tw-->
3. **資料結構**<!--zh_tw-->
    - 列表：[列表操作](ultimatepython/data_structures/list.py) ( 🍰 )<!--zh_tw-->
    - 元組：[元組操作](ultimatepython/data_structures/tuple.py)<!--zh_tw-->
    - 集合：[集合操作](ultimatepython/data_structures/set.py)<!--zh_tw-->
    - 字典：[字典操作](ultimatepython/data_structures/dict.py) ( 🍰 )<!--zh_tw-->
    - 字典聯合：[字典合併 | 和 |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )<!--zh_tw-->
    - 綜合：[list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)<!--zh_tw-->
    - 字串：[字串操作](ultimatepython/data_structures/string.py) ( 🍰 )<!--zh_tw-->
    - 雙端隊列：[deque](ultimatepython/data_structures/deque.py) ( 🤯 )<!--zh_tw-->
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )<!--zh_tw-->
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )<!--zh_tw-->
    - 迭代器工具：[迭代器工具](ultimatepython/data_structures/itertools.py) ( 🤯 )<!--zh_tw-->
    - 時間複雜度：[cPython操作](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )<!--zh_tw-->
4. **類別**<!--zh_tw-->
    - 基本類別：[基本定義](ultimatepython/classes/basic_class.py) ( 🍰 )<!--zh_tw-->
    - 抽象類別：[抽象定義](ultimatepython/classes/abstract_class.py)<!--zh_tw-->
    - 異常類別：[異常定義](ultimatepython/classes/exception_class.py)<!--zh_tw-->
    - 迭代類別：[迭代器定義](ultimatepython/classes/iterator_class.py) ( 🤯 )<!--zh_tw-->
    - 封裝: [封裝定義](ultimatepython/classes/encapsulation.py)<!--zh_tw-->
5. **進階技巧**<!--zh_tw-->
    - 裝飾器：[Decorator definition | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )<!--zh_tw-->
    - 文件處理: [File Handling](ultimatepython/advanced/file_handling.py) ( 🤯 )<!--zh_tw-->
    - 資源管理器：[Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )<!--zh_tw-->
    - 方法解析順序：[mro](ultimatepython/advanced/mro.py) ( 🤯 )<!--zh_tw-->
    - Mixin：[Mixin定義](ultimatepython/advanced/mixin.py) ( 🤯 )<!--zh_tw-->
    - 元類：[Metaclass定義](ultimatepython/advanced/meta_class.py) ( 🤯 )<!--zh_tw-->
    - 執行緒：[ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )<!--zh_tw-->
    - 異步：[async | await](ultimatepython/advanced/async.py) ( 🤯 )<!--zh_tw-->
    - 弱引用：[weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )<!--zh_tw-->
    - 基準：[cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )<!--zh_tw-->
    - 模擬：[MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )<!--zh_tw-->
    - 正規表示式：[search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )<!--zh_tw-->
    - 數據格式：[json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )<!--zh_tw-->
    - 日期時間: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )<!--zh_tw-->
    - 模式匹配：[match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )<!--zh_tw-->
<!--zh_tw-->
## 額外資源<!--zh_tw-->
<!--zh_tw-->
👔 = 面試資源，<!--zh_tw-->
🧪 = 代碼範例，<!--zh_tw-->
🧠 = 項目構想<!--zh_tw-->
<!--zh_tw-->
### GitHub儲存庫<!--zh_tw-->
<!--zh_tw-->
通過閱讀其他備受尊重的資源來繼續學習。<!--zh_tw-->
<!--zh_tw-->
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔, 🧪 )<!--zh_tw-->
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔, 🧪 )<!--zh_tw-->
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )<!--zh_tw-->
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )<!--zh_tw-->
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )<!--zh_tw-->
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )<!--zh_tw-->
- [vinta/awesome-python](https://github.com/vinta/awesome-python)<!--zh_tw-->
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)<!--zh_tw-->
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)<!--zh_tw-->
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)<!--zh_tw-->
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )<!--zh_tw-->
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)<!--zh_tw-->
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)<!--zh_tw-->
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )<!--zh_tw-->
<!--zh_tw-->
### 作者的專案<!--zh_tw-->
<!--zh_tw-->
我用 Python 構建的專案，展示學習這些概念後可以創造的內容：<!--zh_tw-->
<!--zh_tw-->
- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )<!--zh_tw-->
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )<!--zh_tw-->
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )<!--zh_tw-->
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )<!--zh_tw-->
<!--zh_tw-->
### 互動練習<!--zh_tw-->
<!--zh_tw-->
繼續練習才能使您的編碼技能不會生疏。<!--zh_tw-->
<!--zh_tw-->
- [codechef.com](https://www.codechef.com/) ( 👔 )<!--zh_tw-->
- [codeforces.com](https://codeforces.com/)<!--zh_tw-->
- [codementor.io](https://www.codementor.io) ( 🧠 )<!--zh_tw-->
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )<!--zh_tw-->
- [codewars.com](https://www.codewars.com/)<!--zh_tw-->
- [exercism.io](https://exercism.io/)<!--zh_tw-->
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )<!--zh_tw-->
- [hackerearth.com](https://www.hackerearth.com/)<!--zh_tw-->
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )<!--zh_tw-->
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )<!--zh_tw-->
- [labex.io](https://labex.io/exercises/python)( 🧪 )<!--zh_tw-->
- [leetcode.com](https://leetcode.com/) ( 👔 )<!--zh_tw-->
- [projecteuler.net](https://projecteuler.net/)<!--zh_tw-->
- [replit.com](https://replit.com/)<!--zh_tw-->
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )<!--zh_tw-->
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )<!--zh_tw-->
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )<!--zh_tw-->
<!--zh_tw-->
## 歷代觀星者<!--zh_tw-->
<!--zh_tw-->
[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)<!--zh_tw-->
