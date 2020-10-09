from django.shortcuts import render, redirect
from .models import *
from .forms import ItemForm
from django.contrib import messages

from datetime import datetime

def index(request):
	products = Product.objects.all()

	context = {'products':products}
	return render(request, 'ShopTemplates/index.html', context)


def cart(request):
	context = {}

	return render(request, 'ShopTemplates/cart.html', context)

def item(request, pk):
	item = Product.objects.get(productId = pk)

	#form = ItemForm(request.POST, instance = item)
	
	#context = {'form':form}
	context = {'item':item}
	return render(request, 'ShopTemplates/item.html', context)

def add_to_cart(request, pk):
	product = Product.objects.get(productId = pk)
	#context = {'product':product}
	return redirect('/')

def adminPanel(request):
	form = ItemForm()
	
	# Delete item
	# Not implemented yet

	# Update existing item (e.g. price?)
	# Not implemented yet

	# Add item
	if request.method == 'POST':
		form = ItemForm(request.POST)

		if form.is_valid():
			form.save()
			item = form.cleaned_data.get('productName')
			messages.success(request, 'Item added to shop: ' + item)
			
			return redirect('/')

	context = {'form':form}
	return render(request, 'ShopTemplates/adminPanel.html', context)
		
		
		





