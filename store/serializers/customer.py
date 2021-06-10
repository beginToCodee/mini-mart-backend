from store.models import *
from rest_framework import serializers
from django.contrib.auth.hashers import check_password


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','full_name', 'email','contact_no')


class CustomerSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150)
    re_password = serializers.CharField(max_length=150)
    class Meta:
        model = Customer
        fields = ('full_name','email','contact_no','password','re_password')
    

    def validate(self,validated_data):
        password = validated_data.get('password')
        re_password = validated_data.get('re_password')
        
        
        if password and re_password:
            if password != re_password:
                error = {
                    'password':['both password is not matched']
                }
            elif len(password)<7:
                
                error = {
                    'password':['at least 7 charectors are required']
                }
            
            elif password.isdigit():
                error = {
                    'password':['only numeric values are not allowed']
                }
            else:
               
                return validated_data
        else:
            error = {
                'password':['This field is required '],
                're_password':['This field is required']
            }
        raise serializers.ValidationError(error)
    
 

class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(max_length=150)

    def validate(self,validated_data):
        email = validated_data.get('email','')
        password = validated_data.get('password','')
    
        if email and password:
            customer = Customer.objects.filter(email=email).first()
            if customer:
                if check_password(password,customer.password):
                    validated_data['customer'] = customer
                    return validated_data
                else:
                    error = {
                        'password':['password is not valid']
                    }
            else:
                error = {
                    'email':["this email id doesn't exist "]
                }
        raise serializers.ValidationError(error)




                
