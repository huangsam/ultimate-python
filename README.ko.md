# Ultimate Python 학습 가이드

[![CircleCI](https://img.shields.io/circleci/build/github/huangsam/ultimate-python)](https://circleci.com/gh/huangsam/ultimate-python)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/master/LICENSE)
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

초보자와 전문가 모두를 위한 최고의 Python 학습 가이드입니다. :snake: :snake: :snake:

```python
print("Ultimate Python 학습 가이드")
```

[English](README.md) |
[한국어](README.ko.md) |
[繁体中文](README.zh_tw.md) |
[Español](README.es.md) |
[Deutsch](README.de.md)

## 동기

이 GitHub 저장소는 대학 졸업 후, 대규모 회사에서 근무하면서
그리고 [Celery](https://github.com/celery/celery)와 [Full Stack Python](https://github.com/mattmakai/fullstackpython.com) 같은 오픈소스 프로젝트에 기여하면서
지난 5년 이상 동안 배운 [core Python](https://www.python.org/)에 대한 지식을 공유하기 위해 만들었습니다.
저는 더 많은 사람들이 Python을 배우고 자신의 열정을 추구하길 기대합니다. :mortar_board:

## 목표

이 가이드를 만드는 주요 목표는 다음과 같습니다:

:trophy: 실습 학습을 선호하는 Python 초보자를 위한 **학습 자료를 제공합니다.**
이 저장소에는 [PyCharm](https://www.jetbrains.com/pycharm/)과 같은 IDE 및 [Replit](https://replit.com/languages/python3)와 같은 브라우저에서 실행할 수 있는 독립형 모듈 모음이 있습니다. 기본 터미널에서도 예제를 실행할 수 있습니다.
대부분의 코드 라인에 프로그램이 단계별로 어떤 작업을 하는지 안내하는 신중하게 작성된 주석이 있습니다.
사용자는 `main` 루틴을 삭제하지 않고, 각 변경 후에 [성공적으로 실행](runner.py)되는 한 소스 코드를 얼마든지 수정할 수 있습니다.

:trophy: core Python 개념을 다시 복습하고 싶은 사람들을 위한 **순수 가이드를 제공합니다.**
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

:books: = 외부 리소스,
:cake: = 초급 주제,
:exploding_head: = 고급 주제

1. **Python 정보**
    - 개요 : [Python이란 무엇인가](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( :books:, :cake: )
    - 디자인 철학 : [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) ( :books: )
    - 스타일 가이드 : [Python 코드 스타일 가이드](https://www.python.org/dev/peps/pep-0008/) ( :books:, :exploding_head: )
    - 데이터 모델 : [데이터 모델](https://docs.python.org/3/reference/datamodel.html) ( :books:, :exploding_head: )
    - 표준 라이브러리 : [Python 표준 라이브러리](https://docs.python.org/3/library/) ( :books:, :exploding_head: )
    - 내장 함수 : [내장 함수](https://docs.python.org/3/library/functions.html) ( :books: )
2. **통사론**
    - 변수 : [내장 리터럴](ultimatepython/syntax/variable.py) ( :cake: )
    - 표현식 : [숫자 연산](ultimatepython/syntax/expression.py) ( :cake: )
    - 비트 연산 : [비트 연산자](ultimatepython/syntax/bitwise.py) ( :cake: ), [1의 보수/2의 보수](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( :books: )
    - 조건문 : [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( :cake: )
    - 반복문 : [for-loop | while-loop](ultimatepython/syntax/loop.py) ( :cake: )
    - 함수 : [def | lambda](ultimatepython/syntax/function.py) ( :cake: )
3. **데이터 구조**
    - 리스트 : [리스트 연산](ultimatepython/data_structures/list.py) ( :cake: )
    - 튜플 : [튜플 연산](ultimatepython/data_structures/tuple.py)
    - 세트 : [세트 연산](ultimatepython/data_structures/set.py)
    - 딕셔너리 : [딕셔너리 연산](ultimatepython/data_structures/dict.py) ( :cake: )
    - 컴프리헨션 : [리스트 | 튜플 | 세트 | 딕셔너리](ultimatepython/data_structures/comprehension.py)
    - 문자열 : [문자열 연산](ultimatepython/data_structures/string.py) ( :cake: )
    - 덱: [deque](ultimatepython/data_structures/deque.py) ( :exploding_head: )
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( :exploding_head: )
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( :exploding_head: )
    - 시간 복잡도 : [cPython 연산](https://wiki.python.org/moin/TimeComplexity) ( :books:, :exploding_head: )
4. **클래스**
    - 기본 클래스 : [기본 정의](ultimatepython/classes/basic_class.py) ( :cake: )
    - 계승: [계승](ultimatepython/classes/inheritance.py) ( :cake: )
    - 추상 클래스 : [추상 정의](ultimatepython/classes/abstract_class.py)
    - 예외 클래스 : [예외 정의](ultimatepython/classes/exception_class.py)
    - 이터레이터 클래스 : [이터레이터 정의 | yield](ultimatepython/classes/iterator_class.py) ( :exploding_head: )
    - 캡슐화: [캡슐화 정의](ultimatepython/classes/encapsulation.py)
5. **고급**
    - 데코레이터 : [데코레이터 정의 | wraps](ultimatepython/advanced/decorator.py) ( :exploding_head: )
    - 파일 처리: [파일 처리](ultimatepython/advanced/file_handling.py) ( :exploding_head: )
    - 컨텍스트 매니저 : [컨텍스트 매니저](ultimatepython/advanced/context_manager.py) ( :exploding_head: )
    - 메서드 결정 순서 : [mro](ultimatepython/advanced/mro.py) ( :exploding_head: )
    - 믹스인 : [믹스인 정의](ultimatepython/advanced/mixin.py) ( :exploding_head: )
    - 메타클래스 : [메타클래스 정의](ultimatepython/advanced/meta_class.py) ( :exploding_head: )
    - 스레드 : [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( :exploding_head: )
    - Asyncio : [async | await](ultimatepython/advanced/async.py) ( :exploding_head: )
    - 약한 참조 : [weakref](ultimatepython/advanced/weak_ref.py) ( :exploding_head: )
    - 벤치마크 : [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( :exploding_head: )
    - 모킹 : [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( :exploding_head: )
    - 정규식 : [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( :exploding_head: )
    - 데이터 포맷 : [json | xml | csv](ultimatepython/advanced/data_format.py) ( :exploding_head: )
    - 날짜와 시간 : [datetime | timezone](ultimatepython/advanced/date_time.py) ( :exploding_head: )

## 추가 자료

:necktie: = 인터뷰 자료,
:test_tube: = 코드 샘플,
:brain: = 프로젝트 아이디어

### GitHub 저장소

잘 알려진 다른 자료를 읽으면서 계속 배우세요.

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( :necktie:, :test_tube: )
- [faif/python-patterns](https://github.com/faif/python-patterns) ( :necktie:, :test_tube: )
- [geekcomputers/Python](https://github.com/geekcomputers/Python) ( :test_tube: )
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) ( :test_tube: )
- [karan/Projects](https://github.com/karan/Projects) ( :brain: )
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) ( :brain: )
- [vinta/awesome-python](https://github.com/vinta/awesome-python)
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python) ( :test_tube: )
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning#python)
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) ( :necktie: )

### 대화형 연습

코딩 실력이 녹슬지 않기 위해 계속 연습하세요.

- [leetcode.com](https://leetcode.com/) ( :necktie: )
- [hackerrank.com](https://www.hackerrank.com/) ( :necktie: )
- [kaggle.com](https://www.kaggle.com/) ( :brain: )
- [exercism.io](https://exercism.io/)
- [projecteuler.net](https://projecteuler.net/)
- [DevProjects](https://www.codementor.io/projects/python)
- [codewars.com](https://www.codewars.com/)
- [hackerearth.com](https://www.hackerearth.com/)
- [codechef.com](https://www.codechef.com/) ( :necktie: )
- [w3schools.com](https://www.w3schools.com/python/) ( :brain: )
- [codeforces.com](https://codeforces.com/)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/) ( :necktie: )
- [coderbyte.com](https://www.coderbyte.com/) ( :necktie: )
- [replit.com](https://replit.com/)
