from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import BookForm 
from .models import Book 


"""
    CRUD operations in this view:

    - book_list()
    - book_view()
    - book_create()
    - book_update()
    - book_delete()

"""


"""
    Template names, just for reference:

    - book_list.html 
    - book_detail.html 
    - book_form.html 
    - book_confirm_delete.html


"""

class BookView(View):
    template_name = 'book_list.html'
    form_class = BookForm 

    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(Book, pk=pk)
            return render(request, 'book_detail.html', {'book': book})
        
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})


    def post(self, request, pk=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            return render(request, 'book_create.html', {'form': form})
    

    def put(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        form = self.form_class(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            return render(request, 'book_update.html', {'form': form, 'book': book})
    
    def delete(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('book_list')