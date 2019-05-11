from django.urls import path
from .views import *

urlpatterns = [
    # Working views for posts
    path('posts/', ListCreatePosts.as_view()),
    path('posts/<int:pk>/', RetrieveUpdateDestroyPosts.as_view()),

    # Working views for books
    path('books/', ListCreateBooks.as_view()),
    path('books/<int:pk>/', RetrieveUpdateDestroyBooks.as_view()),

    # Working auth urls
    path('login/', login),
    path('logout/', logout),
    path('users/', ListUsers.as_view()),



    # Home urls
    path('home/', MyPosts.as_view()),
]