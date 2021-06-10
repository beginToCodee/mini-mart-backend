from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategories")

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand_name = models.CharField(max_length=120)
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="brand_category")

    def __str__(self):
        return self.brand_name