from django.urls import path
from books.views import get_book

urlpatterns = [
    path('', get_book)
]