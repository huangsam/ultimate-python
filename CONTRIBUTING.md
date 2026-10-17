# 🚀 Welcome to the Ultimate Python Study Guide! 📚

🎉 Thank you for considering contributing to this awesome project! 🎉

But first, before you jump in, let's vibe with our [Code of Conduct](CODE_OF_CONDUCT.md). We want this space to be 🌈 inclusive, respectful, and nothing but fun!

## 🐍 What's This All About?

Our Python Study Guide is your ticket to Python mastery! 🐍 This place is all about energy, excitement, and pure Python magic. 💫

## 📖 Let's Talk Documentation

Our README is like the opening act at a concert. It's where the party starts, and we want it to be sensational! Here are the keys to this performance:

- Translations? 🌍 Yes, they're right at the top for everyone to enjoy!
- Python modules? 🤓 Oh, they've got a VIP seat in our Table of Contents (ToC).
- External links? 🔗 They're all about HTTPS and that sweet `2xx` status.
- Python documentation? For both newbies and wizards, it's all in here!
- GitHub repositories? 🌟 We love stars! If it's got at least 1k stars, bring it on!
- Practice resources? 🏋️‍♂️ We've got Python exercises to keep you in shape.

### 🌍 README Translations & Global Sync

Please update `README.md` (English) first — it's our source of truth! Whenever you add or reorder lesson links, remember to mirror that link across all corresponding `README.<lang>.md` files. Our CI runs `python check_readmes.py` to ensure all 8 translations stay in perfect harmony, so keeping them in sync guarantees your PR passes smoothly! Thanks — your help keeps the docs welcoming for learners worldwide! 🌏💖

## 📚 Get into Python Modules

Our Python modules are like mini-python-parties that you can host anywhere! They're packed with energy and make learning a blast! 🎉

### 📂 Category Folders

We organize our Python modules into clean, logical categories:
- `ultimatepython/fundamentals/` - Core syntax and basic constructs.
- `ultimatepython/oop/` - Object-Oriented Programming principles.
- `ultimatepython/stdlib/` - Python standard library modules.
- `ultimatepython/advanced/` - Metaprogramming and advanced features.
- `ultimatepython/concurrency/` - Multitasking models.
- `ultimatepython/engineering/` - Profiling, algorithms, and data structures.

If you are adding a new lesson, please place it in the appropriate folder.

### 🏷️ Web UI Navigation & Version Badges

Our web UI is powered by [ui/parse_lessons.py](ui/parse_lessons.py). When adding a new module:
- Add your lesson's file name (without `.py`) to `LESSON_ORDER` under its category so it appears in the sidebar and navigation sequence.
- If your new lesson showcases a cutting-edge feature (like a new syntax feature in Python 3.8+), update the `LESSON_ANNOTATIONS` dictionary. This will automatically display the version badge (e.g., `Python 3.10`) on the web UI!

### 🧩 The Setup

Each Python module follows a rock-solid structure:

```python
# The main event 🎉
def main():
    # Here's where the magic happens!
    assert 1 + 1 == 2
    assert True is not False


# The show must go on
if __name__ == "__main__":
    main()
```

If there's more Python goodness, it's up front before the main event!

### ✨ Style and Shine

We've got style, oh baby! Check out the PEPs:

