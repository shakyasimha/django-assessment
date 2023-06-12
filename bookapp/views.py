from django.shortcuts import get_object_or_404, HttpResponse
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q 
from rest_framework import serializers
from rest_framework.parsers import JSONParser 

from .models import Book 

"""
    Template names, just for reference:

    - book_list.html 
    - book_detail.html 
    - book_search.html

"""

## Serializer class here
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ['id', 'title', 'author', 'publication_year']


@csrf_exempt
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=400)


@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.object.all()
        serializer = BookSerializer(books, safe=True)

        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.data, status=400)
    

@csrf_exempt
def book_search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)