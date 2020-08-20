from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.contrib.auth.models import Group




class RolListView(LoginRequiredMixin,ListView):
    model = Group
    context_object_name = 'rol_l'
    template_name = "roles/rol_list.html"

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Roles'
        return context
