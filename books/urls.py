from django.urls import path

from . import views

app_name='books'

urlpatterns = [
    path('',views.home_books_view, name='home'),

]