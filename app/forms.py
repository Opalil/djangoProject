from django import forms
from django.forms import ModelForm
from .models import Product

class ItemForm(ModelForm):
    productId = forms.CharField(label="Product Id", max_length=10)
    productName = forms.CharField(label="Name", max_length=45)
    productPrice = forms.DecimalField(label="Price", max_digits=4, decimal_places=2)
    app_productdesc = forms.CharField(label="Description", max_length=150)
    
    class Meta:
        model = Product
        fields = '__all__'