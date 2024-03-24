from django.db import models


class Venda(models.Model):
    # manager 
    objects = models.Manager()

    # fields
    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
    )

    def __str__(self) -> str:
        return f'ID da venda: {self.id}'