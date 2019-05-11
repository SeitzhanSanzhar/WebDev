from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>/', post_detail),
    # path('users/<int:pk>/', ListUsers.as_view()),


    path('home/', MyPosts.as_view()),



    # Working views for books
    path('books/', ListCreateBooks.as_view()),
    path('books/<int:pk>/', RetrieveUpdateDestroyBook.as_view()),

    # Working auth urls
    path('login/', login),
    path('logout/', logout),
    path('users/', ListUsers.as_view()),


]