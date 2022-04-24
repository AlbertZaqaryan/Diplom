from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from . import myscript
# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(request, 'index.html', context)


def mybook(request):
    book_list = Book.objects.all().values()    
    book = request.POST['book_name']
    filename = myscript.myfunc(book)
    output = ''
    for j in book_list:
        output += j['section']
    if output == filename:
        return HttpResponse('Yes')
    return HttpResponse('No')