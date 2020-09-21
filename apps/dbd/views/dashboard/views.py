import datetime

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.acts.models import User
from apps.dbd.modelos.estructura_model_catalogo import Categoria
from apps.dbd.modelos.esctructura_model_cliente import Cliente
from apps.dbd.modelos.estructura_model_producto import Producto
from apps.dbd.modelos.estructura_model_proveedor import Proveedor
from apps.dbd.modelos.estructura_model_pedido import Pedido
from apps.dbd.modelos.estructura_model_pedido import Pedido

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Inicio|Asoprotesue'
        context['usuarios'] = User.objects.filter(is_active=True).count()
        context['clientes'] = Cliente.objects.filter(estado=True).count()
        context['proveedor'] = Proveedor.objects.filter(estado=True).count()
        context['pedido'] = Pedido.objects.filter(estado=True).count()
        context['pedidos'] = Pedido.objects.filter(fecha_crea=datetime.date.today())[:5]
        context['productos'] = Producto.objects.filter(fecha_crea=datetime.date.today())[:5]

        return context


class HistorialView(LoginRequiredMixin,TemplateView):
    template_name = 'historial/historial_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Historial | Registros - Cambios'
        context['pedidos'] = Pedido.objects.all()
        context['productos'] = Producto.objects.all()
        context['clientes'] = Cliente.objects.all()
        context['categorias'] = Categoria.objects.all()
        context['proveedores'] = Proveedor.objects.all()
        return context