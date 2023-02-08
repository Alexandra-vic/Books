from django.shortcuts import render

from .serializers import UserSerializers
from .models import User

from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
