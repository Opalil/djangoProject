from django.db import models

# Create your models here.
CATEGORY_CHOICES = [
    ('1','Sport wear'),
    ('2','Mens clothing'),
    ('3', 'Womens clothing'),
    ('4', '-'),
]

class Product(models.Model):
    productId = models.CharField(max_length=10, primary_key=True)
    productName = models.CharField(max_length=45)
    productPrice = models.DecimalField(max_digits=4, decimal_places=2)
    app_productdesc = models.CharField(max_length=150)
    productCategory = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    class Meta:
        db_table: 'product'


    def __str__(self):
        return self.productId





class ProductCategory(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=45)
    creationtime = models.DateTimeField()

    def __str__(self):
        return self.categoryName  

class ProductCategories(models.Model):
    productId = models.IntegerField
    elementId = models.IntegerField
    categoryId = models.IntegerField