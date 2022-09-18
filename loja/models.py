from django.db import models
from django.core.validators import MinLengthValidator


class Produto(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(null=False, blank=True, default='descrição')
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return (f'{self.nome}.....R${self.valor}')
    
    
class Pedido(models.Model):
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], null=False, blank=False, default='')
    endereco = models.CharField(max_length=100, default='')
    prazoEntrega = models.CharField(max_length=11, default='1 dia')
    codigoProduto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    
    def __str__(self):
        return (f'{self.cpf} - {self.codigoProduto} - {prazoEntrega}')
