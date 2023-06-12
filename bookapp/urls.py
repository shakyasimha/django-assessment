from django.urls import path 

from .views import book_list, book_detail, book_search

app_name = 'bookapp'

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('books/search/', book_search, name='book-search')
]