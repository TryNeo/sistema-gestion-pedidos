from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User



class UserListView(LoginRequiredMixin,ListView):
    model = User
    context_object_name = 'usuario_l'
    template_name = "usuario/usuario_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        return context
