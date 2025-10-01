from django.urls import URLPattern
from django.urls import URLResolver
from django.urls import path

from . import views

app_name = 'serverstatus'

urlpatterns: list[URLPattern | URLResolver] = [
    path('current-status/', views.current_status, name='current-status'),
]
