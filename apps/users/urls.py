from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('characters/', views.characters, name='characters'),
    path('characters/redirect/', views.character_redirect, name='character_redirect'),
    path('character/<int:character_id>/delete/', views.character_delete, name='character_delete'),
]
