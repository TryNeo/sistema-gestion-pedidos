from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from apps.dbd.modelos.estructura_model_proveedor import Proveedor
from apps.dbd.forms.proveedor.proveedor_form import ProveedorForm,ConsultaProveedorForm
from apps.dbd.views.mixin.mixin import MixinFormInvalid
from apps.dbd.views.errors.views import Privilegios

class ProveedorListView(LoginRequiredMixin,Privilegios,ListView):
    model = Proveedor
    permission_required = "dbd.view_proveedor"
    context_object_name = 'proveedor_l'
    template_name = "proveedor/proveedor_list.html"

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Proveedores'
        return context


class ProveedorCreateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,CreateView):
    model = Proveedor
    permission_required = "dbd.add_proveedor"
    form_class = ProveedorForm
    context_object_name = 'obj'
    template_name = "proveedor/proveedor_form.html"
    success_url = reverse_lazy('dbd:proveedor_list')
    
    def form_valid(self,form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creación de Proveedor'
        return context


class ProveedorUpdateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,UpdateView):
    model = Proveedor
    permission_required = "dbd.change_proveedor"
    form_class = ProveedorForm
    context_object_name = 'obj'
    template_name = "proveedor/proveedor_form.html"
    success_url = reverse_lazy('dbd:proveedor_list')

    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de Proveedor'
        return context

class ProveedorConsultView(LoginRequiredMixin,Privilegios,UpdateView):
    model = Proveedor
    permission_required = "dbd.delete_proveedor"
    form_class = ConsultaProveedorForm
    context_object_name = 'obja'
    template_name = "proveedor/proveedor_form.html"
    success_url = reverse_lazy('dbd:proveedor_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Consulta de Proveedor'
        return context

class ProveedorDeleteView(LoginRequiredMixin,DeleteView):
    model = Proveedor
    context_object_name = 'obj'
    template_name = "proveedor/proveedor_delete.html"

    
    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user
        return super().form_valid(form)

    def post(self,request,pk,*args, **kwargs):
        proveedor = Proveedor.objects.get(id_proveedor=pk)
        proveedor.estado = False
        proveedor.save()
        return redirect('dbd:proveedor_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminacion de Proveedor'
        return context