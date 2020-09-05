import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from apps.dbd.modelos.estructura_model_producto import Producto

class ReporteProductoPdf(LoginRequiredMixin,View):
    def get (self, request,*args,**kwargs):
        try:
            today = timezone.now()
            productos = Producto.objects.all()
            total_productos  = Producto.objects.filter().count()
            context = {
                    'user': self.request.user,
                    'today':today,
                    'datos':{'empresa':'Asoproteseu S.A','telefono':'099-8364-0298','ruc':'1790004104001'},
                    'productos':productos,
                    'total_productos':total_productos
            }
            template = get_template("reportes/producto_report.html")
            html = template.render(context)
            response = HttpResponse(content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename="reporte_producto.pdf"'

            pisa_status = pisa.CreatePDF(
            html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('dbd:producto_list'))