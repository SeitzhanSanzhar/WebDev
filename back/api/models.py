from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    category = models.CharField(max_length=50, default='Fiction')
    genre = models.CharField(max_length=50, default="Classic")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=700, default="Classic")
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
