from django.urls import path
from .views import (
    ProductsList,
    CreateProduct,
    UpdateProduct,
    DeleteProduct,
    # GetOneObject,
    # ListCreateProduct,
    # GetUpdateProduct,
    # GetDeleteProduct,
    # GetUpdateDeleteProduct,
    )

urlpatterns = [
    path('', ProductsList.as_view(), name='products-list'),
    path('create/', CreateProduct.as_view(), name='create-product'),
    path('update/<int:pk>', UpdateProduct.as_view(), name='update-product'),
    path('delete/<int:pk>', DeleteProduct.as_view(), name='delete-product'),
    # path('get-one/<int:pk>', GetOneObject.as_view(), name='get-one-product'),
    # path('list-create/', ListCreateProduct.as_view(), name='list-create-product'),
    # path('get-update/<int:pk>', GetUpdateProduct.as_view(), name='get-update-product'),
    # path('get-delete/<int:pk>', GetDeleteProduct.as_view(), name='get-delete/product'),
    # path('get-update-delete/<int:pk>', GetUpdateDeleteProduct.as_view(), name='get-update-delete-product'),
]