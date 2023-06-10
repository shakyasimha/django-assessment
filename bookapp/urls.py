from django.urls import path 

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='all'),
    path('bookapp/<int:pk>/detail', views.BookDetailView.as_view(), name='book_detail'),
    path('bookapp/create/', views.BookCreateView.as_view(), name='book_create'),
    path('bookapp/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('bookapp/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete')
]