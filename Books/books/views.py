from django.shortcuts import render
from .models import Books
from .serializers import BooksSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
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

class BooksList(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        rpns = {
            'data': serializer.data,
            'status': status.HTTP_200_OK,
            "message": 'Book List'
        }
        return Response(rpns)


class BookCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
                "message": 'Book Created'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
            return Response(rpns)
 

class BookUpdate(APIView):
    def put(self, request, pk, *args, **kwargs):
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Book Updated'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)
 

    def patch(self, request, pk, *args, **kwargs):
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Book Updated'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)


class BookDelete(APIView):
    def post(self, request, pk, *args, **kwargs):
        book = Books.objects.get(pk=pk)
class BookList(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        rpns = {
            'data': serializer.data,
            'status': status.HTTP_200_OK,
            "message": 'Book List'
        }
        return Response(rpns)


class BookCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
                "message": 'Book Created'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
            return Response(rpns)
 

class BookUpdate(APIView):
    def put(self, request, pk, *args, **kwargs):
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Book Updated'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)
 

    def patch(self, request, pk, *args, **kwargs):
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Book Updated'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)


class BookDelete(APIView):
    def post(self, request, pk, *args, **kwargs):
        book = Books.objects.get(pk=pk)
        



# class ForAPIView():
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


# class BooksList(ForAPIView, ListAPIView):
#     pass


# class BookCreate(ForAPIView, CreateAPIView):
#     pass


# class BookUpdate(UpdateAPIView):
#     pass


# class BookDelete(ForAPIView, DestroyAPIView):
#     pass


# class GetBook(ForAPIView, RetrieveAPIView):
#     pass


# class ListCreateBook(ForAPIView, ListCreateAPIView):
#     pass


# class GetUpdateBook(ForAPIView, RetrieveUpdateAPIView):
#     pass


# class GetDeleteBook(ForAPIView, RetrieveDestroyAPIView):
#     pass


# class GetUpdateDelete(ForAPIView, RetrieveUpdateDestroyAPIView):
#     pass