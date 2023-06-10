from django.urls import path 

from .views import views


"""
    Template names, just for reference:

    - book_list.html 
    - book_detail.html 
    - book_form.html 
    - book_confirm_delete.html

"""

urlpatterns = [
    path('books/', BookView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookView.as_view(), name='book_detail')
]