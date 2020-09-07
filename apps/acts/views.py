from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.dbd.views.mixin.mixin import MixinFormInvalid

from apps.acts.models import User
from apps.acts.forms import UsuarioForm
from apps.dbd.views.errors.views import Privilegios


class UserListView(LoginRequiredMixin,Privilegios,ListView):
    model = User
    permission_required = "dbd.view_user"
    context_object_name = 'usuario_l'
    template_name = "usuario/usuario_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        return context

class UserCreateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,CreateView):
    model = User
    permission_required = "dbd.add_user"
    form_class = UsuarioForm
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('dbd:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creación de Usuario'
        return context


class UserUpdateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,UpdateView):
    model = User
    permission_required = "dbd.change_user"
    form_class = UsuarioForm
    context_object_name = 'obj'
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('dbd:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de Usuario'
        return context

class UserDeleteView(LoginRequiredMixin,Privilegios,DeleteView):
    model = User
    permission_required = "dbd.delete_user"
    context_object_name = 'obj'
    template_name = "usuario/usuario_delete.html"
    success_url = reverse_lazy('dbd:usuario_list')
    
    def post(self,request,pk,*args, **kwargs):
        usuario = User.objects.get(id=pk)
        usuario.id_active = False
        usuario.save()
        return redirect('dbd:usuario_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminacion de Usuario'
        return context