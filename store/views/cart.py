from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.models import *
from store.serializers import *


class CartIndexView(APIView):
    def get(self,request):
        product_id = str(request.GET.get('product_id'))
        quantity = request.GET.get('quantity')
        try:
            cart = request.session['cart']
        except:
            cart = {}
        if product_id and quantity and Product.objects.filter(id=product_id).first():
            
            keys = list(cart.keys())
            if product_id in keys and int(quantity)<=0:
                cart.pop(product_id)
            else:
                cart[product_id] = int(quantity)
            request.session['cart'] = cart
        products = Product.get_product_by_keys(list(cart.keys()))
        temp = []
        for product in products:
            q = cart[str(product.id)]
            serializer = ProductSerializer(product,many=False)
            t = {
                'qunatity':q,
                'product':dict(serializer.data)
            }
            temp.append(t)
        return Response(temp,status=status.HTTP_200_OK)







        

        



