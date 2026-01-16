from django.shortcuts import render

# Create your views here.
def fotos(request):
    contexto = {
        'title' : 'Jornada Viagem | Fotos'
    }
    return render(
        request,
        'fotos/index.html',
        contexto,
    )