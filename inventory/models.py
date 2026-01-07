from django.db import models
from django.contrib.auth import get_user_model

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descricao = models.TextField(blank=True)
    quantidade = models.IntegerField(default=0)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_minimo = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} ({self.codigo})'
    
class Movimentacao(models.Model):
    TIPOS = [
        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPOS)
    quantidade = models.IntegerField()
    usuario = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    observacao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} - {self.produto.nome} ({self.quantidade})'