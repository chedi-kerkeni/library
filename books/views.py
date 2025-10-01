from django.shortcuts import render
from .models import Book, Author


# Create your views here.

def home_books_view(request):
    books= Book.objects.all()
    context={'books':books}
    return render(request, 'books/home.html', context)

def single_book_view(request, book_id):
    book = Book.objects.get(id=book_id)
    author=book.author
    context= {'book':book, 'author':author}
    return render(request, 'books/single_book.html', context)

#def author_view(request, author_id):



