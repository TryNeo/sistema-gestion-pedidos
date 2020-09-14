from django.contrib import admin
from apps.dbd.modelos.estructura_model_producto import Producto
from apps.dbd.modelos.esctructura_model_cliente import Cliente
from apps.dbd.modelos.estructura_model_catalogo import Categoria
from apps.dbd.modelos.estructura_model_pedido import Pedido,PedidoItem

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(PedidoItem)
