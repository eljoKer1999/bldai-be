from django.urls import path

from bld.serializers import BookSerializer
from . import views
from rest_framework import generics
from .models import Book, Category
from .views import BookViewSet

urlpatterns = [
path('book/', BookViewSet.as_view())
]