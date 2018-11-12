# Python Data Analysis Starter Kit

## Introduction

Really Simple starter kit to kick off a small project.

You can simply start any project by...

0. (make your own virtualenv)
1. `pip install -r requirements.txt`
2. `source bin/activate` to enable virtualenv
3. `python manage.py runserver` to start django

## What have done

- sample1 app

```
$> django-admin startapp sample1
```

- uwsgi

```
$> uwsgi --ini mysite.ini
```

- nginx

```
$> sudo ln -s /path/to/your/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/
```

- plus simple JSON endpoint `/sample1`

```python

urlpatterns = [
    path('', views.index, name='index'),
    path('ping', views.ping, name='ping'), # return pong
    path('hi/<name>/<old>', views.hi, name='hi'), # path variable
    path('hello', views.hello, name='hello'), # request param
    path('body', views.body, name='body'), # request body
    path('foo/list', views.getFooList, name="foo_list") # simple end point with Foo instance list
]
```

- gitignore for PyCharm, Django, Virtualenv

## Included package

- Django==2.1.2
- numpy==1.15.3
- scipy==1.1.0
- matplotlib==3.0.1
- uWSGI==2.0.17.1
- mysql-connector-python==8.0.13
