from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('Post/', PostView.as_view()),
    path('Post/<int:pk>/', post_detail),
    path('Book/<int:pk>/', BookView.as_view()),
    path('User/<int:pk>/', UserList.as_view()),
    path('login/',login),
    path('logout/',logout),
    path('home/', MyPosts.as_view()),
    path('home/edit/', edit_profile),
]