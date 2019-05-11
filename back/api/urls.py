from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>/', post_detail),
    path('books/<int:pk>/', BookView.as_view()),

    # path('users/<int:pk>/', ListUsers.as_view()),

    path('login/', login),
    path('logout/', logout),
    path('users/', ListUsers.as_view()),

    path('home/', MyPosts.as_view()),
]