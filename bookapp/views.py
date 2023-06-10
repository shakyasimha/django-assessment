from django.shortcuts import render, HttpResponse
from bookapp.forms import BookForm 

# Create your views here.
def index(request):
    return render(request, 'bookapp/home.html')