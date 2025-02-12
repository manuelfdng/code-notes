# Django Notes

Show django-admin commands
```python
django-admin
```

Initializing the project.
```bash
django-admin startproject django_project
cd django_project
```

Starting the dev server.
```bash
python manage.py runserver
```

Creating an app within an app. This is similar to Blueprints in Flask, but the structure is pre-configured.
```bash
python manage.py startapp blog
```

```python
```

```python
```

### Other Notes
- Previous versions of Django used regex to match paths from the main app to the sub-apps.