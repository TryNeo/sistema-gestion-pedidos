from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.acts.models import User
from apps.acts.forms import UsuarioForm


class UserListView(LoginRequiredMixin,ListView):
    model = User
    context_object_name = 'usuario_l'
    template_name = "usuario/usuario_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        return context

class UserCreateView(LoginRequiredMixin,CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('dbd:usuario_list')


    def post(self, request,*args ,**kwargs):
        self.object = self.get_object
        form = UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            print(form.errors)
            return redirect('dbd:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creación de Usuario'
        return context


class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UsuarioForm
    context_object_name = 'obj'
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('dbd:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de Usuario'
        return context

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = User
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