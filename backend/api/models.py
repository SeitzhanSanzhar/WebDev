from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50,default="Klassika")

class Post(models.Model):
    title = models.CharField(max_length=100,default="Klassika")
    body = models.CharField(max_length=500,default="Klassika")
    created_by = models.ForeignKey(User,on_delete=None)
    created_at = models.DateTimeField(auto_now_add=True)
    book_info = models.ManyToManyField(Book)