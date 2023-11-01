from django.contrib import admin
from django.urls import path
from .views import spam_classifier

urlpatterns = [
    path('', spam_classifier),
]