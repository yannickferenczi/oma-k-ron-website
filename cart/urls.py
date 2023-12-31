from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_cart, name='cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust_cart/<item_id>/', views.adjust_cart, name='adjust_cart'),
]
