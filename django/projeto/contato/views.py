from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contato(request):
    pagina = '<body><h1><center>pedro</center></h1>'
    return HttpResponse(pagina)
