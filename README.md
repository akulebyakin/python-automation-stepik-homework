## Test automation with Selenium and Python

> Stepik course: [https://stepik.org/course/575/syllabus"](https://stepik.org/course/575/syllabus)
---

### Structure

```
    ├── pages
    │   ├── base_page.py
    │   ├── basket_page.py
    │   ├── locators.py
    │   ├── login_page.py
    │   ├── main_page.py
    │   └── product_page.py
    ├── tests
    │   ├── test_basket_page.py
    │   ├── test_main_page.py
    │   └── test_product_page.py
    ├── .gitignore
    ├── __init__.py
    ├── conftest.py
    ├── pytest.ini
    ├── README.md
    └── requirements.txt
```

### Steps

- Clone repo
- `cd` to the project folder
- Setup virtual environment

```bash
    pip install virtualenv
    virtualenv venv
    source venv/Scripts/activate
```

- Install packages

```bash
    pip install -r requirements.txt
```

- Run tests

```bash
  pytest -v --tb=line --language=en -m need_review
```

---

### Requirements:

- Python: Python 3.9