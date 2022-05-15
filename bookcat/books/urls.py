from django.urls import path
from .views import BookList, BookCreate

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('create/', BookCreate.as_view(), name='book_create')
]
