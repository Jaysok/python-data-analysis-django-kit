# Python Data Analysis Starter Kit

## Introduction

Really Simple starter kit to kick off a small project.

You can simply start any project by...

0. git clone <thisRepo> <your_directory>
1. virtualenv --python=<python3path> <your_directory>
2. `source bin/activate` to enable virtualenv
3. `pip install -r requirements.txt`
4. `python manage.py runserver` to start django

## What have done

- sample1 app

```
$ django-admin startapp sample1
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

### Local WSGI

- uwsgi

From the project directory (not `sampleapp/` !!!)

```
$ uwsgi --ini mysite.ini
```

- nginx

```
$ sudo ln -s /path/to/your/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/
```

### Dockerized WSGI

Docker image is built on top of [`tiangolo/uwsgi-nginx:python3.5`](https://hub.docker.com/r/tiangolo/uwsgi-nginx/).

Simply build and run a docker image from `Dockerfile`.

1. Building a docker image.
```
$ docker build -t <image>:<tag> . 
```

2. Run the image.
```
$ docker run -d -p <hostport>:<containerport> <image>:<tag>
```

3. After then, try request to `localhost:<hostport>`


## Included package

- Django==2.1.2
- numpy==1.15.3
- scipy==1.1.0
- matplotlib==3.0.1
- uWSGI==2.0.17.1
- mysql-connector-python==8.0.13
