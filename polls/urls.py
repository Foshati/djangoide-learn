from django.urls import path
from . import views

urlpatterns = [
    path("http/", views.index, name="index"),
    path("", views.polls, name="polls"),
]
