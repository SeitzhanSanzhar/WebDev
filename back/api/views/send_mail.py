from django.core.mail import send_mail

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from django.db.utils import IntegrityError


@api_view(['POST'])
def send_answer(request):
    send_mail(':)', ':)', 'kitapswap@gmail.com', ['lejena@key-mail.net'], fail_silently=False)