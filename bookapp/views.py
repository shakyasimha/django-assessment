from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import BookForm 
from .models import Book 


"""
    Template names, just for reference:

    - book_list.html 
    - book_detail.html 
    - book_create.html

"""

class BookView(View):
    template_name = 'book_list.html'
    #template_name = 'book_detail.html'
    form_class = BookForm 

    ## For retrieving book entries
    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(Book, pk=pk)
            return render(request, 'book_detail.html', {'book': book})
        
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})


    ## For creating new book entries
    def post(self, request, pk=None):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            return render(request, 'book_create.html', {'form': form})
    

    ## For updating book entries
    def put(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        form = self.form_class(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            return render(request, 'book_update.html', {'form': form, 'book': book})
    

    ## For deleting the book entry
    def delete(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('book_list.html')