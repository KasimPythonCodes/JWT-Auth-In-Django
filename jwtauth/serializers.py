from jwtauth.models import Regisration
from rest_framework import serializers

class RegisrationSerializerApi(serializers.ModelSerializer):
    class Meta:
        model = Regisration
        fields = ('username','first_name','last_name','email','password')
    
    
     

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
