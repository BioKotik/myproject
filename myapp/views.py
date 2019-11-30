from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world!")


def table(request):
    return render(request, 'table.html')


