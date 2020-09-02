from django.contrib import admin
from apps.dbd.modelos.estructura_model_producto import Producto
from apps.dbd.modelos.esctructura_model_cliente import Cliente
from apps.dbd.modelos.estructura_model_catalogo import Categoria

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Categoria)