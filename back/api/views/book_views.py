from rest_framework.permissions import IsAuthenticated
from api.serializers import BookSerializer
from api.models import Book
from rest_framework import generics


class ListCreateBooks(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Book.objects.filter(added_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class RetrieveUpdateDestroyBook(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Book.objects.filter(added_by=self.request.user)