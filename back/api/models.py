from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    category = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
