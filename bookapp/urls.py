from django.urls import path 

from .views import BookView

app_name = 'bookapp'

urlpatterns = [
    path('', BookView.as_view(), name='book_list'),
    path('<int:pk>/', BookView.as_view(), name='book_detail')
]