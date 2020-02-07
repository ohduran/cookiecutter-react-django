from django.contrib import admin
from django.urls import path
from .views import CharCount

urlpatterns = [
    path('char_count', CharCount.as_view(), name='char_count'),
]
