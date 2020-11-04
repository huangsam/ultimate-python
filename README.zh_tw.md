# Ultimate Python 學習大綱

[![CircleCI](https://img.shields.io/circleci/build/github/huangsam/ultimate-python)](https://circleci.com/gh/huangsam/ultimate-python)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/master/LICENSE)
[![r/Python](https://img.shields.io/reddit/subreddit-subscribers/Python)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

Ultimate Python 學習大綱 - 適用於新手和專業人士。:snake: :snake: :snake:

```python
print("Ultimate Python 學習大綱")
```

[English](README.md) |
[한국어](README.ko.md) |
[中文](README.zh_tw.md)

## 動力

我為了分享過去五年作為一個學生，大公司員工，以及開源（例如 Celery 和 Full Stack Python）貢獻者所習得的知識而創
建了這個代碼倉庫。我期待更多人能抱持熱忱並開始一段與Python的美好旅程。:mortar_board:

## 目標

這是創建本指南的主要目標：

:trophy: **為喜歡動手學習的Python新手提供資源。** 本存儲庫集合了不同題目的獨立模組範例，而每個模組可以獨立在普通
終端機（Terminal），IDE（如PyCharm）或者瀏覽器（如Repl.it）中運行。範例中的註解都經過精心編寫，引導讀者逐步了解程
式流程。在不刪除主例程（main)並在修改後成功運行大前題下，我鼓勵讀者修改源代碼作練習。

:trophy: **為想重溫Python核心概念的程式員提供指南。** 本存儲庫主要借助內置庫（builtin libraries）作重溫工具，
故不需額外安裝開源庫（如`sqlalchemy`，`requests`，`pandas`）。但是，如果您的目標是成為一個真正的Python
達人（Pythonista)，那麼我會鼓勵您閱讀這些源代碼，而激發靈感。

## 學習之旅

[![Run on Repl.it](https://repl.it/badge/github/huangsam/ultimate-python)](https://repl.it/github/huangsam/ultimate-python)

單擊上面的徽章就可在瀏覽器中啟動工作環境，而無需在電腦上額外安裝Git和Python。當你完成啟動，請複製這存儲庫。
當你可以開啟你所複製存儲庫後，您就準備好Python學習之旅!善用每個模組，請細讀註解並嘗試運行模組代碼。

有兩種運行模組的方式：

1. 運行單一模組：`python ultimatepython/syntax/variable.py`
2. 運行所有模組：`python runner.py`

## 目錄

:books: = 外部資源，
:cake: = 入門題目，
:exploding_head: = 進階題目

1. **關於 Python**
    - 概述：[什麼是 Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) (:books:, :cake:)
    - 設計理念：[Python之格言](https://www.python.org/dev/peps/pep-0020/) (:books:)
    - 樣式指南：[Python代碼樣式指南](https://www.python.org/dev/peps/pep-0008/) (:books:, :exploding_head:)
    - 數據模型：[數據模型](https://docs.python.org/3/reference/datamodel.html) (:books:, :exploding_head:)
    - 標準庫：[Python標準庫](https://docs.python.org/3/library/) (:books:, :exploding_head:)
    - 內置函式：[內置函式](https://docs.python.org/3/library/functions.html) (:books:)
2. **語法**
    - 變數：[內置值](ultimatepython/syntax/variable.py) (:cake:)
    - 運算式：[數值運算](ultimatepython/syntax/expression.py) (:cake:)
    - 條件運算式：[if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) (:cake:)
    - 迴圈：[for迴圈 | while迴圈](ultimatepython/syntax/loop.py) (:cake:)
    - 定義函式：[def | lambda](ultimatepython/syntax/function.py) (:cake:)
3. **資料結構**
    - 列表：[列表操作](ultimatepython/data_structures/list.py) (:cake:)
    - 元組：[元組操作](ultimatepython/data_structures/tuple.py)
    - 集合：[集合操作](ultimatepython/data_structures/set.py)
    - 字典：[字典操作](ultimatepython/data_structures/dict.py) (:cake:)
    - 綜合：[list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)
    - 字串：[字串操作](ultimatepython/data_structures/string.py) (:cake:)
    - 雙端隊列：[deque](ultimatepython/data_structures/deque.py) (:exploding_head:)
    - 時間複雜度：[cPython操作](https://wiki.python.org/moin/TimeComplexity) (:books:, :exploding_head:)
4. **類別**
    - 基本類別：[基本定義](ultimatepython/classes/basic_class.py) (:cake:)
    - 抽象類別：[抽象定義](ultimatepython/classes/abstract_class.py)
    - 異常類別：[異常定義](ultimatepython/classes/exception_class.py)
    - 迭代類別：[迭代器定義](ultimatepython/classes/iterator_class.py) (:exploding_head:)
5. **進階技巧**
    - 裝飾器：[Decorator definition | wraps](ultimatepython/advanced/decorator.py) (:exploding_head:)
    - 資源管理器：[Context managers](ultimatepython/advanced/context_manager.py) (:exploding_head:)
    - 方法解析順序：[mro](ultimatepython/advanced/mro.py) (:exploding_head:)
    - Mixin：[Mixin定義](ultimatepython/advanced/mixin.py) (:exploding_head:)
    - 元類：[Metaclass定義](ultimatepython/advanced/meta_class.py) (:exploding_head:)
    - 執行緒：[ThreadPoolExecutor](ultimatepython/advanced/thread.py) (:exploding_head:)
    - 異步：[async | await](ultimatepython/advanced/async.py) (:exploding_head:)
    - 弱引用：[weakref](ultimatepython/advanced/weak_ref.py) (:exploding_head:)
    - 基準：[cProfile | pstats](ultimatepython/advanced/benchmark.py) (:exploding_head:)
    - 模擬：[MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) (:exploding_head:)
    - 正規表示式：[search | findall | match | fullmatch](ultimatepython/advanced/regex.py) (:exploding_head:)
    - 數據格式：[json | xml | csv](ultimatepython/advanced/data_format.py) (:exploding_head:)

## 額外資源

:necktie: = 面試資源，
:test_tube: = 代碼範例，
:brain: = 項目構想

### GitHub儲存庫

通過閱讀其他備受尊重的資源來繼續學習。

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

### 互動練習

繼續練習才能使您的編碼技能不會生疏。

- [leetcode.com](https://leetcode.com/) (:necktie:)
- [hackerrank.com](https://www.hackerrank.com/) (:necktie:)
- [kaggle.com](https://www.kaggle.com/) (:brain:)
- [exercism.io](https://exercism.io/)
- [projecteuler.net](https://projecteuler.net/)
