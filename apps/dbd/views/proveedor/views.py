from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from apps.dbd.modelos.estructura_model_proveedor import Proveedor
from apps.dbd.forms.proveedor.proveedor_form import ProveedorForm


class ProveedorListView(ListView):
    model = Proveedor
    context_object_name = 'proveedor_l'
    template_name = "proveedor/proveedor_list.html"
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Proveedores'
        return context


class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    context_object_name = 'obj'
    template_name = "proveedor/proveedor_form.html"
    success_url = reverse_lazy('dbd:proveedor_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.usuario_crea =  self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creación de Proveedor'
        return context