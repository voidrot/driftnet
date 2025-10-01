from django.urls import path

from . import views

app_name = 'market'

urlpatterns = [
    path('', views.market_index, name='market_index'),
    path('_/item-details/<int:item_id>/', views.item_details, name='item-details'),
    path('_/market-sidebar/', views.market_sidebar, name='market-sidebar'),
]
