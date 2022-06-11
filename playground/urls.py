from django.urls import path

from .views import say_hello

urlpatterns = [path("playground/hello/", say_hello)]
