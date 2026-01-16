from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cadastro.models import Pessoa

# Create your views here.
def cadastro(request):
    contexto = {
        'title' : 'Jornada Viagem | Cadastro',
        'mensagem': 'Você acessou o cadastro'
    }
    return render(
        request,
        'cadastro/index.html',
        contexto,
    )

def gravar(request):
    # Salvar os dados para tabela
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.idade = request.POST.get('idade')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()

    return cadastro(request)


@login_required
def exibe(request):
    # exibir todas as pessoas
    exibe_pessoas = {
        'pessoas': Pessoa.objects.all()
    }
    # Retornar os dados para a página
    return render(
        request,
        'cadastro/mostrar.html',
        exibe_pessoas,
    )

def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render(
        request,
        'cadastro/editar.html',
        {"pessoa": pessoa}
    )

def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.idade = request.POST.get('idade')
    pessoa.email = request.POST.get('email')
    pessoa.save()

    return exibe(request)

def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()     

    return exibe(request)
