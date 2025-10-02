from django.shortcuts import render , redirect
from .models import Book, Author
from django.contrib.auth.decorators import login_required



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

def author_view(request, author_id):
    books= Book.objects.filter(author_id=author_id)
    context={'books':books}
    return render(request, 'books/author_view.html', context)

@login_required(login_url='login')
def choose_favorite(request, book_id):
    book=Book.objects.get(id=book_id)
    if request.user in book.favorited_by.all():
        book.favorited_by.remove(request.user)
    else:
        book.favorited_by.add(request.user)
    return redirect('single_book', book_id=book_id)

@login_required
def user_favorites(request):
    favorite_books = request.user.favorite_books.all()
    context = {'books': favorite_books}
    return render(request, 'books/user_favorite.html', context)
