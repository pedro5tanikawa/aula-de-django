from django.shortcuts import render

# Create your views here.
def fotos(request):
    return render(
        request,
        'fotos/index.html'
    )

