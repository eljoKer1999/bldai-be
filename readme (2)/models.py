from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-published_at"]
