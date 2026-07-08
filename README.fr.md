# Guide d’étude Python ultime

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

Guide d’étude Python ultime pour les débutants comme pour les professionnels. 🐍 🐍 🐍

```python
print("Guide d’étude Python ultime")
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

J’ai créé ce dépôt GitHub pour partager ce que j’ai appris sur le [cœur de Python](https://www.python.org/)
au cours de plus de 5 années d’utilisation: en tant que diplômé universitaire, employé
dans de grandes entreprises et contributeur open-source à des dépôts tels que
[Celery](https://github.com/celery/celery) et
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).
J’espère voir de plus en plus de personnes apprendre Python et poursuivre leurs passions
grâce à ce langage. 🎓

## Objectifs

Voici les principaux objectifs de ce guide :

🏆 **Servir de ressource** pour les débutants en Python qui préfèrent apprendre de manière pratique.
Ce dépôt contient une collection de modules indépendants pouvant être exécutés dans un IDE
comme [PyCharm](https://www.jetbrains.com/pycharm/) ou dans le navigateur via
[Replit](https://replit.com/languages/python3). Même un simple terminal suffit
pour exécuter les exemples. La plupart des lignes contiennent des commentaires détaillés
qui guident le lecteur pas à pas.
Les utilisateurs sont encouragés à modifier le code source à leur guise tant que les
routines `main` ne sont pas supprimées et que les programmes
[s’exécutent correctement](runner.py) après chaque modification.

🏆 **Servir de guide pur** pour ceux qui souhaitent revoir les concepts fondamentaux de Python.
Seules les [bibliothèques intégrées](https://docs.python.org/3/library/) sont utilisées afin de
présenter les concepts sans dépendre de notions spécifiques à un domaine. Ainsi, les
bibliothèques open-source populaires comme `sqlalchemy`, `requests` ou `pandas`
ne sont pas installées.
Cependant, lire le code source de ces frameworks est fortement recommandé
si ton objectif est de devenir un véritable
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).

## Pour commencer

[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)

Clique sur le badge ci-dessus pour lancer un environnement fonctionnel dans ton navigateur
sans avoir besoin d’installer Git ou Python localement.
Si ces outils sont déjà installés, tu peux cloner directement le dépôt.

Une fois le dépôt accessible, tu es prêt à apprendre à partir des modules indépendants.
Pour tirer le meilleur parti de chaque module, lis le code et exécute-le.

Deux méthodes sont possibles :

1. Exécuter un seul module :
  `python ultimatepython/fundamentals/variable.py`
2. Exécuter tous les modules :
  `python runner.py`

## Table des matières

📚 = Ressource externe
🍰 = Sujet débutant
🤯 = Sujet avancé

1. **À propos de Python**
    - Vue d’ensemble : [Qu’est-ce que Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )
    - Philosophie : [Le Zen de Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )
    - Guide de style : [Guide de style du code Python](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )
    - Modèle de données : [Modèle de données](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )
    - Bibliothèque standard : [Bibliothèque standard Python](https://docs.python.org/3/library/) ( 📚, 🤯 )
    - Fonctions intégrées : [Fonctions intégrées](https://docs.python.org/3/library/functions.html) ( 📚 )

2. **Fondations**
    - Variable : [Littéraux intégrés](ultimatepython/fundamentals/variable.py) ( 🍰 )
    - Expression : [Opérations numériques](ultimatepython/fundamentals/expression.py) ( 🍰 )
    - Chaîne : [Opérations sur les chaînes](ultimatepython/fundamentals/string.py) ( 🍰 )
    - Liste : [Opérations sur les listes](ultimatepython/fundamentals/list.py) ( 🍰 )
    - Tuple : [Opérations sur les tuples](ultimatepython/fundamentals/tuple.py)
    - Ensemble : [Opérations sur les ensembles](ultimatepython/fundamentals/set.py)
    - Dictionnaire : [Opérations sur les dictionnaires](ultimatepython/fundamentals/dict.py) ( 🍰 )
    - Conditionnelle : [if | if-else | if-elif-else](ultimatepython/fundamentals/conditional.py) ( 🍰 )
    - Boucle : [for-loop | while-loop](ultimatepython/fundamentals/loop.py) ( 🍰 )
    - Fonction : [def | lambda](ultimatepython/fundamentals/function.py) ( 🍰 )
    - Compréhension : [list | tuple | set | dict](ultimatepython/fundamentals/comprehension.py)
3. **Programmation orientée objet**
    - Classe basique : [Définition basique](ultimatepython/oop/basic_class.py) ( 🍰 )
    - Héritage : [Héritage](ultimatepython/oop/inheritance.py) ( 🍰 )
    - Encapsulation : [Définition de l’encapsulation](ultimatepython/oop/encapsulation.py)
    - Classe abstraite : [Définition abstraite](ultimatepython/oop/abstract_class.py)
    - Classe d’exception : [Définition d’exception](ultimatepython/oop/exception_class.py)
    - Itérateur : [Définition d’itérateur | yield](ultimatepython/oop/iterator_class.py) ( 🤯 )
    - Mixin : [Définition de Mixin](ultimatepython/oop/mixin.py) ( 🤯 )
    - Ordre de résolution des méthodes : [mro](ultimatepython/oop/mro.py) ( 🤯 )
4. **Bibliothèque standard**
    - Gestion de fichiers : [File Handling](ultimatepython/stdlib/file_handling.py) ( 🤯 )
    - Expressions régulières : [search | findall | match | fullmatch](ultimatepython/stdlib/regex.py) ( 🤯 )
    - Format de données : [json | xml | csv](ultimatepython/stdlib/data_format.py) ( 🤯 )
    - Date et heure : [datetime | timezone](ultimatepython/stdlib/date_time.py) ( 🤯 )
5. **Avancé**
    - Décorateur : [Définition de décorateur | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )
    - Gestionnaire de contexte : [Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )
    - Métaclasse : [Définition de métaclasse](ultimatepython/advanced/meta_class.py) ( 🤯 )
    - Référence faible : [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )
    - Opérateur morse : [Expressions d'affectation :=](ultimatepython/advanced/walrus_operator.py) ( 🤯 )
    - Application d'arguments : [Positionnels uniquement / | Mots-clés uniquement *](ultimatepython/advanced/arg_enforcement.py) ( 🤯 )
    - Correspondance de motifs : [match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )
    - Template strings : [Template strings (PEP 750)](ultimatepython/advanced/template_strings.py) ( 🤯 )
6. **Concurrence**
    - Thread : [ThreadPoolExecutor](ultimatepython/concurrency/thread.py) ( 🤯 )
    - Asyncio : [async | await](ultimatepython/concurrency/async.py) ( 🤯 )
    - Sous-interpréteurs : [concurrent.interpreters](ultimatepython/concurrency/subinterpreters.py) ( 🤯 )
7. **Ingénierie**
    - Mocking : [MagicMock | PropertyMock | patch](ultimatepython/engineering/mocking.py) ( 🤯 )
    - Benchmark : [cProfile | pstats](ultimatepython/engineering/benchmark.py) ( 🤯 )
    - Opérateurs binaires : [Opérateurs binaires](ultimatepython/engineering/bitwise.py) ( 🍰 ), [Complément à un et à deux](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )
    - Deque : [deque](ultimatepython/engineering/deque.py) ( 🤯 )
    - Namedtuple : [namedtuple](ultimatepython/engineering/namedtuple.py) ( 🤯 )
    - Defaultdict : [defaultdict](ultimatepython/engineering/defaultdict.py) ( 🤯 )
    - Outils d'itérateurs : [Outils d'itérateurs](ultimatepython/engineering/itertools.py) ( 🤯 )
    - Union de dictionnaires : [Fusion de dictionnaires | et |=](ultimatepython/engineering/dict_union.py) ( 🤯 )
    - Heap : [heap queue](ultimatepython/engineering/heap.py) ( 🤯 )
    - Complexité temporelle : [Opérations CPython](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )

## Ressources supplémentaires

👔 = Ressource d’entretien
🧪 = Exemples de code
🧠 = Idées de projets

### Dépôts GitHub

Continue d’apprendre grâce à ces ressources bien établies :

#### Python fondamental et modèles

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔 , 🧪 )
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔 , 🧪 )
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( 🧪 )
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)

#### Science des données et apprentissage automatique

- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( 🧪 )
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) ( 🧪 )
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) ( 🧪 )
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)

#### Listes sélectionnées et idées de projets

- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( 🧠 )
- [vinta/awesome-python](https://github.com/vinta/awesome-python)
- [lukasmasuch/best-of-python](https://github.com/lukasmasuch/best-of-python)
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( 👔 )

### Pratique interactive

Continue à t’exercer pour ne pas perdre la main :

#### Préparation aux entretiens

- [leetcode.com](https://leetcode.com/) ( 👔 )
- [hackerrank.com](https://www.hackerrank.com/) ( 👔 )
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( 👔 )

#### Apprentissage pratique

- [exercism.io](https://exercism.io/)
- [codewars.com](https://www.codewars.com/)
- [labex.io](https://labex.io/exercises/python) ( 🧪 )
- [teclado.com](https://teclado.com/30-days-of-python/#prerequisites) ( 🧪 )
- [projecteuler.net](https://projecteuler.net/)
- [kaggle.com](https://www.kaggle.com/) ( 🧠 )
