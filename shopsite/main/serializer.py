from django.urls import include,path
from django.contrib.auth.models import User
from rest_framework import routers,serializers,viewsets
from .models import Users

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Users
        fileds = ['name','password','email','phone','time','confirmed','account']