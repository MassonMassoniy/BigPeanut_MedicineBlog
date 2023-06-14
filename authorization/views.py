from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User
from .forms import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from .serializers import UserSerializer, GetUserSerializer, TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def test(request):
    return render(request, 'test.html')

class UserView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        return super().get_permissions()

    def get_current_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer


class RegisterView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer