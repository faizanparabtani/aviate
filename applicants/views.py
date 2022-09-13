from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from rest_framework.views import APIView
from .models import User
from django.contrib.auth import login, logout


from rest_framework import generics, mixins, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from . serializers import (
    CreateUserSerializer,
    AuthCustomTokenSerializer,
    ChangePasswordSerializer
)


from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication



class CreateUserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": CreateUserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer