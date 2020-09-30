from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from apps.dbd.modelos.estructura_model_producto import Producto
from apps.dbd.forms.producto.producto_form import ProductoForm
from apps.dbd.views.mixin.mixin import MixinFormInvalid
from apps.dbd.views.errors.views import Privilegios

#consultar
class ProductoListView(LoginRequiredMixin,Privilegios,ListView):
    model = Producto #le pasamos el model
    permission_required = "dbd.view_producto" #le ponemos el permiso view 
    context_object_name = 'producto_l' #lo renombramos ahora no sera object_list si no producto_l
    template_name = "producto/producto_list.html" #le pasamoas el template

    def get_context_data(self, **kwargs): #sobreescribmos el metodo 
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Productos' # y simplemente le pasamos un str como contexto para poder reutilazar en nuesto template
        return context
#crear
class ProductoCreateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,CreateView):
    model = Producto #le pasamos el model
    permission_required = "dbd.add_producto" #le pasamos el permiso
    form_class = ProductoForm #le pasamos nuestro form
    context_object_name = 'obj' #lo renombramos ahora sera obj
    template_name = "producto/producto_form.html" #le pasamos el template
    success_url = reverse_lazy('dbd:producto_list') #una vez ejecutado nos retornara a nuestro listado
    #sobreescribimos el metodo form_valid
    def form_valid(self,form):
        form.instance.usuario_crea = self.request.user #hacemos una instancia de usuario_crea un atributo que ya tenemos en nuestro model donde se guardara el usuario actual que esta logeado
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creación de Producto'
        return context
#actualizar
class ProductoUpdateView(LoginRequiredMixin,MixinFormInvalid,Privilegios,UpdateView):
    model = Producto #le pasamos el model
    permission_required = "dbd.change_producto" #le asignamos el permiso
    form_class = ProductoForm #le pasamos el form
    context_object_name = 'obj' #renombramos
    template_name = "producto/producto_form.html" #pasamos el template
    success_url = reverse_lazy('dbd:producto_list')

    #sobreescribimos el metodo form_valid
    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user #obtenemos la instacia de usuario_Modifica el cual guardara el usuario que lo haya modidificado
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de Producto'
        return context
#delete
class ProductoDeleteView(LoginRequiredMixin,Privilegios,DeleteView):
    model = Producto #pasamos el model
    permission_required = "dbd.delete_producto" #le asignamos el permiso
    context_object_name = 'obj' #renombramos
    template_name = "producto/producto_delete.html" #le pasamos el template
    
    #sobreescribimos el metodo form_valid
    def form_valid(self, form):
        form.instance.usuario_modifica =  self.request.user #obtenemos la instacia de usuario_Modifica el cual guardara el usuario que lo haya modidificado
        return super().form_valid(form)

    #sobreescribimos el metodo post y le pasamos como parametro pk
    def post(self,request,pk,*args, **kwargs):
        producto = Producto.objects.get(id_producto=pk) #obtenemos el pk actual al  vamos a eliminar
        producto.estado = False #le ponemos el estado en false, por defecto es True
        producto.save()#guardamos
        return redirect('dbd:producto_list') #redirecionamos
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminacion de producto'
        return context
