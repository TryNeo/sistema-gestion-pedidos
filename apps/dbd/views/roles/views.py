from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.contrib.auth.models import Group
from apps.dbd.forms.roles.rol_form import GroupForm



class RolListView(LoginRequiredMixin,ListView):
    model = Group
    context_object_name = 'rol_l'
    template_name = "roles/rol_list.html"

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Roles'
        return context


class RolCreateView(LoginRequiredMixin,CreateView):
    model = Group
    form_class = GroupForm
    context_object_name = 'obj'
    template_name = "roles/rol_form.html"
    success_url = reverse_lazy('dbd:rol_list')

    def form_valid(self, form):
        form.instance.usuario_crea =  self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de Rol'
        return context

class RolUpdateView(LoginRequiredMixin,UpdateView):
    model = Group
    form_class = GroupForm
    context_object_name = 'obj'
    template_name = "roles/rol_form.html"
    success_url = reverse_lazy('dbd:rol_list')


    def form_valid(self, form):
        form.instance.usuario_crea =  self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de rol'
        return context

class RolDeleteView(LoginRequiredMixin,DeleteView):
    model = Group
    context_object_name = 'obj'
    template_name = "roles/rol_delete.html"
    success_url = reverse_lazy('dbd:rol_list')

    def form_valid(self, form):
        form.instance.usuario_crea =  self.request.user
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminacion de rol'
        return context