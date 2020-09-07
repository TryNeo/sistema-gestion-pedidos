from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.views.generic import TemplateView


class Privilegios(PermissionRequiredMixin):
    raise_excepction = False
    redirect_field_name = "redirecto_to"

    def handle_no_permission(self):
        self.login_url = "dbd:error_403"
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Error403View(LoginRequiredMixin,TemplateView):
    template_name = 'errors/error403.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user 
        return context
    
