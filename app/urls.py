from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('adminPanel/', views.adminPanel, name='adminPanel'),
	path('item/<str:pk>/', views.item, name='item'),
	path('cart/', views.cart, name='cart'),
]
