from django.shortcuts import render, redirect
from .models import *
from .forms import ItemForm, CartForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

def index(request):
	products = Product.objects.all()

	context = {'products':products}
	return render(request, 'ShopTemplates/index.html', context)

@csrf_exempt #Workaround at the moment
def cart(request):
	cart, created = Cart.objects.get_or_create()
	context = {'cart': cart}
	return render(request, 'ShopTemplates/cart.html', context)

def item(request, pk):
	item = Product.objects.get(id = pk)
	if request.method == 'POST':
		product = Product.objects.get(id = pk)
		try: #Workaround at the moment
			order = Cart.objects.get(pk=1)
		except:
			order, created = Cart.objects.get_or_create()

		cItem, created = CartItem.objects.get_or_create(product = product, order = order)
		cItem.save()

		return redirect('/')
	context = {'item':item}
	return render(request, 'ShopTemplates/item.html', context)

def adminPanel(request):
	form = ItemForm()
	# Add item
	if request.method == 'POST':
		form = ItemForm(request.POST)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			item = form.cleaned_data.get('productName')
			messages.success(request, 'Item added to shop: ' + item)
			
			return redirect('/')

	context = {'form':form}
	return render(request, 'ShopTemplates/adminPanel.html', context)
		
		
		