- [PEP 8](https://www.python.org/dev/peps/pep-0008) - Our fashion bible!
- [PEP 257](https://www.python.org/dev/peps/pep-0257) - Docstring Glamour!

But there's more! We have our own style:

- Imports are perfectly sorted with [isort](https://github.com/timothycrosley/isort).
- Constants? They follow the `_UNDER_SCORE_FIRST` party rule.
- Strings love double-quotes, but if there's a `"`, they'll use single quotes!
- For dynamic strings, it's all about those fabulous f-strings! 🎤

### 📈 Code Coverage Stars

We like to keep the energy high, and that means every module should have a whopping 80-100% code coverage! Our modules are like dance floors, and we don't want any empty spaces. That's because each module is a standalone lesson, and the `main` function is where the magic happens.

## 🎸 The Master Track: Adding a New Lesson Step-by-Step 🎟️

Ready to drop a brand new lesson into the mix? Here’s your backstage pass to get your new Python lesson from your local editor straight to the main stage without missing a beat! 🎶

### 1. 🐍 Craft the Python Module
- Pick the right category folder under `ultimatepython/<category>/<module_name>.py`.
- Rely **only on Python's built-in standard library** — no external packages required!
- Keep `main()` parameterless, idempotent, and side-effect free. Use `assert` statements as your choreography to prove everything works as advertised!
- Wrap it up with the classic `if __name__ == "__main__": main()`.

### 2. 🌐 Tune the Web UI (`ui/parse_lessons.py`)
- **Set the Order**: In [ui/parse_lessons.py](ui/parse_lessons.py), add your module's filename (without `.py`) to `LESSON_ORDER` under the right category. This guarantees the sidebar and the "Next / Previous" navigation flow seamlessly!
- **Add Python Version Badges**: If you're showing off a modern Python superpower (like Python 3.8+ syntax), add an entry in `LESSON_ANNOTATIONS` with its version, PEP number, and highlight summary.

### 3. 🌍 Sync the Global Tour (All 8 READMEs!)
We share Python love around the globe! 🌎 CI has an automated gatekeeper (`python check_readmes.py`) that checks all translations for consistency:
- Add your new lesson link to the Table of Contents in `README.md`.
- Mirror that link in **all 7 translated READMEs** (`README.ko.md`, `README.zh_tw.md`, `README.es.md`, `README.de.md`, `README.fr.md`, `README.hi.md`, `README.pt_br.md`) in the exact same spot and sequence.

### 4. 🎛️ Run the Pre-Flight Soundcheck! 🧪
Before you push your branch, run these quick checks locally so CI gives you a standing ovation on the first try:

```bash
# 1. Linting & Formatting harmony ✨
ruff check
ruff format --check
mypy ultimatepython

# 2. Test runner & coverage check (aim for 80-100%!) 📈
coverage run runner.py
coverage report

# 3. Verify all 8 READMEs sing in perfect harmony 🌍
python check_readmes.py

# 4. Verify the web UI build 🚀
cd ui && npm run build && cd ..
```

## 🌟 Why Contribute to Ultimate Python?

Your contributions are like the encore at a concert — they're a big deal! Python is a worldwide phenomenon, and when you contribute, you're making a lasting difference in the learning journey of developers everywhere. 🤘🐍💥

### 🧑‍💻 Learn and Grow Together
Our project isn't just a repository; it's a collaborative learning experience. When you contribute, you're not just improving the guide—you're sharpening your own Python skills, discovering best practices, and sharing your wisdom with learners worldwide.

### 🌍 Make a Global Impact
Python is constantly evolving, and so is our guide. Your contributions help keep the content up-to-date and accessible for beginners and professionals across the globe. You might help someone on the other side of the planet grasp a core concept or kickstart their career!

### 🙋‍♀️ Inclusive & Supportive Community
Our community is welcoming, inclusive, and always here to help. Your unique perspective matters, and no contribution is too small. Together, we're building a resource that makes mastering Python fun and empowering!

## 🚀 How to Contribute (Git Workflow)

Ready to dive in? Here's how you can take the stage:

1. **Fork the Repository**: Head to [https://github.com/huangsam/ultimate-python/](https://github.com/huangsam/ultimate-python/) and click the "Fork" button in the top right corner.

2. **Clone Your Fork**: After forking, clone your repository to your local machine.

3. **Make Your Contributions**: Create or update Python modules, documentation, or anything that adds value to the project.

4. **Push Your Changes**: Once your work is ready, push your changes to your forked repository branch.

5. **Create a Pull Request**: Head back to the original repository (https://github.com/huangsam/ultimate-python/) and create a pull request. Describe your changes and let us know why they're awesome!

We're excited to see what you bring to the table! If you have any questions along the way, don't hesitate to reach out. 🌟🐍💥

## Feel the Pythonic Energy - Contribute Now! 🔥
