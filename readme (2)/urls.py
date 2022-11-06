from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookListCreateView.as_view(), name="list_books"),
    path("<int:pk>/", views.BookRetrieveUpdateDeleteView.as_view(), name="list_books"),
    path("categories/", views.CategoriesListCreateView.as_view(), name="list_categories"),
]
