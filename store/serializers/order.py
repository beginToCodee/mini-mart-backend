from rest_framework import serializers
from store.models import *
from store.serializers.product import *


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(max_length=100)
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = ('id','customer','product','price','quantity','created_date','created_time','status')

        read_only_fields = ['product']