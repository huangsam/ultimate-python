# Guía de estudio "Ultimate Python"

[![CircleCI](https://img.shields.io/circleci/build/github/huangsam/ultimate-python)](https://circleci.com/gh/huangsam/ultimate-python)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/master/LICENSE)
[![r/Python](https://img.shields.io/reddit/subreddit-subscribers/Python)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

Guía de estudio "Ultimate Python" para principiantes y profesionales. :snake: :snake: :snake:

```python
print("Guía de estudio 'Ultimate Python'")
```

[English](README.md) |
[한국어](README.ko.md) |
[繁体中文](README.zh_tw.md) |
[Español](README.es.md)

## Motivación

Creé este repositorio de GitHub para compartir lo que he aprendido sobre [Python](https://www.python.org/)
en estos últimos 5 años utilizándolo como un graduado de universidad, un empleado en compañías de gran
escala y un contribuidor de código abierto en repositorios como [Celery](https://github.com/celery/celery)
y [Full Stack Python](https://github.com/mattmakai/fullstackpython.com).
Espero ver a más personas aprendiendo Python y persiguiendo su pasión a través de él. :mortar_board:

## Objetivos

Estos son los objetivos principales de esta guía:

:trophy: **Servir como un recurso** para principiantes en Python que prefieren aprender por su cuenta.
Este repositorio lista una colección de módulos independientes los cuales pueden ser ejecutados en
un IDE como [PyCharm](https://www.jetbrains.com/pycharm/) e incluso en el navegador, como
[Repl.it](https://repl.it/languages/python3). Sin embargo, una vieja terminal funcionará igualmente
con los ejemplos. La mayoría de las líneas de código tienen comentarios útiles que ayudan a guiar
al lector paso a paso a través del proceso que un programa está ejecutando. Los usuarios
pueden modificar el código fuente en cualquier parte siempre y cuando las rutinas principales (`main`)
no sean eliminadas y sean [ejecutadas con éxito](runner.py) luego de cada cambio.

:trophy: **Servir como una guía pura** para aquellos que quieren reforzar los conceptos base de
Python. Son utilizadas solo las [librerías integradas](https://docs.python.org/3/library/) para que
estos conceptos puedan ser aprendidos sin el esfuerzo de aprender conceptos específicos.
Siguiendo esta declaración, librerías y frameworks (como `sqlalchemy`, `requests`, `pandas`) no
están instalados. No obstante, leer el código fuente de estos frameworks es inspirador y altamente
recomendado si tu objetivo es convertirte en un verdadero
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).

## Empezando

[![Run on Repl.it](https://repl.it/badge/github/huangsam/ultimate-python)](https://repl.it/github/huangsam/ultimate-python)

Clickea la imagen de arriba para crear un ambiente de trabajo en el navegador sin la necesidad
de tener Git y Python instalados en tu ordenador local. Si estos requisitos ya se cumplen,
puedes clonar el repositorio directamente.

Una vez que el repositodio es accesible, estás listo para aprender de los módulos independientes.
Para aprender el máximo de cada módulo, lee el código del módulo y ejecútalo.
Hay dos maneras de ejecutar los módulos:

1. Ejecuta un solo módulo: `python ultimatepython/syntax/variable.py`
2. Ejecuta todos los módulos: `python runner.py`

## Contenido

:books: = Recurso externo,
:cake: = Tema principiante,
:exploding_head: = Tema avanzado

1. **Sobre Python**
    - Descripción: [¿Qué es Python?](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) (:books:, :cake:)
    - Filosofía de diseño: [El Zen de Python](https://www.python.org/dev/peps/pep-0020/) (:books:)
    - Guía de estilos: [Guía de estilos para código de Python](https://www.python.org/dev/peps/pep-0008/) (:books:, :exploding_head:)
    - Modelo de datos: [Modelo de datos](https://docs.python.org/3/reference/datamodel.html) (:books:, :exploding_head:)
    - Librería estándar: [La librería estándar de Python](https://docs.python.org/3/library/) (:books:, :exploding_head:)
    - Funciones integradas: [Funciones integradas](https://docs.python.org/3/library/functions.html) (:books:)
2. **Sintaxis**
    - Variables: [Literales integrados](ultimatepython/syntax/variable.py) (:cake:)
    - Expresiones: [Operaciones numéricas](ultimatepython/syntax/expression.py) (:cake:)
    - Condicionales: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) (:cake:)
    - Iteraciones: [for-loop | while-loop](ultimatepython/syntax/loop.py) (:cake:)
    - Funciones: [def | lambda](ultimatepython/syntax/function.py) (:cake:)
3. **Estructura de datos**
    - Lista: [Operaciones con listas](ultimatepython/data_structures/list.py) (:cake:)
    - Tuple: [Operaciones con tuples](ultimatepython/data_structures/tuple.py)
    - Set: [Operaciones con sets](ultimatepython/data_structures/set.py)
    - Diccionario: [Operaciones con dicts](ultimatepython/data_structures/dict.py) (:cake:)
    - Comprensión: [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)
    - String: [Operaciones con strings](ultimatepython/data_structures/string.py) (:cake:)
    - Deque: [deque](ultimatepython/data_structures/deque.py) (:exploding_head:)
    - Complejidad de tiempo: [Operaciones de cPython](https://wiki.python.org/moin/TimeComplexity) (:books:, :exploding_head:)
4. **Clases**
    - Clase básica: [Definición de básica](ultimatepython/classes/basic_class.py) (:cake:)
    - Clase abstracta: [Definición de abstracta](ultimatepython/classes/abstract_class.py)
    - Clase de excepción: [Defición de excepción](ultimatepython/classes/exception_class.py)
    - Clase iteradora: [Definición de iteradora | yield](ultimatepython/classes/iterator_class.py) (:exploding_head:)
5. **Avanzado**
    - Decorador: [Definición de decorador | wraps](ultimatepython/advanced/decorator.py) (:exploding_head:)
    - Gestor de contexto: [Gestores de contexto](ultimatepython/advanced/context_manager.py) (:exploding_head:)
    - Orden de resolución de método (mro por sus siglas en inglés): [mro](ultimatepython/advanced/mro.py) (:exploding_head:)
    - Mixin: [Definición de Mixin](ultimatepython/advanced/mixin.py) (:exploding_head:)
    - Metaclase: [Definición de metaclase](ultimatepython/advanced/meta_class.py) (:exploding_head:)
    - Thread: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) (:exploding_head:)
    - Asyncio: [async | await](ultimatepython/advanced/async.py) (:exploding_head:)
    - Weak reference: [weakref](ultimatepython/advanced/weak_ref.py) (:exploding_head:)
    - Referencia: [cProfile | pstats](ultimatepython/advanced/benchmark.py) (:exploding_head:)
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) (:exploding_head:)
    - Expresiones regulares: [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) (:exploding_head:)
    - Formatos de datos: [json | xml | csv](ultimatepython/advanced/data_format.py) (:exploding_head:)
    - Fecha y hora: [datetime | timezone](ultimatepython/advanced/datetime.py) (:exploding_head:)

## Recursos adicionales

:necktie: = Recurso de entrevista,
:test_tube: = Ejemplos de código,
:brain: = Ideas de proyecto

### Repositorios de GitHub

Sigue aprendiendo al leer otros buenos recursos.

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

### Práctica interactiva

No dejes de practicar para que no se oxiden tus habilidades de programación.

- [leetcode.com](https://leetcode.com/) (:necktie:)
- [hackerrank.com](https://www.hackerrank.com/) (:necktie:)
- [kaggle.com](https://www.kaggle.com/) (:brain:)
- [exercism.io](https://exercism.io/)
- [projecteuler.net](https://projecteuler.net/)
