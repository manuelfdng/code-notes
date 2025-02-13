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

Make sure to add this new app's Config class into the main app's settings.py INSTALLED_APPS list. This configures Django to reference the correct templates and db models within sub-apps.
```bash
python manage.py startapp blog
```

Creating a superuser that can access the admin page. Running the initial migrate command before writing db models creates default models for Django.
```bash
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
```

```python
```

### Notable Differences from Flask
- Use of urlpatterns to assign route names instead of decorators
- Use of a context dictionary to input data in HTML templates instead of adding arguments to a render_template function.
- Static directory must contain a sub-directory with the sub-app name. 
- need to add `{% load static %}` at the top of the HTML file to access static files.
- Django handles password hashing out-of-the-box

### Other Notes
- Previous versions of Django used regex to match paths from the main app to the sub-apps.
- Views either have to return an HTTP response or an exception.