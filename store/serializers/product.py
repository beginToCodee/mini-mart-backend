from rest_framework import serializers
from store.models import *


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=120)
    class Meta:
        model = Product
        fields = ('id','title','image','description','old_price','current_price','category','brand')
        