from django.shortcuts import render
from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer