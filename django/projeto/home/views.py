from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    lista = '<ol><li>Kassimano</li><li>Pedro</li><li>Vitor</li></ol>'
    return HttpResponse(lista)