# Ultimate Python 학습 가이드

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

초보자와 전문가 모두를 위한 최고의 Python 학습 가이드입니다. 🐍 🐍 🐍

```python
print("Ultimate Python 학습 가이드")
```

[English](README.md) |
[한국어](README.ko.md) |
[繁体中文](README.zh_tw.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[हिन्दी](README.hi.md)

<img src="images/ultimatepython.webp" alt="Ultimate Python" width="250px" />

## 동기

이 GitHub 저장소는 대학 졸업 후, 대규모 회사에서 근무하면서
그리고 [Celery](https://github.com/celery/celery)와 [Full Stack Python](https://github.com/mattmakai/fullstackpython.com) 같은 오픈소스 프로젝트에 기여하면서
지난 5년 이상 동안 배운 [core Python](https://www.python.org/)에 대한 지식을 공유하기 위해 만들었습니다.
저는 더 많은 사람들이 Python을 배우고 자신의 열정을 추구하길 기대합니다. 🎓

## 목표

이 가이드를 만드는 주요 목표는 다음과 같습니다:

🏆 실습 학습을 선호하는 Python 초보자를 위한 **학습 자료를 제공합니다.**
이 저장소에는 [PyCharm](https://www.jetbrains.com/pycharm/)과 같은 IDE 및 [Replit](https://replit.com/languages/python3)와 같은 브라우저에서 실행할 수 있는 독립형 모듈 모음이 있습니다. 기본 터미널에서도 예제를 실행할 수 있습니다.
대부분의 코드 라인에 프로그램이 단계별로 어떤 작업을 하는지 안내하는 신중하게 작성된 주석이 있습니다.
사용자는 `main` 루틴을 삭제하지 않고, 각 변경 후에 [성공적으로 실행](runner.py)되는 한 소스 코드를 얼마든지 수정할 수 있습니다.

🏆 core Python 개념을 다시 복습하고 싶은 사람들을 위한 **순수 가이드를 제공합니다.**
여기서는 오직 [내장 라이브러리](https://docs.python.org/3/library/)만을 사용하여 이러한 개념을 도메인 특화된 개념의 오버헤드 없이 전달합니다.
따라서 유명한 오픈소스 라이브러리와 프레임워크(`sqlalchemy`, `requests`, `pandas` 등)는 설치되어 있지 않습니다.
그러나, 당신의 목표가 진정한 진정한 [Pythonista](https://www.urbandictionary.com/define.php?term=pythonista)이 되는 것 이라면 이러한 프레임워크의 소스 코드를 읽는 것은 매우 고무적이고 권장이 됩니다.

## 시작하기

[![Run on Replit](https://repl.it/badge/github/huangsam/ultimate-python)](https://repl.it/github/huangsam/ultimate-python)

로컬 컴퓨터에 Git 및 Python을 설치하지 않고도 브라우저에서 작업 환경을 시작하려면 위의 배지를 클릭하세요. 이러한
요구 사항이 이미 충족된 경우, 저장소를 바로 clone해도 됩니다.

저장소에 접근할 수 있게 되면 단독 모듈에서 배울 준비가 된 것입니다. 각 모듈을 최대한 활용하려면 모듈 코드를
읽고 실행하십시오. 모듈을 실행하는 두 가지 방법이 있습니다:

1. 단일 모듈 실행 : `python ultimatepython/syntax/variable.py`
2. 전체 모듈 실행 : `python runner.py`

## 목차

📚 = 외부 리소스,
🍰 = 초급 주제,
🤯 = 고급 주제

1. **Python 정보**
    - 개요 : [Python이란 무엇인가](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )
    - 디자인 철학 : [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) ( 📚 )
    - 스타일 가이드 : [Python 코드 스타일 가이드](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )
    - 데이터 모델 : [데이터 모델](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )
    - 표준 라이브러리 : [Python 표준 라이브러리](https://docs.python.org/3/library/) ( 📚, 🤯 )
    - 내장 함수 : [내장 함수](https://docs.python.org/3/library/functions.html) ( 📚 )
2. **통사론**
    - 변수 : [내장 리터럴](ultimatepython/syntax/variable.py) ( 🍰 )
    - 표현식 : [숫자 연산](ultimatepython/syntax/expression.py) ( 🍰 )
    - 비트 연산 : [비트 연산자](ultimatepython/syntax/bitwise.py) ( 🍰 ), [1의 보수/2의 보수](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )
    - 조건문 : [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )
    - 반복문 : [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )
    - 함수 : [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )
3. **데이터 구조**
    - 리스트 : [리스트 연산](ultimatepython/data_structures/list.py) ( 🍰 )
    - 튜플 : [튜플 연산](ultimatepython/data_structures/tuple.py)
    - 세트 : [세트 연산](ultimatepython/data_structures/set.py)
    - 딕셔너리 : [딕셔너리 연산](ultimatepython/data_structures/dict.py) ( 🍰 )
    - 컴프리헨션 : [리스트 | 튜플 | 세트 | 딕셔너리](ultimatepython/data_structures/comprehension.py)
    - 문자열 : [문자열 연산](ultimatepython/data_structures/string.py) ( 🍰 )
    - 덱: [deque](ultimatepython/data_structures/deque.py) ( 🤯 )
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )
    - 시간 복잡도 : [cPython 연산](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )
4. **클래스**
    - 기본 클래스 : [기본 정의](ultimatepython/classes/basic_class.py) ( 🍰 )
    - 계승: [계승](ultimatepython/classes/inheritance.py) ( 🍰 )
    - 추상 클래스 : [추상 정의](ultimatepython/classes/abstract_class.py)
    - 예외 클래스 : [예외 정의](ultimatepython/classes/exception_class.py)
    - 이터레이터 클래스 : [이터레이터 정의 | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )
    - 캡슐화: [캡슐화 정의](ultimatepython/classes/encapsulation.py)
5. **고급**
    - 데코레이터 : [데코레이터 정의 | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )
    - 파일 처리: [파일 처리](ultimatepython/advanced/file_handling.py) ( 🤯 )
    - 컨텍스트 매니저 : [컨텍스트 매니저](ultimatepython/advanced/context_manager.py) ( 🤯 )
    - 메서드 결정 순서 : [mro](ultimatepython/advanced/mro.py) ( 🤯 )
    - 믹스인 : [믹스인 정의](ultimatepython/advanced/mixin.py) ( 🤯 )
    - 메타클래스 : [메타클래스 정의](ultimatepython/advanced/meta_class.py) ( 🤯 )
    - 스레드 : [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )
    - Asyncio : [async | await](ultimatepython/advanced/async.py) ( 🤯 )
    - 약한 참조 : [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )
    - 벤치마크 : [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )
    - 모킹 : [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )
    - 정규식 : [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )
    - 데이터 포맷 : [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )
    - 날짜와 시간 : [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )

## 추가 자료

👔 = 인터뷰 자료,
🧪 = 코드 샘플,
🧠 = 프로젝트 아이디어

### GitHub 저장소

잘 알려진 다른 자료를 읽으면서 계속 배우세요.

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

### 대화형 연습

코딩 실력이 녹슬지 않기 위해 계속 연습하세요.

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
