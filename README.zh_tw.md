# Ultimate Python 學習大綱

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

Ultimate Python 學習大綱 - 適用於新手和專業人士。🐍 🐍 🐍

```python
print("Ultimate Python 學習大綱")
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

## 動力

我為了分享過去五年作為一個學生，大公司員工，以及開源（例如 Celery 和 Full Stack Python）貢獻者所習得的知識而創
建了這個代碼倉庫。我期待更多人能抱持熱忱並開始一段與Python的美好旅程。🎓

## 目標

這是創建本指南的主要目標：

🏆 **為喜歡動手學習的Python新手提供資源。** 本存儲庫集合了不同題目的獨立模組範例，而每個模組可以獨立在普通
終端機（Terminal），IDE（如PyCharm）或者瀏覽器（如Repl.it）中運行。範例中的註解都經過精心編寫，引導讀者逐步了解程
式流程。在不刪除主例程（main)並在修改後成功運行大前題下，我鼓勵讀者修改源代碼作練習。

🏆 **為想重溫Python核心概念的程式員提供指南。** 本存儲庫主要借助內置庫（builtin libraries）作重溫工具，
故不需額外安裝開源庫（如`sqlalchemy`，`requests`，`pandas`）。但是，如果您的目標是成為一個真正的Python
達人（Pythonista)，那麼我會鼓勵您閱讀這些源代碼，而激發靈感。

## 學習之旅

[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)

單擊上面的徽章就可在瀏覽器中啟動工作環境，而無需在電腦上額外安裝Git和Python。當你完成啟動，請複製這存儲庫。
當你可以開啟你所複製存儲庫後，您就準備好Python學習之旅!善用每個模組，請細讀註解並嘗試運行模組代碼。

有兩種運行模組的方式：

1. 運行單一模組：`python ultimatepython/syntax/variable.py`
2. 運行所有模組：`python runner.py`

## 目錄

📚 = 外部資源，
🍰 = 入門題目，
🤯 = 進階題目

1. **關於 Python**
    - 概述：[什麼是 Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )
    - 設計理念：[Python之格言](https://www.python.org/dev/peps/pep-0020/) ( 📚 )
    - 樣式指南：[Python代碼樣式指南](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )
    - 數據模型：[數據模型](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )
    - 標準庫：[Python標準庫](https://docs.python.org/3/library/) ( 📚, 🤯 )
    - 內置函式：[內置函式](https://docs.python.org/3/library/functions.html) ( 📚 )
2. **語法**
    - 變數：[內置值](ultimatepython/syntax/variable.py) ( 🍰 )
    - 運算式：[數值運算](ultimatepython/syntax/expression.py) ( 🍰 )
    - 按位: [中的位元運算符](ultimatepython/syntax/bitwise.py) ( 🍰 ), [一個的補語/補碼](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )
    - 條件運算式：[if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )
    - 迴圈：[for迴圈 | while迴圈](ultimatepython/syntax/loop.py) ( 🍰 )
    - 定義函式：[def | lambda](ultimatepython/syntax/function.py) ( 🍰 )
    - 海象運算子：[賦值表達式 :=](ultimatepython/syntax/walrus_operator.py) ( 🤯 )
    - 參數強制：[僅位置 / | 僅關鍵字 *](ultimatepython/syntax/arg_enforcement.py) ( 🤯 )
3. **資料結構**
    - 列表：[列表操作](ultimatepython/data_structures/list.py) ( 🍰 )
    - 元組：[元組操作](ultimatepython/data_structures/tuple.py)
    - 集合：[集合操作](ultimatepython/data_structures/set.py)
    - 字典：[字典操作](ultimatepython/data_structures/dict.py) ( 🍰 )
    - 字典聯合：[字典合併 | 和 |=](ultimatepython/data_structures/dict_union.py) ( 🤯 )
    - 綜合：[list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)
    - 字串：[字串操作](ultimatepython/data_structures/string.py) ( 🍰 )
    - 雙端隊列：[deque](ultimatepython/data_structures/deque.py) ( 🤯 )
    - Namedtuple: [namedtuple](ultimatepython/data_structures/namedtuple.py) ( 🤯 )
    - Defaultdict: [defaultdict](ultimatepython/data_structures/defaultdict.py) ( 🤯 )
    - 迭代器工具：[迭代器工具](ultimatepython/data_structures/itertools.py) ( 🤯 )
    - 時間複雜度：[cPython操作](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )
4. **類別**
    - 基本類別：[基本定義](ultimatepython/classes/basic_class.py) ( 🍰 )
    - 抽象類別：[抽象定義](ultimatepython/classes/abstract_class.py)
    - 異常類別：[異常定義](ultimatepython/classes/exception_class.py)
    - 迭代類別：[迭代器定義](ultimatepython/classes/iterator_class.py) ( 🤯 )
    - 封裝: [封裝定義](ultimatepython/classes/encapsulation.py)
5. **進階技巧**
    - 裝飾器：[Decorator definition | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )
    - 文件處理: [File Handling](ultimatepython/advanced/file_handling.py) ( 🤯 )
    - 資源管理器：[Context managers](ultimatepython/advanced/context_manager.py) ( 🤯 )
    - 方法解析順序：[mro](ultimatepython/advanced/mro.py) ( 🤯 )
    - Mixin：[Mixin定義](ultimatepython/advanced/mixin.py) ( 🤯 )
    - 元類：[Metaclass定義](ultimatepython/advanced/meta_class.py) ( 🤯 )
    - 執行緒：[ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )
    - 異步：[async | await](ultimatepython/advanced/async.py) ( 🤯 )
    - 弱引用：[weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )
    - 基準：[cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )
    - 模擬：[MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )
    - 正規表示式：[search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )
    - 數據格式：[json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )
    - 日期時間: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )
    - 模式匹配：[match | case](ultimatepython/advanced/pattern_matching.py) ( 🤯 )

## 額外資源

👔 = 面試資源，
🧪 = 代碼範例，
🧠 = 項目構想

### GitHub儲存庫

通過閱讀其他備受尊重的資源來繼續學習。

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) ( 👔, 🧪 )
- [faif/python-patterns](https://github.com/faif/python-patterns) ( 👔, 🧪 )
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

### 作者的專案

我用 Python 構建的專案，展示學習這些概念後可以創造的內容：

- [huangsam/chowist](https://github.com/huangsam/chowist) ( 🧪 )
- [huangsam/githooks](https://github.com/huangsam/githooks) ( 🧪 )
- [huangsam/ragchain](https://github.com/huangsam/ragchain) ( 🧪 )
- [huangsam/mailprune](https://github.com/huangsam/mailprune) ( 🧪 )

### 互動練習

繼續練習才能使您的編碼技能不會生疏。

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

## 歷代觀星者

[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)
