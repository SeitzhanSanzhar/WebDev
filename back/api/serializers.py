from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200, required=True)
    author = serializers.CharField(max_length=200, required=True)
    year = serializers.IntegerField(required=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    # Use id references for testing. Change back to proper serializers when done
    book_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
