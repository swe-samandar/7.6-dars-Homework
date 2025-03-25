from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
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


class ForAPIView():
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsList(ForAPIView, ListAPIView):
    pass


class CreateProduct(ForAPIView, CreateAPIView):
    pass


class UpdateProduct(ForAPIView, UpdateAPIView):
    pass


class DeleteProduct(ForAPIView, DestroyAPIView):
    pass

# Faqat bitta obyektni olish uchun ishlatiladi.
class GetOneObject(ForAPIView, RetrieveAPIView):
    pass


# Obyektlar ro‘yxatini olish (GET) va yangi obyekt yaratish (POST) uchun ishlatiladi.
class ListCreateProduct(ForAPIView, ListCreateAPIView):
    pass


# Bitta obyektni olish (GET) va uni yangilash (PUT/PATCH) uchun ishlatiladi.
class GetUpdateProduct(ForAPIView, RetrieveUpdateAPIView):
    pass


# Bitta obyektni olish (GET) va o‘chirish (DELETE) uchun ishlatiladi.
class GetDeleteProduct(ForAPIView, RetrieveDestroyAPIView):
    pass


# Bitta obyektni olish (GET), yangilash (PUT/PATCH) va o‘chirish (DELETE) uchun ishlatiladi.
class GetUpdateDeleteProduct(ForAPIView, RetrieveUpdateDestroyAPIView):
    pass
