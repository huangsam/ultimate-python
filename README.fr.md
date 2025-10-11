# Guide d’étude Python ultime  
  
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)  
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)  
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)  
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
[हिन्दी](README.hi.md)  
  
<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" />  
  
## Motivation  
  
J’ai créé ce dépôt GitHub pour partager ce que j’ai appris sur le [cœur de Python](https://www.python.org/)  
au cours de plus de 5 années d’utilisation — en tant que diplômé universitaire, employé  
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
  
[![Exécuter sur Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)  
  
Clique sur le badge ci-dessus pour lancer un environnement fonctionnel dans ton navigateur  
sans avoir besoin d’installer Git ou Python localement.   
Si ces outils sont déjà installés, tu peux cloner directement le dépôt.  
  
Une fois le dépôt accessible, tu es prêt à apprendre à partir des modules indépendants.   
Pour tirer le meilleur parti de chaque module, lis le code et exécute-le.  
  
Deux méthodes sont possibles :  
  
1. Exécuter un seul module :   
  `python ultimatepython/syntax/variable.py`  
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
  
2. **Syntaxe**  
    - Variable : [Littéraux intégrés](ultimatepython/syntax/variable.py) ( 🍰 )  
    - Expression : [Opérations numériques](ultimatepython/syntax/expression.py) ( 🍰 )  
    - Opérateurs binaires : [Opérateurs binaires](ultimatepython/syntax/bitwise.py) ( 🍰 ), [Complément à un et à deux](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )  
    - Conditionnelle : [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )  
    - Boucle : [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )  
    - Fonction : [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )  
  
3. **Structures de données**  
    - Liste : [Opérations sur les listes](ultimatepython/data_structures/list.py) ( 🍰 )  
    - Tuple : [Opérations sur les tuples](ultimatepython/data_structures/tuple.py)  
    - Ensemble : [Opérations sur les ensembles](ultimatepython/data_structures/set.py)  
    - Dictionnaire : [Opérations sur les dictionnaires](ultimatepython/data_structures/dict.py) ( 🍰 )  
    - Compréhension : [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)  
    - Chaîne : [Opérations sur les chaînes](ultimatepython/data_structures/string.py) ( 🍰 )  
    - Deque : [deque](ultimatepython/data_structures/deque.py) ( 🤯 )  
    - Namedtuple : [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )  
    - Defaultdict : [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )  
    - Complexité temporelle : [Opérations CPython](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )  
  
4. **Classes**  
    - Classe basique : [Définition basique](ultimatepython/classes/basic_class.py) ( 🍰 )  
    - Héritage : [Héritage](ultimatepython/classes/inheritance.py) ( 🍰 )  
    - Classe abstraite : [Définition abstraite](ultimatepython/classes/abstract_class.py)  
    - Classe d’exception : [Définition d’exception](ultimatepython/classes/exception_class.py)  
    - Itérateur : [Définition d’itérateur | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )  
    - Encapsulation : [Définition de l’encapsulation](ultimatepython/classes/encapsulation.py)  
  
5. **Avancé**  
    - Décorateur : [Définition de décorateur | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )  
    - Gestion de fichiers : [File Handling](ultimatepython/advanced/file_handling.py) ( 🤯 )  
    - Gestionnaire de contexte : [Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )  
    - Ordre de résolution des méthodes : [mro](ultimatepython/advanced/mro.py) ( 🤯 )  
    - Mixin : [Définition de Mixin](ultimatepython/advanced/mixin.py) ( 🤯 )  
    - Métaclasse : [Définition de métaclasse](ultimatepython/advanced/meta_class.py) ( 🤯 )  
    - Thread : [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )  
    - Asyncio : [async | await](ultimatepython/advanced/async.py) ( 🤯 )  
    - Référence faible : [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )  
    - Benchmark : [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )  
    - Mocking : [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )  
    - Expressions régulières : [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )  
    - Format de données : [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )  
    - Date et heure : [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )  
  
## Ressources supplémentaires  
  
👔 = Ressource d’entretien   
🧪 = Exemples de code   
🧠 = Idées de projets   
  
### Dépôts GitHub  
  
Continue d’apprendre grâce à ces ressources bien établies :  
  
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
  
### Pratique interactive  
  
Continue à t’exercer pour ne pas perdre la main :  
  
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
- [labex.io](https://labex.io/exercises/python) ( 🧪 )  
- [leetcode.com](https://leetcode.com/) ( 👔 )  
- [projecteuler.net](https://projecteuler.net/)  
- [replit.com](https://replit.com/)  
- [w3schools.com](https://www.w3schools.com/python/) ( 🧪 )