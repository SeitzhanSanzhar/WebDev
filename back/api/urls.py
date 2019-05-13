from django.urls import path
from .views import *
from django.urls import path, include


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
    path('signup/', Signup.as_view()),
    path('users/', ListUsers.as_view()),

    #mail
    path('send_mail/', send_answer),

    # Home urls
    path('home/', MyPosts.as_view()),
]
