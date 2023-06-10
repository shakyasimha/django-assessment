from django.urls import path 

from . import views


"""
    Template names, just for reference:

    - book_list.html 
    - book_detail.html 
    - book_form.html 
    - book_confirm_delete.html

"""

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('view/<int:pk>', views.book_view, name='book_view'),
    path('new', views.book_create, name='book_new'),
    path('edit/<int:pk>', views.book_update, name='book_edit'), 
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
]