from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from apps.dbd.modelos.estructura_model_producto import Producto
from apps.dbd.forms.producto.producto_form import ProductoForm


class ProductoListView(LoginRequiredMixin,ListView):
    model = Producto
    context_object_name = 'producto_l'
    template_name = "producto/producto_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Productos'
        return context