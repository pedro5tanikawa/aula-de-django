from django.shortcuts import render

# Create your views here.

def blog(request):
    contexto = {
        'title' : 'Jornada Viagem | Blog'
    }
    return render(
        request,
        'blog/index.html',
        contexto,
    )

