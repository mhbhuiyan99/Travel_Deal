```
git clone https://github.com/mhbhuiyan99/Travel_Deal.git
cd project

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

`python3 app.py`


----
# Glossary

### SQLAlchemy
A Python library that lets you work with databases using Python objects instead of writing raw SQL all the time.

### Load Config
Flask reads all UPPERCASE attributes from the object and stores them in app config.

```python
    app.config.from_object(
            Config
    )
```

### Register Blueprint
Blueprints in Flask help you organize your application into modular, reusable components. They let you group related routes, templates, and static files together.

