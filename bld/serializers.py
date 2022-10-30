from rest_framework import serializers
from .models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'author', 'category', 'publish_date')
        model = Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Category