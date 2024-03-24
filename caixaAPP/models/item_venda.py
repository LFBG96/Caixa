from django.db import models


class ItemVenda(models.Model):
    # manager
    objects = models.Manager()

    # fields
    produto = models.ForeignKey(
        to='caixaAPP.Produto',
        on_delete=models.PROTECT,
        related_name='produtos_itensvendas',
        null=True
    )
    venda = models.ForeignKey(
        to='caixaAPP.Venda',
        on_delete=models.PROTECT,
        related_name='vendas_itensvendas',
        null=True
    )
    quantidade = models.SmallIntegerField(null=True)

    
    def __str__(self) -> str:
        return f'{self.produto} - {self.quantidade}x : Venda: {self.venda}'