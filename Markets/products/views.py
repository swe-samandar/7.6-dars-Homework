from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
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

# Create your views here.



class ProductsList(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        rpns = {
            'data': serializer.data,
            'status': status.HTTP_200_OK,
            "message": 'product List'
        }
        return Response(rpns)


class CreateProduct(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
                "message": 'product Created'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
            return Response(rpns)
 

class UpdateProduct(APIView):
    def put(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'product Updated'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)
 

    def patch(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'product Updated'
            }
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)


class DeleteProduct(APIView):
    def post(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)


# class ForAPIView():
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductsList(ForAPIView, ListAPIView):
#     pass


# class CreateProduct(ForAPIView, CreateAPIView):
#     pass


# class UpdateProduct(ForAPIView, UpdateAPIView):
#     pass


# class DeleteProduct(ForAPIView, DestroyAPIView):
#     pass

# Faqat bitta obyektni olish uchun ishlatiladi.
# class GetOneObject(ForAPIView, RetrieveAPIView):
#     pass


# Obyektlar ro‘yxatini olish (GET) va yangi obyekt yaratish (POST) uchun ishlatiladi.
# class ListCreateProduct(ForAPIView, ListCreateAPIView):
#     pass


# Bitta obyektni olish (GET) va uni yangilash (PUT/PATCH) uchun ishlatiladi.
# class GetUpdateProduct(ForAPIView, RetrieveUpdateAPIView):
#     pass


# Bitta obyektni olish (GET) va o‘chirish (DELETE) uchun ishlatiladi.
# class GetDeleteProduct(ForAPIView, RetrieveDestroyAPIView):
#     pass


# Bitta obyektni olish (GET), yangilash (PUT/PATCH) va o‘chirish (DELETE) uchun ishlatiladi.
# class GetUpdateDeleteProduct(ForAPIView, RetrieveUpdateDestroyAPIView):
#     pass
