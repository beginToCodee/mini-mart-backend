from django.db import models
from store.models import *


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    old_price = models.IntegerField()
    current_price = models.IntegerField()
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="product_category")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="brand")


    def __str__(self):
        return self.title

    @staticmethod
    def get_product_by_keys(keys):
        return [Product.objects.filter(id=key).first() for key in keys]
    
    