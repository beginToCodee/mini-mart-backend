from django.db import models
from django.contrib.auth.hashers import make_password


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200,unique=True,blank=False)
    contact_no = models.CharField(max_length=15)
    password = models.CharField(max_length=150)


    def __str__(self):
        return self.full_name

    def save(self,*args,**kwargs):
        if self.id is None:
            self.password = make_password(self.password)
        return super(Customer, self).save(*args,**kwargs)

