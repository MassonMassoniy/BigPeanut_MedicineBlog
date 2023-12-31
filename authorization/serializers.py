from .models import User, Country
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer, TokenObtainPairSerializer
)
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.core.exceptions import ObjectDoesNotExist


class CountryUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ['country']

    def get_user_info(self, obj):
        serializer = GetUserSerializer(obj.user)
        return serializer.data


class CountryCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = '__all__'

    def get_user_info(self, obj):
        serializer = GetUserSerializer(obj.user)
        return serializer.data


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'account_name', 'role', 'date_joined']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['account_name', 'password',]


class UserPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, *args, **kwargs):
        data = super().validate(*args, **kwargs)

        if not self.user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {self.user.account_name} был деактивирован!"
            }, code='user_deleted')

        data['id'] = self.user.id
        data['account_name'] = self.user.account_name

        return data


class TokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])

        try:
            user = User.objects.get(
                pk=refresh.payload.get('user_id')
            )
        except ObjectDoesNotExist:
            raise serializers.ValidationError({
                'detail': f"Пользователь был удалён!"
            }, code='user_does_not_exists')

        if not user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {user.account_name} был заблокирован!"
            }, code='user_deleted')

        data['id'] = user.id
        data['account_name'] = user.account_name

        return data
