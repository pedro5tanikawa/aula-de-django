from django.shortcuts import render

# Create your views here.
def destinos(request):
    contexto = {
        'title' : 'Jornada Viagem | Destino'
    }
    return render(
        request,
        'destinos/index.html',
        contexto,
    )
