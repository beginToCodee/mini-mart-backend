from rest_framework.response import Response
from rest_framework.views import APIView
from store.serializers import *
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from store.permissions import *



class CustomerSignUpView(APIView):
    def post(self,request):
        serializer = CustomerSignUpSerializer(data=request.data)
        if serializer.is_valid():
            full_name = serializer.validated_data.get('full_name')
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            contact_no = serializer.validated_data.get('contact_no')
            customer = Customer(full_name=full_name,contact_no=contact_no,password=password,email=email)
            customer.save()
            serializer = CustomerSerializer(customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailView(APIView):
    def get_customer(self,request):
        customer = Customer.objects.filter(id=request.session['customer_id']).first()
        return customer
    def get(self,request):
        customer = self.get_customer(request)

        serializer = CustomerSerializer(customer)

        return Response(serializer.data,status=status.HTTP_200_OK)
    


class CustomerLoginView(APIView):
    def post(self,request):
        serializer = CusomterLoginSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.validated_data['customer']
            request.session['customer_id'] = customer.id
            serializer = CustomerSerializer(customer)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomerLogoutView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsCustomerAuthenticated]
    def get(self,request):
        try:
            del request.session['customer_id']
        except Exception as e:
            print(e)
        return Response(status=status.HTTP_200_OK)

class IsAuthencatedCustomer(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsCustomerAuthenticated]
    def get(self,request):
        try:
            customer = Customer.objects.get(id=request.session['customer_id'])
        except Exception as e:
            print(e)
        serializer = CustomerSerializer(customer,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)