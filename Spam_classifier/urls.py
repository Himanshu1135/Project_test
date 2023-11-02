from django.contrib import admin
from django.urls import path
from .views import spam_classifier, home

urlpatterns = [
    path('', spam_classifier),
    path('home/',home),
]