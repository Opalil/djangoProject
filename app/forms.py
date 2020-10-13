from django import forms
from django.forms import ModelForm
from .models import Product, Cart

CATEGORY_CHOICES = [
    ('1','Sport wear'),
    ('2','Mens clothing'),
    ('3', 'Womens clothing'),
    ('4', '-'),
]

class ItemForm(ModelForm):
    productId = forms.CharField(label="Product Id", max_length=10)
    productName = forms.CharField(label="Name", max_length=45)
    productPrice = forms.DecimalField(label="Price", max_digits=6, decimal_places=4)
    app_productdesc = forms.CharField(label="Description", max_length=150)
    productCategory = forms.CharField(
        label="Product category", 
        max_length=20,
        widget=forms.Select(choices=CATEGORY_CHOICES))
    
    class Meta:
        model = Product
        exclude = ['id']

class CartForm(forms.Form):
    productId = forms.CharField(label="Product Id", max_length=10)

    class Meta:
        model = Cart
        fields = '__all__'