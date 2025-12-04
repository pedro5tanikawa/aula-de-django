from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    print('passei no blog')
    return HttpResponse('<body bgcolor="blue">alo mundo</body>')
