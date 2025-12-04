from django.http import HttpResponse
import socket


def home(request):
    # Obter o nome do host ou IP do cliente
    hostname = socket.gethostname()
       
    message = f"Olá, visitante de {hostname}! - Create by aluno do Elias"
    
   
    return HttpResponse(message)


