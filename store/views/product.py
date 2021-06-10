from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.models import *
from store.serializers import *
from django.http import Http404
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


class CategoryView(APIView):
    def get(self,request):
        serializer = CategorySerializer(Category.objects.all(),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class ProductView(APIView):
    def get(self,request):
        category = request.GET.get('category')
        query = request.GET.get('query')
       
        if category and query:
            category = SubCategory.objects.filter(name=category).first()
            if query:
                products = Product.objects.filter(category=category,title__contains=query)
            else:
                products = Product.objects.filter(category=category)
        elif query:
            products = Product.objects.filter(title__contains=query)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ProductNotFound(APIException):
    status_code = 404
    default_detail = "Unable to find the product"
    default_code = "Unable to found product"

class ProductDetailView(APIView):

    def get_instance(self,product_id):
        try:
            product = Product.objects.get(id=product_id)
            return product
        except:
            raise ProductNotFound()

    def get(self,request,product_id):
        product = self.get_instance(product_id)
        serializer = ProductSerializer(product,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

        
        
        