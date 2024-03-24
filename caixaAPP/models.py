from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class ItensVenda(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.produto.nome


class Carrinho(models.Model):
    produtos = models.ManyToManyField(to=Produto)
    total = models.DecimalField(max_digits=10, decimal_places=2)
