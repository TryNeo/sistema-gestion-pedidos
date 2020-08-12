from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from apps.dbd.modelos.estructura_model_catalogo import Categoria
from apps.dbd.forms.categoria.categoria_form import CategoriaForm


class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'categoria_l'
    template_name = "categoria/categoria_list.html"
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorías'
        return context


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria/categoria_form.html"
    success_url = reverse_lazy('dbd:categoria_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.usuario_crea =  self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creación de Categoria'
        return context
