from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #GET ,POST ,PU ,DELETE
from .models import User ,Post
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user' , 'title' , 'text','create']

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer









# Create your views here.
