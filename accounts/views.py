from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import BusinessProfile
from .permissions import IsSelfOrReadOnly, IsOwner
from .serializers import BusinessSerializer, UserSerializer, UserCreateSer

# Create your views here.
class UserCreate(generics.CreateAPIView):
    Authentication_classes = ()
    permission_classes = ()
    serializer_class = UserCreateSer

class LoginView(APIView):
    permission_classes = ()
    serializer_class = UserCreateSer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token':user.auth_token.key, 'id' : user.id})
        else:
            return Response({'error': 'wrong credentials'},
                status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()#.filter(user.id)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

class BusinessViewset(viewsets.ModelViewSet):
    queryset = BusinessProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsSelfOrReadOnly,)
    serializer_class = BusinessSerializer
