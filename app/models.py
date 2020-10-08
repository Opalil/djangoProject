from django.db import models

# Create your models here.


class Product(models.Model):
    productId = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=45)
    creationtime = models.DateTimeField()
    productPrice = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        db_table: 'product'


    def __str__(self):
        return self.productName

class ProductCategory(models.Model):
    categoryId = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length=45)
    creationtime = models.DateTimeField()

    def __str__(self):
        return self.categoryName  

class ProductCategories(models.Model):
    productId = models.IntegerField
    elementId = models.IntegerField
    categoryId = models.IntegerField