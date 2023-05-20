
from django.contrib import admin
from django.urls import path
from generator import view

urlpatterns = [
    path('', view.home),
    path('password/', view.password,name='password'),
]
