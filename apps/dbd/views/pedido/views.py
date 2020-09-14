from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Sum

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

import datetime
from apps.dbd.modelos.estructura_model_producto import Producto
from apps.dbd.modelos.esctructura_model_cliente import Cliente
from apps.dbd.modelos.estructura_model_pedido import Pedido,PedidoItem
from apps.dbd.forms.pedido.pedido_form import PedidoForm
from apps.dbd.views.mixin.mixin import MixinFormInvalid
from apps.dbd.views.errors.views import Privilegios



class PedidoListView(LoginRequiredMixin,Privilegios,ListView):
    model = Pedido
    permission_required = "dbd.view_pedido"
    context_object_name = 'pedido_l'
    template_name = "pedido/pedido_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Pedido'
        return context

class PedidoUpdateView(LoginRequiredMixin,Privilegios,UpdateView):
    model = Pedido
    permission_required = "dbd.change_pedido"
    form_class = PedidoForm
    context_object_name = 'obj'
    success_url = reverse_lazy('dbd:pedido_list')
    template_name = "pedido/pedido_update.html"

    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Estado  del Pedido'
        return context

@login_required(login_url="/")
@permission_required("dbd.view_pedido",login_url="dbd:privilegios")
def pedidosdetalle(request,id_pedido=None):
    template_name = "pedido/pedido_form.html"
    #filtramos el producto si esta  activo
    prod = Producto.objects.filter(estado=True)
    form_pedido_detalle = {} #creamos el fom_class
    contexto = {} #creamos el contexto
    if request.method=='GET': #comprobamos si es por metodo post
        form_pedido_detalle = PedidoForm() #traemos nuestro Form
        ped = Pedido.objects.filter(id_pedido=id_pedido).first() #filtramos el pedido por id_pedido pasado por el url
        if ped:#comprobamos que el pedido exista
            ped_det = PedidoItem.objects.filter(pedido=ped) #filtramos en PedidoItem, los pedidos correspondientes
            fecha_pedido = datetime.date.isoformat(ped.fecha_pedido) #pasamos la fecha de pedido a una variabla externa
            p = { #creamos el contexto que se le pasara una vez comprobado que el pedido exista 
                'fecha_pedido':fecha_pedido,
                'num_pedido':ped.num_pedido,
                'estado_pedido':ped.estado_pedido,
                'form_pago':ped.forma_pago,
                'cliente':ped.cliente,
                'nota':ped.nota,
                'subtotal':ped.subtotal,
                'iva':ped.iva,
                'total':ped.total
            }
            form_pedido_detalle = PedidoForm(p) #y le pasamos el contexto en nuestro PedidoForm
        else: #caso contrario que no exista simplemente le pasamos que no existe nada en pedido detalle
            ped_det = None 
        contexto = {'productos':prod,'enca_ped':ped,'ped_detalle':ped_det,'form_enc':form_pedido_detalle} #al final pasamos 4 variables a nuestro contexto

    if request.method == 'POST':#comprobamos si lo hace por el metodo post
            #obtenemos nuesta data del form
            fecha_pedido = request.POST.get("fecha_pedido")
            forma_pago = request.POST.get("forma_pago")
            estado_pedido = request.POST.get("estado_pedido")
            nota = request.POST.get("nota")
            num_pedido = request.POST.get("num_pedido")
            cliente = request.POST.get("cliente")
            subtotal = 0
            iva = 0
            total = 0
            if not id_pedido:
                cli = Cliente.objects.get(pk=cliente) #filtramos por el cliente
                enc = Pedido( #y se le pasamos a nuestro modelo 
                    fecha_pedido = fecha_pedido,
                    estado_pedido = estado_pedido,
                    forma_pago = forma_pago,
                    nota = nota,
                    num_pedido = num_pedido,
                    cliente = cli,
                    usuario_crea = request.user
                )
                if enc: #comprobamos que todo este correcto
                    enc.save() # y lo guardamos
                    id_pedido =  enc.id_pedido #obtenemos el id del pedido accediendo a nuestra cabezera
            else: 
                enc = Pedido.objects.filter(pk=id_pedido).first() #filtramos el pedido y obtenemos el primero con .first()
                if enc: #le pasamos  nuestra variables obtenidas anteriormente del form
                    enc.fecha_pedido = fecha_pedido
                    enc.forma_pago = forma_pago
                    enc.estado_pedido = estado_pedido
                    enc.nota = nota
                    enc.num_pedido = num_pedido
                    enc.usuario_modifica = request.user
                    enc.save()
            if not id_pedido:
                return redirect('dbd:pedido_list')

            #obtenemos la data de nuesttro form pedido detalle
            producto = request.POST.get('id_id_producto_producto')
            cantidad = request.POST.get('id_cantidad_detalle')
            precio = request.POST.get('id_precio_detalle')
            subtotal_detalle = request.POST.get('id_subtotal_detalle')
            iva_detalle = request.POST.get('id_iva_detalle')
            total_detalle = request.POST.get('id_total_detalle')

            pro = Producto.objects.get(pk=producto) #filtramos el producto

            det = PedidoItem( #le pasamos nuestra data
                pedido = enc,
                producto = pro,
                cantidad = cantidad,
                precio = precio,
                iva = iva_detalle,

            )
            if det:#comprobamos
                det.save() #guardamos
                subtotal = PedidoItem.objects.filter(pedido=id_pedido).aggregate(Sum('subtotal')) #filtramos y usamos  Sum para obtener el subtotal total de nuestro items
                iva =PedidoItem.objects.filter(pedido=id_pedido).aggregate(Sum('iva')) #lo mismo con el iva
                enc.subtotal = subtotal["subtotal__sum"] 
                enc.iva=iva["iva__sum"]
                enc.save() # y guardamos
            
            return redirect("dbd:pedido_edit",id_pedido=id_pedido) # y redirecionamos al edit una vez que todo haya editado o haya agregado un nuevo item
    return render(request,template_name,contexto)


class PedidoItemDelete(LoginRequiredMixin,Privilegios,DeleteView):
    model = PedidoItem
    permission_required = "dbd.delete_pedidoitem"
    template_name = "pedido/pedido_item_delete.html"
    context_object_name = 'obj'

    def get_success_url(self):
        id_pedido = self.kwargs['id_pedido']
        return reverse_lazy('dbd:pedido_edit',kwargs={'id_pedido':id_pedido})

class PedidoDeleteView(LoginRequiredMixin,Privilegios,DeleteView):
    model = Pedido
    permission_required = "dbd.delete_pedido"
    context_object_name = 'obj'
    template_name = "pedido/pedido_delete.html"

    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user
        return super().form_valid(form)

    def post(self,request,pk,*args, **kwargs):
        pedido = Pedido.objects.get(id_pedido=pk)
        pedido.estado = False
        pedido.save()
        return redirect('dbd:pedido_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminacion de Pedido'
        return context