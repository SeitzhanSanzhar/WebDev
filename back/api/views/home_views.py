from api.serializers import *
from api.models import *
from rest_framework import generics


class MyPosts(generics.ListCreateAPIView):
	serializer_class = PostSerializer

	def get_queryset(self):
		return Post.objects.filter(created_by=self.request.user)

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
