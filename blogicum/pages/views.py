
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    """Функция открывает страницу с описанием Блогикума."""
    return render(request, 'pages/about.html')


def rules(request: HttpRequest) -> HttpResponse:
    """Функция открывает страницу с правилами Блогикума."""
    return render(request, 'pages/rules.html')
