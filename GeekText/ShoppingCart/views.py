from django.shortcuts import render
from rest_framework import generics

from ShoppingCart.models import Users, Books
from ShoppingCart.serializers import UserSerializer, BookSerializer
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserIndividual(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookIndividual(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

