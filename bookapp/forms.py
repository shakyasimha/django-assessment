from django import forms
from bookapp.models import Book 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['title', 'author', 'pub_year']