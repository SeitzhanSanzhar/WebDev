from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    year = serializers.IntegerField()
    author = serializers.CharField()
    genre = serializers.CharField()
    class Meta:
        model = Book
        fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    body = serializers.CharField()
    created_by = UserSerializer()
    created_at = serializers.DateTimeField()
    book_info = BookSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'