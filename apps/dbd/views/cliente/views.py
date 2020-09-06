from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.dbd.modelos.esctructura_model_cliente import Cliente
from apps.dbd.forms.cliente.cliente_form import ClienteForm
from apps.dbd.views.mixin.mixin import MixinFormInvalid


class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    context_object_name = 'cliente_l'
    template_name = "cliente/cliente_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Clientes'
        return context

class ClienteCreateView(LoginRequiredMixin,MixinFormInvalid,CreateView):
    model = Cliente
    form_class = ClienteForm
    context_object_name = 'obj'
    template_name = "cliente/cliente_form.html"
    success_url = reverse_lazy('dbd:cliente_list')

    def form_valid(self,form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de Cliente'
        return context


class ClienteUpdateView(LoginRequiredMixin,MixinFormInvalid,UpdateView):
    model = Cliente
    form_class = ClienteForm
    context_object_name = 'obj'
    template_name = "cliente/cliente_form.html"
    success_url = reverse_lazy('dbd:cliente_list')


    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de Cliente'
        return context


class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    model = Cliente
    context_object_name = 'obj'
    template_name = "cliente/cliente_delete.html"

    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user
        return super().form_valid(form)

    def post(self,request,pk,*args, **kwargs):
        cliente = Cliente.objects.get(id_cliente=pk)
        cliente.estado = False
        cliente.save()
        return redirect('dbd:cliente_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminacion de Cliente'
        return context