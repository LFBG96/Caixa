from django.db import models


class Produto(models.Model):
    # manager
    objects = models.Manager()
    # fields
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.nome}'