from django.shortcuts import render

# Create your views here.
def destinos(request):
    return render(
        request,
        'destinos/index.html'
    )

