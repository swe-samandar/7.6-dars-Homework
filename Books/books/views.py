from django.shortcuts import render
from .models import Books
from .serializers import BooksSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView, 
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    )

class ForAPIView():
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksList(ForAPIView, ListAPIView):
    pass


class BookCreate(ForAPIView, CreateAPIView):
    pass


class BookUpdate(UpdateAPIView):
    pass


class BookDelete(ForAPIView, DestroyAPIView):
    pass


class GetBook(ForAPIView, RetrieveAPIView):
    pass


class ListCreateBook(ForAPIView, ListCreateAPIView):
    pass


class GetUpdateBook(ForAPIView, RetrieveUpdateAPIView):
    pass


class GetDeleteBook(ForAPIView, RetrieveDestroyAPIView):
    pass


class GetUpdateDelete(ForAPIView, RetrieveUpdateDestroyAPIView):
    pass