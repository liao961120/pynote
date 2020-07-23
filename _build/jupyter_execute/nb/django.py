# Django

[Course notes](https://cs50.harvard.edu/web/2019/spring/notes/7/)

## Project Directory Structure

1. To start a Django project, enter the command below in terminal:

    ```bash
    # django-admin startproject <project-name>
    django-admin startproject project_name
    ```

2. To create an app, cd to the project root (`project_name/` in this case) and run:

    ```bash
    # python manage.py startapp <app-name>
    python manage.py startapp app1
    ```


This creates the directory stucture below:

```yaml
project_name/
├── project_name/    # website App: project-level configurations
│   ├── __init__.py
│   ├── settings.py  # Link Apps: INSTALLED_APPS
│   ├── urls.py      # Link apps' routes to main site 
│   └── wsgi.py
│ 
├── app1/
│   ├── migrations/
│   ├── templates/
│   │   └── app1/
│   │       ├── base.html
│   │       └── index.html
│   ├── static/
│   │       └── style.css
│   ├── __init__.py
│   ├── admin.py     # Customize administrator panel
│   ├── apps.py
│   ├── tests.py
│   ├── models.py    # app database definition
│   ├── urls.py      # app route
│   └── views.py     # app functions
│
├── manage.py
└── db.sqlite3
```

## Common Commands

- Start new Django project
    ```bash
    django-admin startproject <project-name>
    ```
    
- Add new app
    ```bash
    python manage.py startapp <app-name>
    ```

- Start server
    ```bash
    python manage.py runserver
    ```

- Update database (after modifying `<app-name>/models.py`
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

- Django shell
    ```bash
    python manage.py shell
    python manage.py shell < script.py
    ```

- Create super user account
    ```bash
    python manage.py createsuperuser
    ```

## `settings.py`

Every time a new app is created, remember to attach this new app to the project. To do this, find `INSTALLED_APPS` in `project_name/settings.py` and add the app to the list:



## `urls.py`

Every app has one `urls.py` and `project_name/` has one `urls.py`. `project_name/urls.py` defines the url relations of every app to the site. `<app-name>/urls.py` defines the relations between individual functions in `<app-name>/views.py` and url paths **within** an app.


For example, `project_name/urls.py` might look like the code below, where `flights`, `users` and `admin` (default Django app) are apps in the project:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('flights/', include('flights.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
```


`flights/urls.py` may look like the code below:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flight_id>', views.flight, name='flight'),
    path('<int:flight_id>/book', views.book, name='book')
]
```

The `path` functions essentially links the functions in `views.py` and url paths together in an app.


As an example, (after running the server locally) if you visit `http://127.0.0.1:8000/flights/1/book`, you will be on a page handled by the function `book()` defined in `flights/views.py`. This relationship is defined in `path('<int:flight_id>/book', views.book, name='book')`. The path right after the base url (`http://127.0.0.1:8000/`) is `flights/` because it was defined in `path('flights/', include('flights.urls')),` in `project_name/urls.py`.