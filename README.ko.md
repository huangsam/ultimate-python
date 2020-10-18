# Ultimate Python 학습 가이드

[![CircleCI](https://img.shields.io/circleci/build/github/huangsam/ultimate-python)](https://circleci.com/gh/huangsam/ultimate-python)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/master/LICENSE)
[![r/Python](https://img.shields.io/reddit/subreddit-subscribers/Python)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

초보자와 전문가 모두를위한 최고의 Python 학습 가이드입니다. :snake: :snake: :snake:

```python
print("Ultimate Python 학습 가이드")
```

## 이 학습 가이드를 만든 이유

저는 지난 5 년 동안 대학 졸업생, 대규모 회사의 직원, 셀러리 및 풀 스택 Python과 같은 저장소의 오픈 소스 기고자로
Python을 사용하면서 핵심 Python에 대해 배운 내용을 공유하기 위해 GitHub 저장소를 만들었습니다. 더 많은 사람들이
파이썬을 배우고 그것을 통해 그들의 열정을 추구하는 것을 기대합니다. :mortar_board:

## 목표

이 가이드를 만드는 기본 목표는 다음과 같습니다.

:trophy: 실습 학습을 선호하는 Python 초보자를위한 리소스 역할을합니다. 이 저장소에는 PyCharm과 같은 IDE 및
Repl.it와 같은 브라우저에서 실행할 수있는 독립형 모듈 모음이 있습니다. 평범한 오래된 터미널조차도 예제와 함께
작동합니다. 대부분의 줄에는 프로그램이 단계별로 수행하는 작업을 독자에게 안내하는 신중하게 작성된 주석이 있습니다.
기본 루틴이 삭제되지 않고 각 변경 후 성공적으로 실행되는 한 사용자는 어디에서나 소스 코드를 수정하는 것이 좋습니다.

:trophy: 핵심 Python 개념을 다시 검토하려는 사용자를위한 순수한 가이드 역할을합니다. 기본 라이브러리 만 활용되므로
도메인 별 개념의 오버 헤드없이 이러한 개념을 전달할 수 있습니다. 따라서 인기있는 오픈 소스 라이브러리 및 프레임 워크
(예 : sqlalchemy, requests, pandas)는 설치되지 않습니다. 그러나 목표가 진정한 Pythonista가되는 것이라면
이러한 프레임 워크의 소스 코드를 읽는 것은 고무적이고 적극 권장됩니다.

## 시작하기

로컬 컴퓨터에 Git 및 Python을 설치하지 않고도 브라우저에서 작업 환경을 시작하려면 위의 배지를 클릭하세요. 이러한
요구 사항이 이미 충족 된 경우 저장소를 직접 복제해도됩니다.

저장소에 액세스 할 수있게되면 독립형 모듈에서 배울 준비가 된 것입니다. 각 모듈을 최대한 활용하려면 모듈 코드를
읽고 실행하십시오. 모듈을 실행하는 두 가지 방법이 있습니다.

1. 단일 모듈 실행 : `python ultimatepython/syntax/variable.py`
2. 모든 모듈을 실행합니다. `python runner.py`

## 목차

:books: = 외부 리소스,
:cake: = 초급 주제,
:exploding_head: = 고급 주제

1. **Python 정보**
    - 개요 : Python이란 무엇입니까 (:books:, :cake:)
    - 디자인 철학 : The Zen of Python (:books:)
    - 스타일 가이드 : Python 코드 용 스타일 가이드 (:books:, :exploding_head:)
    - 데이터 모델 : 데이터 모델 (:books:, :exploding_head:)
    - 표준 라이브러리 : Python 표준 라이브러리 (:books:, :exploding_head:)
    - 내장 기능 : 내장 기능 (:books:)
2. **통사론**
    - 변수 : 내장 리터럴 (:cake:)
    - 식 : 숫자 연산 (:cake:)
    - 조건부 : if | if-else | if-elif-else (:cake:)
    - 루프 : for 루프 | while-loop (:cake:)
    - 함수 : def | 람다 (:cake:)
3. **데이터 구조**
    - 목록 : 목록 작업 (:cake:)
    - 튜플 : 튜플 연산
    - 설정 : 설정 작업
    - Dict : 사전 작업 (:cake:)
    - 이해력 : 목록 | 튜플 | 세트 | dict
    - 문자열 : 문자열 연산 (:cake:)
    - 시간 복잡성 : cPython 작업 (:books:, :exploding_head:)
4. **클래스**
    - 기본 클래스 : 기본 정의 (:cake:)
    - 추상 클래스 : 추상 정의
    - 예외 클래스 : 예외 정의
    - 반복기 클래스 : 반복기 정의 | 수익률 (:exploding_head:)
5. **고급**
    - 데코레이터 : 데코레이터 정의 | 랩 (:exploding_head:)
    - 컨텍스트 관리자 : 컨텍스트 관리자 (:exploding_head:)
    - 메서드 해결 순서 : mro (:exploding_head:)
    - Mixin : Mixin 정의 (:exploding_head:)
    - 메타 클래스 : 메타 클래스 정의 (:exploding_head:)
    - 글타래 (쓰레드) : ThreadPoolExecutor (:exploding_head:)
    - Asyncio : 비동기 | 기다리다 (:exploding_head:)
    - 약한 참조 : weakref (:exploding_head:)
    - 벤치 마크 : cProfile | pstats (:exploding_head:)
    - 조롱 : MagicMock | PropertyMock | 패치 (:exploding_head:)
    - 정규식 : 검색 | findall | 일치 | fullmatch (:exploding_head:)
    - 데이터 형식 : json | xml | csv (:exploding_head:)

## 추가 자료

:necktie: = 인터뷰 리소스,
:test_tube: = 코드 샘플,
:brain: = 프로젝트 아이디어

### GitHub 저장소

다른 잘 알려진 자료를 읽으면서 계속 배우십시오.

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

### 대화 형 연습

코딩 기술이 녹슬지 않도록 계속 연습하십시오.

- [leetcode.com](https://leetcode.com/) (:necktie:)
- [hackerrank.com](https://www.hackerrank.com/) (:necktie:)
- [kaggle.com](https://www.kaggle.com/) (:brain:)
- [exercism.io](https://exercism.io/)
- [projecteuler.net](https://projecteuler.net/)
