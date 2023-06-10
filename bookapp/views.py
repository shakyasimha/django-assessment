from django.shortcuts import render, redirect, get_object_or_404

from bookapp.forms import BookForm 
from bookapp.models import Book 


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



## Lists down the books
def book_list(request, template_name='books/book_list.html'):
    book = Book.objects.all() 
    data = {}
    data['object_list'] = book 

    return render(request, template_name, data)


## For viewing the books
def book_view(request, pk, template_name='books/book_detail.html'):
    book = get_object_or_404(Book, pk=pk)
    
    return render(request, template_name, {object: 'book'})



## For creating a book entry
def book_create(request, template_name='books/book_form.html'):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save() 
        return redirect('book_list')
    
    return render(request, template_name, {'form': form})



## For updating a book entry
def book_update(request, pk, template_name='books/book_form.html'):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()

        return redirect('book_list')
    
    return render(request, template_name, {'form': form})


## For deleting the book 
def book_delete(request, pk, template_name='books/book_confirm_delete.html'):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete() 

        return redirect('book_list')
    
    return render(request, template_name, {'object': book})