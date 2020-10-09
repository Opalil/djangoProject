from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('adminPanel/', views.adminPanel, name='adminPanel'),
	path('item/<str:pk>/', views.item, name='item'),
	path('add_to_cart/<str:pk>/', views.add_to_cart, name='add_to_cart'),
	path('cart/', views.cart, name='cart'),
]