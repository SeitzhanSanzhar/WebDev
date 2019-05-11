from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('id', 'username', 'email')

=======
        fields = ('__all__')
>>>>>>> a2740318152ca2de67472b52227db542ad6de913

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200, required=True)
    year = serializers.IntegerField(required=True)
    author = serializers.CharField(max_length=200, required=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200, required=True)
    created_by = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'