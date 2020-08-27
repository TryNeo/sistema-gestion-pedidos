from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.dbd.modelos.esctructura_model_cliente import Cliente
from apps.dbd.forms.cliente.cliente_form import ClienteForm

class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    context_object_name = 'cliente_l'
    template_name = "cliente/cliente_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Clientes'
        return context