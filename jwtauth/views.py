from django.shortcuts import render
from jwtauth.serializers import RegisrationSerializerApi ,LoginSerializer
from jwtauth.models import Regisration
from rest_framework import serializers ,status ,response ,permissions
from rest_framework.generics import GenericAPIView
from django.contrib.auth.hashers import check_password,make_password 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class UserRegistrationApi(GenericAPIView):
    serializer_class = RegisrationSerializerApi
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self ,request):
        obj = Regisration.objects.all()
        serializer = self.serializer_class(obj ,many=True)
        return response.Response(serializer.data)
        
        
    def get_queryset(self):
        obj = Regisration.objects.all()
        return obj
    def post(self , request):
        serializer  = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username=serializer.validated_data.get('username')
        first_name=serializer.validated_data.get('first_name')
        last_name=serializer.validated_data.get('last_name')
        email=serializer.validated_data.get('email')
        password=serializer.validated_data.get('password')
        confirm_password=serializer.validated_data.get('confirm_password')
        obj = Regisration.objects.create(user_roll='client',username=username , first_name=first_name,last_name=last_name ,email=email,password=make_password(password))
        obj.save()
        return response.Response(serializer.data)


