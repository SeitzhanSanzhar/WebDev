from api.serializers import *
from api.models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

class MyPosts(generics.ListCreateAPIView):

	def get_queryset(self):
		return Post.objects.filter(created_by=self.request.user)

	def get_serializer_class(self):
		return PostSerializer

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
