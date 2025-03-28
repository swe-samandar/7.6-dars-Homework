from django.urls import path
from .views import (
    BooksList,
    BookCreate,
    BookUpdate,
    BookDelete,
    # GetBook,
    # ListCreateBook,
    # GetUpdateBook,
    # GetDeleteBook,
    # GetUpdateDelete,
    )

urlpatterns = [
    # path('', BooksList.as_view(), name='book-list' ),
    path('create/', BookCreate.as_view(), name='book-create' ),
    path('update/<int:pk>', BookUpdate.as_view(), name='book-update'),
    path('delete/<int:pk>', BookDelete.as_view(), name='book-delete'),
    # path('get-one/<int:pk>', GetBook.as_view(), name='get-one-book'),
    # path('list-create/', ListCreateBook.as_view(), name='list-create-book'),
    # path('get-update/<int:pk>', GetUpdateBook.as_view(), name='get-update-book'),
    # path('get-delete/<int:pk>', GetDeleteBook.as_view(), name='get-delete-book'),
    # path('get-update-delete/<int:pk>', GetUpdateDelete.as_view(), name='get-update-delete-book'),
]

