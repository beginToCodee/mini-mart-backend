from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.models import *
from store.serializers import *


class OrderIndexView(APIView):
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)

