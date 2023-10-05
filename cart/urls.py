from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_cart, name='cart'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]
