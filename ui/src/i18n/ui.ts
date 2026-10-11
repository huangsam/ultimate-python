export const languages = {
  en: 'English',
  ko: '한국어',
  'zh-tw': '繁體中文',
  es: 'Español',
  de: 'Deutsch',
  fr: 'Français',
  hi: 'हिन्दी',
  'pt-br': 'Português',
};

export const defaultLang = 'en';

export const ui = {
  en: {
    'site.title': 'Ultimate Python',
    'nav.start': 'Start Learning',
    'nav.home': 'Back to home',
    'nav.github': 'View on GitHub',
    'nav.prev': 'Previous',
    'nav.next': 'Next',

    'notFound.title': 'Page not found',
    'notFound.message':
      "This page doesn't exist or may have moved. Search the sidebar or start from the first lesson.",

    'welcome.title': 'Master Python by example',
    'welcome.subtitle':
      'An interactive study guide for newcomers and professionals. Learn from clean, heavily-commented code runnable on Replit or locally with zero dependencies.',
    'card.lessons.title': 'Standalone Lessons',
    'card.lessons.desc':
      'Every concept is explained via self-contained, executable modules. No fluff, just clean code and comments.',
    'card.stdlib.title': 'Standard Library Only',
    'card.stdlib.desc':
      "Built exclusively on Python's built-in modules so you can understand core features without third-party framework overhead.",
    'card.run.title': 'Run Anywhere',
    'card.run.desc':
      'View code with VS Code-quality syntax highlighting, run it on Replit, or execute it locally in your own terminal.',
    'zen.title': 'The Zen of Python',
    'search.placeholder': 'Search topics (e.g. loops)...',
    'search.lessons': 'lessons',
    'search.empty': 'No matching lessons found',
    'category.fundamentals': 'Fundamentals',
    'category.oop': 'OOP',
    'category.stdlib': 'Standard Library',
    'category.advanced': 'Advanced',
    'category.concurrency': 'Concurrency',
    'category.engineering': 'Engineering',
    'category.fundamentals.desc':
      'Core syntax and structural constructs of the language. Learn how Python binds names to objects, evaluates expressions, and handles fundamental collections with zero external dependencies.',
    'category.oop.desc':
      'Object-Oriented Programming concepts and patterns. Explore class mechanics, inheritance hierarchies, method resolution order (MRO), encapsulation, and custom iterators.',
    'category.stdlib.desc':
      'Essential Python standard library modules. Master file handling, regular expressions, structured data serialization (JSON & CSV), and precise date and time arithmetic.',
    'category.advanced.desc':
      'Metaprogramming and modern runtime behaviors. Dive into decorators, context managers, metaclasses, structural pattern matching, and template strings.',
    'category.concurrency.desc':
      'Multitasking and asynchronous execution models. Understand thread synchronization, non-blocking coroutines with asyncio Task Groups, and isolated subinterpreters.',
    'category.engineering.desc':
      'Production code quality, data structures, and algorithmic tooling. Study unit test mocking, micro-benchmarking, specialized collections, and bitwise operations.',
    'chapter.start': 'Start Chapter',
    'chapter.lessons': 'Chapter Lessons',
    'chapter.badge': 'Lessons',
    'chapter.viewCode': 'View Code',
    'chapter.prev': 'Previous Chapter',
    'chapter.next': 'Next Chapter',
  },
  ko: {
    'site.title': 'Ultimate Python',
    'nav.start': '학습 시작하기',
    'nav.home': '홈으로 돌아가기',
    'nav.github': 'GitHub에서 보기',
    'nav.prev': '이전 레슨',
    'nav.next': '다음 레슨',

    'notFound.title': '페이지를 찾을 수 없습니다',
    'notFound.message':
      '이 페이지가 없거나 이동했을 수 있습니다. 사이드바에서 검색하거나 첫 레슨부터 시작하세요.',

    'welcome.title': '예제로 마스터하는 Python',
    'welcome.subtitle':
      '초보자와 전문가 모두를 위한 대화형 학습 가이드. Replit이나 로컬에서 의존성 없이 실행 가능한 깨끗하고 주석이 잘 달린 코드로 학습하세요.',
    'card.lessons.title': '독립형 레슨',
    'card.lessons.desc':
      '모든 개념은 자립적이고 실행 가능한 모듈을 통해 설명됩니다. 핵심 코드와 주석으로만 구성됩니다.',
    'card.stdlib.title': '표준 라이브러리 전용',
    'card.stdlib.desc':
      '파이썬 내장 모듈만을 사용하여 제3자 프레임워크의 부담 없이 핵심 기능을 이해할 수 있습니다.',
    'card.run.title': '어디서나 실행',
    'card.run.desc':
      'VS Code 수준의 구문 강조 기능으로 코드를 보고, Replit에서 실행하거나, 터미널에서 로컬로 실행해보세요.',
    'zen.title': '파이썬의 Zen',
    'search.placeholder': '주석 검색 (예: 루프)...',
    'search.lessons': '레슨',
    'search.empty': '일치하는 레슨이 없습니다',
    'category.fundamentals': '기초',
    'category.oop': '객체 지향 프로그래밍',
    'category.stdlib': '표준 라이브러리',
    'category.advanced': '고급 기능',
    'category.concurrency': '동시성',
    'category.engineering': '엔지니어링',
    'category.fundamentals.desc':
      '파이썬의 핵심 문법과 구조적 언어 구성 요소. 이름-객체 바인딩, 표현식 평가, 외부 의존성 없는 기본 컬렉션을 학습합니다.',
    'category.oop.desc':
      '객체 지향 프로그래밍 개념과 디자인 패턴. 클래스 매커니즘, 상속 계층, 메서드 결정 순서(MRO), 캡슐화 및 사용자 정의 반복자를 탐구합니다.',
    'category.stdlib.desc':
      '필수 파이썬 표준 라이브러리 모듈. 파일 처리, 정규 표현식, 구조화된 데이터 직렬화(JSON & CSV), 날짜 및 시간 계산을 마스터합니다.',
    'category.advanced.desc':
      '메타프로그래밍과 고급 런타임 동작. 데코레이터, 컨텍스트 관리자, 메타클래스, 구조적 패턴 매칭 및 템플릿 문자열을 다룹니다.',
    'category.concurrency.desc':
      '멀티태스킹과 비동기 실행 모델. 스레드 동기화, asyncio 태스크 그룹을 활용한 논블로킹 코루틴, 격리된 서브인터프리터를 이해합니다.',
    'category.engineering.desc':
      '프로덕션 코드 품질, 자료구조 및 알고리즘 유틸리티. 단위 테스트 모킹, 마이크로 벤치마킹, 특수 컬렉션 및 비트 연산을 학습합니다.',
    'chapter.start': '챕터 시작하기',
    'chapter.lessons': '챕터 레슨 목록',
    'chapter.badge': '개 레슨',
    'chapter.viewCode': '코드 보기',
    'chapter.prev': '이전 챕터',
    'chapter.next': '다음 챕터',
  },
  'zh-tw': {
    'site.title': 'Ultimate Python',
    'nav.start': '開始學習',
    'nav.home': '返回首頁',
    'nav.github': '在 GitHub 上查看',
    'nav.prev': '上一課',
    'nav.next': '下一課',

    'notFound.title': '找不到頁面',
    'notFound.message':
      '此頁面不存在或可能已移動。請使用側邊欄搜尋，或從第一課開始。',

    'welcome.title': '通過範例掌握 Python',
    'welcome.subtitle':
      '適合初學者和專業人士的互動式學習指南。通過可在 Replit 或本地無依賴運行的乾淨、注釋豐富的程式碼進行學習。',
    'card.lessons.title': '獨立課程',
    'card.lessons.desc':
      '每個概念都通過獨立且可運行的模組進行說明。無冗餘，只有乾淨的代碼和注釋。',
    'card.stdlib.title': '僅限標準庫',
    'card.stdlib.desc':
      '完全基於 Python 內置模組構建，無需第三方框架開銷即可理解核心功能。',
    'card.run.title': '隨處運行',
    'card.run.desc':
      '以 VS Code 級別的語法高亮查看代碼，在 Replit 上運行，或在本地終端運行。',
    'zen.title': 'Python 禪意',
    'search.placeholder': '搜尋主題（例如：迴圈）...',
    'search.lessons': '個課程',
    'search.empty': '找不到相符的課程',
    'category.fundamentals': '基礎知識',
    'category.oop': '物件導向程式設計',
    'category.stdlib': '標準函式庫',
    'category.advanced': '高級功能',
    'category.concurrency': '併發',
    'category.engineering': '工程實踐',
    'category.fundamentals.desc':
      '語言的核心語法與結構構造。學習 Python 如何將名稱綁定到物件、求值表達式以及在零外部依賴下操作基礎集合。',
    'category.oop.desc':
      '物件導向程式設計概念與模式。探索類別機制、繼承體系、方法解析順序（MRO）、封裝與自訂迭代器。',
    'category.stdlib.desc':
      '必備 Python 標準函式庫模組。掌握檔案處理、正規表達式、結構化資料序列化（JSON 與 CSV）以及精確的日期時間運算。',
    'category.advanced.desc':
      '元程式設計與現代執行階段行為。深入探索裝飾器、上下文管理器、元類別、結構化模式匹配與範本字串。',
    'category.concurrency.desc':
      '多工與非同步執行模型。理解執行緒同步、基於 asyncio 任務群組的非阻塞協程以及隔離的子直譯器。',
    'category.engineering.desc':
      '生產級程式碼品質、資料結構與演算法工具。學習單元測試模擬、微基準測試、特化集合與位元運算。',
    'chapter.start': '開始章節',
    'chapter.lessons': '章節課程',
    'chapter.badge': '堂課程',
    'chapter.viewCode': '查看程式碼',
    'chapter.prev': '上一章',
    'chapter.next': '下一章',
  },
  es: {
    'site.title': 'Ultimate Python',
    'nav.start': 'Comenzar a Aprender',
    'nav.home': 'Volver al inicio',
    'nav.github': 'Ver en GitHub',
    'nav.prev': 'Anterior',
    'nav.next': 'Siguiente',

    'notFound.title': 'Página no encontrada',
    'notFound.message':
      'Esta página no existe o puede haberse movido. Busca en la barra lateral o empieza desde la primera lección.',

    'welcome.title': 'Domina Python a través de ejemplos',
    'welcome.subtitle':
      'Una guía de estudio interactiva para principiantes y profesionales. Aprende con código limpio y comentado, ejecutable localmente o en Replit sin dependencias.',
    'card.lessons.title': 'Lecciones Independientes',
    'card.lessons.desc':
      'Cada concepto se explica a través de módulos ejecutables independientes. Sin rodeos, solo código limpio y comentarios.',
    'card.stdlib.title': 'Solo Biblioteca Estándar',
    'card.stdlib.desc':
      'Construido exclusivamente sobre módulos integrados de Python para entender características principales sin sobrecarga de frameworks externos.',
    'card.run.title': 'Ejecutar en Cualquier Lugar',
    'card.run.desc':
      'Visualiza el código con resaltado de sintaxis tipo VS Code, ejecútalo en Replit, o córrelo localmente en tu terminal.',
    'zen.title': 'El Zen de Python',
    'search.placeholder': 'Buscar temas (ej. bucles)...',
    'search.lessons': 'lecciones',
    'search.empty': 'No se encontraron lecciones',
    'category.fundamentals': 'Fundamentos',
    'category.oop': 'Programación orientada a objetos',
    'category.stdlib': 'Librería estándar',
    'category.advanced': 'Avanzado',
    'category.concurrency': 'Concurrencia',
    'category.engineering': 'Ingeniería',
    'category.fundamentals.desc':
      'Sintaxis central y constructos estructurales del lenguaje. Aprende cómo Python vincula nombres a objetos, evalúa expresiones y gestiona colecciones básicas sin dependencias externas.',
    'category.oop.desc':
      'Conceptos y patrones de Programación Orientada a Objetos. Explora la mecánica de clases, jerarquías de herencia, orden de resolución de métodos (MRO), encapsulamiento e iteradores personalizados.',
    'category.stdlib.desc':
      'Módulos esenciales de la biblioteca estándar de Python. Domina el manejo de archivos, expresiones regulares, serialización de datos estructurados (JSON y CSV) y aritmética de fecha y hora.',
    'category.advanced.desc':
      'Metaprogramación y comportamientos modernos en tiempo de ejecución. Sumérgete en decoradores, gestores de contexto, metaclases, coincidencia de patrones estructurales y cadenas de plantilla.',
    'category.concurrency.desc':
      'Modelos de multitarea y ejecución asíncrona. Comprende la sincronización de hilos, corrutinas no bloqueantes con Grupos de Tareas de asyncio y subintérpretes aislados.',
    'category.engineering.desc':
      'Calidad de código en producción, estructuras de datos y herramientas algorítmicas. Estudia mocking para pruebas unitarias, microbenchmarking, colecciones especializadas y operaciones bit a bit.',
    'chapter.start': 'Comenzar Capítulo',
    'chapter.lessons': 'Lecciones del Capítulo',
    'chapter.badge': 'Lecciones',
    'chapter.viewCode': 'Ver Código',
    'chapter.prev': 'Capítulo Anterior',
    'chapter.next': 'Capítulo Siguiente',
  },
  de: {
    'site.title': 'Ultimate Python',
    'nav.start': 'Lernen starten',
    'nav.home': 'Zur Startseite',
    'nav.github': 'Auf GitHub anzeigen',
    'nav.prev': 'Zurück',
    'nav.next': 'Weiter',

    'notFound.title': 'Seite nicht gefunden',
    'notFound.message':
      'Diese Seite existiert nicht oder wurde verschoben. Nutze die Seitenleiste oder starte mit der ersten Lektion.',

    'welcome.title': 'Python an Beispielen meistern',
    'welcome.subtitle':
      'Ein interaktiver Leitfaden für Einsteiger und Profis. Lerne mit sauberem, gut kommentiertem Code, der lokal oder in Replit ohne Abhängigkeiten läuft.',
    'card.lessons.title': 'Eigenständige Lektionen',
    'card.lessons.desc':
      'Jedes Konzept wird durch eigenständige, ausführbare Module erklärt. Kein Schnickschnack, nur sauberer Code und Kommentare.',
    'card.stdlib.title': 'Nur Standardbibliothek',
    'card.stdlib.desc':
      'Baut ausschließlich auf integrierten Python-Modulen auf, um Kernfunktionen ohne den Overhead von Drittanbieter-Frameworks zu verstehen.',
    'card.run.title': 'Überall ausführen',
    'card.run.desc':
      'Code mit Syntaxhervorhebung in VS Code-Qualität anzeigen, in Replit ausführen oder lokal im Terminal starten.',
    'zen.title': 'Das Zen von Python',
    'search.placeholder': 'Themen suchen (z.B. Schleifen)...',
    'search.lessons': 'Lektionen',
    'search.empty': 'Keine passenden Lektionen gefunden',
    'category.fundamentals': 'Grundlagen',
    'category.oop': 'Objektorientierte Programmierung',
    'category.stdlib': 'Standardbibliothek',
    'category.advanced': 'Fortgeschritten',
    'category.concurrency': 'Nebenläufigkeit',
    'category.engineering': 'Softwaretechnik',
    'category.fundamentals.desc':
      'Kernsyntax und strukturelle Sprachkonstrukte. Lerne, wie Python Namen an Objekte bindet, Ausdrücke auswertet und grundlegende Sammlungen ohne externe Abhängigkeiten handhabt.',
    'category.oop.desc':
      'Konzepte und Muster der objektorientierten Programmierung. Erkunde Klassenmechanismen, Vererbungshierarchien, Methodenauflösungsreihenfolge (MRO), Kapselung und benutzerdefinierte Iteratoren.',
    'category.stdlib.desc':
      'Wichtige Module der Python-Standardbibliothek. Meistere Dateiverarbeitung, reguläre Ausdrücke, strukturierte Datenserialisierung (JSON & CSV) sowie präzise Datums- und Zeitarithmetik.',
    'category.advanced.desc':
      'Metaprogrammierung und moderne Laufzeitverhalten. Tauche ein in Dekoratoren, Kontextmanager, Metaklassen, strukturelles Pattern Matching und Template-Strings.',
    'category.concurrency.desc':
      'Multitasking und asynchrone Ausführungsmodelle. Verstehe Thread-Synchronisation, nicht-blockierende Coroutinen mit asyncio Task Groups und isolierte Subinterpreter.',
    'category.engineering.desc':
      'Codequalität für die Produktion, Datenstrukturen und algorithmische Werkzeuge. Erforsche Unit-Test-Mocking, Micro-Benchmarking, spezialisierte Sammlungen und bitweise Operationen.',
    'chapter.start': 'Kapitel starten',
    'chapter.lessons': 'Kapitel-Lektionen',
    'chapter.badge': 'Lektionen',
    'chapter.viewCode': 'Code anzeigen',
    'chapter.prev': 'Vorheriges Kapitel',
    'chapter.next': 'Nächstes Kapitel',
  },
  fr: {
    'site.title': 'Ultimate Python',
    'nav.start': "Commencer l'apprentissage",
    'nav.home': "Retour à l'accueil",
    'nav.github': 'Voir sur GitHub',
    'nav.prev': 'Précédent',
    'nav.next': 'Suivant',

    'notFound.title': 'Page introuvable',
    'notFound.message':
      "Cette page n'existe pas ou a peut-être été déplacée. Utilisez la barre latérale ou commencez par la première leçon.",

    'welcome.title': "Maîtrisez Python par l'exemple",
    'welcome.subtitle':
      "Un guide d'étude interactif pour débutants et professionnels. Apprenez grâce à un code propre et commenté, exécutable localement ou sur Replit sans dépendances.",
    'card.lessons.title': 'Leçons Autonomes',
    'card.lessons.desc':
      'Chaque concept est expliqué à travers des modules autonomes exécutables. Pas de superflu, juste du code propre et des commentaires.',
    'card.stdlib.title': 'Bibliothèque Standard Uniquement',
    'card.stdlib.desc':
      'Construit exclusivement sur les modules intégrés de Python pour comprendre les fonctionnalités de base sans surcharge liée à des frameworks tiers.',
    'card.run.title': "Exécuter N'importe Où",
    'card.run.desc':
      'Visualisez le code avec une coloration syntaxique de qualité VS Code, lancez-le sur Replit, ou exécutez-le localement dans votre terminal.',
    'zen.title': 'Le Zen de Python',
    'search.placeholder': 'Rechercher des sujets (ex: boucles)...',
    'search.lessons': 'leçons',
    'search.empty': 'Aucune leçon correspondante trouvée',
    'category.fundamentals': 'Fondations',
    'category.oop': 'Programmation orientée objet',
    'category.stdlib': 'Bibliothèque standard',
    'category.advanced': 'Avancé',
    'category.concurrency': 'Concurrence',
    'category.engineering': 'Ingénierie',
    'category.fundamentals.desc':
      'Syntaxe fondamentale et constructions structurelles du langage. Découvrez comment Python lie les noms aux objets, évalue les expressions et manipule les collections de base sans dépendance externe.',
    'category.oop.desc':
      'Concepts et modèles de programmation orientée objet. Explorez les mécanismes de classes, les hiérarchies d’héritage, l’ordre de résolution des méthodes (MRO), l’encapsulation et les itérateurs personnalisés.',
    'category.stdlib.desc':
      'Modules essentiels de la bibliothèque standard de Python. Maîtrisez la gestion de fichiers, les expressions régulières, la sérialisation de données structurées (JSON & CSV) et l’arithmétique temporelle.',
    'category.advanced.desc':
      'Métaprogrammation et comportements modernes à l’exécution. Plongez dans les décorateurs, gestionnaires de contexte, métaclasses, filtrage par motif structurel et chaînes de modèles.',
    'category.concurrency.desc':
      'Modèles d’exécution multitâche et asynchrone. Comprenez la synchronisation de threads, les coroutines non bloquantes avec les groupes de tâches asyncio et les sous-interpréteurs isolés.',
    'category.engineering.desc':
      'Qualité du code de production, structures de données et outils algorithmiques. Étudiez le mocking de tests unitaires, le micro-benchmarking, les collections spécialisées et les opérations au niveau du bit.',
    'chapter.start': 'Commencer le chapitre',
    'chapter.lessons': 'Leçons du chapitre',
    'chapter.badge': 'Leçons',
    'chapter.viewCode': 'Voir le code',
    'chapter.prev': 'Chapitre précédent',
    'chapter.next': 'Chapitre suivant',
  },
  hi: {
    'site.title': 'Ultimate Python',
    'nav.start': 'सीखना शुरू करें',
    'nav.home': 'होम पर वापस जाएँ',
    'nav.github': 'GitHub पर देखें',
    'nav.prev': 'पिछला पाठ',
    'nav.next': 'अगला पाठ',

    'notFound.title': 'पृष्ठ नहीं मिला',
    'notFound.message':
      'यह पृष्ठ मौजूद नहीं है या स्थान बदल गया हो सकता है। साइडबार में खोजें या पहले पाठ से शुरू करें।',

    'welcome.title': 'उदाहरणों के माध्यम से पायथन को मास्टर करें',
    'welcome.subtitle':
      'शुरुआती और पेशेवरों के लिए एक इंटरैक्टिव स्टडी गाइड। बिना किसी निर्भरता के स्थानीय रूप से या Replit पर चलने वाले स्पष्ट, टिप्पणियों से युक्त कोड से सीखें।',
    'card.lessons.title': 'स्वतंत्र पाठ',
    'card.lessons.desc':
      'हर अवधारणा को स्वतंत्र, निष्पादन योग्य मॉड्यूल के माध्यम से समझाया गया है। कोई बकवास नहीं, केवल स्पष्ट कोड और टिप्पणियां।',
    'card.stdlib.title': 'केवल मानक लाइब्रेरी',
    'card.stdlib.desc':
      'विशेष रूप से पायथन के अंतर्निहित मॉड्यूल पर निर्मित ताकि आप बिना किसी तीसरे पक्ष के ढांचे के ओवरहेड के मुख्य विशेषताओं को समझ सकें।',
    'card.run.title': 'कहीं भी चलाएं',
    'card.run.desc':
      'VS Code गुणवत्ता वाले सिंटैक्स हाइलाइटिंग के साथ कोड देखें, इसे Replit पर चलाएं, या अपने स्वयं के टर्मिनल में स्थानीय रूप से चलाएं।',
    'zen.title': 'पायथन का ज़ेन',
    'search.placeholder': 'विषय खोजें (जैसे लूप)...',
    'search.lessons': 'पाठ',
    'search.empty': 'कोई मेल खाता पाठ नहीं मिला',
    'category.fundamentals': 'बुनियादी बातें',
    'category.oop': 'ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग',
    'category.stdlib': 'मानक पुस्तकालय',
    'category.advanced': 'उन्नत',
    'category.concurrency': 'समानांतरता',
    'category.engineering': 'इंजीनियरिंग',
    'category.fundamentals.desc':
      'भाषा का मूल सिंटैक्स और संरचनात्मक निर्माण। जानें कि पायथन कैसे नामों को वस्तुओं से बांधता है, अभिव्यक्तियों का मूल्यांकन करता है, और बिना किसी बाहरी निर्भरता के मौलिक संग्रहों को संभालता है।',
    'category.oop.desc':
      'ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग अवधारणाएं और पैटर्न। क्लास मैकेनिक्स, इनहेरिटेंस पदानुक्रम, मेथड रिज़ॉल्यूशन ऑर्डर (MRO), इनकैप्सुलेशन और कस्टम इटरेटर का अन्वेषण करें।',
    'category.stdlib.desc':
      'आवश्यक पायथन मानक लाइब्रेरी मॉड्यूल। फ़ाइल हैंडलिंग, रेगुलर एक्सप्रेशन, संरचित डेटा सीरियलाइज़ेशन (JSON और CSV), और सटीक दिनांक व समय अंकगणित में महारत हासिल करें।',
    'category.advanced.desc':
      'मेटाप्रोग्रामिंग और आधुनिक रनटाइम व्यवहार। डेकोरेटर्स, संदर्भ प्रबंधक, मेटाक्लास, स्ट्रक्चरल पैटर्न मैचिंग और टेम्पलेट स्ट्रिंग्स में गहराई से उतरें।',
    'category.concurrency.desc':
      'मल्टीटास्किंग और एसिंक्रोनस निष्पादन मॉडल। थ्रेड सिंक्रोनाइज़ेशन, asyncio टास्क ग्रुप्स के साथ नॉन-ब्लॉकिंग कोरूटीन और पृथक सब-इंटरप्रेटर्स को समझें।',
    'category.engineering.desc':
      'उत्पादन कोड गुणवत्ता, डेटा संरचनाएं और एल्गोरिथम टूलींग। यूनिट टेस्ट मॉकिंग, माइक्रो-बेंचमार्किंग, विशेष संग्रह और बिटवाइज़ संचालन का अध्ययन करें।',
    'chapter.start': 'अध्याय शुरू करें',
    'chapter.lessons': 'अध्याय के पाठ',
    'chapter.badge': 'पाठ',
    'chapter.viewCode': 'कोड देखें',
    'chapter.prev': 'पिछला अध्याय',
    'chapter.next': 'अगला अध्याय',
  },
  'pt-br': {
    'site.title': 'Ultimate Python',
    'nav.start': 'Começar a Aprender',
    'nav.home': 'Voltar ao início',
    'nav.github': 'Ver no GitHub',
    'nav.prev': 'Lição anterior',
    'nav.next': 'Próxima lição',

    'notFound.title': 'Página não encontrada',
    'notFound.message':
      'Esta página não existe ou pode ter sido movida. Pesquise na barra lateral ou comece pela primeira lição.',

    'welcome.title': 'Domine o Python através de exemplos',
    'welcome.subtitle':
      'Um guia de estudo interativo para iniciantes e profissionais. Aprenda com código limpo e comentado, executável localmente ou no Replit sem dependências.',
    'card.lessons.title': 'Lições Independentes',
    'card.lessons.desc':
      'Cada conceito é explicado através de módulos independentes executáveis. Sem enrolação, apenas código limpo e comentários.',
    'card.stdlib.title': 'Apenas Biblioteca Padrão',
    'card.stdlib.desc':
      'Construído exclusivamente sobre módulos integrados do Python para entender os recursos principais sem sobrecarga de frameworks externos.',
    'card.run.title': 'Executar em Qualquer Lugar',
    'card.run.desc':
      'Visualize o código com destaque de sintaxe estilo VS Code, execute no Replit ou rode localmente em seu terminal.',
    'zen.title': 'O Zen do Python',
    'search.placeholder': 'Buscar tópicos (ex: loops)...',
    'search.lessons': 'lições',
    'search.empty': 'Nenhuma lição encontrada',
    'category.fundamentals': 'Fundamentos',
    'category.oop': 'Programação orientada a objetos',
    'category.stdlib': 'Biblioteca padrão',
    'category.advanced': 'Avançado',
    'category.concurrency': 'Concorrência',
    'category.engineering': 'Engenharia',
    'category.fundamentals.desc':
      'Sintaxe principal e construções estruturais da linguagem. Aprenda como o Python vincula nomes a objetos, avalia expressões e lida com coleções fundamentais sem dependências externas.',
    'category.oop.desc':
      'Conceitos e padrões de Programação Orientada a Objetos. Explore a mecânica de classes, hierarquias de herança, ordem de resolução de métodos (MRO), encapsulamento e iteradores personalizados.',
    'category.stdlib.desc':
      'Módulos essenciais da biblioteca padrão do Python. Domine manipulação de arquivos, expressões regulares, serialização de dados estruturados (JSON e CSV) e aritmética de data e hora.',
    'category.advanced.desc':
      'Metaprogramação e comportamentos modernos em tempo de execução. Mergulhe em decoradores, gerenciadores de contexto, metaclases, correspondência de padrões estruturais e strings de modelo.',
    'category.concurrency.desc':
      'Modelos de multitarefa e execução assíncrona. Compreenda sincronização de threads, corrotinas não bloqueantes com Grupos de Tarefas do asyncio e subintérpretes isolados.',
    'category.engineering.desc':
      'Qualidade de código para produção, estruturas de dados e ferramentas algorítmicas. Estude simulação de testes unitários (mocking), micro-benchmarking, coleções especializadas e operações bit a bit.',
    'chapter.start': 'Iniciar Capítulo',
    'chapter.lessons': 'Lições do Capítulo',
    'chapter.badge': 'Lições',
    'chapter.viewCode': 'Ver Código',
    'chapter.prev': 'Capítulo Anterior',
    'chapter.next': 'Próximo Capítulo',
  },
};

export function getLangFromUrl(url: URL) {
  const [, lang] = url.pathname.split('/ultimate-python/');
  // Remove trailing slashes and check if lang is a supported language
  const cleanLang = lang ? lang.split('/')[0] : '';
  if (cleanLang in ui) return cleanLang as keyof typeof ui;
  return defaultLang;
}

export function useTranslations(lang: keyof typeof ui) {
  return function t(key: keyof (typeof ui)[typeof defaultLang]) {
    return ui[lang][key] || ui[defaultLang][key];
  };
}
