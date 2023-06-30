import requests
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from .models import User, Country
from .forms import *
from .serializers import *
from .permissions import AmI, IsMyCountry
from blog.views import get_client_ip
# Create your views here.

def password_update_page(request):
    return render(request, 'login/password_change.html')

def profile(request):
    return render(request, 'profile.html')


def login(request):
    return render(request, 'login/login.html')


def register(request):
    return render(request, 'login/register.html')


class CountryUpdateView(ModelViewSet):
    permission_classes = [IsMyCountry]
    serializer_class = CountryUpdateSerializer
    queryset = Country.objects.all()

    def get_permissions(self):
        return super().get_permissions()
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class CountryCreateView(ModelViewSet):
    permission_classes = [IsMyCountry]
    serializer_class = CountryCreateSerializer
    queryset = Country.objects.all()

    def get_permissions(self):
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UserView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        return super().get_permissions()

    def get_current_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserUpdateView(ModelViewSet):
    permission_classes = [AmI]
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        return super().get_permissions()

    def get_current_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        return Response('Запрещённая операция')
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UserPrivateView(ModelViewSet):
    permission_classes = [AmI]
    serializer_class = UserPrivateSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        return super().get_permissions()

    def get_current_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class RegisterView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    serializer_class = UserUpdateSerializer


class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer