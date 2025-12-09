from django.shortcuts import render

# Create your views here.
# Criação de funções de visualização
def home(request):
    return render(
        request,
        'home/index.html'
    )

