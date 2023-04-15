from django.shortcuts import render
from .serializers import PlayerCreateSerializer, PlayerSerializer, UserCreateSerializer, ChangePasswordSerializer, MyTokenObtainPairSerializer, PlayerProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import generics
from .models import User, Player, AdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PlayerCreateSerializer

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_superuser'] = False
        serializer.save()
    

class AdminUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = True
        serializer.validated_data['is_superuser'] = True
        serializer.save()


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.queryset.get(pk=self.request.user.player.id)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK, goodbye"})