from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from apps.dbd.modelos.estructura_model_producto import Producto
from apps.dbd.forms.producto.producto_form import ProductoForm
from apps.dbd.views.mixin.mixin import MixinFormInvalid
from apps.dbd.views.errors.views import Privilegios

            
class ProductoListView(LoginRequiredMixin,Privilegios,ListView):
    model = Producto
    permission_required = "dbd.view_producto"
    context_object_name = 'producto_l'
    template_name = "producto/producto_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Productos'
        return context

class ProductoCreateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,CreateView):
    model = Producto
    permission_required = "dbd.add_producto"
    form_class = ProductoForm
    context_object_name = 'obj'
    template_name = "producto/producto_form.html"
    success_url = reverse_lazy('dbd:producto_list')
    
    def form_valid(self,form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creación de Producto'
        return context

class ProductoUpdateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,UpdateView):
    model = Producto
    permission_required = "dbd.change_producto"
    form_class = ProductoForm
    context_object_name = 'obj'
    template_name = "producto/producto_form.html"
    success_url = reverse_lazy('dbd:producto_list')


    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de Producto'
        return context

class ProductoDeleteView(LoginRequiredMixin,Privilegios,DeleteView):
    model = Producto
    permission_required = "dbd.delete_producto"
    context_object_name = 'obj'
    template_name = "producto/producto_delete.html"

    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user
        return super().form_valid(form)

    def post(self,request,pk,*args, **kwargs):
        producto = Producto.objects.get(id_producto=pk)
        producto.estado = False
        producto.save()
        return redirect('dbd:producto_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminacion de producto'
        return context
