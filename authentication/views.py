from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
