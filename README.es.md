# Guía de estudio "Python Definitivo"

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

Guía de estudio "Python Definitivo" para principiantes y profesionales. 🐍 🐍 🐍

```python
print("Guía de estudio 'Python Definitivo'")
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

## Motivación

Creé este repositorio de GitHub para compartir lo que he aprendido sobre [Python](https://www.python.org/)
durante más de 5 años usándolo como graduado de universidad, empleado en grandes empresas y como contribuidor
de código abierto en repositorios como [Celery](https://github.com/celery/celery) y
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).
Espero ver a más personas aprendiendo Python y persiguiendo su pasión a través de él. 🎓

## Objetivos

Estos son los objetivos principales de esta guía:

🏆 **Servir como un recurso** para principiantes de Python que prefieren aprender de forma práctica.
Este repositorio contiene una colección de módulos independientes que pueden ejecutarse en
un IDE como [PyCharm](https://www.jetbrains.com/pycharm/) y en el navegador, como
[Replit](https://replit.com/languages/python3). Incluso una terminal sencilla funcionará con los ejemplos.
La mayoría de las líneas de código tienen comentarios útiles que guían al lector paso a paso.
Se anima a los usuarios a modificar el código fuente en cualquier parte siempre y cuando las rutinas
principales (`main`) no se eliminen y los programas se ejecuten con éxito tras cada cambio (ver `runner.py`).

🏆 **Servir como una guía pura** para aquellos que quieren reforzar los conceptos base de
Python. Se utilizan sólo las [librerías integradas](https://docs.python.org/3/library/) para que
estos conceptos puedan adquirirse sin el esfuerzo de aprender conocimientos de dominios específicos.
Por ello no se han instalado librerías y entornos de código abierto populares (como `sqlalchemy`,
`requests`, `pandas`). No obstante, leer el código fuente de estos frameworks es inspirador y altamente
recomendado si tu objetivo es convertirte en un verdadero
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).

## Empezando

[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)

Haz clic en la imagen de arriba para crear un ambiente de trabajo en el navegador sin necesidad
de tener Git y Python instalados en tu ordenador local. Si estos requisitos ya se cumplen,
puedes clonar el repositorio directamente.

Una vez que el repositorio sea accesible, estás listo para aprender de los módulos independientes.
Para aprender el máximo de cada módulo, lee el código del módulo y ejecútalo.
Hay dos maneras de ejecutar los módulos:

1. Ejecuta un solo módulo: `python ultimatepython/fundamentals/variable.py`
2. Ejecuta todos los módulos: `python runner.py`

## Contenido

📚 = Recurso externo,
🍰 = Tema principiante,
🤯 = Tema avanzado

1. **Sobre Python**
    - Resumen: [¿Qué es Python?](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )
    - Filosofía de diseño: [El Zen de Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )
    - Guía de estilos: [Guía de estilos para código de Python](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )
    - Modelo de datos: [Modelo de datos](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )
    - Librería estándar: [La librería estándar de Python](https://docs.python.org/3/library/) ( 📚, 🤯 )
    - Funciones integradas: [Funciones integradas](https://docs.python.org/3/library/functions.html) ( 📚 )
2. **Fundamentos**
    - Variables: [Literales integrados](ultimatepython/fundamentals/variable.py) ( 🍰 )
    - Expresiones: [Operaciones numéricas](ultimatepython/fundamentals/expression.py) ( 🍰 )
    - Cadena: [Operaciones con strings](ultimatepython/fundamentals/string.py) ( 🍰 )
    - Lista: [Operaciones con listas](ultimatepython/fundamentals/list.py) ( 🍰 )
    - Tupla: [Operaciones con tuplas](ultimatepython/fundamentals/tuple.py)
    - Set: [Operaciones con sets](ultimatepython/fundamentals/set.py)
    - Diccionario: [Operaciones con dicts](ultimatepython/fundamentals/dict.py) ( 🍰 )
    - Condicionales: [if | if-else | if-elif-else](ultimatepython/fundamentals/conditional.py) ( 🍰 )
    - Iteraciones: [for-loop | while-loop](ultimatepython/fundamentals/loop.py) ( 🍰 )
    - Funciones: [def | lambda](ultimatepython/fundamentals/function.py) ( 🍰 )
    - Comprensión: [list | tuple | set | dict](ultimatepython/fundamentals/comprehension.py)
3. **Programación orientada a objetos**
    - Clase básica: [Definición de básica](ultimatepython/oop/basic_class.py) ( 🍰 )
    - Herencia: [Herencia](ultimatepython/oop/inheritance.py) ( 🍰 )
    - Encapsulación: [Definición de encapsulación](ultimatepython/oop/encapsulation.py)
    - Clase abstracta: [Definición de abstracta](ultimatepython/oop/abstract_class.py)
    - Clase de excepción: [Definición de excepción](ultimatepython/oop/exception_class.py)
    - Clase iteradora: [Definición de iteradora | yield](ultimatepython/oop/iterator_class.py) ( 🤯 )
    - Mixin: [Definición de Mixin](ultimatepython/oop/mixin.py) ( 🤯 )
    - Orden de resolución de método (MRO por sus siglas en inglés): [mro](ultimatepython/oop/mro.py) ( 🤯 )
4. **Librería estándar**
    - Manejo de archivos: [Manejo de archivos](ultimatepython/stdlib/file_handling.py) ( 🤯 )
    - Expresiones regulares: [search | findall | match | fullmatch](ultimatepython/stdlib/regex.py) ( 🤯 )
    - Formatos de datos: [json | xml | csv](ultimatepython/stdlib/data_format.py) ( 🤯 )
    - Fecha y hora: [datetime | timezone](ultimatepython/stdlib/date_time.py) ( 🤯 )
5. **Avanzado**
    - Decorador: [Definición de decorador | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )
    - Gestor de contexto: [Gestores de contexto](ultimatepython/advanced/context_manager.py) ( 🤯 )
    - Metaclase: [Definición de metaclase](ultimatepython/advanced/meta_class.py) ( 🤯 )
    - Referencias débiles: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )
    - Operador morsa: [Expresiones de asignación :=](ultimatepython/advanced/walrus_operator.py) ( 🤯 )
    - Aplicación de argumentos: [Solo posicional / | Solo palabra clave *](ultimatepython/advanced/arg_enforcement.py) ( 🤯 )
    - Coincidencia de patrones: [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )
    - Template strings: [Template strings (PEP 750)](ultimatepython/advanced/template_strings.py) ( 🤯 )
6. **Concurrencia**
    - Hilos: [ThreadPoolExecutor](ultimatepython/concurrency/thread.py) ( 🤯 )
    - Asyncio: [async | await](ultimatepython/concurrency/async.py) ( 🤯 )
    - Subinterpretes: [concurrent.interpreters](ultimatepython/concurrency/subinterpreters.py) ( 🤯 )
7. **Ingeniería**
    - Mocking: [MagicMock | PropertyMock | patch](ultimatepython/engineering/mocking.py) ( 🤯 )
    - Referencia: [cProfile | pstats](ultimatepython/engineering/benchmark.py) ( 🤯 )
    - Bit a bit: [Operadores bit a bit](ultimatepython/engineering/bitwise.py) ( 🍰 ), [Complemento a uno/dos](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )
    - Deque: [deque](ultimatepython/engineering/deque.py) ( 🤯 )
    - Namedtuple: [namedtuple](ultimatepython/engineering/namedtuple.py) ( 🤯 )
    - Defaultdict: [defaultdict](ultimatepython/engineering/defaultdict.py) ( 🤯 )
    - Herramientas de iteradores: [Herramientas de iteradores](ultimatepython/engineering/itertools.py) ( 🤯 )
    - Unión de diccionarios: [Fusión de diccionarios | y |=](ultimatepython/engineering/dict_union.py) ( 🤯 )
    - Heap: [heap queue](ultimatepython/engineering/heap.py) ( 🤯 )
    - Complejidad de tiempo: [Operaciones de cPython](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )

## Recursos adicionales

👔 = Recurso de entrevista,
🧪 = Ejemplos de código,
🧠 = Ideas para proyecto

### Repositorios de GitHub

Sigue aprendiendo leyendo otros buenos recursos.

#### Python fundamental y patrones

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)

#### Ciencia de datos y aprendizaje automático

- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)

#### Listas curadas e ideas de proyectos

- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )
- [vinta/awesome-python](https://github.com/vinta/awesome-python)
- [lukasmasuch/best-of-python](https://github.com/lukasmasuch/best-of-python)
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )

### Práctica interactiva

Continua practicando para que no se oxiden tus habilidades de programación.

#### Preparación para entrevistas

- [leetcode.com](https://leetcode.com/) ( 👔 )
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )

#### Aprendizaje práctico

- [exercism.io](https://exercism.io/)
- [codewars.com](https://www.codewars.com/)
- [labex.io](https://labex.io/exercises/python) ( 🧪 )
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 🧪 )
- [projecteuler.net](https://projecteuler.net/)
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )
