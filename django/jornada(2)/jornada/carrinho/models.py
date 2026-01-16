from django.db import models
# Importa o módulo models do Django, que contém as classes
# necessárias para criar modelos ligados ao banco de dados

from blog.models import Topico
# Importa o model Topico do app blog


# Create your models here.
class CarrinhoItem(models.Model):
    # Classe responsável por representar um item dentro do carrinho
    # Cada registro desta tabela será um produto adicionado ao carrinho


    produto = models.ForeignKey(
        Topico,
        on_delete=models.CASCADE
    )
    # ForeignKey cria um relacionamento entre o Carrinho e o Produto (Topico)
    # Isso significa que cada item do carrinho está ligado a um Topico
    #
    # on_delete=models.CASCADE:
    # Caso o produto seja excluído do sistema,
    # todos os registros relacionados a ele no carrinho também serão removidos


    quantidade = models.PositiveIntegerField(default=1)
    # Campo que armazena a quantidade do produto no carrinho
    # PositiveIntegerField garante que o valor seja sempre positivo (>= 0)
    # default=1 define que, ao adicionar um produto,
    # a quantidade inicial será 1


    def total_preco(self):
        # Método responsável por calcular o valor total do item no carrinho
        # Multiplica a quantidade pelo preço do produto
        return self.quantidade * self.produto.preco
    def __str__(self):
        # Método especial que define como o objeto será exibido
        # no Django Admin e em impressões no terminal
        #
        # Exemplo de saída:
        # "Pacote Rio de Janeiro (2)"
        return f"{self.produto.tema} ({self.quantidade})"