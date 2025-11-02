# अल्टीमेट Python अध्ययन गाइड

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/ultimate-python/ci.yml)](https://github.com/huangsam/ultimate-python/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/huangsam/ultimate-python)](https://codecov.io/gh/huangsam/ultimate-python)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/huangsam_ultimate-python?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=huangsam_ultimate-python)
[![License](https://img.shields.io/github/license/huangsam/ultimate-python)](https://github.com/huangsam/ultimate-python/blob/main/LICENSE)
[![r/Python](https://img.shields.io/badge/reddit-original_post-red)](https://www.reddit.com/r/Python/comments/inllmf/ultimate_python_study_guide/)

नए और पेशेवर लोगों के लिए अल्टीमेट पायथन अध्ययन गाइड। 🐍 🐍 🐍

```python
print("Ultimate Python स्टडी गाइड")
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

## प्रेरणा

मैंने यह गिटहब रिपोजिटरी [core Python](https://www.python.org/) के बारे में जो कुछ मैंने पिछले 5+ वर्षों में सीखा है, उसे साझा करने के लिए बनाई है। मैंने इसे एक कॉलेज ग्रेजुएट, बड़ी कंपनियों के कर्मचारी, और [Celery](https://github.com/celery/celery) और [Full Stack Python](https://github.com/mattmakai/fullstackpython.com) जैसी रिपोजिटरी के ओपन-सोर्स कंट्रीब्यूटर के रूप में उपयोग किया है। मैं यह देखने के लिए उत्सुक हूँ कि और लोग पायथन सीखें और इसके माध्यम से अपने जुनून को आगे बढ़ाएं। 🎓


## लक्ष्य

इस गाइड को बनाने के मुख्य लक्ष्य निम्नलिखित हैं:

🏆 **संसाधन के रूप में सेवा देना** उन नए पायथन उपयोगकर्ताओं के लिए जो प्रैक्टिकल तरीके से सीखना पसंद करते हैं। इस रिपोजिटरी में स्वतंत्र मॉड्यूलों का एक संग्रह है, जिन्हें IDE जैसे [PyCharm](https://www.jetbrains.com/pycharm/) में या [Replit](https://replit.com/languages/python3) जैसे ब्राउज़र में चलाया जा सकता है। पुराने साधारण टर्मिनल में भी इन उदाहरणों को चलाया जा सकता है। अधिकतर लाइनों में बहुत ही अच्छे से लिखे गए comments होते हैं, जो पाठक को प्रोग्राम्स के प्रत्येक चरण के माध्यम से मार्गदर्शन करते हैं। उपयोगकर्ताओं को कोड में बदलाव करने के लिए प्रोत्साहित किया जाता है, बशर्ते कि `main` रूटीन को हटाया न जाए और हर परिवर्तन के बाद [सफलतापूर्वक चलाया जाए](runner.py)।

🏆 **शुद्ध गाइड के रूप में सेवा देना** उन लोगों के लिए जो मुख्य पायथन अवधारणाओं को फिर से समझना चाहते हैं। केवल [बिल्ट-इन लाइब्रेरीज़](https://docs.python.org/3/library/) का उपयोग किया गया है ताकि इन अवधारणाओं को बिना किसी विशेष डोमेन की अवधारणाओं के सरलता से समझाया जा सके। इसी कारण से लोकप्रिय ओपन-सोर्स लाइब्रेरीज़ और फ्रेमवर्क (जैसे `sqlalchemy`, `requests`, `pandas`) को इंस्टॉल नहीं किया गया है। हालांकि, इन फ्रेमवर्क्स के स्रोत कोड को पढ़ना प्रेरणादायक है और यदि आपका लक्ष्य एक सच्चे [Pythonista](https://www.urbandictionary.com/define.php?term=pythonista) बनने का है तो इसे ज़रूर पढ़ना चाहिए।


## शुरूआत

[![Run on Replit](https://replit.com/badge/github/huangsam/ultimate-python)](https://replit.com/github/huangsam/ultimate-python)

ऊपर दिए गए बैज पर क्लिक करें ताकि आप ब्राउज़र में एक कार्यशील वातावरण शुरू कर सकें, इसके लिए आपके स्थानीय मशीन पर Git और पायथन की आवश्यकता नहीं होगी। यदि ये आवश्यकताएँ पहले से ही पूरी हो चुकी हैं, तो आप सीधे रिपोजिटरी को क्लोन कर सकते हैं।

एक बार जब रिपोजिटरी उपलब्ध हो जाती है, तो आप स्वतंत्र मॉड्यूल से सीखने के लिए तैयार हैं। प्रत्येक मॉड्यूल का अधिकतम लाभ उठाने के लिए, मॉड्यूल का कोड पढ़ें और इसे चलाएं। मॉड्यूल चलाने के दो तरीके हैं:

1. एकल मॉड्यूल चलाएं: `python ultimatepython/syntax/variable.py`
2. सभी मॉड्यूल चलाएं: `python runner.py`

## विषय सूची

📚 = बाहरी स्रोत,
🍰 = शुरुआती विषय,
🤯 = उन्नत विषय


1. **पायथन के बारे में**
    - अवलोकन: [पायथन क्या है](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) ( 📚, 🍰 )
    - डिज़ाइन दर्शन: [पायथन का ज़ेन](https://www.python.org/dev/peps/pep-0020/) ( 📚 )
    - शैली मार्गदर्शिका: [पायथन कोड के लिए शैली मार्गदर्शिका](https://www.python.org/dev/peps/pep-0008/) ( 📚, 🤯 )
    - डेटा मॉडल: [डेटा मॉडल](https://docs.python.org/3/reference/datamodel.html) ( 📚, 🤯 )
    - मानक पुस्तकालय: [पायथन मानक पुस्तकालय](https://docs.python.org/3/library/) ( 📚, 🤯 )
    - अंतर्निहित कार्य: [अंतर्निहित कार्य](https://docs.python.org/3/library/functions.html) ( 📚 )
2. **सिंटेक्स**
    - वेरिएबल: [अंतर्निहित लिटरल](ultimatepython/syntax/variable.py) ( 🍰 )
    - अभिव्यक्ति: [संख्यात्मक ऑपरेशन्स](ultimatepython/syntax/expression.py) ( 🍰 )
    - बाइनरी: [बाइनरी ऑपरेटर](ultimatepython/syntax/bitwise.py) ( 🍰 ), [एक्स/टू का पूरक](https://www.geeksforgeeks.org/difference-between-1s-complement-representation-and-2s-complement-representation-technique/) ( 📚 )
    - कंडीशनल: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) ( 🍰 )
    - लूप: [for-loop | while-loop](ultimatepython/syntax/loop.py) ( 🍰 )
    - फ़ंक्शन: [def | lambda](ultimatepython/syntax/function.py) ( 🍰 )
3. **डेटा संरचनाएँ**
    - लिसट: [लिसट ऑपरेशन्स](ultimatepython/data_structures/list.py) ( 🍰 )
    - ट्यूपल: [ट्यूपल ऑपरेशन्स](ultimatepython/data_structures/tuple.py)
    - सेट: [सेट ऑपरेशन्स](ultimatepython/data_structures/set.py)
    - डिक्ट: [डिक्शनरी ऑपरेशन्स](ultimatepython/data_structures/dict.py) ( 🍰 )
    - संकलन: [लिसट | ट्यूपल | सेट | डिक्ट](ultimatepython/data_structures/comprehension.py)
    - स्ट्रिंग: [स्ट्रिंग ऑपरेशन्स](ultimatepython/data_structures/string.py) ( 🍰 )
    - डेक: [डेक](ultimatepython/data_structures/deque.py) ( 🤯 )
    - नामित ट्यूपल: [नामित ट्यूपल](ultimatepython/data_structures/namedtuple.py) ( 🤯 )
    - डिफ़ॉल्ट डिक्ट: [डिफ़ॉल्ट डिक्ट](ultimatepython/data_structures/defaultdict.py) ( 🤯 )
    - समय कोम्पलेक्सिटी: [cPython ऑपरेशन्स](https://wiki.python.org/moin/TimeComplexity) ( 📚, 🤯 )
4. **क्लासेज़**
    - बेसिक क्लास: [बेसिक परिभाषा](ultimatepython/classes/basic_class.py) ( 🍰 )
    - इन्हरिटैंस: [इन्हरिटैंस](ultimatepython/classes/inheritance.py) ( 🍰 )
    - एैबस्टराक्ट क्लास: [एैबस्टराक्ट परिभाषा](ultimatepython/classes/abstract_class.py)
    - एक्सेपशन क्लास: [एक्सेपशन परिभाषा](ultimatepython/classes/exception_class.py)
    - इटरेटर क्लास: [इटरेटर परिभाषा | yield](ultimatepython/classes/iterator_class.py) ( 🤯 )
    - ऐनकैपसुलेषन: [ऐनकैपसुलेषन परिभाषा](ultimatepython/classes/encapsulation.py)
5. **उन्नत**
    - डेकोरेटर: [डेकोरेटर परिभाषा | wraps](ultimatepython/advanced/decorator.py) ( 🤯 )
    - फ़ाइल प्रबंधन: [फ़ाइल प्रबंधन](ultimatepython/advanced/file_handling.py) ( 🤯 )
    - संदर्भ प्रबंधक: [संदर्भ प्रबंधक](ultimatepython/advanced/context_manager.py) ( 🤯 )
    - मेथड रिज़ॉल्यूशन क्रम: [mro](ultimatepython/advanced/mro.py) ( 🤯 )
    - मिक्सिन: [मिक्सिन परिभाषा](ultimatepython/advanced/mixin.py) ( 🤯 )
    - मेटाक्लास: [मेटाक्लास परिभाषा](ultimatepython/advanced/meta_class.py) ( 🤯 )
    - थ्रेड: [ThreadPoolExecutor](ultimatepython/advanced/thread.py) ( 🤯 )
    - एसिंको: [async | await](ultimatepython/advanced/async.py) ( 🤯 )
    - वीक रेफरेंस: [weakref](ultimatepython/advanced/weak_ref.py) ( 🤯 )
    - बेंचमार्क: [cProfile | pstats](ultimatepython/advanced/benchmark.py) ( 🤯 )
    - मॉकिंग: [MagicMock | PropertyMock | patch](ultimatepython/advanced/mocking.py) ( 🤯 )
    - नियमित अभिव्यक्ति: [search | findall | match | fullmatch](ultimatepython/advanced/regex.py) ( 🤯 )
    - डेटा फ़ॉर्मेट: [json | xml | csv](ultimatepython/advanced/data_format.py) ( 🤯 )
    - दिनांक और समय: [datetime | timezone](ultimatepython/advanced/date_time.py) ( 🤯 )


## अतिरिक्त संसाधन

👔 = इंटरव्यू संसाधन,
🧪 = कोड नमूने,
🧠 = प्रोजेक्ट विचार


### गिटहब रिपॉजिटरी

अन्य उच्च मानक संसाधनों से पढ़कर सीखना जारी रखें।

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

### इंटरैक्टिव प्रैक्टिस

अभ्यास करते रहें ताकि आपकी कोडिंग कौशल खराब न हों।

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

## समय के खगोलशास्त्री

[![Stargazers over time](https://starchart.cc/huangsam/ultimate-python.svg?variant=adaptive)](https://starchart.cc/huangsam/ultimate-python)
