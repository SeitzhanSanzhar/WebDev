from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.forms import UserChangeForm
from api.forms import EditProfile


# class RetrieveUpdateProfile(generics.RetrieveUpdateAPIView):
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         return Post.objects.filter(created_by=self.request.user)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return Response('Successfully edited')

        return Response('Please, try again')
    return Response('This method is not allowed')
