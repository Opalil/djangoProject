from django.db import models

# Create your models here.
CATEGORY_CHOICES = [
    ('1','Sport wear'),
    ('2','Mens clothing'),
    ('3', 'Womens clothing'),
    ('4', '-'),
]

class Product(models.Model):
    productId = models.CharField(max_length=10)
    productName = models.CharField(max_length=45)
    productPrice = models.DecimalField(max_digits=4, decimal_places=0)
    app_productdesc = models.CharField(max_length=150)
    productCategory = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    class Meta:
        db_table: 'product'


    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    cartId = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def get_items(self):
        items = self.cartitem_set.all()
        return items

    @property
    def get_total(self):
        cItems = self.cartitem_set.all()
        total = sum([i.get_total_price for i in cItems])
        return total    

    class Meta:
        db_table: 'cart'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    @property
    def get_total_price(self):
        price = self.product.productPrice * self.quantity
        return price

    class Meta:
        db_table: 'cartitem'
