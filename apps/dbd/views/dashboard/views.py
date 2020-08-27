from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.acts.models import User


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Inicio|Asoprotesue'
        context['usuarios'] = User.objects.filter().count()
        return context
