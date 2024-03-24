from django.contrib import admin
from .models import Produto, ItemVenda, Venda
# Register your models here.

admin.site.register(Produto)
admin.site.register(ItemVenda)
admin.site.register(Venda)