from django.urls import path

from . import views

app_name='books'

urlpatterns = [
    path('',views.home_books_view, name='home'),
    path('book/<int:book_id>/', views.single_book_view, name='single_book'),
    path('author/<int:author_id>/', views.author_view, name='author'),
    path('favorite/<int:book_id>/', views.choose_favorite, name='toggle_favorite'),
    path('favorite/<int:book_id>/', views.user_favorites, name='user_favorite'),
]