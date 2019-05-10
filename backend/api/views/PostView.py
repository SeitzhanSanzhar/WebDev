from api.serializers import *
from api.models import *
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response

class PostView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET','POST','DELETE','PUT'])
@permission_classes((IsAuthenticated, ))
def post_detail(request, pk) :
     try:
         res = Post.objects.get(id=pk)
     except Post.DoesNotExist:
         return Response('Post list not found',status=404)
     if(request.method == 'GET'):
         ser = PostSerializer(res)
         return Response(ser.data)
     if(request.method == 'PUT'):
         ser = PostSerializer(instance=res,data=request.data)
         if(ser.is_valid()):
             ser.save()
             return Response(ser.data,status=201)
         return Response('some error occured')
     if(request.method == 'DELETE'):
         res.delete()
         return Response('done:')