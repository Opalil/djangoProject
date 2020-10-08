from django.shortcuts import render, redirect
from .models import *

def index(request):
	products = Product.objects.all()
	categories = ProductCategory.objects.all()

	context = {'products':products, 'categories':categories}
	return render(request, 'index.html', context)


def cart(request):
	context = {}

	return render(request, 'cart.html', context)

def product(request, pk):
	product = Product.objects.get(pk=1)

	context = {'product':product}
	return render(request, 'item.html', context)


def adminPanel(request):
	products = Product.objects.all()





