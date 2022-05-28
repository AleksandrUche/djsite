from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения women.")

def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

