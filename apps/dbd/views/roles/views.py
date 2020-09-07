from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from apps.dbd.views.mixin.mixin import MixinFormInvalid

from django.urls import reverse_lazy

from django.contrib.auth.models import Group
from apps.dbd.forms.roles.rol_form import GroupForm
from apps.dbd.views.errors.views import Privilegios



class RolListView(LoginRequiredMixin,Privilegios,ListView):
    model = Group
    permission_required = "dbd.view_group"
    context_object_name = 'rol_l'
    template_name = "roles/rol_list.html"

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Roles'
        return context


class RolCreateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,CreateView):
    model = Group
    permission_required = "dbd.add_group"
    form_class = GroupForm
    context_object_name = 'obj'
    template_name = "roles/rol_form.html"
    success_url = reverse_lazy('dbd:rol_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de Rol'
        return context

class RolUpdateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,UpdateView):
    model = Group
    permission_required = "dbd.change_group"
    form_class = GroupForm
    context_object_name = 'obj'
    template_name = "roles/rol_form.html"
    success_url = reverse_lazy('dbd:rol_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de rol'
        return context

class RolDeleteView(LoginRequiredMixin,Privilegios,DeleteView):
    model = Group
    permission_required = "dbd.delete_group"
    context_object_name = 'obj'
    template_name = "roles/rol_delete.html"
    success_url = reverse_lazy('dbd:rol_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminacion de rol'
        return context