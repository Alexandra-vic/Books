from django.shortcuts import render
from . serializers import BookSerializers
from . models import Book

from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
