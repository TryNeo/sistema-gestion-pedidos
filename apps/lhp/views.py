from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView
import SistemaGestionPedidos.settings.base as setting

#-------CREACION DE LOGIN------------#
class LoginFormView(LoginView):
    #Pasandole el template
    template_name = 'login.html'

    #Sobreescribiendo el metodo dispatch 
    def dispatch(self, request, *args, **kwargs):
        #Authentificando el usuario que sea correcto
        if request.user.is_authenticated:
            #rediricionando el usuario al Dashboard
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Asoprotosue | Iniciar Seccion'
        return context


class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
