from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Topico
from .models import CarrinhoItem
from django.contrib import messages
from urllib.parse import quote
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def adicionar_ao_carrinho(request, produto_id):
    # Função responsável por adicionar um produto ao carrinho
    # Recebe dois parâmetros:
    # request → contém as informações da requisição HTTP
    # produto_id → identifica qual produto (Topico) foi selecionado


    produto = get_object_or_404(Topico, id=produto_id)
    # Busca o produto no banco de dados pelo ID recebido
    # Caso o produto não exista, o Django retorna automaticamente
    # um erro 404 (página não encontrada)
    #
    # Isso evita erros e garante mais segurança à aplicação


    item, criado = CarrinhoItem.objects.get_or_create(produto=produto)
    # Tenta localizar um item do carrinho relacionado a esse produto
    #
    # Se o produto ainda NÃO estiver no carrinho:
    # → um novo registro é criado
    #
    # Se o produto JÁ estiver no carrinho:
    # → o registro existente é retornado
    #
    # A variável "criado" recebe:
    # True  → se o item foi criado agora
    # False → se o item já existia


    if not criado:
        # Se o item já existia no carrinho
        # aumentamos a quantidade em 1
        item.quantidade += 1
        item.save()
        # Salva a alteração no banco de dados


    messages.success(request, 'Produto adicionado ao carrinho!')
    # Exibe uma mensagem de sucesso para o usuário
    # Essa mensagem pode ser mostrada no template usando
    # o sistema de messages do Django


    return redirect('ver_carrinho')
    # Redireciona o usuário para a página de visualização do carrinho

@login_required
def ver_carrinho(request):
    # Função responsável por exibir os itens que estão no carrinho


    itens = CarrinhoItem.objects.all()
    # Recupera todos os itens armazenados no carrinho
    # Cada item representa um produto adicionado pelo usuário


    total = sum(item.total_preco() for item in itens)
    # Calcula o valor total da compra
    # Para cada item do carrinho:
    # - chama o método total_preco()
    # - soma todos os valores retornados
    #
    # Isso evita cálculos no template e mantém a lógica no backend


    return render(request, 'carrinho/carrinho.html', {
        'itens': itens,
        'total': total
    })
    # Renderiza o template do carrinho
    # Envia para o HTML:
    # - a lista de itens
    # - o valor total da compra


def remover_do_carrinho(request, item_id):
    # Função responsável por remover um item específico do carrinho
    # Recebe o ID do item que será excluído


    item = get_object_or_404(CarrinhoItem, id=item_id)
    # Busca o item no carrinho pelo ID
    # Caso o item não exista, retorna erro 404 automaticamente


    item.delete()
    # Remove o item do banco de dados


    return redirect('ver_carrinho')
    # Após remover, redireciona o usuário
    # para a página de visualização do carrinho


def finalizar_compra(request):
    # Função responsável por finalizar a compra
    # Gera uma mensagem com os dados do carrinho
    # e redireciona o usuário para o WhatsApp


    itens = CarrinhoItem.objects.all()
    # Recupera todos os itens que estão no carrinho


    if not itens:
        # Verifica se o carrinho está vazio
        messages.error(request, 'Carrinho vazio!')
        # Exibe uma mensagem de erro para o usuário
        return redirect('ver_carrinho')
        # Redireciona de volta para o carrinho


    mensagem = "🛒 Pedido de Compra:%0A%0A"
    # Texto inicial da mensagem que será enviada ao WhatsApp
    # %0A representa quebra de linha na URL


    total = 0
    # Variável que armazenará o valor total da compra


    for item in itens:
        # Percorre todos os itens do carrinho
        mensagem += (
            f"- {item.produto.tema} x {item.quantidade} "
            f"= R$ {item.total_preco()}%0A"
        )
        # Monta a descrição de cada item no pedido


        total += item.total_preco()
        # Soma o valor de cada item ao total


    mensagem += f"%0A💰 Total: R$ {total}"
    # Acrescenta o valor total ao final da mensagem


    CarrinhoItem.objects.all().delete()
    # Limpa o carrinho após a finalização da compra
    # Simula o fechamento do pedido


    whatsapp_url = f"https://wa.me/5521998200102?text={mensagem}"
    # Cria a URL de redirecionamento para o WhatsApp
    # O número deve ser substituído pelo telefone da empresa


    return redirect(whatsapp_url)
    # Redireciona o usuário para o WhatsApp
    # com a mensagem do pedido já preenchida