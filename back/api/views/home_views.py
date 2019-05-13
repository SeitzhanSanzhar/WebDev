from api.serializers import *
from api.models import *
from rest_framework import generics



# Надо добавить сюда две вьюшки написанные через CBV
class MyPosts(generics.ListCreateAPIView):
	def get_queryset(self):
		return Post.objects.filter(created_by=self.request.user)

	def get_serializer_class(self):
		return PostSerializer

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
