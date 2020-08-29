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

from apps.dbd.modelos.estructura_model_proveedor import Proveedor

class ReporteProveedorPdf(LoginRequiredMixin,View):
    def get (self, request,*args,**kwargs):
        try:
            today = timezone.now()
            proveedores = Proveedor.objects.all()
            total_proveedores = Proveedor.objects.filter().count()
            context = {
                    'proveedor':proveedores,
                    'today':today,
                    'request':request,
                    'total_proveedores':total_proveedores
            }
            template = get_template("reportes/proveedor_report.html")
            html = template.render(context)
            response = HttpResponse(content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename="reporte_proveedores.pdf"'

            pisa_status = pisa.CreatePDF(
            html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('dbd:proveedor_list'))