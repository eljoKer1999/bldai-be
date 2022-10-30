from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import BookSerializer, CategorySerializer
from .models import Book, Category

class BookViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
