from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ping', views.ping, name='ping'),
    path('hi/<name>/<old>', views.hi, name='hi'),
    path('hello', views.hello, name='hello'),
    path('body', views.body, name='body'),
    path('foo/list', views.getFooList, name="foo_list")
]