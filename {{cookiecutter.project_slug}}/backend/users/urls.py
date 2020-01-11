from django.contrib import admin
from django.urls import path
from .views import char_count

urlpatterns = [
    path('char_count', char_count, name='char_count'),
]
