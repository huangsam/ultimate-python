# Ultimativer Python-Lernführer

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

Der ultimative Python-Lernführer für Einsteiger und Profis gleichermaßen. 🐍 🐍 🐍

```python
print("Ultimativer Python-Lernführer")
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

Ich habe dieses GitHub-Repository erstellt, um meine Erkenntnisse über [core Python](https://www.python.org/)
in den letzten 5 Jahren als Hochschulabsolvent, Angestellter in
großen Unternehmen und als Open-Source-Mitarbeiter von Repositories wie
[Celery](https://github.com/celery/celery) und
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com) weiterzugeben.
Ich freue mich darauf, dass noch mehr Menschen Python lernen und damit ihren Leidenschaften nachgehen. 🎓

## Ziele

Dies sind die Hauptziele bei der Erstellung dieses Leitfadens:

🏆 **Als Ressource fungieren** für Python-Neulinge, die es vorziehen, praktisch zu lernen.
Dieses Repository enthält eine Sammlung von eigenständigen Modulen, die in einer IDE
 wie [PyCharm](https://www.jetbrains.com/pycharm/) oder im Browser via
 [Replit](https://replit.com/languages/python3) ausgeführt werden können. Ein Terminal funktioniert
 ebenfalls gut für die Beispiele. Die meisten Zeilen enthalten sorgfälltig formulierte Kommentare, die den Leser
 Schritt für Schritt durch die Abläufe führen. Benutzer werden ermutigt, den Quellcode zu ändern,
 sofern die `main`-Routinen nicht entfernt werden und die Programme nach Änderungen weiterhin erfolgreich
 ausgeführt werden (siehe `runner.py`).

🏆 **Als reiner Leitfaden dienen** für diejenigen, die die wichtigsten Python-Konzepte wiederholen möchten.
Wo nur [builtin libraries](https://docs.python.org/3/library/) genutzt werden, so dass
diese Konzepte ohne den Overhead der bereichsspezifischen Konzepte vermittelt werden können. Als
beliebte Open-Source-Bibliotheken und -Frameworks (d.h. `sqlalchemy`, `requests`,
`pandas`) nicht installiert sind. Das Lesen des Quellcodes dieser Frameworks ist jedoch
inspirierend und wird dringend empfohlen, wenn Sie ein echter Profi werden wollen.
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).

## Erste Schritte

[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)

Klicken Sie auf das obige Abzeichen, um eine Arbeitsumgebung im Browser zu starten, ohne
ohne dass Sie Git und Python auf Ihrem lokalen Rechner installiert haben müssen. Wenn diese Voraussetzungen
bereits erfüllt sind, können Sie das Repository direkt klonen.

Sobald das Repository zugänglich ist, können Sie mit den eigenständigen
Modulen lernen. Um den größtmöglichen Nutzen aus jedem Modul zu ziehen, lesen Sie den Modulcode und führen Sie ihn aus.
Es gibt zwei Möglichkeiten, die Module auszuführen:

1. Führen Sie ein einzelnes Modul aus: `python ultimatepython/syntax/variable.py`
2. Führen Sie alle Module aus: `python runner.py`

## Inhaltsübersicht

📚 = Externe Ressource,
🍰 = Thema für Anfänger,
🤯 = Fortgeschrittenes Thema

1. **Über Python**
    - Overview: [What is Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )
    - Design philosophy: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )
    - Style guide: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )
    - Data model: [Data model](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )
    - Standard library: [The Python Standard Library](https://docs.python.org/3/library/) ( 📚, 🤯 )
    - Built-in functions: [Built-in Functions](https://docs.python.org/3/library/functions.html) ( 📚 )
2. **Syntax**
    - Variable: [Built-in literals](ultimatepython/syntax/variable.py) ( 🍰 )
    - Expression: [Numeric operations](ultimatepython/syntax/expression.py) ( 🍰 )
    - Bitwise: [Bitwise operators](ultimatepython/syntax/bitwise.py) ( 🍰 ), [One's/Two's Complement](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )
    - Conditional: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )
    - Loop: [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )
    - Function: [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )
3. **Daten-Strukturen**
    - List: [List operations](ultimatepython/data_structures/list.py) ( 🍰 )
    - Tuple: [Tuple operations](ultimatepython/data_structures/tuple.py)
    - Set: [Set operations](ultimatepython/data_structures/set.py)
    - Dict: [Dictionary operations](ultimatepython/data_structures/dict.py) ( 🍰 )
    - Comprehension: [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)
    - String: [String operations](ultimatepython/data_structures/string.py) ( 🍰 )
    - Deque: [deque](ultimatepython/data_structures/deque.py) ( 🤯 )
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )
    - Time complexity: [cPython operations](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )
4. **Klassen**
    - Basic class: [Basic definition](ultimatepython/classes/basic_class.py) ( 🍰 )
    - Inheritance: [Inheritance](ultimatepython/classes/inheritance.py) ( 🍰 )
    - Abstract class: [Abstract definition](ultimatepython/classes/abstract_class.py)
    - Exception class: [Exception definition](ultimatepython/classes/exception_class.py)
    - Iterator class: [Iterator definition | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )
    - Encapsulation: [Encapsulation definition](ultimatepython/classes/encapsulation.py)
5. **Fortgeschrittene**
    - Decorator: [Decorator definition | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )
    - File Handling: [File Handling](ultimatepython/advanced/file_handling.py) ( 🤯 )
    - Context manager: [Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )
    - Method resolution order: [mro](ultimatepython/advanced/mro.py) ( 🤯 )
    - Mixin: [Mixin definition](ultimatepython/advanced/mixin.py) ( 🤯 )
    - Metaclass: [Metaclass definition](ultimatepython/advanced/meta_class.py) ( 🤯 )
    - Thread: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )
    - Asyncio: [async | await](ultimatepython/advanced/async.py) ( 🤯 )
    - Weak reference: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )
    - Benchmark: [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )
    - Regular expression: [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )
    - Data format: [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )
    - Datetime: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )

## Zusätzliche Ressourcen

👔 = Interview-Ressource,
🧪 = Code-Beispiele,
🧠 = Projektideen

### GitHub repositories

Lernen Sie weiter, indem Sie von anderen Quellen lesen.

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )
- [karan/Projects](https://github.com/karan/Projects) ( 🧠 )
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )
- [vinta/awesome-python](https://github.com/vinta/awesome-python)
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( 🧪 )
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) ( 🧪 )

### Interaktive Übungen

Üben Sie weiter, damit Ihre Programmierkenntnisse nicht einrosten.

- [codechef.com](https://www.codechef.com/) ( 👔 )
- [codeforces.com](https://codeforces.com/)
- [codementor.io](https://www.codementor.io) ( 🧠 )
- [coderbyte.com](https://www.coderbyte.com/) ( 👔 )
- [codewars.com](https://www.codewars.com/)
- [exercism.io](https://exercism.io/)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )
- [hackerearth.com](https://www.hackerearth.com/)
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )
- [labex.io](https://labex.io/exercises/python)( 🧪 )
- [leetcode.com](https://leetcode.com/) ( 👔 )
- [projecteuler.net](https://projecteuler.net/)
- [replit.com](https://replit.com/)
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 👔 )
- [fullstakpython.org](https://fullstackpython.org/) ( 🧪 )

## Sternengucker der Zeit

[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)
