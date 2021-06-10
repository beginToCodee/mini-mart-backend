from django.db import models
from store.models import *



class DateTimeTracker(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    created_time = models.TimeField(auto_now_add=True)
    updated_time = models.TimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(DateTimeTracker):
    status_choices = (
        ('approve','approve'),
        ('pending','pending')
    )
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=50,choices=status_choices,default="pending")

    def __str__(self):
        return f"{self.customer} {self.product}"
