from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_book(request):
    return HttpResponse('Enter a book title you want to take: ')