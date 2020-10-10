from django.shortcuts import render, redirect
from .models import *
from .forms import ItemForm, CartForm
from django.contrib import messages
from django.http import JsonResponse

def index(request):
	products = Product.objects.all()

	context = {'products':products}
	return render(request, 'ShopTemplates/index.html', context)


def cart(request):
	form = ItemForm()
	if request.method == 'POST':
		form = ItemForm(request)
	context = {'form':form}
	return render(request, 'ShopTemplates/cart.html', context)

def item(request, pk):
	item = Product.objects.get(productId = pk)

	form = CartForm(request.POST)
	
	#context = {'form':form}
	context = {'item':item, 'form':form}
	return render(request, 'ShopTemplates/item.html', context)

def add_to_cart(request):
	cart = CartForm(request)
	productId = request.GET('productId')
	#productName = request.GET('productName')
	product = Product.objects.get(id = productId)
	cart.add(product=product)

	return JsonResponse('')

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
		
		
		





